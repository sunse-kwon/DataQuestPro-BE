# Generated by Django 4.2.4 on 2023-08-24 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0015_rename_answer_answeroption_remove_tag_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='answer_point',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.CreateModel(
            name='UserAnswerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True)),
                ('answer_point', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.answeroption')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.question')),
                ('useranswer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.useranswer')),
            ],
        ),
    ]
