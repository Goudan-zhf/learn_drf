from django.urls import path,include
from api2 import views

urlpatterns=[
    path('books/', views.BookApiView.as_view()),
    path('books/<str:id>/', views.BookApiView.as_view()),
]