from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Academic
from django.contrib import messages

# Create your views here.

def login_student(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student/login.html', context)

def index_student(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student/index.html', context)

def student_sections(request):
    students = Student.objects.all()
    context = {
        'students': students, 
    }
    return render(request, 'student/sections.html', context)

def create_student(request):
    student = Student.objects.all()

    context = {
        'student' : student
    }

    return render(request, 'student/create.html', context)

def store_student(request):
    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    birth_date = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    contact = request.POST.get('contact')

    Student.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, age=age, 
                            birth_date=birth_date, gender=gender, address=address, contact=contact)
    
    messages.success(request, 'Student successfully added!')
    return redirect('/student/sections')
    
def show_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    academics = Academic.objects.filter(student=student)
    context = {
        'student': student,
        'academics': academics,
    }
    return render(request, 'student/show.html', context)

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.middle_name = request.POST.get('middle_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.birth_date = request.POST.get('birth_date')
        student.gender = request.POST.get('gender')
        student.address = request.POST.get('address')
        student.contact = request.POST.get('contact')
        student.save()

        messages.success(request, 'Student information updated successfully!')
        return redirect('/student/sections')

    context = {
        'student': student,
    }

    return render(request, 'student/edit.html', context)
    

def delete_student(request, student_id):
    student = Student.objects.get(pk = student_id)

    context = {
        'student' : student,
    }

    return render(request, 'student/delete.html', context)

def destroy_student(request, student_id):
    Student.objects.filter(pk = student_id).delete()
    messages.success(request, 'Student successfully deleted.')

    return redirect('/student/sections')

def add_academic(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        course = request.POST.get('course')
        year_level = request.POST.get('year_level')
        section = request.POST.get('section')
        semester = request.POST.get('semester')
        ay = request.POST.get('ay')
        classification = request.POST.get('classification')
        id_number = request.POST.get('id_number')
        
        Academic.objects.create(student=student, course=course, year_level=year_level, section=section, 
                                semester=semester, ay=ay, classification=classification, id_number=id_number)
        messages.success(request, 'Academic information added successfully!')
        return redirect('show_student', student_id=student.student_id)
    
    context = {
        'student': student
    }
    return render(request, 'student/academic/add.html', context)

def edit_academic(request, academic_id):
    academic = get_object_or_404(Academic, pk=academic_id)
    student = academic.student
    
    if request.method == 'POST':
        academic.id_number = request.POST.get('id_number')
        academic.course = request.POST.get('course')
        academic.year_level = request.POST.get('year_level')
        academic.section = request.POST.get('section')
        academic.semester = request.POST.get('semester')
        academic.ay = request.POST.get('ay')
        academic.classification = request.POST.get('classification')
        academic.save()
        
        messages.success(request, 'Academic information updated successfully!')
        return redirect('show_student', student_id=student.student_id)
    
    context = {
        'academic': academic,
        'student': student,
    }
    return render(request, 'student/academic/edit.html', context)

def delete_academic(request, academic_id):
    academic = get_object_or_404(Academic, pk=academic_id)
    student_id = academic.student.pk
    if request.method == 'POST':
        academic.delete()
        messages.success(request, 'Academic information deleted successfully!')
        return redirect('show_student', student_id=student_id)
    
    context = {
        'academic': academic
    }
    return render(request, 'student/academic/delete.html', context)

def view_student_report(request, student_id):
    student = Student.objects.get(pk=student_id)
    academics = Academic.objects.filter(student=student)
    context = {
        'student': student,
        'academics': academics
    }
    return render(request, 'student/academic/view_student_report.html', context)