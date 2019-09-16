"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import todo_view, todo_create_view, todo_index, todo_delete, todo_search, todo_update

urlpatterns = [
    path('', todo_index),
    path('admin/', admin.site.urls),
    path('todo/', todo_index, name='todo_index'),
    path('todo_view/<int:pk>', todo_view, name='todo_view'),
    path('todo/add/', todo_create_view, name='todo_add'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
    path('search/', todo_search, name='todo_search'),
    path('article/<int:pk>/edit/', todo_update, name='todo_update'),
]

