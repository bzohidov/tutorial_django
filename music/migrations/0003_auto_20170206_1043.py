# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170202_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer', models.CharField(max_length=200)),
                ('song1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Person')),
            ],
        ),
        migrations.AddField(
            model_name='album1',
            name='album1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.Person'),
        ),
    ]