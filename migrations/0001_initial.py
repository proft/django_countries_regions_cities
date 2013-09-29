# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_countries_regions_cities', ['Country'])

        # Adding model 'Region'
        db.create_table('region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_countries_regions_cities.Country'])),
        ))
        db.send_create_signal(u'django_countries_regions_cities', ['Region'])

        # Adding model 'City'
        db.create_table('city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_countries_regions_cities.Country'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_countries_regions_cities.Region'])),
        ))
        db.send_create_signal(u'django_countries_regions_cities', ['City'])

        # Adding model 'TestModel'
        db.create_table('testmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_countries_regions_cities.Country'])),
            ('region', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['django_countries_regions_cities.Region'])),
            ('city', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['django_countries_regions_cities.City'])),
        ))
        db.send_create_signal(u'django_countries_regions_cities', ['TestModel'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('country')

        # Deleting model 'Region'
        db.delete_table('region')

        # Deleting model 'City'
        db.delete_table('city')

        # Deleting model 'TestModel'
        db.delete_table('testmodel')


    models = {
        u'django_countries_regions_cities.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City', 'db_table': "'city'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_countries_regions_cities.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_countries_regions_cities.Region']"})
        },
        u'django_countries_regions_cities.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country', 'db_table': "'country'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_countries_regions_cities.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region', 'db_table': "'region'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_countries_regions_cities.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_countries_regions_cities.testmodel': {
            'Meta': {'ordering': "['username']", 'object_name': 'TestModel', 'db_table': "'testmodel'"},
            'city': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_countries_regions_cities.City']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_countries_regions_cities.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_countries_regions_cities.Region']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_countries_regions_cities']