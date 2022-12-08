from django.urls import path
from parties import views

urlpatterns = [
    path('parties/', views.PartyList.as_view()),
    path('parties/<int:pk>/', views.PartyDetail.as_view()),
]
