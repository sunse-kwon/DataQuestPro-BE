# Generated by Django 4.2.4 on 2023-08-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('targets', models.TextField()),
                ('purpose', models.CharField(choices=[('register', 'Register')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
