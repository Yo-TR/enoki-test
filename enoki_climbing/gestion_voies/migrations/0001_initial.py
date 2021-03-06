# Generated by Django 3.1.2 on 2021-08-14 21:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import gestion_voies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=60, verbose_name='Titre')),
                ('art_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('slug', models.SlugField(max_length=100)),
                ('art_content', models.TextField(verbose_name='contenu')),
            ],
            options={
                'verbose_name': 'article',
                'ordering': ['-art_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_img', models.ImageField(upload_to=gestion_voies.models.get_upload_path, verbose_name="Image d'article")),
                ('media_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_voies.articles')),
            ],
            options={
                'verbose_name': "Images d'articles",
            },
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=280, verbose_name='auteur')),
                ('comment_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution')),
                ('comment_content', models.TextField(verbose_name='contenu')),
                ('comment_grade', models.IntegerField(verbose_name='note')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_voies.articles')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'ordering': ['comment_datetime'],
            },
        ),
    ]
