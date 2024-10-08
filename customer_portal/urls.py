from django.urls import path
from customer_portal.views import *

urlpatterns = [
    # path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('registration/', registration, name='registration'),
    path('search/', search, name='search'),
    path('search_results/', search_results, name='search_results'),
    path('rent/', rent_vehicle, name='rent'),
    path('confirmed/', confirm, name='confirmed'),
    # path('manage/', manage, name='manage'),
    path('update/', update_order, name='update'),
    path('delete/', delete_order, name='delete'),
    path('all/', all_houses, name='all'),
    path('student_section/', student_section, name='student_section'),  # Add this line
]
