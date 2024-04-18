from django.urls import path

from . import views

urlpatterns = [
    path('quizes/', views.QuizListAPIView.as_view()),
    path('quizes/<int:pk>/', views.QuizRetrieveDestroyAPIView.as_view()),
    path('create/', views.QuizCreateAPIView.as_view()),
]
