from django.shortcuts import render, redirect
from .models import *

from django.db.models import Count
# Create your views here.


def data_drive_home(request):
    if request.method == 'POST':
        # Get the data from the form
        action_id = request.POST.get('actionId')
        audio_file = request.FILES.get('audioData')
        transcription = request.POST.get('transcription')

        # Get Movement object
        movement = Movement.objects.get(id=action_id)

        # create a new movement entry
        new_entry = MovementEntry(
            movement=movement,
            audio_file=audio_file,
            notes=transcription
        )
        new_entry.save()

        return redirect('/datadrive')

    # Get the count of entries for each movement
    movement_counts = MovementEntry.objects.values('movement').annotate(entry_count=Count('movement'))
    movement_with_least_entries = Movement.objects.annotate(entry_count=Count('movemententry')).order_by('entry_count').first()

    context = {
        'action': movement_with_least_entries,
    }

    print(context)

    return render(request, 'datadrive/index.html', context)