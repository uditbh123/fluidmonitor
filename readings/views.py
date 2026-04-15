from django.shortcuts import render, redirect
from .models import Reading
from .forms import ReadingForm
from django.db.models import Avg, Min, Max
from django.http import JsonResponse

def home(request):
    readings = Reading.objects.all().order_by('-recorded_at')

    stats = Reading.objects.aggregate(
        avg_value=Avg('value'),
        min_value=Min('value'),
        max_value=Max('value'),
    )

    context = {
        'readings': readings,
        'stats': stats,
    }
    return render(request, 'readings/home.html', context)


def add_reading(request):
    if request.method == 'POST':
        form = ReadingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReadingForm()

    return render(request, 'readings/add_reading.html', {'form': form})

def chart_data(request):
    readings = Reading.objects.all().order_by('recorded_at')

    data = {
        'labels': [r.recorded_at.strftime('%d %b %H:%M') for r in readings],
        'values': [float(r.value) for r in readings],
        'sensors': [r.sensor_name for r in readings],
    }
    return JsonResponse(data)