"""
URL configuration for flippy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get('/add')
def add(request, a: int | float, b: int | float) -> dict:
    return {'result': a + b}

@api.get('/subtract')
def subtract(request, a: int | float, b: int | float) -> dict:
    return {'result': a - b}

@api.get('/multiply')
def multiply(request, a: int | float, b: int | float) -> dict:
    return {'result': a * b}

@api.get('/divide')
def divide(request, a: int | float, b: int | float) -> dict:
    return {'result': a / b} if b != 0 else {'Result' : 'Error: Zero Division Error.'}

@api.get('/IDdaw')
def yveshouse(request) -> dict:
    return {'name': 'Miguel Angel Bautista',
            'USN' : '18003092300',
            'Program': 'Computer Science'}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
