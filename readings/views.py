from django.shortcuts import render, redirect
from .models import Reading
from .forms import ReadingForm
from django.db.models import Avg, Min, Max
from django.http import JsonResponse

def home(request):
    sensor_filter = request.GET.get('sensor', '')
    readings = Reading.objects.all().order_by('-recorded_at')

    if sensor_filter:
        readings = readings.filter(sensor_name__icontains=sensor_filter)

    # Calculate stats separately for each unit type
    units = Reading.objects.values_list('unit', flat=True).distinct()
    
    stats_by_unit = []
    for unit in units:
        unit_readings = Reading.objects.filter(unit=unit)
        unit_stats = unit_readings.aggregate(
            avg_value=Avg('value'),
            min_value=Min('value'),
            max_value=Max('value'),
        )
        stats_by_unit.append({
            'unit': unit,
            'avg': unit_stats['avg_value'],
            'min': unit_stats['min_value'],
            'max': unit_stats['max_value'],
            'count': unit_readings.count(),
        })
    
    sensors = Reading.objects.values_list('sensor_name', flat=True).distinct()
    total_count = Reading.objects.count()

    context = {
        'readings': readings,
        'stats_by_unit': stats_by_unit,
        'sensors': sensors,
        'sensor_filter': sensor_filter,
        'total_count': total_count,
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

def delete_reading(request, pk):
    reading = Reading.objects.get(pk=pk)
    if request.method == 'POST':
        reading.delete()
        return redirect('home')
    return render(request, 'readings/confirm_delete.html', {'reading': reading})