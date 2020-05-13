

from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('list', list1,name='list'),
    path('a1', a1,name="a1"),
    path('a2', a2,name="a2"),
    path('a3', a3,name="a3"),
    path('a4', a4,name="a4"),
    path('a5', a5,name="a5"),
    path('create', create,name='create'),
    path('<int:pk>/update',PostUpdateView.as_view(),name='update'),

    path('',TemplateView.as_view(template_name='blog/index2.html'),name='index'),
    path('listGeneric',PostListView.as_view(),name='listGeneric')

]
