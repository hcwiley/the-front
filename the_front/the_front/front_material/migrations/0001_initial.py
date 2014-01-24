# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FrontMedia'
        db.create_table(u'front_material_frontmedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('video_link', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('full_res_image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('is_default_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'front_material', ['FrontMedia'])

        # Adding model 'NewsArticle'
        db.create_table(u'front_material_newsarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('is_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'front_material', ['NewsArticle'])

        # Adding model 'NewsMedia'
        db.create_table(u'front_material_newsmedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('news_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front_material.NewsArticle'])),
        ))
        db.send_create_signal(u'front_material', ['NewsMedia'])


    def backwards(self, orm):
        # Deleting model 'FrontMedia'
        db.delete_table(u'front_material_frontmedia')

        # Deleting model 'NewsArticle'
        db.delete_table(u'front_material_newsarticle')

        # Deleting model 'NewsMedia'
        db.delete_table(u'front_material_newsmedia')


    models = {
        u'front_material.frontmedia': {
            'Meta': {'object_name': 'FrontMedia'},
            'full_res_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_default_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'front_material.newsarticle': {
            'Meta': {'object_name': 'NewsArticle'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'front_material.newsmedia': {
            'Meta': {'object_name': 'NewsMedia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front_material.NewsArticle']"})
        }
    }

    complete_apps = ['front_material']