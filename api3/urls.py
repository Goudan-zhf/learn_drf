from django.urls import path,include
from api3 import views
urlpatterns = [
    path('course/', views.CourseGenericsViews.as_view()),
    path('course/<str:id>/', views.CourseGenericsViews.as_view()),
    path('zhf/',views.LoginViews.as_view({"post":"login","patch":"patch_all"}))

]