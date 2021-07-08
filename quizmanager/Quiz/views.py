from collections import UserDict, UserList
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from Quiz.models import *
from Quiz.forms import *

# Create your views here.
class List(LoginRequiredMixin, TemplateView):
    template_name = "Quiz/list.html"
    login_url = '/login/'
    redirect_field_name = 'Quiz/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = QuizModel.objects.all()
        context['questions'] = QuestionsModel.objects.all()
        return context

class Questions(LoginRequiredMixin, TemplateView):
    template_name = "Quiz/questions.html"
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['quizzes'] = QuizModel.objects.get(id=self.kwargs['quiz_id'])
        context['questions'] = QuestionsModel.objects.filter(quiz=self.kwargs['quiz_id'])

        return context
class CreateQuizFormView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "Quiz/add_quiz.html"
    form_classes = {'quiz_form': CreateQuizForm,
                    'question_form': CreateQuestionForm,
                    }

    permission_required = ('can_edit_quiz','can_edit_questions','can_view_questions', 'can_view_answers')
    
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

class EditQuizFormView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "Quiz/edit_quiz.html"
    form_classes = {'edit_quiz_form': EditQuizForm,
                    'edit_question_form': EditQuestionForm,
                    }
    
    permission_required = ('can_edit_quiz','can_edit_questions','.can_view_questions', 'can_view_answers')

    def get(self,request,*args,**kwargs):
        quiz_id = self.kwargs['quiz_id']
        quizes = QuizModel.objects.get(id=quiz_id)
        questions = QuestionsModel.objects.filter(quiz=quiz_id)
        edit_quiz_form = EditQuizForm(instance=quizes)
        edit_question_form = EditQuestionForm()
        # edit_question_formset_factory = formset_factory(EditQuestionForm, extra=10)

    
        context = {'edit_quiz_form': edit_quiz_form, 'edit_question_form':edit_question_form, 'quizes':quizes}
        return render(request, 'Quiz/edit_quiz.html', context)

    def post(self, request, *args, **kwargs):
        edit_quiz_form = EditQuizForm()
        edit_question_form = EditQuestionForm()

        quiz_id = self.kwargs['quiz_id']

        delete_quiz = request.POST.get('delete-quiz')

        action = self.request.POST['action']
        if delete_quiz is not None:
            quiz_to_edit = QuizModel.objects.get(id=quiz_id)  
            quiz_to_edit.delete()
            # TODO redirect somewhere else when form saved
            edit_quiz_form = EditQuizForm()
        elif action == 'add_quiz':
            edit_quiz_form = EditQuizForm(request.POST)
            quiz_to_edit = QuizModel.objects.get(id=quiz_id)
            if edit_quiz_form.is_valid():
                edit_quiz_form = EditQuizForm(request.POST, instance=quiz_to_edit)
                edit_quiz_form.save()
                context = {'edit_quiz_form': edit_quiz_form}
                # TODO redirect somewhere else when form saved
                edit_quiz_form = EditQuizForm()
                
        # elif action == 'add_question':
        #     edit_question_form = EditQuestionForm(request.POST)
        #     if edit_question_form.is_valid():
        #         edit_question_form.save()
        #         context = {'edit_question_form': edit_question_form}
        #         # TODO redirect somewhere else when form saved
        #         edit_question_form = EditQuestionForm()
        context = {
            'edit_quiz_form': edit_quiz_form,
            # 'edit_question_form': edit_question_form,
        }
        return render(request, 'Quiz/edit_quiz.html', context)

class EditQuestionFormView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "Quiz/edit_question.html"
    form_classes = {'edit_quiz_form': EditQuizForm,
                    'edit_question_form': EditQuestionForm,
                    }

    permission_required = ('can_edit_questions','.can_view_questions', 'can_view_answers')

    def get(self,request,*args,**kwargs):
        quiz_id = self.kwargs['quiz_id']
        queistion_id = self.kwargs['question_id']
        quizes = QuizModel.objects.get(id=quiz_id)
        # questions = QuestionsModel.objects.filter(quiz=quiz_id)
        question = QuestionsModel.objects.get(id=queistion_id)
        edit_question_form = EditQuestionForm(instance=question)


    
        context = {'edit_question_form':edit_question_form, 'quizes':quizes}
        return render(request, 'Quiz/edit_question.html', context)
    
    def post(self, request, *args, **kwargs):
        queistion_id = self.kwargs['question_id']
        edit_question_form = EditQuestionForm()

        quiz_id = self.kwargs['quiz_id']
        delete_question = request.POST.get('delete-question')
        action = self.request.POST['action']
        if delete_question is not None:
            question_to_edit = QuestionsModel.objects.get(id=queistion_id)  
            question_to_edit.delete()
            # TODO redirect somewhere else when form saved
            edit_question_form = EditQuestionForm()
        elif action == 'edit_question':
            edit_question_form = EditQuestionForm(request.POST)
            question_to_edit = QuestionsModel.objects.get(id=queistion_id)
  
            if edit_question_form.is_valid():
                edit_question_form = EditQuestionForm(request.POST, instance=question_to_edit)
                edit_question_form.save()
                context = {'edit_question_form': edit_question_form}
                # TODO redirect somewhere else when form saved
                edit_question_form = EditQuestionForm()
        context = {
            'edit_question_form': edit_question_form,
        }
        return render(request, 'Quiz/edit_question.html', context)
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