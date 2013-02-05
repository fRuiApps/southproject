# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ToDoList.dt'
        db.alter_column('todoapp_todolist', 'dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Changing field 'ToDoList.dt'
        db.alter_column('todoapp_todolist', 'dt', self.gf('django.db.models.fields.DateField')(auto_now_add=True))


    models = {
        'todoapp.todolist': {
            'Meta': {'object_name': 'ToDoList'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['todoapp']
