from django.shortcuts import render
from .models import *

from django.db.models import Count
# Create your views here.


def data_drive_home(request):
    # Get the count of entries for each movement
    movement_counts = MovementEntry.objects.values('movement').annotate(entry_count=Count('movement'))
    movement_with_least_entries = Movement.objects.annotate(entry_count=Count('movemententry')).order_by('entry_count').first()

    context = {
        'action': movement_with_least_entries.name,
        'description': movement_with_least_entries.description,
    }

    print(context)

    return render(request, 'datadrive/index.html', context)