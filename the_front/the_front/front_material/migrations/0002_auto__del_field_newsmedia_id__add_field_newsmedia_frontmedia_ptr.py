# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NewsMedia.id'
        db.delete_column(u'front_material_newsmedia', u'id')

        # Adding field 'NewsMedia.frontmedia_ptr'
        db.add_column(u'front_material_newsmedia', u'frontmedia_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['front_material.FrontMedia'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'NewsMedia.id'
        db.add_column(u'front_material_newsmedia', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'NewsMedia.frontmedia_ptr'
        db.delete_column(u'front_material_newsmedia', u'frontmedia_ptr_id')


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
            'Meta': {'object_name': 'NewsMedia', '_ormbases': [u'front_material.FrontMedia']},
            u'frontmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['front_material.FrontMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'news_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front_material.NewsArticle']"})
        }
    }

    complete_apps = ['front_material']