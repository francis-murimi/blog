# Generated by Django 4.0.3 on 2022-10-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_alter_post_status_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]