from django.contrib import admin
from .models import *
# Register your models here.
class QuestionInline(admin.TabularInline):
    model = QuestionsModel


class QuizModelAdmin(admin.ModelAdmin):
    list_display = ["quiz_title"]
    # list_select_related = ["quiz_title"]
    search_fields = ["quiz_title"]
    inlines = [
        QuestionInline,
    ]


admin.site.register(QuizModel, QuizModelAdmin)
# admin.site.register([QuizModel, QuestionsModel])