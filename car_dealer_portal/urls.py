from django.urls import path
from car_dealer_portal.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('registration/', registration, name='registration'),
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    path('manage_House/', manage_House, name='manage_House'),
    path('order_list/', order_list, name='order_list'),
    path('complete/', complete, name='complete'),
    path('history/', history, name='history'),
    path('delete/', delete, name='delete'),
]
