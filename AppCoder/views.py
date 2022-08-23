from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar

# Create your views here.
def familiar(request):
    familiar=Familiar(nombre="Beatriz", apellido="Alvarez", edad=int(60), parentezco="Mama")
    familiar.save()
    texto=f"Familiar creado: nombre:   {familiar.nombre} apellido:   {familiar.apellido} edad:   {familiar.edad} parentezco: {familiar.parentezco}"
    return HttpResponse(texto)

def familiar2(request):
    familiar2=Familiar(nombre="Wilfredo", apellido="Ramírez", edad=int(62), parentezco="Papa")
    familiar2.save()
    texto=f"Familiar creado: nombre:   {familiar2.nombre} apellido:   {familiar2.apellido} edad:   {familiar2.edad} parentezco: {familiar2.parentezco}"
    return HttpResponse(texto)

def familiar3(request):
    familiar3=Familiar(nombre="Francismar", apellido="Campos", edad=int(33), parentezco="Hermana")
    familiar3.save()
    texto=f"Familiar creado:   nombre:   {familiar3.nombre}  apellido:   {familiar3.apellido}   edad:   {familiar3.edad} parentezco: {familiar3.parentezco}"
    return HttpResponse(texto)