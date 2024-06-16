# Generated by Django 5.0.6 on 2024-06-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_user_organisation_sector"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                default="Москва", max_length=128, verbose_name="Город"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="country",
            field=models.CharField(
                default="Россия", max_length=128, verbose_name="Страна"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(default="Иван", max_length=255, verbose_name="Имя"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="inn",
            field=models.CharField(
                default="1111111111", max_length=25, verbose_name="ИНН"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                default="Иванов", max_length=255, verbose_name="Фамилия"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="organisation",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Наименование организации",
            ),
        ),
    ]
