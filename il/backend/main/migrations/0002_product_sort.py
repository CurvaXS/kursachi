# Generated by Django 5.0.3 on 2024-03-20 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sort',
            field=models.CharField(choices=[('Говядина', 'Говядина'), ('Свинина', 'Свинина'), ('Курица', 'Курица'), ('Колбасы', 'Колбасы')], default='', max_length=10),
        ),
    ]
