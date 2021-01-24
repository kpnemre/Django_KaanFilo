from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .models import Slider, Blog, Setting, Car
from .forms import OfferForm, ContactForm

# Create your views here.
def home(request):
    sliders = Slider.objects.filter(active = True)
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)
    setting= Setting.objects.first()
    cars = Car.objects.all()

    
    # print(sliders)
    # print(first_slider)
    
    context = {
        "sliders": sliders,
        "abouts": abouts,
        "rentings": rentings,
        "setting":setting,
        "cars": cars,
        #"active_home": "active"
    }
    return render(request, "index.html", context)



def blog_detail(request, slug):
    blog = get_object_or_404(Blog, active = True, slug = slug)
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)
    setting= Setting.objects.first()

    context = {
        "blog": blog,
        "abouts": abouts,
        "rentings": rentings,
        "setting":setting,
        #"active_detail": "active"
        }
    return render(request, "blog_detail.html", context)


def offer(request):
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)
    setting= Setting.objects.first()
    
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
        "setting":setting,
        #"active_offer": "active"
    }

    return render(request, "forms/offer.html", context)


def contact(request):
    abouts = Blog.objects.filter(active = True, about = False)
    rentings = Blog.objects.filter(active = True, about = True)
    setting= Setting.objects.first()
    # print(setting)
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
        "setting":setting,
        #"active_contact": "active"
    }

    return render(request, "contact.html", context)


# def footer(request):
#     setting= Setting.objects.first()
#     # print(setting)
#     context = {

#         "setting":setting,
#     }
#     return render(request, "footer.html", context)

# def cars(request):
#     cars = Car.objects.all()  
#     context = {

#         "cars":cars,
#     }
#     return render(request, "index.html", context) 
