# Generated by Django 5.1.3 on 2024-12-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='micro_degree',
            new_name='majortype',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='second_major',
            new_name='microdegree',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_id',
            new_name='studentId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='major_type',
        ),
        migrations.AddField(
            model_name='user',
            name='secondmajor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
