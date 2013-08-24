# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.forms import forms
from django.conf import settings
#from django.core.exceptions import ValidationError
from django.contrib import messages
#from django.utils.translation import ugettext_lazy as _

from fitsapp.upload.models import Document
from fitsapp.upload.forms import DocumentForm
from fitsapp.upload.forms import DocumentSearchForm

import os

def search(request):
    # Handle search
    if request.method == 'GET':
        form = DocumentSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            messages.info(request, 'Search query: ' + query)
        else:
            messages.error(request, 'Search error.')

        # Redirect to the document list after POST
        #return HttpResponseRedirect(reverse('fitsapp.upload.views.upload'))

    else:
        form = DocumentSearchForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.filter(docfile__contains=query)

    # Render list page with the documents and the form
    return render_to_response(
        'upload/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES['docfile'].name.lower().endswith(('.xml', '.utree')):

            newdoc = Document(docfile = request.FILES['docfile'], uploader = request.user, description = 'Test description.')
            newdoc.save()
            #if os.path.getsize(request.FILES['docfile']) > settings.MAX_UPLOAD_SIZE:
            #    messages.error(request, 'File size is too big.')
            #else:
            #    newdoc.save()

        else:
            messages.error(request, 'File type is not supported.')
            #raise forms.ValidationError(_('File type is not supported'))

        # Redirect to the document list after POST
        return HttpResponseRedirect(reverse('fitsapp.upload.views.upload'))

    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'upload/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
