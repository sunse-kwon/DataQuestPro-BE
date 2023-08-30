# Generated by Django 4.2.4 on 2023-08-30 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnum', models.IntegerField()),
                ('type', models.CharField(choices=[('scale', 'Scale'), ('open', 'Open-ended')], max_length=10)),
                ('is_required', models.BooleanField(default=False)),
                ('question_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True, null=True)),
                ('answer_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.answeroption')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.question')),
                ('useranswer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.useranswer')),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='surveys', to='surveys.tag'),
        ),
        migrations.AddField(
            model_name='survey',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.survey'),
        ),
        migrations.AddField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.question'),
        ),
    ]
