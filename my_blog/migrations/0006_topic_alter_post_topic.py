# Generated by Django 5.2.3 on 2025-07-12 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0005_alter_post_topic_delete_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.topic'),
        ),
    ]
