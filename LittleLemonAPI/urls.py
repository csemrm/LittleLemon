from django.urls import path
from . import views



urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('groups/manager/users', views.ManagerUserView.as_view(), name='managers-list'),
    path('groups/manager/users/<int:pk>', views.ManagerSingleView.as_view(), name='manager-detail'),
    path('groups/delivery-crew/users/', views.DeliveryCrewView.as_view(), name='delivery-crew-list'),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewSingleView.as_view(), name='delivery-crew-detail'),
    path('cart/menu-items', views.CustomerCart.as_view()),
    path('orders', views.OrderView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view())
]
