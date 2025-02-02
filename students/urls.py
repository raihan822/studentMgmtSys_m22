from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
]
