"""orm02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book/list/', views.book_list,name='book_list'),
    url(r'^index/', views.index,name='index'),
    url(r'^login/', views.login,name='login'),
    url(r'^yanzhou/', views.yanzhou,name='yanzhou'),
    url(r'^register/', views.register,name='register'),
    url(r'^xx/', views.xx,name='xx'),
    url(r'^book/add/', views.BookAddView.as_view(),name='book_add'),
    url(r'^book/edit/(\d+)/', views.BookEditView.as_view(),name='book_edit'),
    url(r'^book/del/(\d+)/', views.book_del,name='book_del'),


    url(r'^book/swal_delete/', views.swal_delete,name='swal_delete'),


]
