# Generated by Django 4.0.5 on 2022-07-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]