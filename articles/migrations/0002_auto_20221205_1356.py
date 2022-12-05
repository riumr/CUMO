# Generated by Django 3.2.13 on 2022-12-05 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='singer',
        ),
        migrations.AlterField(
            model_name='article',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.song'),
        ),
    ]