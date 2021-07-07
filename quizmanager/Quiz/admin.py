from django.contrib import admin
from .models import *
# Register your models here.
class QuestionInline(admin.TabularInline):
    model = QuestionsModel
    fields = ('quiz', 'question_title', 'question_number', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5')

class QuizModelAdmin(admin.ModelAdmin):
    list_display = ["quiz_title" ]
    list_select_related = ["questions"]
    search_fields = ["quiz_title"]
    inlines = [
        QuestionInline,
    ]

class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = ["question_title"]
    search_fields = ["question_title"]

admin.site.register(QuizModel, QuizModelAdmin)
admin.site.register(QuestionsModel, QuestionsModelAdmin)