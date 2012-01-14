import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import get_model

from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey

from apps.core.models import ThreadedEntry, ThreadedEntryHistory, Entry, EntryHistory
from apps.articles.models import Article


''' NEW FORUM '''

class Forum(Entry):
    """
    Forum thread

    """
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=5120)
    tags = TaggableManager()
    last_comment = models.ForeignKey('ForumComment', null=True, blank=True, default = None)
    posts_index = models.IntegerField(null=True, blank=True)

    def get_posts_index(self):
    
        if not self.posts_index:
            number = ForumComment.objects.filter(post=self).count()
            self.posts_index = number
        
        number = self.posts_index
            
        return number
     
    def get_absolute_url(self):
        return "/forum/read/%s/" % self.id
        
    def __unicode__(self):
        return u'%s' % self.title
 
class ForumComment(MPTTModel):
    post = models.ForeignKey(Forum)
    author = models.CharField(max_length=60)
    created_by = models.ForeignKey(User, related_name="created_%(class)s_entries", blank=True, null=True)
    comment = models.TextField()
    added  = models.DateTimeField(default=datetime.datetime.now,blank=True)
    tags = TaggableManager()
    
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['added']
        
''' END NEW FORUM '''   

class Thread(Entry):
    """
    A collection of ForumPost:s.

    """
    title = models.CharField(max_length=100)
    tags = TaggableManager()
    posts_index = models.IntegerField(null=True, blank=True)
    last_post = models.ForeignKey('ForumPost', null=True, blank=True, default = None)
    
    def get_absolute_url(self):
        return "/forum/thread/read/%s/" % self.id
    
    def __unicode__(self):
        return u'%s' % self.title

    def get_latest_post(self):
        if not self.last_post:
            self.last_post = ForumPost.objects.filter(collection=self).order_by('-id')[0]
        return self.last_post

    def get_number_of_post(self):
        
        if not self.posts_index:
            number = len ( ForumPost.objects.decorated(collection=self) )
            self.posts_index = number
        
        number = self.posts_index -1
        
        if number < 0:
            number = 0
            
        return number

class ThreadHistory(EntryHistory):
    """
    History for the Thread model.
    
    """
    origin = models.ForeignKey(Thread)
    title = models.CharField(max_length=100)


class ForumPost(ThreadedEntry):
    """
    A post in the forum.
    
    """
    collection = models.ForeignKey(Thread)
    body = models.TextField()
    
    def __unicode__(self):
    
        text = u"Forumpost #{0} av {1}. {2}...".format(self.id, self.created_by, self.body[:10])
        
        return text


class ForumPostHistory(ThreadedEntryHistory):
    """
    History for the ForumPost model.
    
    """
    origin = models.ForeignKey(ForumPost)
    body = models.TextField()


class defaultCategories(models.Model):
    """
    Default categories for the forum
    using tags
    """
    tags = TaggableManager()

    def __unicode__(self):

        text = self.tags.all()[0]

        return u'%s' % (text)
