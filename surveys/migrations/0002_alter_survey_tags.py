# Generated by Django 4.2.4 on 2023-08-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='surveys', to='surveys.tag'),
        ),
    ]
