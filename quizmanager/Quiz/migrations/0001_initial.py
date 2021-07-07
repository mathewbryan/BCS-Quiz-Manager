# Generated by Django 3.2.5 on 2021-07-06 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('question_number', models.IntegerField()),
                ('correct_answer', models.CharField(max_length=200)),
                ('answer_1', models.CharField(blank=True, max_length=200, null=True)),
                ('answer_2', models.CharField(blank=True, max_length=200, null=True)),
                ('answer_3', models.CharField(blank=True, max_length=200, null=True)),
                ('answer_4', models.CharField(blank=True, max_length=200, null=True)),
                ('answer_5', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=150)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.questionsmodel')),
            ],
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.quizmodel'),
        ),
    ]