# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatetimeStamp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name=b'Modified Date', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaggedQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ForeignKey(related_name='web_taggedquestions_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('datetimestamp_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='web.DatetimeStamp')),
                ('answer', models.TextField(blank=True)),
                ('added_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            bases=('web.datetimestamp',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('datetimestamp_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='web.DatetimeStamp')),
                ('question', models.TextField(blank=True)),
                ('answer', models.ForeignKey(to='web.Answer', blank=True)),
            ],
            bases=('web.datetimestamp',),
        ),
        migrations.AddField(
            model_name='taggedquestions',
            name='content_object',
            field=models.ForeignKey(to='web.Question', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='web.TaggedQuestions', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
