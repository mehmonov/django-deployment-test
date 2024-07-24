
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("BU sayt serverda ishlamoqda")

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home)
]
