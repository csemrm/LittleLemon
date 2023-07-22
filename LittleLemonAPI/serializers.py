from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price',
                  'featured', 'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    Date_Joined = serializers.SerializerMethodField()
    date_joined = serializers.DateField(write_only=True)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'Date_Joined']

    def get_Date_Joined(self, obj):
        obj.date_joined.strftime('%Y-%m-%d')


class UserCartSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(decimal_places=2, max_digits=6)
    name = serializers.CharField(source='menuitem.title', read_only=True)

    class Meta:
        model: Cart
        fields = ['user_id', 'menuitem_id', 'quantity', 'unit_price', 'price']

        extra_kwargs = {
            'price': {
                'read_only': True
            }
        }


class OrderItemSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(
        max_digits=6, decimal_places=2,
        source='menuitem.price',
        read_only=True
    )
    price = serializers.DecimalField(max_digits=6, decimal_places=2,
                                     read_only=True)
    name = serializers.CharField(source='menuitem.title', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['name', 'price', 'unit_price', 'quantity']
        extra_kwargs = {
            'menuitem': {
                'read_only': True
            }
        }


class OrderSerializer(serializers.ModelSerializer):
    Date = serializers.SerializerMethodField()
    date = serializers.DateTimeField(write_only=True, default=datetime.now)
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew',
                  'status', 'total', 'date', 'order_items']
        extra_kwargs = {
            'total': {
                'read_only': True
            }
        }

    def get_Date(self, obj):
        return obj.date.strftime('%Y-%m-%d')

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(
            order_items,
            many=True,
            context={
                self.context['request']
            })
