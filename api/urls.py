from django.urls import path,include
from api import views

urlpatterns=[
    path('emps/', views.EmpApiViews.as_view()),
    path('emps/<str:id>', views.EmpApiViews.as_view()),
]