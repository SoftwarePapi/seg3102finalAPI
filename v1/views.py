from django.shortcuts import render

from django.contrib.auth.mixins import UserPassesTestMixin

from v1.models import Comments, Courses, Section_students, Sections, Team_Members, Teams, Threads, Users
from v1.serializers import CommentsSerializer, CoursesSerializer, Section_studentsSerializer
from v1.serializers import SectionsSerializer, Team_MembersSerializer, TeamsSerializer, ThreadsSerializer, UsersSerializer
#from v1.permissions import IsOwnerOrReadOnly <-- not implemented

from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response

# Create your views here.
class Comments_List(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

#RetrieveUpdateDestroyAPIView
#RetrieveAPIView sets to readonly
class Comments_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class Users_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    # def get_queryset(self):
    #     import pdb;pdb.set_trace()
    #     return Users.objects.filter(**self.request.query_params)

class Users_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class Courses_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class Courses_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class Section_students_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Section_students.objects.all()
    serializer_class = Section_studentsSerializer

class Section_students_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Section_students.objects.all()
    serializer_class = Section_studentsSerializer

class Sections_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer

class Sections_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer

class Team_Members_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Team_Members.objects.all()
    serializer_class = Team_MembersSerializer

class Team_Members_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Team_Members.objects.all()
    serializer_class = Team_MembersSerializer

class Teams_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class Teams_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class Threads_list(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer

class Threads_detail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAdminUser]

    queryset = Threads.objects.all()
    serializer_class = ThreadsSerializer
