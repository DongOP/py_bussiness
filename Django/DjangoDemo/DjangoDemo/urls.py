"""DjangoDemo URL Configuration

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
from . import view,testdb,search,search_post
from django.conf.urls import url



urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', view.hello),
    url(r'^testdb_add$', testdb.testdb_add),
    url(r'^testdb_get$', testdb.testdb_get),
    url(r'^testdb_update$', testdb.testdb_update),
    url(r'^testdb_del$', testdb.testdb_del),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search_post.search_post),
    # Django Admin
    url(r'^admin/', admin.site.urls), 
]
