from django.urls import path
from v1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('emails/', views.email_list.as_view()),
    # path('emails/<int:pk>/', views.email_detail.as_view()),
    # path('users/', views.user_list.as_view()),
    # path('users/<int:pk>/', views.user_detail.as_view()),
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
