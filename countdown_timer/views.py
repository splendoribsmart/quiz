from django.shortcuts import render
from django.utils import timezone

def countdown_timer(request):
    current_time = timezone.now()
    target_time = current_time + timezone.timedelta(minutes=10)
    context = {
        'target_time': target_time,
    }
    return render(request, 'countdown_timer/countdown.html', context)
