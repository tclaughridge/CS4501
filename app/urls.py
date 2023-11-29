from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

app_name = 'app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='app/index.html'), name='index'),
    path('filter/', views.filterProviders, name='filter'),
    path('search/', views.searchProviders, name='search'),
    path("admin/", admin.site.urls)
]
