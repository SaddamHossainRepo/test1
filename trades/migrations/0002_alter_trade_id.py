# Generated by Django 5.0.6 on 2024-06-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
