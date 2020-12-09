"""movie URL Configuration

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
from rest_framework import routers

# from .views import MovieViewSet, PersonViewSet, ReviewsViewSet
from app.views import UserViewSet, ActiveViewSet, QuestViewSet, UserOneViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('active', ActiveViewSet, basename='active')
router.register('quest', QuestViewSet, basename='quest')
router.register('no-detail-user', UserOneViewSet, basename='1user')


# router.register('movie', MovieViewSet, basename='movie')
# router.register('review', ReviewsViewSet, basename='movie')
# urlpatterns = [
#     # path('movies', MovieViewSet.as_view({'get':'list'})),
#     # path('movies/<int:pk>/', MovieViewSet.as_view({'get':'retrieve'}))
# ]
urlpatterns = router.urls