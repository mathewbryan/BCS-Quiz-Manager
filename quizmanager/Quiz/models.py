from django.db import models

# Create your models here.
# Database model for the quiz table
class QuizModel(models.Model):
    quiz_title = models.CharField(max_length=150, null=False, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    questions = models.ForeignKey('Quiz.QuestionsModel', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.quiz_title
# Database model for the question/ answer table
class QuestionsModel(models.Model):
    quiz = models.ForeignKey('Quiz.QuizModel', on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200, null=False, blank=False)
    question_number = models.IntegerField(null=True, blank=True)
    correct_answer = models.CharField(max_length=200, null=True, blank=True)
    answer_1 = models.CharField(max_length=200, null=False, blank=False)
    answer_2 = models.CharField(max_length=200, null=False, blank=False)
    answer_3 = models.CharField(max_length=200, null=True, blank=True)
    answer_4 = models.CharField(max_length=200, null=True, blank=True)
    answer_5 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question_title
    

