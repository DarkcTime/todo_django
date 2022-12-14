# Generated by Django 4.1.2 on 2022-10-11 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2022-10-11')),
                ('due_date', models.DateField(default='2022-10-11')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todolist.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
