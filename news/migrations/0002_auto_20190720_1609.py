# Generated by Django 2.2.2 on 2019-07-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('0', 'Politics'), ('1', 'Sports'), ('2', 'International'), ('3', 'Entertainment'), ('4', 'Local News'), ('5', 'Valley News')], max_length=2),
        ),
        migrations.AlterField(
            model_name='news',
            name='story',
            field=models.TextField(verbose_name='article'),
        ),
    ]
