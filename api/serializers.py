from rest_framework import serializers
from rest_framework import exceptions

from api.models import Employee
from learn_drf import settings

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField()
    '''常规自动获取数据库里的值'''
    password=serializers.CharField()
    tell=serializers.CharField()
    is_work=serializers.BooleanField()
    entry_time=serializers.DateTimeField()
    status=serializers.BooleanField()
    gender = serializers.SerializerMethodField()
    '''这里利用新建一个字段，用于自定义获取：选择类型的数据，用obj.get_gender_display()'''
    def get_gender(self,obj):
        '''这里反应gender没有选择类型'''
        print(type(obj.gender))
        return obj.gender
    pic=serializers.SerializerMethodField()
    '''自定义图片回显的全路径'''
    def get_pic(self,obj):
        print(obj)
        '''这里的obj代指数据库对应的那个记录，这里是有.pic属性的，可以用于路径的拼接'''
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, obj.pic)


class EmployeeDeSerializer(serializers.Serializer):
    '''反序列化，实际是序列化的一种，进行校验巴拉巴拉的'''
    '''这里我懒得下钩子了，，，'''
    name = serializers.CharField(
        max_length=8,
        min_length=2,
        error_messages={
            "max_length": "长度太长了",
            "min_length": "长度太短了"
        }
    )
    password=serializers.CharField()
    tell=serializers.CharField(min_length=11, required=True)
    gender = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


