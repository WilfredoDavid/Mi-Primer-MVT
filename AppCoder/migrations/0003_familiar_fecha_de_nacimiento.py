# Generated by Django 4.1 on 2022-08-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_familiar_delete_curso_delete_enregable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_de_nacimiento',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
