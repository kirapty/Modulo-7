from django.shortcuts import render
from django.http import HttpResponse
from .models import Slang, Item
# Create your views here.

def index(response, name):
    ls = Slang.objects.get(name=name)
    item = ls.item_set.get(id=1)
    item = ls.item_set.get(id=2)
    item = ls.item_set.get(id=3)
    item = ls.item_set.get(id=4)
    item = ls.item_set.get(id=5)
    return  HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
