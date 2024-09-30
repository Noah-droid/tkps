from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import RentalItem, Rental

# View for listing all available rental items
@login_required
def available_items(request):
    items = RentalItem.objects.filter(is_available=True)
    return render(request, 'available_items.html', {'items': items})

# View for renting an item
@login_required
def rent_item(request, item_id):
    item = get_object_or_404(RentalItem, id=item_id)
    
    if not item.is_available:
        return redirect('available_items')  # Prevent renting if item is not available
    
    # Create a new rental instance
    rental = Rental.objects.create(
        item=item,
        user=request.user,
        rental_date=timezone.now()
    )
    
    # Mark the item as not available
    item.is_available = False
    item.save()
    
    return redirect('rental_history')  # Redirect to user's rental history

# View for returning a rented item
@login_required
def return_item(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id, user=request.user)
    
    if rental.return_date is not None:
        return redirect('rental_history')  # Prevent returning if already returned
    
    rental.return_date = timezone.now()
    rental.save()
    
    # Mark the item as available again
    rental.item.is_available = True
    rental.item.save()
    
    return redirect('rental_history')

# View for user's rental history
@login_required
def rental_history(request):
    rentals = Rental.objects.filter(user=request.user).order_by('-rental_date')
    return render(request, 'rental_history.html', {'rentals': rentals})
