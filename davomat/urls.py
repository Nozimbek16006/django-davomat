from django.urls import path
from .views import *

urlpatterns = [
    path('', dates_list, name='dates_list'),
    path('dates_with_course/<uuid:id>', dates_with_course, name='dates_with_course'),
    path('course_detail/<uuid:id>', course_detail, name='course_detail'),
    path('course_students/<uuid:id>', course_students, name='course_students'),
]