# Generated by Django 2.2.17 on 2021-03-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('url_hash', models.CharField(db_index=True, editable=False, max_length=32, unique=True)),
                ('title', models.TextField(blank=True, editable=False)),
                ('publisher', models.TextField(editable=False)),
                ('publisher_logo_src', models.TextField(blank=True, editable=False, verbose_name='Publisher logo URL')),
                ('poster_portrait_src', models.TextField(blank=True, editable=False, verbose_name='Poster portrait image URL')),
                ('poster_square_src', models.TextField(blank=True, editable=False, verbose_name='Poster square image URL')),
                ('poster_landscape_src', models.TextField(blank=True, editable=False, verbose_name='Poster landscape image URL')),
                ('last_fetched_at', models.DateTimeField()),
            ],
        ),
    ]
