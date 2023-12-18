#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from InstallHome.models import Album, Uslugi, Factory, Kwalifikacje, Contakt


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)

class UslugiForm(forms.ModelForm):

    class Meta:
        model = Uslugi
        exclude = ['title', 'description', 'photo']

class FactoryForm(forms.ModelForm):

    class Meta:
        model = Factory
        exclude = ['titlemain', 'describemain', 'titlehelp','describehelp']

class KwalForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znaków')

    class Meta:
        model = Kwalifikacje
        fields = ['nazwa','opis','image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contakt
        exclude = ['Nazwa', 'NIP', 'NrTel', 'Email', 'Miejscowosc', 'Ulica']


class MainForm(forms.ModelForm):
    class Meta:
        model = Contakt
        exclude = ['Wstep', 'Opis']
