from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

import io


# # Класс который будет имитировать модель джанго
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.ModelSerializer):
    # этот код создает скрытое поле HiddenField, которое будет автоматически устанавливать значение на текущего пользователя user, когда объект будет создаваться с использованием этого сериализатор
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # Связываем с моделью Women
        model = Women
        # Какие поля модели Women, будем возвращать клиенту
        # Возвращаем cat, но клиент будет получать cat_id
        # fields = ('title', 'content', 'cat')
        fields = '__all__'



# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers. DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     # cat_id - прописываем как обычное целое число, не внешний ключ
#     cat_id = serializers.IntegerField()
#
#     # Метод для добавления записи в модель Women
#     def create(self, validated_data):
#         # validated_data - создается в post запросе Представления
#         return Women.objects.create(**validated_data)
#
#     # Метод для изменения данных в модели Women
#     # instance - ссылкуа на модель Women
#     # validated_data - словарь который нужно изменить
#     def update(self, instance, validated_data):
#         # Присваиваем title в модели - значение переданого title
#         # из переданного словаря. Иначе присваиваем: instance.title
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         # Когда изменили все данные, теперь сохраняем в базе данных
#         instance.save()
#         return instance




# наследуемся от базового касса ModelSerializer
# Этот сериализатор работает с моделями
# Будет формировать json на запрос пользователей
# class WomenSerializer(serializers.Serializer):
#     # WomenModel - Модель из которой мы будем формировать JSON
#     # для этого нам нужно оперделить 2 атрибута WomenSerializer
#     # CharField, для того, что бы title был строкой
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()




# # Функция для преобразования в JSON формат
# def encode():
#     # Поулчим model от WomenModel
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     # Пропустим эту модель через сериалайзер
#     model_sr = WomenSerializer(model)
#     # model_sr.data - это сериализованные данные
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # json - это для передачи json формата
#     # render - метод класса JSONRenderer
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# # Функция для преобразования из JSON в данные
# def decode():
#     # io.BytesIO(b'{"title":"Angelina - это стракой мы иметируем входные данные
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



    # class Meta:
    #     model = Women
    #     # fields - поля которые будут использоваться
    #     # для сериализации. Они отправляются пользователю
    #     fields = ('title', 'cat_id')

