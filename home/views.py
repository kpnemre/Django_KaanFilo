from django.shortcuts import render

from .models import Slider

# Create your views here.
def home(request):
    sliders = Slider.objects.filter(active = True)

    
    # print(sliders)
    # print(first_slider)
    
    context = {
        "sliders": sliders
    }
    return render(request, "index.html", context)