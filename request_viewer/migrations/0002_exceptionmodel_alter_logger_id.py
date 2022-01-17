# Generated by Django 4.0.1 on 2022-01-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExceptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exc_type', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True, null=True)),
                ('func_name', models.CharField(max_length=1024)),
                ('line_no', models.IntegerField()),
                ('line', models.TextField(blank=True, null=True)),
                ('stacks', models.JSONField(default=list)),
                ('logged_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='logger',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
