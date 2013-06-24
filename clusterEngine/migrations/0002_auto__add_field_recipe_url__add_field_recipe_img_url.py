# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Recipe.url'
        db.add_column('clusterEngine_recipe', 'url', self.gf('django.db.models.fields.CharField')(default='none', max_length=200), keep_default=False)

        # Adding field 'Recipe.img_url'
        db.add_column('clusterEngine_recipe', 'img_url', self.gf('django.db.models.fields.CharField')(default='none', max_length=200), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Recipe.url'
        db.delete_column('clusterEngine_recipe', 'url')

        # Deleting field 'Recipe.img_url'
        db.delete_column('clusterEngine_recipe', 'img_url')
    
    
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
