# Generated by Django 2.0.1 on 2018-10-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar', models.CharField(max_length=120)),
                ('eng', models.CharField(max_length=120)),
            ],
        ),
    ]