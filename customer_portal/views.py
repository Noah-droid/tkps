from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from house_portal.models import *
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'customer/login.html')
    else:
        return render(request, 'customer/home_page.html')

def login(request):
    return render(request, 'customer/login.html')

def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'customer/all_houses.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            customer = Customer.objects.get(user = user)
        except:
            customer = None
        if customer is not None:
            auth.login(request, user)
            return render(request, 'customer/all_houses.html')
        else:
            return render(request, 'customer/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'customer/login.html')

def register(request):
    return render(request, 'customer/register.html')



def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        city = request.POST.get('city')
        city = city.lower()

        # Check if the student field is provided in the form
        is_student = request.POST.get('is_student') == 'on'

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
        except Exception as e:
            return render(request, 'customer/registration_error.html')

        try:
            area = Area.objects.get(city=city)
        except Area.DoesNotExist:
            area = Area.objects.create(city=city)

        customer = Customer.objects.create(user=user, mobile=mobile, area=area)

        # If the user is a student, create a StudentHouse instance for them
        # if is_student:
        #     student_house = StudentHouse.objects.create(house=customer.area.house_set.first(), is_student_only=True)

        return render(request, 'customer/registered.html')

    return render(request, 'customer/registration_form.html')


# @login_required
def search(request):
    return render(request, 'customer/search.html')

# @login_required
def search_results(request):
    city = request.POST.get('city')
    houses_list = []
    area = Area.objects.filter(city=city)
    for a in area:
        houses = House.objects.filter(area=a)
        for house in houses:
            if house.is_available:
                house_dictionary = {
                    'name': house.house_name,
                    'price': house.price,
                    'id': house.id,
                    'pincode': house.area.pincode,
                    'capacity': house.bedrooms,
                    'description': house.description,
                    'bathrooms': house.bathrooms,
                    'image_url': house.image.url  # Add image URL to the dictionary
                }
                houses_list.append(house_dictionary)
    request.session['houses_list'] = houses_list
    return render(request, 'customer/search_results.html')


def all_houses(request):
    houses = House.objects.all()
    return render(request, 'customer/all_houses.html', {'houses': houses})


# @login_required
def rent_vehicle(request):
    id = request.POST['id']
    house = House.objects.get(id = id)
    cost_per_day = int(house.bedrooms)*365
    return render(request, 'customer/confirmation.html', {'house':house, 'cost_per_day':cost_per_day})

from django.shortcuts import get_object_or_404
from .models import Orders

from django.shortcuts import get_object_or_404
from .models import Orders

@login_required
def confirm(request):
    house_id = request.POST.get('id')
    user = request.user
    days = request.POST.get('days')
    
    # Retrieve the House object
    house = get_object_or_404(House, id=house_id)
    
    # Retrieve the associated CarDealer
    car_dealer = house.owner
    
    # Check if the house is available
    if house.is_available:
        # Create the Orders instance
        order = Orders.objects.create(
            user=user,
            # car_dealer=car_dealer,
            house=house,
            rent=str(house.price),
            days=days
        )
        # Update the availability of the house
        house.is_available = False
        house.save()
        
        # Render the confirmation page
        return render(request, 'customer/confirmed.html', {'order': order})
    else:
        # Render the order failed page if the house is not available
        return render(request, 'customer/order_failed.html')






@login_required
def manage(request):
    order_list = []
    user = User.objects.get(username = request.user)
    try:
        orders = Orders.objects.filter(user = user)
    except:
        orders = None
    if orders is not None:
        for o in orders:
            if o.is_complete == False:
                order_dictionary = {'id':o.id,'rent':o.rent, 'house':o.house, 'days':o.days, }
                order_list.append(order_dictionary)
    return render(request, 'customer/manage.html', {'od':order_list})

@login_required
def update_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    car_dealer = order.car_dealer
    car_dealer.wallet -= int(order.rent)
    car_dealer.save()
    order.delete()
    cost_per_day = int(vehicle.capacity)*13
    return render(request, 'customer/confirmation.html', {'vehicle':vehicle}, {'cost_per_day':cost_per_day})

@login_required
def delete_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    car_dealer = order.car_dealer
    car_dealer.wallet -= int(order.rent)
    car_dealer.save()
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    order.delete()
    return HttpResponseRedirect('/customer_portal/manage/')






def student_section(request):
    student_houses = House.objects.filter(is_student_only=True)
    return render(request, 'customer/student_section.html', {'student_houses': student_houses})