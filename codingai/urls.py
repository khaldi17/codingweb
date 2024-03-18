from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('signup', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service_view, name='service'),
    path('project/', views.project_view, name='project'),
    path('team/', views.team_view, name='team'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
    path('page_not_found/', views.page_not_found_view, name='page_not_found'),
]