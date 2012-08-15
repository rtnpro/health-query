# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    needed_by = (
        ('people', '0001_initial'),        
    )

    def forwards(self, orm):

        # Adding model 'Place'
        db.create_table('places_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place_type', self.gf('django.db.models.fields.CharField')(max_length='2')),
            ('address', self.gf('django_google_maps.fields.AddressField')(max_length=200)),
            ('geolocation', self.gf('django_google_maps.fields.GeoLocationField')(max_length=100)),
        ))
        db.send_create_signal('places', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('places_place')


    models = {
        'places.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django_google_maps.fields.AddressField', [], {'max_length': '200'}),
            'geolocation': ('django_google_maps.fields.GeoLocationField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place_type': ('django.db.models.fields.CharField', [], {'max_length': "'2'"})
        }
    }

    complete_apps = ['places']
