"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from post import views as post_views
from user import views as user_views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', user_views.register, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('home/', post_views.home, name='home'),
    path('posts/<int:post_id>/', post_views.post, name='post'),
    path('new_post/', post_views.new_post, name='new_post'),
    path('update_user/<int:id>/', user_views.update_user, name='update_user'),
    path('person/<int:id>/', user_views.person, name='person'),
    path('like/<int:pk>/', post_views.like_post, name='like_post'),
    path('add_friend/<int:id>/', user_views.add_friend, name='add_friend'),
    path('accept_friend/<int:id>/', user_views.accept_friend, name='accept_friend'),
    path('requests/<int:id>/', user_views.requests_page, name='requests')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
