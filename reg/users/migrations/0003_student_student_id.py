# Generated by Django 3.1.1 on 2020-09-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=6010613468, max_length=8),
            preserve_default=False,
        ),
    ]
