# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PressLink'
        db.create_table(u'front_material_presslink', (
            (u'link_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['front_material.Link'], unique=True, primary_key=True)),
            ('press_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front_material.Press'])),
        ))
        db.send_create_signal(u'front_material', ['PressLink'])

        # Adding model 'Press'
        db.create_table(u'front_material_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('is_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'front_material', ['Press'])

        # Adding model 'Link'
        db.create_table(u'front_material_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'front_material', ['Link'])

        # Adding model 'PressMedia'
        db.create_table(u'front_material_pressmedia', (
            (u'frontmedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['front_material.FrontMedia'], unique=True, primary_key=True)),
            ('press_article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['front_material.Press'])),
        ))
        db.send_create_signal(u'front_material', ['PressMedia'])


    def backwards(self, orm):
        # Deleting model 'PressLink'
        db.delete_table(u'front_material_presslink')

        # Deleting model 'Press'
        db.delete_table(u'front_material_press')

        # Deleting model 'Link'
        db.delete_table(u'front_material_link')

        # Deleting model 'PressMedia'
        db.delete_table(u'front_material_pressmedia')


    models = {
        u'front_material.faq': {
            'Meta': {'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
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
        u'front_material.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
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
        },
        u'front_material.press': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Press'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'front_material.presslink': {
            'Meta': {'object_name': 'PressLink', '_ormbases': [u'front_material.Link']},
            u'link_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['front_material.Link']", 'unique': 'True', 'primary_key': 'True'}),
            'press_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front_material.Press']"})
        },
        u'front_material.pressmedia': {
            'Meta': {'object_name': 'PressMedia', '_ormbases': [u'front_material.FrontMedia']},
            u'frontmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['front_material.FrontMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'press_article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['front_material.Press']"})
        }
    }

    complete_apps = ['front_material']