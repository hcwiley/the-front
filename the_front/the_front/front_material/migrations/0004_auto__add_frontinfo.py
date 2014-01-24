# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FrontInfo'
        db.create_table(u'front_material_frontinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal(u'front_material', ['FrontInfo'])


    def backwards(self, orm):
        # Deleting model 'FrontInfo'
        db.delete_table(u'front_material_frontinfo')


    models = {
        u'front_material.frontinfo': {
            'Meta': {'object_name': 'FrontInfo'},
            'about': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'front_material.frontmedia': {
            'Meta': {'object_name': 'FrontMedia'},
            'full_res_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_default_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'portrait': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'front_material.newsarticle': {
            'Meta': {'ordering': "['-date']", 'object_name': 'NewsArticle'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'front_material.newsmedia': {
            'Meta': {'object_name': 'NewsMedia', '_ormbases': [u'front_material.FrontMedia']},
            u'frontmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['front_material.FrontMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'news_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front_material.NewsArticle']"})
        }
    }

    complete_apps = ['front_material']