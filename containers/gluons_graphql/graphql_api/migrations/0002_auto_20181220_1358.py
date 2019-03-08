# Generated by Django 2.1.4 on 2018-12-20 04:58

from __future__ import unicode_literals
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0001_initial'),
    ]

    operations = [
        # pgroonga を登録する(一回のみ)
        migrations.RunSQL(
            'CREATE EXTENSION pgroonga',
            'DROP EXTENSION pgroonga',
        ),

        # 全文検索用インデックスを作成する(検索対象のカラムごとに作成)
        migrations.RunSQL(
            'CREATE INDEX pgroonga_fulltext ON graphql_api_quark USING pgroonga (name, description)',
            'DROP INDEX pgroonga_fulltext',
        )
    ]