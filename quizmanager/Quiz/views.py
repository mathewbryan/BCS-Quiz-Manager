from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from Quiz.models import *
from Quiz.forms import *

# Create your views here.
class List( TemplateView):
    template_name = "Quiz/list.html"
    login_url = '/login/'
    redirect_field_name = 'Quiz/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = QuizModel.objects.all()
        context['questions'] = QuestionsModel.objects.all()
        return context

class Questions(TemplateView):
    template_name = "Quiz/questions.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = QuizModel.objects.get(id=self.kwargs['quiz_id'])
        context['questions'] = QuestionsModel.objects.filter(quiz=self.kwargs['quiz_id'])

        return context
class CreateQuizFormView(TemplateView):
    template_name = "Quiz/add_quiz.html"
    form_classes = {'quiz_form': CreateQuizForm,
                    'question_form': CreateQuestionForm,
                    }
    
    def get(self,request,*args,**kwargs):
        quiz_form = CreateQuizForm()
        question_form = CreateQuestionForm()
        quizes = QuizModel.objects.all()
    
        context = {'quiz_form': quiz_form, 'question_form':question_form, 'quizes':quizes}
        return render(request, 'Quiz/add_quiz.html', context)

    def post(self, request):
        quiz_form = CreateQuizForm()
        question_form = CreateQuestionForm()
        quizes = QuizModel.objects.all()

        action = self.request.POST['action']
        if (action == 'add_quiz'):
            quiz_form = CreateQuizForm(request.POST)
            if quiz_form.is_valid():
                quiz_form.save()
                context = {'quiz_form': quiz_form}
                quiz_form = CreateQuizForm()
                
        elif (action == 'add_question'):
            question_form = CreateQuestionForm(request.POST)
            if question_form.is_valid():
                question_form.save()
                context = {'question_form': question_form}
                question_form = CreateQuestionForm()
        context = {
            'quiz_form': quiz_form,
            'question_form': question_form,
        }
        return render(request, 'Quiz/add_quiz.html', context)


# def create_quiz_form(request):
#     form = CreateQuizForm()
#     form2 = CreateQuestionForm()
#     quizes = QuizModel.objects.all()
#     if request.method == 'POST':
#         form = CreateQuizForm(request.POST)
#         form2 = CreateQuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {'form': form}  
#         if form2.is_valid():
#             form2.save()
#             context = {'form2': form2}  
#     context = {'form': form, 'form2':form2, 'quizes':quizes}
#     return render(request, 'Quiz/add_quiz.html', context)