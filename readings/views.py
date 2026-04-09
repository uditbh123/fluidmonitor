from django.shortcuts import render
from .models import Reading 
from django.db.models import Avg, Min, Max

def home(request):
    readings = Reading.objects.all().order_by('-recorded_at')

    stats = Reading.objects.aggregate(
        avg_value=Avg('value'),
        min_value=Min('value'),
        max_value=Max('value')
    )

    context = {
        'readings': readings, 
        'stats': stats,
    }
    return render(request, 'readings/home.html', context)