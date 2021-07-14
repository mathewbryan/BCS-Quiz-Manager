from django.http.response import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.apps import apps
from Quiz.models import *
from Quiz.forms import *

# Create your views here.

# Redirect users to the List view if they do not have the correct permissions
class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args,**kwargs):
        if not request.user.is_authenticated: # in Django > 3 this is a boolean
            return redirect('/login/')    
        if not self.has_permission():
            return redirect('/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

class List(LoginRequiredMixin, TemplateView):
    template_name = "Quiz/list.html"
    login_url = '/login/'
    redirect_field_name = 'Quiz/login.html'

    # Creating view context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizzes'] = QuizModel.objects.all()
        context['questions'] = QuestionsModel.objects.all()
        return context

class Questions(LoginRequiredMixin, TemplateView):
    template_name = "Quiz/questions.html"

    # Creating view context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.permissions = self.request.user.user_permissions.all()
        if self.permissions.exists:
            self.permissions_list = []
            for perm in self.permissions:
                 self.permissions_list.append(perm.name)

        context['quizzes'] = QuizModel.objects.get(id=self.kwargs['quiz_id'])
        context['questions'] = QuestionsModel.objects.filter(quiz=self.kwargs['quiz_id']).order_by('question_number')
        context['permissions'] = self.permissions_list

        return context
class CreateQuizFormView(LoginRequiredMixin, UserAccessMixin, TemplateView):
    template_name = "Quiz/add_quiz.html"
    form_classes = {'quiz_form': CreateQuizForm,
                    'question_form': CreateQuestionForm,
                    }

    permission_required = ('can_edit_quiz','can_edit_questions','can_view_questions', 'can_view_answers')
    permission_denied_message = "Permission Denied - You do not have the correct level of permissions"

    # Get the intial form and present it to the user
    def get(self,request,*args,**kwargs):
        quiz_form = CreateQuizForm()
        question_form = CreateQuestionForm()
        quizes = QuizModel.objects.all()
    
        context = {'quiz_form': quiz_form, 'question_form':question_form, 'quizes':quizes}
        return render(request, 'Quiz/add_quiz.html', context)

    # Handling the form post request
    def post(self, request, *args,**kwargs):
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
        # Redirect to main page on submition
        return HttpResponsePermanentRedirect("/")
# View to create a new Question via a form
class CreateQuestionFormView(LoginRequiredMixin, UserAccessMixin, TemplateView):
    template_name = "Quiz/add_question.html"
    form_classes = {'question_form': CreateQuestionForm,
                    }

    permission_required = ('can_edit_quiz','can_edit_questions','can_view_questions', 'can_view_answers')
    permission_denied_message = "Permission Denied - You do not have the correct level of permissions"

    def get(self,request,*args,**kwargs):
        quiz_id = self.kwargs['quiz_id']
        question_form = CreateQuestionForm(initial={'quiz': quiz_id})
        quizes = QuizModel.objects.all()
    
        context = {'question_form':question_form, 'quizes':quizes}
        return render(request, 'Quiz/add_question.html', context)

    # Handling the form post request
    def post(self, request,*args,**kwargs):
        quiz_id = self.kwargs['quiz_id']
        question_form = CreateQuestionForm()
        quiz = QuizModel.objects.get(id=quiz_id)
    
        action = self.request.POST['action']
       
        if action == 'add_question':
            question_form = CreateQuestionForm(request.POST)
            if question_form.is_valid():
                question_form.save()
                context = {'question_form': question_form}
                question_form = CreateQuestionForm()
        context = {
            'question_form': question_form,
            "quiz_id":quiz_id   
        }
        # Redirect to main page on submition 
        return HttpResponsePermanentRedirect(f'/quiz/{quiz_id}')
        
# View to edit Quizzes via a for
class EditQuizFormView(LoginRequiredMixin, UserAccessMixin, TemplateView):
    template_name = "Quiz/edit_quiz.html"
    form_classes = {'edit_quiz_form': EditQuizForm,
                    'edit_question_form': EditQuestionForm,
                    }
    
    permission_required = ('can_edit_quiz','can_edit_questions','.can_view_questions', 'can_view_answers')
    permission_denied_message = "Permission Denied - You do not have the correct level of permissions"

     # Get the intial form and present it to the user
    def get(self,request,*args,**kwargs):
        quiz_id = self.kwargs['quiz_id']
        quizes = QuizModel.objects.get(id=quiz_id)
        questions = QuestionsModel.objects.filter(quiz=quiz_id)
        edit_quiz_form = EditQuizForm(instance=quizes)
        edit_question_form = EditQuestionForm()
    
        context = {'edit_quiz_form': edit_quiz_form, 'edit_question_form':edit_question_form, 'quizes':quizes}
        return render(request, 'Quiz/edit_quiz.html', context)

    # Handling the form post request
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
                
        context = {
            'edit_quiz_form': edit_quiz_form,
        }
        # Redirect to previous page on submition
        return HttpResponsePermanentRedirect(f"/quiz/{quiz_id}/")

class EditQuestionFormView(LoginRequiredMixin,UserAccessMixin, TemplateView):
    template_name = "Quiz/edit_question.html"
    form_classes = {'edit_quiz_form': EditQuizForm,
                    'edit_question_form': EditQuestionForm,
                    }

    permission_required = ('can_edit_questions','.can_view_questions', 'can_view_answers')
    permission_denied_message = "Permission Denied - You do not have the correct level of permissions"

    # Get the intial form and present it to the user
    def get(self,request,*args,**kwargs):
        quiz_id = self.kwargs['quiz_id']
        queistion_id = self.kwargs['question_id']
        quizes = QuizModel.objects.get(id=quiz_id)
        # questions = QuestionsModel.objects.filter(quiz=quiz_id)
        question = QuestionsModel.objects.get(id=queistion_id)
        edit_question_form = EditQuestionForm(instance=question)
    
        context = {'edit_question_form':edit_question_form, 'quizes':quizes}
        return render(request, 'Quiz/edit_question.html', context)
    
    # Handling the form post request
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
        # Redirect to previous page on submition
        return HttpResponsePermanentRedirect(f"/quiz/{quiz_id}/")