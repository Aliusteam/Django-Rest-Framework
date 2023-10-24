"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from women.views import WomenViewSet
from women.views import *
from rest_framework import routers


# # Создаем обьект router для облегчения кода
# router = routers.DefaultRouter()
# # router = routers.SimpleRouter()
# # Регистрируем ViewSet, создаем префикс для работы маршрута: 'women'
# # А вторым аргументом WomenViewSet
# router.register(r'women', WomenViewSet, basename='women')
# # Вот так мы создали просто роутер - SimpleRouter
#
# print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Для аутентификации пользователя
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')), # Для авторизации пользователя
    re_path(r'^auth/', include('djoser.urls.authtoken')), # Авторизация по токену

    # JWT-токены
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

    # # Пропишем весь набор маршрута, который был сгенерирован роутером router.urls
    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/
    # # # Во ViewSet - мы указываем метод для обработки запроса: GET
    # # # А вторым параметром - метод, который будет вызываться, для
    # # # обработки Get запроса - 'list'
    # # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # # # <int:pk> - указывает какой id модели будет изменен
    # # # Так как передается PK - то представление понимает,
    # # # что нужно вызвать PUT в WomenAPIUpdate представлении
    # # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # # # # Представление для CRUD запросов одновремено
    # # # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),









