# Generated by Django 4.2.7 on 2023-11-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kcal', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
