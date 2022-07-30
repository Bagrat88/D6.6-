# Generated by Django 4.0.6 on 2022-07-29 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News_Portal', '0003_category_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='News_Portal.category', verbose_name='Категория'),
        ),
    ]