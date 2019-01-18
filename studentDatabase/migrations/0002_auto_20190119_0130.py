# Generated by Django 2.1.5 on 2019-01-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_phone_number',
            field=models.CharField(default='011', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentfather',
            name='father_phone_number',
            field=models.CharField(default='011', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentmother',
            name='mother_phone_number',
            field=models.CharField(default='011', max_length=50),
            preserve_default=False,
        ),
    ]