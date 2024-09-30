from django.urls import path
from . import views

urlpatterns = [
    path('available/', views.available_items, name='available_items'),
    path('rent/<int:item_id>/', views.rent_item, name='rent_item'),
    path('return/<int:rental_id>/', views.return_item, name='return_item'),
    path('history/', views.rental_history, name='rental_history'),
]
