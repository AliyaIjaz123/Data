from django.urls import path
from .views import data,dash

urlpatterns=[
    path('',dash),
    path('get_data/',data.as_view()),
    path('get_data/<int:key>',data.as_view()),
    path('del_data/',data.as_view()),
    path('del_data/<int:key>',data.as_view()),
    
    
]