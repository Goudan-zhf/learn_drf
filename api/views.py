from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Employee
from api.serializers import EmployeeSerializer,EmployeeDeSerializer

# Create your views here.
class EmpApiViews(APIView):
    def get(self,request,*args,**kwargs):
        user_id=kwargs.get('id')
        if user_id:
            emp=Employee.objects.get(pk=user_id)
            '''开始自动序列化'''
            emp_ser=EmployeeSerializer(emp).data
            return Response({
                "status":200,
                "message":'查询单个成功',
                "result":emp_ser
            })
        else:
            '''开始查询所有'''
            emp_all=Employee.objects.all()
            emp_all=EmployeeSerializer(emp_all,many=True).data
            return Response({
                "status":200,
                "message":'查询全部员工成功',
                "result":emp_all,
            })


    def post(self,request,*args,**kwargs):
        user_data=request.data
        print(user_data)
        '''先进行数据类型判断'''
        if not isinstance(user_data,dict) or user_data=={}:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":'你他娘的发歪啦'
            })
        ser=EmployeeDeSerializer(data=user_data)
        if ser.is_valid():
            rst=ser.save()
            return Response({
                "status":status.HTTP_200_OK,
                "message":'用户成功存进去了',
                "result":EmployeeSerializer(rst).data
            })
        return Response({
            "status":status.HTTP_400_BAD_REQUEST,
            "message":ser.errors
        })
