from rest_framework import generics, viewsets

# Create your views here.
from api3.models import Course
from api3.serializers import CourseSerializer
from utils.response import ZhfResponse


class CourseGenericsViews(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.filter(is_delete=False)
    lookup_field = 'id'
    serializer_class = CourseSerializer
    def get(self, request, *args, **kwargs):
        course_id=kwargs.get('id')
        if course_id:
            data=generics.RetrieveUpdateDestroyAPIView.get(self, request, *args, **kwargs).data
            return ZhfResponse(data=data)
        else:
            print(self)
            data=generics.ListCreateAPIView.get(self,request,*args,**kwargs).data
            return ZhfResponse(data=data)


class LoginViews(viewsets.ViewSet):
    def login(self,request):
        request_data=request.data
        course=request_data['course_name']
        course=Course.objects.filter(course_name=course,is_delete=False)[0]
        if not course:
            data={'不存在门课程'}
            return ZhfResponse(data=data)
        teachers=request_data['teachers']
        print('111',teachers)
        teachers=Course.objects.filter(teachers=teachers,course_name=course)[0]
        if not teachers :
            data=('这门课不是这个老师教的，你个假学生，滚粗')
            return ZhfResponse(data=data)
        data={'恭喜你，有这门课程，赶紧滚回来写作业吧！！！'}
        return ZhfResponse(data=data)

    def patch_all(self,request,*args,**kwargs):
        request_data = request.data
        course_id = kwargs.get('id')
        if course_id and isinstance(request_data, dict):
            course_ids = [course_id, ]
            request_data = [request_data]
        elif not course_id and isinstance(request_data, list):
            course_ids = []
            print(request_data)
        else:
            data={'数据有误2'}
            return ZhfResponse(data=data)
        for dic in request_data:
            pk = dic.pop("id", None)
            if pk:
                course_ids.append(pk)
            else:
                data='数据有误'
                return ZhfResponse(data=data)

        course_list = []
        for pk in course_ids:
            course_obj=Course.objects.filter(pk=pk)[0]
            course_list.append(course_obj)
            if not course_obj:
                index = course_ids.index(pk)
                request_data.pop(index)
        print('111',course_list)
        print('222',request_data)
        course_ser = CourseSerializer(data=request_data,instance=course_list,partial=True,many=True)
        course_ser.is_valid(raise_exception=True)
        course_ser.save()
        data={'批量更新成功'}
        return ZhfResponse(data=data)








