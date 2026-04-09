from django.shortcuts import render
from .models import Reading 
from django.db.models import Avg, Min, Max
from django.shortcuts import redirect 
from .forms import ReadingForm

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

def add_reading(request):
    if request.method == 'POST':
        form = ReadingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ReadingForm()
        return render(request, 'readings/add_reading.html', {'form': form})
    