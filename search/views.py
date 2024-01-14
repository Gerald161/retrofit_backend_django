import re, json
from rest_framework.views import APIView
from rest_framework.response import Response
from adrf.views import APIView as ASYNCAPIVIEW
from .models import Picture

from pathlib import Path


# Create your views here.
class GetPost(APIView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get("slug") is not None:
            return Response({
                'status': 'complete',
                "name": "Kofi",
                "age": int(self.kwargs.get("slug")),
                "slug": "present"
            })
        else:
            if request.GET.get("name") is not None:
                # print("here")
                return Response([{
                    'status': 'complete',
                    "name": request.GET.get("name"),
                    "age": 400,
                    "slug": "not present",
                    "query": "present"
                }])
            else:
                return Response({
                    'status': 'complete',
                    "name": "Kofi",
                    "age": 700,
                    "slug": "not present",
                    "query": "absent"
                })
            

class GetPosts(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'status': 'complete',
            "name": "Kofi",
            "age": 200,
            "query": request.GET.get("name")
        })
    

class PostStuff(APIView):
    def post(self, request, *args, **kwargs):
        return Response({
            'status': request.data.get("name"),
        })



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