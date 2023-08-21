# Generated by Django 4.2.4 on 2023-08-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_remove_tag_survey_survey_tags_tag_surveys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='surveys',
        ),
        migrations.AlterField(
            model_name='survey',
            name='tags',
            field=models.ManyToManyField(related_name='surveys', to='surveys.tag'),
        ),
    ]
