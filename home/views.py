from django.shortcuts import get_object_or_404, render

from .models import Slider, Blog

# Create your views here.
def home(request):
    sliders = Slider.objects.filter(active = True)
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)


    
    # print(sliders)
    # print(first_slider)
    
    context = {
        "sliders": sliders,
        "abouts": abouts,
        "rentings": rentings,
    }
    return render(request, "index.html", context)



def blog_detail(request, slug):
    blog = get_object_or_404(Blog, active = True, slug = slug)
    
    context = {
        "blog": blog,
    }
    return render(request, "blog_detail.html", context)
