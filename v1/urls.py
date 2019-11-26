from django.urls import path
from v1 import views
from v1.models import Comments, Courses, Section_students, Sections, Team_Members, Teams, Threads, Users
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('comments/', views.Comments_List.as_view()),
    path('comments/<int:pk>/', views.Comments_detail.as_view()),
    path('courses/', views.Courses_list.as_view()),
    path('courses/<int:pk>/', views.Courses_detail.as_view()),
    path('section_students/', views.Section_students_list.as_view()),
    path('section_students/<int:pk>/', views.Section_students_detail.as_view()),
    path('sections/', views.Sections_list.as_view()),
    path('sections/<int:pk>/', views.Sections_list.as_view()),
    path('team_members/', views.Team_Members_list.as_view()),
    path('team_members/<int:pk>/', views.Team_Members_detail.as_view()),
    path('teams/', views.Teams_list.as_view()),
    path('teams/<int:pk>/', views.Teams_detail.as_view()),
    path('threads/', views.Threads_list.as_view()),
    path('threads/<int:pk>/', views.Threads_detail.as_view()),
    path('users/', views.Users_list.as_view()),
    path('users/<int:pk>/', views.Users_detail.as_view()),

    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
