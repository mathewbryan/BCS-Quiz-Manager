# import form class from django
from django import forms
  
# import from models.py
from .models import *
  
# create a ModelForm
class CreateQuizForm(forms.ModelForm):
    quiz_title = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    class Meta:
        model = QuizModel
        fields = ['quiz_title',]

class CreateQuestionForm(forms.ModelForm):
    question_title = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    answer_1 = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    answer_2 = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    answer_3 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    answer_4 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    answer_5 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    class Meta:
        model = QuestionsModel
        fields = ['quiz', 'question_title', 'answer_1', 'answer_2','answer_3','answer_4','answer_5',]

class EditQuizForm(forms.ModelForm):
    quiz_title = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}))
    class Meta:
        model = QuizModel
        fields = ['quiz_title',]

class EditQuestionForm(forms.ModelForm):
    question_title = forms.CharField(widget=forms.TextInput(attrs={'size': '75'}))
    answer_1 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    answer_2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    answer_3 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    answer_4 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    answer_5 = forms.CharField(required=False,widget=forms.TextInput(attrs={'size': '50'}))
    class Meta:
        model = QuestionsModel
        fields = ['quiz', 'question_title', 'answer_1', 'answer_2','answer_3','answer_4','answer_5',]