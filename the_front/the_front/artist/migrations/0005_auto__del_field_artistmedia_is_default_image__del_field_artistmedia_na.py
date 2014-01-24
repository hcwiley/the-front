# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ArtistMedia.is_default_image'
        db.delete_column(u'artist_artistmedia', 'is_default_image')

        # Deleting field 'ArtistMedia.name'
        db.delete_column(u'artist_artistmedia', 'name')

        # Deleting field 'ArtistMedia.video_link'
        db.delete_column(u'artist_artistmedia', 'video_link')

        # Deleting field 'ArtistMedia.full_res_image'
        db.delete_column(u'artist_artistmedia', 'full_res_image')

        # Deleting field 'ArtistMedia.image'
        db.delete_column(u'artist_artistmedia', 'image')

        # Deleting field 'ArtistMedia.id'
        db.delete_column(u'artist_artistmedia', u'id')

        # Deleting field 'ArtistMedia.thumbnail'
        db.delete_column(u'artist_artistmedia', 'thumbnail')

        # Adding field 'ArtistMedia.frontmedia_ptr'
        db.add_column(u'artist_artistmedia', u'frontmedia_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['front_material.FrontMedia'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ArtistMedia.is_default_image'
        db.add_column(u'artist_artistmedia', 'is_default_image',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ArtistMedia.name'
        db.add_column(u'artist_artistmedia', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ArtistMedia.video_link'
        db.add_column(u'artist_artistmedia', 'video_link',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArtistMedia.full_res_image'
        db.add_column(u'artist_artistmedia', 'full_res_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArtistMedia.image'
        db.add_column(u'artist_artistmedia', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArtistMedia.id'
        db.add_column(u'artist_artistmedia', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'ArtistMedia.thumbnail'
        db.add_column(u'artist_artistmedia', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ArtistMedia.frontmedia_ptr'
        db.delete_column(u'artist_artistmedia', u'frontmedia_ptr_id')


    models = {
        u'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'artist_statement': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'artist.artistmedia': {
            'Meta': {'object_name': 'ArtistMedia', '_ormbases': [u'front_material.FrontMedia']},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.Artist']"}),
            u'frontmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['front_material.FrontMedia']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'front_material.frontmedia': {
            'Meta': {'object_name': 'FrontMedia'},
            'full_res_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_default_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['artist']