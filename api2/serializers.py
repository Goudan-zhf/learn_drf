from rest_framework import serializers
from api2.models import *
from rest_framework import exceptions
from api.models import Employee
from learn_drf import settings

class Press(serializers.ModelSerializer):
    class Meta:
class BookSerializer(serializers.ModelSerializer):
    '''整合序列化'''
    class Meta:
        model = Book
        fields = ('book_name', 'price', 'pic', 'publish', 'authors')
        exclude = ('is_delete', 'create_time', 'status')
        extra_kwargs={
            '''开始定义校验规则'''
            "book_name":{
                '''
                这里是对书名的校验
                扯淡的是这里最好用“”，这可能是因为他是个Json格式数据
                '''
                "max_length":10,
                "min_length":2,
                "error_messages":{
                    "max_length":'too long',
                    "min_length":'too slot',
                }
            },
            "price":{
                '''价格默认为0.你不写就不要钱'''
                "default":0,
                "decimal_places":2,
            },
        }


    def validate(self, attrs):
        '''全局钩子，数据的最先获取和检验'''
        book_name=attrs.get("book_name")
        book=Book.objects.filter(book_name=book_name,is_delete=False)
        if len(book)>0 :
            '''这里考虑直接book行不行，因为空的QuerySet不知道是不是为假'''
            raise exceptions.ValidationError('这本书已经存在了')
        price=attrs.get("book_name")
        if price:
            '''这里我脑残，给价格设置了默认，所以可能取出来是没有的'''
            if price>500 :
                raise exceptions.ValidationError('你这么贵怎么不去抢啊')

        '''检测完了，把数据塞回去'''
        return attrs

    def validate_publish(self,obj):
        '''这里准备用publish的嵌套查询，顺便用一下局部钩子'''
