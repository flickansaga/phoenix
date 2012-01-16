# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Guestbook_Notification'
        db.delete_table('notifications_guestbook_notification')

        # Adding model 'Notification'
        db.create_table('notifications_notification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('message', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('announced', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='receiver_entries', to=orm['auth.User'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sender_entries', null=True, to=orm['auth.User'])),
            ('sender_name', self.gf('django.db.models.fields.CharField')(max_length='1024', null=True, blank=True)),
            ('instance_type', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('instance_id', self.gf('django.db.models.fields.IntegerField')()),
            ('instance_url', self.gf('django.db.models.fields.CharField')(max_length='1024', null=True, blank=True)),
        ))
        db.send_create_signal('notifications', ['Notification'])


    def backwards(self, orm):
        
        # Adding model 'Guestbook_Notification'
        db.create_table('notifications_guestbook_notification', (
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guestbook.Guestbooks'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender_entries', null=True, to=orm['auth.User'], blank=True)),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='receiver_entries', to=orm['auth.User'])),
            ('sender_name', self.gf('django.db.models.fields.CharField')(max_length='1024', null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('instance_url', self.gf('django.db.models.fields.CharField')(max_length='1024', null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='1024')),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('notifications', ['Guestbook_Notification'])

        # Deleting model 'Notification'
        db.delete_table('notifications_notification')


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
        'notifications.notification': {
            'Meta': {'object_name': 'Notification'},
            'announced': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance_id': ('django.db.models.fields.IntegerField', [], {}),
            'instance_type': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"}),
            'instance_url': ('django.db.models.fields.CharField', [], {'max_length': "'1024'", 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'receiver_entries'", 'to': "orm['auth.User']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sender_entries'", 'null': 'True', 'to': "orm['auth.User']"}),
            'sender_name': ('django.db.models.fields.CharField', [], {'max_length': "'1024'", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"})
        }
    }

    complete_apps = ['notifications']
