from django.http import HttpResponse, Http404
from django.template import Context, loader                               
from django.shortcuts import render_to_response, get_object_or_404        
from clusterEngine.models import Recipe
import datetime                                                           
from django.conf import settings

def main(request):
    
    AllRec = Recipe.objects.all()

    return render_to_response(
        'main.html',
        {
            'AllRec': AllRec,
        } 
    )
