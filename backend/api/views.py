from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView

from . import models, serializers

class QuizCreateAPIView(CreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizCreateSerializer

class QuizListAPIView(ListAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizListSerializer

class QuizRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizRetrieveDestroySerializer