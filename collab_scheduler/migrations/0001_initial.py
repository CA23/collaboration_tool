# Generated by Django 2.1.4 on 2018-12-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=50)),
                ('available_from', models.IntegerField()),
                ('available_until', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
