from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete-student/<int:sid>/',views.delete_student,name='delete-student'),
    path('delete-all-students/',views.delete_all_students,name='delete-all-students'),
    path('api/list/',views.ListView.as_view()),
    path('api/create/',views.CreateView.as_view()),
    path('api/<int:pk>/detail/',views.DetailView.as_view()),
    path('api/update/<int:pk>/',views.UpdateView.as_view()),
    path('api/delete/<int:pk>/',views.DeleteView.as_view()),
]
