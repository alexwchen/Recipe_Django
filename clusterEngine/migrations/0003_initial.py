# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Recipe'
        db.create_table('clusterEngine_recipe', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('method', self.gf('django.db.models.fields.TextField')()),
            ('ingredient', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('clusterEngine', ['Recipe'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Recipe'
        db.delete_table('clusterEngine_recipe')
    
    
    models = {
        'clusterEngine.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ingredient': ('django.db.models.fields.TextField', [], {}),
            'method': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['clusterEngine']
