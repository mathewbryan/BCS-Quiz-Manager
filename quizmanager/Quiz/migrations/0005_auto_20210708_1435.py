# Generated by Django 3.2.5 on 2021-07-08 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_alter_questionsmodel_question_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionsmodel',
            options={'permissions': (('can_edit_questions', 'can_edit_questions'), ('can_view_questions', 'can_view_questions'))},
        ),
        migrations.AlterModelOptions(
            name='quizmodel',
            options={'permissions': (('can_edit_quiz', 'can_edit_quiz'),)},
        ),
    ]
