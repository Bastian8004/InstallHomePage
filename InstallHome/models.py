#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    title = models.CharField(max_length=70)
    description1 = models.TextField(max_length=1024)
    description2 = models.TextField(max_length=1024, blank=True, null=True)
    description3 = models.TextField(max_length=1024, blank=True, null=True)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title

class AlbumImage(models.Model):
    # Zaktualizuj import
    from pilkit.processors import ResizeToFill
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFill(1280, 1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFill(300, 300)], format='JPEG', options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

class Uslugi(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Factory(models.Model):
    titlemain = models.CharField(max_length=70, blank=True, null=True)
    describemain = models.TextField(max_length=1024, blank=True, null=True)
    titlehelp = models.CharField(max_length=70, blank=True, null=True)
    describehelp = models.TextField(max_length=1024, blank=True, null=True)

class Kwalifikacje(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(upload_to='images/')
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwa

class Contakt(models.Model):
    Nazwa = models.CharField(max_length=70,blank=True, null=True)
    NIP = models.CharField(max_length=70,blank=True, null=True)
    NrTel = models.CharField(max_length=70,blank=True, null=True)
    EMail = models.CharField(max_length=70,blank=True, null=True)
    Miejscowosc = models.CharField(max_length=70,blank=True, null=True)
    Ulica = models.CharField(max_length=70,blank=True, null=True)


class Main(models.Model):
    Wstep = models.CharField(max_length=70, blank=True, null=True)
    Opis = models.TextField(max_length=1024, blank=True, null=True)

class Oferty(models.Model):
    nazwa = models.CharField(max_length=70, blank=True, null=True)
    opis = models.TextField(max_length=1024, blank=True, null=True)
    zdjecie = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.nazwa

class Cennik(models.Model):
    category = models.ForeignKey(Oferty, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=70, blank=True, null=True)
    opis = models.TextField(max_length=1024, blank=True, null=True)
    cena = models.CharField(max_length=70, blank=True, null=True)
    zdjecie = models.ImageField(upload_to='albums', blank=True, null=True)
    lewo = models.BooleanField()
    prawo = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.nazwa