# import form class from django
from django import forms
  
# import from models.py
from .models import *
  
# create a ModelForm
class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = ['quiz_title',]

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ['quiz', 'question_title', 'answer_1', 'answer_2','answer_3','answer_4','answer_5',]

class EditQuizForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = ['quiz_title',]

class EditQuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ['quiz', 'question_title', 'answer_1', 'answer_2','answer_3','answer_4','answer_5',]