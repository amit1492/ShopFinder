from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Shop
from shops.forms import ShopSearchForm, ShopForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def shop_list(request):
    if request.method == 'POST':
        form = ShopSearchForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            distance = form.cleaned_data['distance']
            user_location = Point(longitude, latitude, srid=4326)
            nearby_shops = shops_within_range = Shop.objects.annotate(distance=Distance('location', user_location)).filter(distance__lt=distance*1000)
            context = {'shops': nearby_shops}
            return render(request, 'shops/shop_list.html', context)
    else:
        form = ShopSearchForm()
    return render(request, 'shops/shop_search.html', {'form': form})


def all_shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop_list2.html', {'shops': shops})

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shop_detail.html', {'shop': shop})

def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'shop_form.html', {'form': form})

def shop_update(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop_form.html', {'form': form})

