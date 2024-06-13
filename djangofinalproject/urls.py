from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_student, name='login_student'),
    path('student/index', views.index_student, name='index_student'),
    path('student/sections', views.student_sections),
    path('student/create', views.create_student),
    path('student/store', views.store_student),
    path('student/show/<int:student_id>', views.show_student, name='show_student'),
    path('student/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('student/', views.index_student, name='index_student'),
    path('student/delete/<int:student_id>', views.delete_student),
    path('student/destroy/<int:student_id>', views.destroy_student),
    path('student/academic/add/<int:student_id>', views.add_academic, name='add_academic'),
    path('academic/edit/<int:academic_id>', views.edit_academic, name='edit_academic'),
    path('academic/delete/<int:academic_id>/', views.delete_academic, name='delete_academic'),
    path('academic/view_report/<int:student_id>/', views.view_student_report, name='view_student_report'),
]