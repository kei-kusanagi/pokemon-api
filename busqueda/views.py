from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(*args, **kwars):
    return HttpResponse("<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png' alt='MDN'>")
