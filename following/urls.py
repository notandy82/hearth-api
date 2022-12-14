from django.urls import path
from following import views

urlpatterns = [
    path('following/', views.FollowingList.as_view()),
    path('following/<int:pk>/', views.FollowingDetail.as_view())
]
