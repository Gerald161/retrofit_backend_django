import re, json
from rest_framework.views import APIView
from rest_framework.response import Response
from adrf.views import APIView as ASYNCAPIVIEW
from .models import Picture

from pathlib import Path


# Create your views here.
class Upload(APIView):
    def post(self, request, *args, **kwargs):
        for image in request.FILES.values():
            picture = Picture()
            
            picture.image = image
            
            picture.save()
    
        return Response({
            'status': 'complete'
        })

class RemovePicture(APIView):
    def delete(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        
        try:
            picture = Picture.objects.filter(image=f'{slug}.jpg').first()
            
            picture.delete()
            
            return Response({
                'status': 'deleted'
            })
        except:
            return Response({
                'status': 'picture not found'
            })