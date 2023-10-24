from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# Создаем представление для Пагинации
class WomenAPIListPagination(PageNumberPagination):
    page_size = 3  # Кол-во заприсей на странице
    page_size_query_param = 'page_size'
    max_page_size = 10000


# Возвращает список статей
class WomenAPIList(generics. ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # Подключаем созданное представление пагинации,
    # которая будет выводить столько записи, сколько мы указали
    # в этом представлении WomenAPIListPagination
    pagination_class = WomenAPIListPagination

# Обновляет статьи только автор
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    permission_classes = (IsAuthenticated, )

    # Мы сделалем Аутантификацию только по Токену, а не по Сесссии
    # Доступ к тем пользователям, которые авторизовываются по Токену
    # authentication_classes = (TokenAuthentication, )

# Удаляет статьи только админ
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


# # Определяем свой собственный ViewSet
# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     # При переходе получения всех записей
#     # Выдаст толлько указаные первые 3 записи
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         # Если pk есть, то это запрос одной записи
#         # Если нет pk, то это получение списка записи
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#     # Добавим новый маршрут в WomenViewSet, при помощи @action,
#     # который будет выводить Категории
#     # methods - поддерживаемые методы
#     # detail=False - будет возвращаться список категорий по адресу:
#     # http://127.0.0.1:8000/api/v1/women/category/
#     # @action(methods=['get'], detail=False)
#     # # Придумываем сами метод - category
#     # def category(self, request):
#     #     cats = Category.objects.all()
#     #     return Response({'cats': [c.name for c in cats]})
#
#     # detail=True - будет возвращать конкретную запись по адресу:
#     # http://127.0.0.1:8000/api/v1/women/1/category/
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# # Для GET и POST запросов
# class WomenAPIList(generics.ListCreateAPIView):
#     # Пропишем 2 атрибута
#     queryset = Women.objects.all()
#     # Укажем тот сериалайзер, который будет применять для этого queryset
#     serializer_class = WomenSerializer
#
# # Для PUT запроса - изменение данных
# class WomenAPIUpdate(generics.UpdateAPIView):
#     # queryset - выдаст только 1 измененную запись, а не все записи
#     queryset = Women.objects.all()
#     # Укажем тот сериалайзер, который будет применять для этого queryset
#     serializer_class = WomenSerializer
#
#
# # Для всех CRUD запросов - то есть Get, Post, Update, Put, Path, Delete
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # queryset - выдаст только 1 измененную запись, а не все записи
#     queryset = Women.objects.all()
#     # Укажем тот сериалайзер, который будет применять для этого queryset
#     serializer_class = WomenSerializer


# Это тестовое представление для понимания
# APIView - Это базовое представление, от которого
# создаются другие представления - ListAPIView
# class WomenAPIView(APIView):
#     # метод get - для всех гет запросов, которые будут приходить
#     # requests - это все параметры входяшего гет запроса
#     def get(self, request):
#         w = Women.objects.all()  # берем все записи
#         # Будет возвращать json формат по get запросу
#         # many=True Что бы выдавал все записи
#         # Response - преобразовывает в JSON строку
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     # Мы через post передаем данные, которые будут записываться
#     # в базу данных и выводить их return: WomenSerializer
#     def post(self, request):
#         # Делаем сериализатор с учетом посутпивших данных
#         # То есть распаковываем данные
#         serializer = WomenSerializer(data=request.data)
#         # Проверяем корректность принятых данных
#         # serializer.is_valid - образуется словарь с этими данными,
#         # который называется: validated_data - его передаем в сериалайзер
#         serializer.is_valid(raise_exception=True)
#         # Сохраняем данные, тем самым вызываем метод create в сериайзере WomenSerializer
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         # Мы получаем <int:pk> в URLS.py, когда переходят на страницу
#         # Этот pk - это и есть id модели, которую надо изменить
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Метод PUT не определен'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Обьект не найден'})
#
#         # Если мы получили ключ успешно, то передаем 2 переметра:
#         # data (это те данные, НА которые мы меняем) и
#         # instance (это те данные, которые мы меняем)
#         # Тем самым в последующем вызове метода save - представление поймет, что
#         # нужно вызвать метод def update в сериализаторе, так как 2 параметра
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         # Проверяем данные
#         serializer.is_valid(raise_exception=True)
#         # Сохраняем, тем самым вызываем метод update в сериалайзере (так как передано
#         # два параметра, а не один: data и instance)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     # Это я сам сделал, метод без Сериалайзера - просто удаляет запись по id
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({'error': 'Метод DELETE не определен'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Обьект не найден'})
#
#         record_to_delete = Women.objects.get(id=pk)
#         record_to_delete.delete()
#
#         return Response({'del': f'Мы удалили id записи: {pk}'})



# # ListAPIView -  это представления
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     # Передаем сериалайзер
#     serializer_class = WomenSerializer



