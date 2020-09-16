from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api2.models import *
from api2.serializers import *


class BookApiView(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            '''查询单个'''
            book = Book.objects.filter(pk=book_id, is_delete=False)
            if len(book) > 0:
                '''这里只能序列化obj,要序列化QuerySet必须用data='''
                book = BookSerializer(book[0]).data
                return Response({
                    "status": 200,
                    "messages": '查询成功',
                    "result": book,
                })
            else:
                return Response({
                    "status": 200,
                    "messages": '查无此书',
                })
        else:
            '''查询全部'''
            book = Book.objects.filter(is_delete=False)
            print(book)
            if len(book) > 0:
                book = BookSerializer(book,many=True).data
                return Response({
                    "status": 200,
                    "messages": '查询成功',
                    "result": book,
                })
            else:
                return Response({
                    "status": 200,
                    "messages": '抱歉，书库真的空了，一点都没有了',
                })

    def post(self, request, *args, **kwargs):
        '''增加开始了，这里增加多个和一个可以合并'''
        '''这里传的格式应该是[{},{},{}],先判断类型，再进行合并，这里的合并就是所谓的many=True'''
        data=request.data
        if isinstance(data,dict):
            flag=False
        elif isinstance(data,list):
            flag=True
        else:
            return Response({
                "status":500,
                "messages":'数据格式有问题',
            })
        book_ser=BookSerializer(data=data,many=flag)
        book_ser.is_valid(raise_exception=True)
        '''这里是如果验证没通过直接就暴毙，返回错误了'''
        save = book_ser.save()
        '''一定要写save()'''
        print(book_ser)
        return Response({
            "status":200,
            "messages":"添加成功",
            "result":BookSerializer(save,many=flag).data,
        })

    def patch(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, dict):
            flag = False
        elif isinstance(data, list):
            flag = True
        else:
            return Response({
                "status": 500,
                "messages": '数据格式有问题',
            })
        success = '成功局部更新了'
        defeat = "这些书更新失败了:"
        for i in data:
            '''遍历进行更新，这样会慢，但是可以实现'''
            '''先进行数据分离清洗'''
            print(i)
            id = str(i.pop('id'))
            book_obj = Book.objects.filter(pk=id,is_delete=False)[0]
            if book_obj:
                book_ser = BookSerializer(data=i, instance=book_obj,partial=True)
                if book_ser.is_valid():
                    save = book_ser.save()
                    success += id + ","
                else:
                    defeat += "未通过检验：" + id
            else:
                defeat += "没有这本书:" + id
        return Response({
            "status": 200,
            "message": success,
            "result": defeat,
        })

    def put(self, request, *args, **kwargs):
        '''这里传的格式应该是[{},{},{}],先判断类型，再进行合并，这里的合并就是所谓的many=True'''

        # request_data=request.data
        # id=kwargs.get('id')
        # '''这里开始是更新单个'''
        # try:
        #     book_obj = Book.objects.get(pk=id)
        #     '''这里用try是因为get查不到会报错，其实可以换一种写'''
        # except:
        #     return Response({
        #         "status": status.HTTP_400_BAD_REQUEST,
        #         "message": "图书不存在",
        #     })
        # # book_obj=Book.objects.filter(pk=id)
        # # if len(book_obj)<1:
        # #     return Response({
        # #         "status": status.HTTP_400_BAD_REQUEST,
        # #         "message": "图书不存在",
        # #     })
        # book_ser = BookSerializer(data=request_data, instance=book_obj)
        # book_ser.is_valid(raise_exception=True)
        # save = book_ser.save()
        # '''这里save是一条Queryset,所以不用写many=many'''
        # return Response({
        #     "status": 200,
        #     "message": "更新成功",
        #     "results": BookSerializer(save).data
        # })
        '''开始考虑群体更新'''
        data = request.data
        if isinstance(data, dict):
            flag = False
        elif isinstance(data, list):
            flag = True
        else:
            return Response({
                "status": 500,
                "messages": '数据格式有问题',
            })
        success='成功添加了'
        defeat="这些书更新失败了:"
        for i in data:
            '''遍历进行更新，这样会慢，但是可以实现'''
            '''先进行数据分离清洗'''
            print(i)
            id=str(i.pop('id'))
            book_obj=Book.objects.filter(pk=id,is_delete=True)[0]
            if book_obj:
                book_ser=BookSerializer(data=i,instance=book_obj)
                if book_ser.is_valid():
                    save=book_ser.save()
                    success+=id+","
                else:
                    defeat+="未通过检验："+id
            else:
                defeat+="没有这本书:"+id
        return Response({
            "status":200,
            "message":success,
            "result":defeat,
        })

    def delete(self, request, *args, **kwargs):
        '''这里假装与前端沟通好了，传过来{ids:[]}'''
        id=kwargs.get('id')
        '''这个地方是只有一个值'''
        if id:
            ids = [id]
        else:
            '''删除一堆'''
            ids = request.data.get("ids")
        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if response:
            return Response({
                "status": status.HTTP_200_OK,
                "message": "删除成功"
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "删除失败或者图书不存在",
        })


