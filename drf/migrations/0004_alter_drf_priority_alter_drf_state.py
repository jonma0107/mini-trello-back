# Generated by Django 4.1.3 on 2023-02-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0003_remove_drf_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drf',
            name='priority',
            field=models.IntegerField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')]),
        ),
        migrations.AlterField(
            model_name='drf',
            name='state',
            field=models.IntegerField(choices=[('BACKLOG', 'BACKLOG'), ('TO DO', 'TO DO'), ('DOING', 'DOING'), ('TEST', 'TEST'), ('DONE', 'DONE')]),
        ),
    ]
