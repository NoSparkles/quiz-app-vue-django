from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . import models
  
class AnswerSerializer(ModelSerializer):
  class Meta:
    model = models.Answer
    fields = [
        'id',
        'body',
    ]

class QuestionSerializer(ModelSerializer):
  answers = AnswerSerializer(many=True)
  class Meta:
    model = models.Question
    fields = [
        'id',
        'body',
        'correct',
        'answers'
    ]
  def get_answers(self, question):
    return AnswerSerializer(question.get_answers(), many=True).data

class QuizCreateSerializer(ModelSerializer):
  questions = QuestionSerializer(many=True)
  class Meta:
    model = models.Quiz
    fields = [
        'id',
        'title',
        'questions'
    ]
  
  def create(self, validated_data):
    questions_data = validated_data.pop('questions')
    quiz = models.Quiz.objects.create(**validated_data)
    for question_data in questions_data:
      answers_data = question_data.pop('answers')
      question = models.Question.objects.create(quiz=quiz, **question_data)
      for answer_data in answers_data:
        models.Answer.objects.create(question=question, **answer_data)
    return quiz
  
class QuizListSerializer(ModelSerializer):
  numOfQuestions = serializers.SerializerMethodField()
  class Meta:
    model = models.Quiz
    fields = [
        'id',
        'title',
        'numOfQuestions'
    ]

  def get_numOfQuestions(self, quiz):
    return quiz.get_questions().count()
  
class QuizRetrieveDestroySerializer(ModelSerializer):
  questions = QuestionSerializer(many=True)
  class Meta:
    model = models.Quiz
    fields = [
        'id',
        'title',
        'questions'
    ]