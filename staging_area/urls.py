from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import AlunoList, CursoList, CicloList, MatriculaList

route = routers.DefaultRouter()

app_name = 'staging_area'

# route.register(r'aluno', AlunoListAPIView, basename='Aluno')

urlpatterns = [
    path('', include(route.urls)),
    path('aluno/', AlunoList.as_view(), name='aluno'),
    path('curso/', CursoList.as_view(), name='curso'),
    path('ciclo/', CicloList.as_view(), name='ciclo'),
    path('matricula/', MatriculaList.as_view(), name='matricula'),
]
