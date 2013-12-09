# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table(u'lfweb_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=130)),
        ))
        db.send_create_signal(u'lfweb', ['Gallery'])

        # Adding model 'Image'
        db.create_table(u'lfweb_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lfweb.Gallery'], null=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('abstract', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'lfweb', ['Image'])

        # Adding model 'Collection'
        db.create_table(u'lfweb_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lfweb.Collection'], null=True)),
            ('name', self.gf('tinymce.models.HTMLField')(max_length=130, null=True)),
            ('name_it', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('name_en', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('title', self.gf('tinymce.models.HTMLField')(max_length=130, null=True)),
            ('title_it', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('title_en', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
            ('abstract', self.gf('tinymce.models.HTMLField')(max_length=255, null=True)),
            ('abstract_it', self.gf('tinymce.models.HTMLField')(max_length=255, null=True, blank=True)),
            ('abstract_en', self.gf('tinymce.models.HTMLField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(null=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lfweb.Gallery'], null=True, blank=True)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'lfweb', ['Collection'])

        # Adding model 'Yarn'
        db.create_table(u'lfweb_yarn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lfweb.Collection'])),
            ('name', self.gf('tinymce.models.HTMLField')(max_length=130)),
            ('name_it', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('name_en', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('title', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('title_it', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('title_en', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lfweb', ['Yarn'])

        # Adding model 'News'
        db.create_table(u'lfweb_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('tinymce.models.HTMLField')(max_length=130, null=True)),
            ('title_it', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('title_en', self.gf('tinymce.models.HTMLField')(max_length=130, null=True, blank=True)),
            ('abstract', self.gf('tinymce.models.HTMLField')(max_length=255, null=True)),
            ('abstract_it', self.gf('tinymce.models.HTMLField')(max_length=255, null=True, blank=True)),
            ('abstract_en', self.gf('tinymce.models.HTMLField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('text', self.gf('tinymce.models.HTMLField')(null=True)),
            ('text_it', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lfweb.Gallery'], null=True, blank=True)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=130, null=True)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')(null=True)),
        ))
        db.send_create_signal(u'lfweb', ['News'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table(u'lfweb_gallery')

        # Deleting model 'Image'
        db.delete_table(u'lfweb_image')

        # Deleting model 'Collection'
        db.delete_table(u'lfweb_collection')

        # Deleting model 'Yarn'
        db.delete_table(u'lfweb_yarn')

        # Deleting model 'News'
        db.delete_table(u'lfweb_news')


    models = {
        u'lfweb.collection': {
            'Meta': {'object_name': 'Collection'},
            'abstract': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True'}),
            'abstract_en': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Gallery']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True'}),
            'name_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'name_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Collection']", 'null': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True'}),
            'title_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        },
        u'lfweb.gallery': {
            'Meta': {'object_name': 'Gallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '130'})
        },
        u'lfweb.image': {
            'Meta': {'object_name': 'Image'},
            'abstract': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Gallery']", 'null': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'lfweb.news': {
            'Meta': {'object_name': 'News'},
            'abstract': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True'}),
            'abstract_en': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('tinymce.models.HTMLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Gallery']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True'}),
            'title_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True'})
        },
        u'lfweb.yarn': {
            'Meta': {'object_name': 'Yarn'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lfweb.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('tinymce.models.HTMLField', [], {'max_length': '130'}),
            'name_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'name_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_en': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('tinymce.models.HTMLField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lfweb']