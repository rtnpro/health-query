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
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('place_type', self.gf('django.db.models.fields.CharField')(max_length='2')),
        ))
        db.send_create_signal('places', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('places_place')


    models = {
        'places.place': {
            'Meta': {'object_name': 'Place'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place_type': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['places']
