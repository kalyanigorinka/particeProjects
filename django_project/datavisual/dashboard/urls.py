from django.urls import path
from .views import index 

urlpatterns = [
    path('', index, name='dashboard-index'),
    path('', index, name='dashboard-main'),

]
