"""socialnetworking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from socialapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.SignUpView.as_view(),name="register"),
    path('login',views.LoginView.as_view(),name="signin"),
    path("index",views.IndexView.as_view(),name="home"),
    path('post/<int:id>/comments/add',views.add_comment,name="add-comment"),
    path('posts/<int:id>/like',views.like_view,name="like"),
    path('user/profile',views.UserprofileView.as_view(),name="userprofile"),
    path('logout',views.signout,name="signout"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)