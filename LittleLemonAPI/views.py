from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer, MenuItemSerializer,
    UserSerializer, UserCartSerializer,
    OrderSerializer,
    OrderItemSerializer
)
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAdminUser, IsAuthenticated, AllowAny
)
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from decimal import Decimal


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    search_fields = ['title']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            return [IsAdminUser]

        return [AllowAny()]


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def perform_create(self, serializer):
        user = serializer.save()



class ManagerUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        manager_group = Group.objects.get(name='Manager')
        queryset = User.objects.filter(groups=manager_group)
        return queryset

    def perform_create(self, serializer):
        manager_group = Group.objects.get(name='Manager')
        user = serializer.save()
        user.groups.add(manager_group)


class ManagerSingleView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        manager_group = Group.objects.get(name='Manager')
        queryset = User.objects.get(groups=manager_group)
        return queryset


class DeliveryCrewView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        queryset = User.objects.filter(groups=delivery_crew)
        return queryset

    def perform_create(self, serializer):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        user = serializer.save()
        user.gruups.add(delivery_crew)


class DeliveryCrewSingleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        queryset = User.objects.filter(groups=delivery_crew)
        return queryset


class CustomerCart(generics.ListCreateAPIView):
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        menuitem = self.request.data.get('menuitem')
        quantity = int(self.request.data.get('quantity'))
        unit_price = MenuItem.objects.get(pk=menuitem).price
        price = quantity * unit_price
        serializer.save(user=user, price=price)

    def delete(self, request):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderView(generics.ListCreateAPIView):
        serializer_class = OrderSerializer
        permission_classes = [IsAuthenticated]
        throttle_classes = [AnonRateThrottle, UserRateThrottle]

        def get_queryset(self):
            user = self.request.user
            if user.groups.filter(name='Manager').exists():
                return Order.objects.all()
            return Order.objects.filter(user=user)

        def calculate_total(self, items):
            total = Decimal(0)
            for item in items:
                total += item.price

            return total

        def perform_create(self, serializer):
            cart_items = Cart.objects.filter(user=self.request.user)
            total = self.calculate_total(cart_items)
            order = serializer.save(user=self.request.user, total=total)

            for item in cart_items:
                OrderItem.objects.create(
                    menuitem=item.menuitem,
                    quantity=item.quantity,
                    price=item.price,
                    unit_price=item.unit_price,
                    order=order
                )

                item.delete()


class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        return Order.objects.filter(user=user)
