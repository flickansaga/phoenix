# -*- coding: utf-8 -*-
from django import forms
from taggit.forms import *

class ThreadForm(forms.Form):
    title_min = 10
    title_max = 100

    title = forms.CharField(
        required=True,
        min_length=title_min,
        max_length=title_max,
        error_messages={
            'required': 'Du har inte angett en titel!',
            'min_length': 'Titeln måste vara minst %s tecken lång.' % title_min,
        }
    )

    tags = TagField(
        required=True,
        error_messages={
            'required': 'Du har inte angett någon kategori!',
        },
        widget=forms.HiddenInput,
    )
    
    body = forms.CharField(
        required=True,
        widget=forms.Textarea,
        error_messages={
            'required': 'Du måste fylla i detta fält.',
        }
    )


class ForumPostForm(forms.Form):
    thread_id = forms.IntegerField()
    parent_id = forms.IntegerField()
    body = forms.CharField(
        widget=forms.Textarea,
        required=True,
        error_messages={
            'required': 'Du måste fylla i detta fält.',
        }
    )
