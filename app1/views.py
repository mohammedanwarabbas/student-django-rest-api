from django.shortcuts import render,redirect
from . import models
from rest_framework import generics
from .serializers import StudentSerializer

# Create your views here.
def home(req):
    students = models.Student.objects.all()
    context_data =  {'students':students}
    return render(req,'index.html',context_data)

def delete_student(req,sid):
    student = models.Student.objects.get(pk=sid)
    student.delete()
    return redirect('home')

def delete_all_students(req):
    students = models.Student.objects.all()
    for student in students:
        student.delete()
    return redirect('home')

class ListView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class CreateView(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer