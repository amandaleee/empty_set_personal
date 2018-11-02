from django.db import models

# Create your models here.

#//A render is a single rendered instance of this artwork in the browser, which can then be printed
# //a render is generated when a Grantor [user] enters their name and submits.
# //each Grantor may create one Render - Renders and Grantors must be unique.
# //each Render is an array of classes that are applied to N Boxes in the UI.
# //The number N is a square; the .box elements in the dom create the render as a grid in the browser, which can then be printed. [
# this might not always be true]
# // the class Render has the following table columns:
# // id - the unique id [the total number of ids available will be N ^ N]. numeric auto-incrementing.
# // grantor_id - the unique Grantor id that created this render. alphanumeric 256 char max.
# // layout - an array of CSS classes, where each element in the array can be any class as determined in the implementation. The length of each array is N - 1. array.
# // cdate - date created. datetime.
class Render(models.Model):
    id = models.AutoField(primary_key=true)
    grantor_id = models.ForeignKey(Grantor, on_delete=models.CASCADE)
    layout = models.CharField(max_length=200000000000) # can i actually do this
    cdate = models.DateTimeField(auto_now=true)


# //we have a class called Grantor, which is a person that creates the Render.
# //the Grantor enters their name and hits "submit" before the Render is created.
# //the Grantor table includes:
# id
# //name
# //ip_address
# //cdate
# //associated renderid

class Grantor(models.Model):
    id = models.AutoField(primary_key=true)
    name = models.CharField(max_length=400)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    cdate = models.DateTimeField(auto_now=true)
    renderid = models.ForeignKey(Render, on_delete=models.CASCADE)


# We have a class Instance
# An instance is a single set of renders that occur in a set at a single event.
# Instance table contains the following columns:
# Id - unique id of row, numerical auto increment
# Name - name of instance.
# Description. Event info or whatever.
# C date
# IP address
# Location

class Grantor(models.Model):
    id = models.AutoField(primary_key=true)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    cdate = models.DateTimeField(auto_now=false)
    location = models.CharField(max_length=400)