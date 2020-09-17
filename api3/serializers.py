from rest_framework import serializers
from rest_framework import exceptions
from api.models import Employee
from api3.models import Course, School, Teacher
from learn_drf import settings


class CourseListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index, obj in enumerate(instance):
            self.child.update(obj, validated_data[index])
        return instance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = CourseListSerializer
        model=Course
        fields=('course_name','hours','price','school',"teachers")
        extra_kwargs=({
            "course_name":{
                "max_length":10,
                "min_length":2,
            },
            "hours":{
                "default":48,
            },
            "school":{
                "write_only":True
            },
            "price":{
                "write_only":True,
            },
            "teachers":{
                "write_only":True,
            }
        })

    # def validate(self, attrs):
    #     '''全局钩子，数据的最先获取和检验'''
    #     print(attrs)
    #     course_id = attrs.get("id")
    #     course = Course.objects.filter(pk=course_id, is_delete=False)
    #     if not course:
    #         '''这里考虑直接book行不行，因为空的QuerySet不知道是不是为假'''
    #         raise exceptions.ValidationError('这门课不存在')
    #     price = attrs.get("price")
    #     if price:
    #         '''这里我脑残，给价格设置了默认，所以可能取出来是没有的'''
    #         if int(price) > 5000:
    #             raise exceptions.ValidationError('你这么贵怎么不去抢啊')
    #
    #     '''检测完了，把数据塞回去'''
    #     return attrs

    # def validate_school(self, obj):
    #     '''用一下钩子'''
    #     res = School.objects.filter(press_name=obj, is_delete=False)
    #     if len(res) < 1:
    #         raise exceptions.ValidationError('你的学校不存在')
    #
    #     return obj
    #
    # def validate_teachers(self, obj):
    #     '''用一下钩子'''
    #     res = Teacher.objects.filter(teacher_name=obj, is_delete=False)
    #     if len(res) < 1:
    #         raise exceptions.ValidationError('你的学校不存在')
    #     return obj

