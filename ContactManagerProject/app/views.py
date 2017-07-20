"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
from datetime import datetime
from django import template
from django.template import RequestContext, loader
from django.db import models
from app.models import *
from app.models import Contact
from .forms import ContactForm



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context =   {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    return render(request, 'app/index.html', context)

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    context = {
  
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'obj': Contact.objects.all(),
        }
    return render(request,'app/contactDetail.html',context)


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    context ={
        'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    return render(request,'app/about.html',context )


def display(request):
  return render_to_response('app/contactDetail.html', {'obj': Contact.objects.all()})

def addContact(request):
    print {'addcontact'}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #if form.is_valid():
        fname = form.data['first_name_Id'].encode('utf-8')
        lname = form.data['last_name_Id'].encode('utf-8')
        email = form.data['email_Id'].encode('utf-8')
        mobNo = form.data['MobileNo_Id'].encode('utf-8')

    if form.data['contact_id']:
        conObj = Contact.objects.filter(pk=form.data['contact_id'].encode('utf-8')).update(FirstName = fname,LastName = lname,Email = email,MobileNo = mobNo)
        #conObj = Contact.objects.create(FirstName = fname,LastName = lname,Email = email,MobileNo = mobNo,pk=form.data['contact_id'].encode('utf-8'))
    elif fname != '':     
        conObj = Contact.objects.create(FirstName = fname,LastName = lname,Email = email,MobileNo = mobNo)
        conObj.save() 
                  
    return HttpResponseRedirect('/contact')                
                            
def delete(request,id):
    query = Contact.objects.get(pk=id)
    query.delete()
    return HttpResponseRedirect('/contact')   


def update(request,id):
    query1 = Contact.objects.get(pk=id)
    first_name_Id = query1.FirstName
    last_name_Id = query1.LastName
    email_Id = query1.Email
    MobileNo_Id = query1.MobileNo
    contact_id = id
    data = {'first_name_Id': query1.FirstName,'last_name_Id':query1.LastName,'email_Id':query1.Email,'MobileNo_Id':query1.MobileNo,'contact_id':id}
    form = ContactForm(initial=data)
    return render(request,'app/contact-edit.html',{'form': form} )
    

def editToSave(request):
    data = {'first_name_Id': '','last_name_Id':'','email_Id':'','MobileNo_Id':'','contact_id':''}
    form = ContactForm(initial=data)
    return render(request,'app/contact-edit.html',{'form': form} )
       