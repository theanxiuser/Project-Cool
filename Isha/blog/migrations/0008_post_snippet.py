# Generated by Django 3.1.2 on 2021-02-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210224_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to read blog post.', max_length=250),
        ),
    ]
