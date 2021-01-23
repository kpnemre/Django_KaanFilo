from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .models import Slider, Blog, ContactInfo
from .forms import OfferForm, ContactForm

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
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)

    context = {
        "blog": blog,
        "abouts": abouts,
        "rentings": rentings,
    }
    return render(request, "blog_detail.html", context)


def offer(request):
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)
    if request.method == 'POST':
        print(request.POST)
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarı bir şekilde mesajınız tarafımıza iletilmiştir. En kısa sürede sizinle iletişime geçilecektir.')
            return redirect("home:offer")
    else:
        form = OfferForm()
    
    context = {
        "form": form,
        "abouts": abouts,
        "rentings": rentings,
    }

    return render(request, "forms/offer.html", context)


def contact(request):
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarı bir şekilde mesajınız tarafımıza iletilmiştir. En kısa sürede sizinle iletişime geçilecektir.')
            return redirect("home:contact")
    else:
        form = ContactForm()
    
    context = {
        "form": form,
        "abouts": abouts,
        "rentings": rentings,
    }

    return render(request, "contact.html", context)

    
