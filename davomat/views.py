from django.shortcuts import render, get_object_or_404
from .models import *

def dates_list(request):
    dates = Dates.objects.all()
    context = {
        'dates': dates
    }
    return render(request, 'davomat/dates_list.html', context)



def dates_with_course(request, id):
    find_course = get_object_or_404(Dates, course=id)
    context = {
        'courses': find_course
    }
    return render(request, 'davomat/dates_with_course.html', context)

def course_detail(request, id):
    course = get_object_or_404(Courses, id=id)
    context = {
        'course': course
    }
    return render(request, 'davomat/course_detail.html', context)

def course_students(request, id):
    id = Courses.objects.get(id=id)
    students = Students.objects.filter(course=id)
    context = {
        'students': students
    }
    return render(request, 'davomat/course_students.html', context)