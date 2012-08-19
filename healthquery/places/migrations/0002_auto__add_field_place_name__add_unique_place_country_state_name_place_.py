# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Place.name'
        db.add_column('places_place', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding unique constraint on 'Place', fields ['country', 'state', 'name', 'place_type', 'zipcode']
        db.create_unique('places_place', ['country', 'state', 'name', 'place_type', 'zipcode'])


    def backwards(self, orm):
        # Removing unique constraint on 'Place', fields ['country', 'state', 'name', 'place_type', 'zipcode']
        db.delete_unique('places_place', ['country', 'state', 'name', 'place_type', 'zipcode'])

        # Deleting field 'Place.name'
        db.delete_column('places_place', 'name')


    models = {
        'places.place': {
            'Meta': {'unique_together': "(('name', 'place_type', 'zipcode', 'state', 'country'),)", 'object_name': 'Place'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place_type': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['places']