# Generated by Django 5.0.6 on 2024-06-14 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistent_app', '0004_alter_chatmessagemodel_is_filter_question'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filterfields',
            name='chat_message',
        ),
        migrations.CreateModel(
            name='FilterConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddField(
            model_name='chatmessagemodel',
            name='filter_model',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assistent_app.filterconfig'),
        ),
        migrations.AddField(
            model_name='filterfields',
            name='model_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assistent_app.filterconfig', verbose_name='Модель фильтрации'),
        ),
        migrations.AddIndex(
            model_name='filterconfig',
            index=models.Index(fields=['model_class'], name='assistent_a_model_c_991a5c_idx'),
        ),
    ]