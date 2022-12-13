from django.urls import path
from dates import views

urlpatterns = [
    path('dates/', views.EventList.as_view()),
]
