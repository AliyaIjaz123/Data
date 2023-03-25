from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import dataSerializers
from .models import humans
from django.shortcuts import render

def dash(request):
    return render(request,'Dashboard.html') 

# Create your views here.
class data(APIView):
    def get(self,request,key=None):
        if key is None:
            all_data=humans.objects.all()
            seria=dataSerializers(all_data,many=True)
            return Response(seria.data)
            
        one_recorde=humans.objects.get(ID=key)
        serializer2=dataSerializers(one_recorde)
        return Response(serializer2.data)
    
    def delete(self,request,key=None):
        if key is None:
            del_all=humans.objects.all()
            del_all.delete()
            return Response({'msg':'All data deleted'})
        particular=humans.objects.get(ID=key)
        particular.delete()
        return Response({'msg':'Data deleted'})
           
        