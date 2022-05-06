"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from notes.views import IndexPage, DeleteNote, change_status, UpdateNote, DeleteComplited, change_delete_status, DeleteSelected

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPage.as_view(), name='index_page'),
    path('delete/<pk>', DeleteNote.as_view(), name='delete'),
    path('change_status/<pk>', change_status, name='change_status'),
    path('delete_complited/', DeleteComplited.as_view(), name='delete_complited'),
    path('update/<pk>', UpdateNote.as_view(), name='update_note'),
    path('change_delete_status/<pk>', change_delete_status),
    path('delete_selected/', DeleteSelected.as_view())
]
