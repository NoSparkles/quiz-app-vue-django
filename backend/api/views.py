from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from . import models, serializers

class QuizCreateAPIView(CreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizCreateSerializer

class QuizListAPIView(ListAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizListSerializer

class QuizRetrieveAPIView(RetrieveAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizRetrieveSerializer