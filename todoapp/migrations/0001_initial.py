# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ToDoList'
        db.create_table('todoapp_todolist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('dt', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('todoapp', ['ToDoList'])


    def backwards(self, orm):
        
        # Deleting model 'ToDoList'
        db.delete_table('todoapp_todolist')


    models = {
        'todoapp.todolist': {
            'Meta': {'object_name': 'ToDoList'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'dt': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['todoapp']
