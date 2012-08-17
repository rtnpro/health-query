# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Doctor'
        db.create_table('people_doctor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('registration_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('people', ['Doctor'])

        # Adding model 'DoctorLocation'
        db.create_table('people_doctorlocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Doctor'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'])),
        ))
        db.send_create_signal('people', ['DoctorLocation'])

        # Adding model 'Day'
        db.create_table('people_day', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('people', ['Day'])

        # Adding model 'Timing'
        db.create_table('people_timing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doctor_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.DoctorLocation'])),
            ('available_from', self.gf('django.db.models.fields.TimeField')()),
            ('available_to', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('people', ['Timing'])

        # Adding M2M table for field days on 'Timing'
        db.create_table('people_timing_days', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('timing', models.ForeignKey(orm['people.timing'], null=False)),
            ('day', models.ForeignKey(orm['people.day'], null=False))
        ))
        db.create_unique('people_timing_days', ['timing_id', 'day_id'])


    def backwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table('people_doctor')

        # Deleting model 'DoctorLocation'
        db.delete_table('people_doctorlocation')

        # Deleting model 'Day'
        db.delete_table('people_day')

        # Deleting model 'Timing'
        db.delete_table('people_timing')

        # Removing M2M table for field days on 'Timing'
        db.delete_table('people_timing_days')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.day': {
            'Meta': {'object_name': 'Day'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'people.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'places': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['places.Place']", 'null': 'True', 'through': "orm['people.DoctorLocation']", 'blank': 'True'}),
            'registration_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'people.doctorlocation': {
            'Meta': {'object_name': 'DoctorLocation'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Doctor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.Place']"})
        },
        'people.timing': {
            'Meta': {'object_name': 'Timing'},
            'available_from': ('django.db.models.fields.TimeField', [], {}),
            'available_to': ('django.db.models.fields.TimeField', [], {}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['people.Day']", 'symmetrical': 'False'}),
            'doctor_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.DoctorLocation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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

    complete_apps = ['people']