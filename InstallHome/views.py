#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from .forms import AlbumForm, UslugiForm, FactoryForm, KwalForm
from InstallHome.models import Album, AlbumImage, Uslugi, Factory, Kwalifikacje, Contakt, Main, Oferty, Cennik

def main(request):
    mains = Main.objects.all().order_by()
    return render(request, 'main.html', {'mains': mains})

def firma(request):
    uslugis = Uslugi.objects.all().order_by('-published_date')
    factorys = Factory.objects.all()
    return render(request, 'firma.html', {'uslugis': uslugis, 'factorys': factorys})
def usluga_new(request):
    if request.method == "USLUGI":
        form = UslugiForm(request.USLUGI, request.FILES)
        if form.is_valid():
            uslugi = form.save(commit=False)
            uslugi.author = request.user
            uslugi.published_date = timezone.now()
            uslugi.save()
            return redirect('Factory')
    else:
        form = UslugiForm()
    return render(request, 'firma_edit.html', {'form': form})

def usluga_edit(request, pk):
    uslugi = get_object_or_404(Uslugi,pk=pk)
    if request.method == "USLUGI":
        form = UslugiForm(request.USLUGI, request.FILES, instance=uslugi)
        if form.is_valid():
            uslugi = form.save(commit=False)
            uslugi.author = request.user
            uslugi.published_date = timezone.now()
            uslugi.save()
            return redirect('Factory')

def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

    return render(request, 'post_list.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album
     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context


def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

def post_list(request):
    posts = Kwalifikacje.objects.all().order_by('-published_date')
    return render(request, 'conowego/post_list.html', {'posts': posts})

def kontakt(request):
    contacts = Contakt.objects.all()
    return render(request, 'kontakt.html', {'contacts': contacts})

def ofert_list(request):
    ofertys = Oferty.objects.all().order_by('-published_date')
    return render(request, 'ofert_list.html', {'ofertys': ofertys})

def ofert_detail(request, pk):
    # Pobieramy kategorię na podstawie przekazanego ID
    oferty = Oferty.objects.get(pk=pk)
    # Pobieramy wszystkie dodatkowe modele powiązane z tą kategorią
    cenniks = Cennik.objects.filter(category=oferty)
    return render(request, 'ofert_detail.html', {'oferta': oferty, 'cenniks': cenniks})