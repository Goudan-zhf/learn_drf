from rest_framework import serializers
from api2.models import *
from rest_framework import exceptions
from api.models import Employee
from learn_drf import settings



class BookSerializer(serializers.ModelSerializer):
    '''整合序列化'''
    class Meta:
        model = Book
        fields = ("price", "pic", "publish", "authors","book_name")
        extra_kwargs={
            '''开始定义校验规则'''
            "book_name":{
                "max_length":10,
                "min_length":2,
                "error_messages":{
                    "max_length":'too long',
                    "min_length":'too slot',
                }
            },
            "price":{
                "default":0,
                "decimal_places":2,
            },
            "publish": {
                "write_only": True,
            },
            "authors": {
                "write_only": True,
            },
            "pic": {
                "read_only": True
            }
        }


    def validate(self, attrs):
        '''全局钩子，数据的最先获取和检验'''
        print(attrs)
        book_name=attrs.get("book_name")
        book=Book.objects.filter(book_name=book_name,is_delete=False)
        if len(book)>0 :
            '''这里考虑直接book行不行，因为空的QuerySet不知道是不是为假'''
            raise exceptions.ValidationError('这本书已经存在了')
        price=attrs.get("price")
        if price:
            '''这里我脑残，给价格设置了默认，所以可能取出来是没有的'''
            if int(price)>500 :
                raise exceptions.ValidationError('你这么贵怎么不去抢啊')

        '''检测完了，把数据塞回去'''
        return attrs

    def validate_publish(self,obj):
        '''用一下钩子'''
        res=Press.objects.filter(press_name=obj,is_delete=False)
        if len(res)<1:
            raise exceptions.ValidationError('你的出版社号不存在')

        return obj
    '''作者校验要写'''

    def update(self, instance, validated_data):
        book_name = validated_data.get("book_name")
        instance.book_name = book_name
        instance.save()
        return instance




