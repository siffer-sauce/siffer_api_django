# Generated by Django 2.2 on 2022-01-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='instruction',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='site',
            name='status',
            field=models.CharField(default='failed', max_length=100),
        ),
        migrations.AddField(
            model_name='site',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='encoding',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='site',
            name='iframe',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='match',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='site',
            name='sitename',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='site',
            name='standard',
            field=models.CharField(default='', max_length=300),
        ),
    ]
