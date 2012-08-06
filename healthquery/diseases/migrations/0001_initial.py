# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Remedy'
        db.create_table('diseases_remedy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(default=None, max_length=5000, null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(default=None, null=True)),
        ))
        db.send_create_signal('diseases', ['Remedy'])

        # Adding unique constraint on 'Remedy', fields ['name']
        db.create_unique('diseases_remedy', ['name'])

        # Adding model 'Medicine'
        db.create_table('diseases_medicine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(default=None, max_length=5000, null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(default=None, null=True)),
        ))
        db.send_create_signal('diseases', ['Medicine'])

        # Adding unique constraint on 'Medicine', fields ['name']
        db.create_unique('diseases_medicine', ['name'])

        # Adding model 'Disease'
        db.create_table('diseases_disease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('summary', self.gf('django.db.models.fields.TextField')(default=None, max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default=None, max_length=1000, blank=True)),
            ('severity', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('tags', self.gf('tagging.fields.TagField')(default=None, null=True)),
        ))
        db.send_create_signal('diseases', ['Disease'])

        # Adding unique constraint on 'Disease', fields ['name']
        db.create_unique('diseases_disease', ['name'])

        # Adding M2M table for field medicines on 'Disease'
        db.create_table('diseases_disease_medicines', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('disease', models.ForeignKey(orm['diseases.disease'], null=False)),
            ('medicine', models.ForeignKey(orm['diseases.medicine'], null=False))
        ))
        db.create_unique('diseases_disease_medicines', ['disease_id', 'medicine_id'])

        # Adding M2M table for field remedies on 'Disease'
        db.create_table('diseases_disease_remedies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('disease', models.ForeignKey(orm['diseases.disease'], null=False)),
            ('remedy', models.ForeignKey(orm['diseases.remedy'], null=False))
        ))
        db.create_unique('diseases_disease_remedies', ['disease_id', 'remedy_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Disease', fields ['name']
        db.delete_unique('diseases_disease', ['name'])

        # Removing unique constraint on 'Medicine', fields ['name']
        db.delete_unique('diseases_medicine', ['name'])

        # Removing unique constraint on 'Remedy', fields ['name']
        db.delete_unique('diseases_remedy', ['name'])

        # Deleting model 'Remedy'
        db.delete_table('diseases_remedy')

        # Deleting model 'Medicine'
        db.delete_table('diseases_medicine')

        # Deleting model 'Disease'
        db.delete_table('diseases_disease')

        # Removing M2M table for field medicines on 'Disease'
        db.delete_table('diseases_disease_medicines')

        # Removing M2M table for field remedies on 'Disease'
        db.delete_table('diseases_disease_remedies')


    models = {
        'diseases.disease': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Disease'},
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicines': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': "orm['diseases.Medicine']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remedies': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': "orm['diseases.Remedy']", 'symmetrical': 'False', 'blank': 'True'}),
            'severity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '200', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': 'None', 'null': 'True'})
        },
        'diseases.medicine': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Medicine'},
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tags': ('tagging.fields.TagField', [], {'default': 'None', 'null': 'True'})
        },
        'diseases.remedy': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Remedy'},
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tags': ('tagging.fields.TagField', [], {'default': 'None', 'null': 'True'})
        }
    }

    complete_apps = ['diseases']