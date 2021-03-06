"""quizmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from Quiz.views import *
# from django.conf import settings
app_name = 'quiz'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List.as_view()),
    path('quiz/<int:quiz_id>/', Questions.as_view()),
    path('add-quiz/', CreateQuizFormView.as_view()),
    path('quiz/<int:quiz_id>/add-quiz/', CreateQuizFormView.as_view()),
    path('', include('django.contrib.auth.urls')),
    path('quiz/<int:quiz_id>/edit-quiz/', EditQuizFormView.as_view()),
    path('quiz/<int:quiz_id>/edit-question/<int:question_id>/', EditQuestionFormView.as_view()),
    path('add-question/', CreateQuestionFormView.as_view()),
    path('add-question/<int:quiz_id>', CreateQuestionFormView.as_view()),
]
