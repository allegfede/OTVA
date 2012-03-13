from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=50)
    tv_number = models.IntegerField(blank=True, null=True)
    #logo_img = models.FilePathField("Logo Image", path='media/img/logo', recursive=False)
    logo_img = models.ImageField('Logo Image', upload_to='img/logo')
    logo_valign = models.CharField(max_length=1, choices=(
        ('t', 'Top'),
        ('c', 'Center'),
        ('b', 'Bottom'),
    ))
    logo_halign = models.CharField(max_length=1, choices=(
        ('l', 'Left'),
        ('c', 'Center'),
        ('r', 'Right'),
    ))
    logo_size = models.IntegerField(default=100)
    def __unicode__(self): 
        return self.name
class Program(models.Model):
    name = models.CharField(max_length=50)
    serie = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=50)
    promo_folder = models.CharField(max_length=50)
    default_lenght = models.IntegerField(blank=True, null=True)
    replicabile = models.BooleanField(default=False)
    formato = models.CharField(max_length=50)
    classificazione_registro = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
class Episode(models.Model):
    program = models.ForeignKey(Program, blank=True, null=True)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    serie = models.IntegerField(blank=True, null=True)
    lenght = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    break_point_list = models.CharField(max_length=50)
    file = models.FileField(upload_to='file')
    logo_special = models.ForeignKey(Channel, blank=True, null=True)
    def __unicode__(self):
        return u"%s, %s %s" % (self.program, self.serie, self.name) # Edit in admin.py
class Playback(models.Model):
    channel = models.ForeignKey(Channel)
    server_ip = models.IPAddressField(default='127.0.0.1')
    server_port = models.IntegerField(default=123)
    connection_password = models.CharField(max_length=50)
    current_state = models.CharField(max_length=10, choices=(
        ('offline', 'Offline'),
        ('online', 'Online'),
        ('stopped', 'Stopped'),
        ('paused', 'Paused'),
        ('fault', 'Fault'),
    ))
    def __unicode__(self):
        return u"%s - %s" % (self.channel, self.current_state) 