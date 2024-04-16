from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    def get_questions(self):
        return self.questions.all()
    
class Question(models.Model):
    body = models.CharField(max_length=200, null=False, blank=False)
    correct = models.IntegerField(null=False, blank=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    body = models.CharField(max_length=200, null=False, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
