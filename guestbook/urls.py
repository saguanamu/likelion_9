from django.urls import path
from .import views

urlpatterns = [
    path('guestbookcreate/', views.guestbookcreate, name='guestbookcreate'),
]