# Generated by Django 4.0.3 on 2022-03-21 09:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0013_article_author_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='users',
            field=models.ManyToManyField(related_name='articles_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ManyToManyField(related_name='comments_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
