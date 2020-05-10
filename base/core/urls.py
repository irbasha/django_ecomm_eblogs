from django.urls import path
from .views import (
    home,
    detail,
    category,
    about,
    contact,
)

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('category/', category, name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
