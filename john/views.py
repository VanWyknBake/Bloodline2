from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Home, Results, Store, Streamers, About, Profile2, Category, Skills, Portfolio, Tourn, News
from django.urls import reverse
from django.views.generic import DetailView

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    

    # News 
    news = News.objects.order_by('updated')
    profiles = Profile2.objects.filter(about=news)

    # Tournaments
    
    tourn = Tourn.objects.order_by('-host')
    

    results = Results.objects.all()
    # Skills
    categories = Category.objects.order_by('-updated')

    

    # Portfolio
    portfolios = Portfolio.objects.order_by('-updated')
    # Streamers
    streamers = Streamers.objects.all()
    store = Store.objects.order_by('name')

    context = {
        'home': home,
        'about': about,
        'news': news,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'streamers': streamers,
        'tourn': tourn,
        'results': results,
        'store': store,
    }
    


    return render(request, 'index.html', context)






