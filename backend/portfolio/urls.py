from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),  # la page principale avec formulaire
    path('contact_success/', views.contact_success, name='contact_success'),
]
