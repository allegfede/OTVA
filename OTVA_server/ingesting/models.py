from django.db import models
from django.contrib.auth.models import User
from OTVA_server.ingesting.fields import MultiSelectField, MultiSelectFormField

#class IngestingUser(models.Model):
    # This field is required.
#    user = models.OneToOneField(User)
    # Other example fields here
#    favorite_animal = models.CharField(max_length=20, default="Dragons")

class Week(models.Model):
    day = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "01. Admin -> Week"
    def __unicode__(self):
        return u"%s" % (self.day)

class Channel(models.Model):
    name = models.CharField(max_length=50)
    tv_number = models.IntegerField('LCN',blank=True, null=True)
    #logo_img = models.FilePathField('Logo Image', path='media/img/logo', recursive=False)
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
    class Meta:
        verbose_name_plural = "02. Admin -> Channels"
    def __unicode__(self): 
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=50)
    season = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=50)
    promo_folder = models.CharField(max_length=50)
    default_lenght = models.IntegerField(blank=True, null=True)
    replicabile = models.BooleanField(default=False)
    formato = models.CharField(max_length=50, default='4:3', choices=(
        ('4:3','4:3'),
        ('16:9','16:9'),
    ))
    #classificazione_registro = models.CharField(max_length=50)
    classificazione_registro = models.CharField(max_length=50, choices=(
        ('1a - Telegiornale', '1a - Telegiornale'),
        ('1b - Telegiornale sportivo', '1b - Telegiornale sportivo'),
        ('1c - Servizi teletext', '1c - Servizi teletext'),
        ('2a - Telequiz', '2a - Telequiz'),
        ('2b - Giochi televisivi', '2b - Giochi televisivi'),
        ('3 Talk Show', '3 Talk Show'),
        ('4 Manifestazioni sportive', '4 Manifestazioni sportive'),
        ('5a - Pubblicità', '5a - Pubblicità'),
        ('5b - Telepromozioni', '5b - Telepromozioni'),
        ('5c - Sponsorizzazioni', '5c - Sponsorizzazioni'),
        ('6 Televendite', '6 Televendite'),
        ('7a - Film cinematografici', '7a - Film cinematografici'),
        ('7b - Film TV', '7b - Film TV'),
        ('8a - Miniserie - sceneggiato', '8a - Miniserie - sceneggiato'),
        ('8b - Telefilm', '8b - Telefilm'),
        ('8c - Situation comedies', '8c - Situation comedies'),
        ('8d - Soap operas - telenovelas', '8d - Soap operas - telenovelas'),
        ("8e - Comiche d'epoca", "8e - Comiche d'epoca"),
        ('9a - Storia - geografia', '9a - Storia - geografia'),
        ('9b - Scienza', '9b - Scienza'),
        ('10a - Informazione parlamentare', '10a - Informazione parlamentare'),
        ('10b - Dichiarazioni parlamentari', '10b - Dichiarazioni parlamentari'),
        ('10c - Inchieste', '10c - Inchieste'),
        ('10d - Rubriche di approfondimento delle testate giornalistiche', '10d - Rubriche di approfondimento delle testate giornalistiche'),
        ('10e - Costume e società', '10e - Costume e società'),
        ('10f - Rubriche religiose', '10f - Rubriche religiose'),
        ('10g - Dibattiti', '10g - Dibattiti'),
        ('10h - Rubriche di approfondimento sportivo', '10h - Rubriche di approfondimento sportivo'),
        ('10i - Teledidattica', '10i - Teledidattica'),
        ('10j - Approfondimento culturale', '10j - Approfondimento culturale'),
        ('11a - Concerti', '11a - Concerti'),
        ('11b - Balletti', '11b - Balletti'),
        ('11c - Lirica', '11c - Lirica'),
        ('11d - Prosa', '11d - Prosa'),
        ('12 Cartoni animati per bambini', '12 Cartoni animati per bambini'),
        ('13a - Programmi musicali', '13a - Programmi musicali'),
        ('13b - Reality show', '13b - Reality show'),
        ('13c - Programmi di montaggio', '13c - Programmi di montaggio'),
        ('13d - Varietà', '13d - Varietà'),
        ('13e - Astrologia - cartomanzia', '13e - Astrologia - cartomanzia'),
        ('13f - Programma contenitore radiofonico', '13f - Programma contenitore radiofonico'),
        ('13g - Cartoni animati per adulti', '13g - Cartoni animati per adulti'),
        ('13h - Trasmissioni per bambini', '13h - Trasmissioni per bambini'),
        ('14a - Anteprima', '14a - Anteprima'),
        ('14b - Promo', '14b - Promo'),
        ('14c - Rotocalchi', '14c - Rotocalchi'),
        ('14d - Meteo', '14d - Meteo'),
        ('14e - Lotterie', '14e - Lotterie'),
        ('14f - Rubriche di servizio', '14f - Rubriche di servizio'),
        ('14g - Trasmissioni di servizio', '14g - Trasmissioni di servizio'),
        ('14h - Inaugurazioni', '14h - Inaugurazioni'),
        ('14i - Premiazioni', '14i - Premiazioni'),
        ('14j - Manifestazioni di piazza', '14j - Manifestazioni di piazza'),
        ('15a -Santa Messa', '15a -Santa Messa'),
        ('15b - Eventi religiosi', '15b - Eventi religiosi'),
        ('16a - Annunci', '16a - Annunci'),
        ('16b - Sigle', '16b - Sigle'),
        ('16c - Intervalli', '16c - Intervalli'),
        ('16d - Segnale orario', '16d - Segnale orario'),
        ('17 Messaggi politici autogestiti gratuiti', '17 Messaggi politici autogestiti gratuiti'),
        ('18 Messaggi politici autogestiti a pagamento', '18 Messaggi politici autogestiti a pagamento'),
        ('19 Comunicazione politica', '19 Comunicazione politica'),
        ('20 Immagini fisse o ripetitive', '20 Immagini fisse o ripetitive'),
    ))
    class Meta:
        verbose_name_plural = "03. Ingesting -> Programs"
    def __unicode__(self):
        return u"%s - Stagione %s" % (self.name, self.season)

class Episode(models.Model):
    program = models.ForeignKey(Program, blank=True, null=True)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    episode_number = models.IntegerField(blank=True, null=True)
    lenght = models.CharField(max_length=50)
    formato = models.CharField(max_length=50, default='4:3', choices=(
        ('4:3','4:3'),
        ('16:9','16:9'),
    ))
    break_point_list = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    file = models.FileField(upload_to='file')
    #file = models.FileField(upload_to='program/season/name.avi')
    content_rating = models.CharField('Childhood Protection', max_length=10, blank=True, choices=(
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('red', 'Red'),
    ))
    #logo_special = models.ForeignKey(Channel, blank=True, null=True)
    logo_special_img = models.ImageField('Logo Image', upload_to='img/logo', blank=True, null=True)
    logo_valign = models.CharField(max_length=1, blank=True, choices=(
        ('t', 'Top'),
        ('c', 'Center'),
        ('b', 'Bottom'),
    ))
    logo_halign = models.CharField(max_length=1, blank=True, choices=(
        ('l', 'Left'),
        ('c', 'Center'),
        ('r', 'Right'),
    ))
    logo_size = models.IntegerField(default=100, null=True, blank=True,)
    class Meta:
        verbose_name_plural = "04. Ingesting -> Episodes"
    def __unicode__(self):
        return u"%s > %s" % (self.program, self.name)

class Agente(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    citta = models.CharField(max_length=50,blank=True, null=True)
    cellulare = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=59)
    note = models.CharField(max_length=50,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "05. Spot -> Agenti"
    def __unicode__(self):
        return u"%s %s" % (self.nome, self.cognome)

class Cliente(models.Model):
    ragione_sociale = models.CharField(max_length=50)
    codife_fiscale = models.CharField(max_length=50)
    partita_iva = models.CharField(max_length=50)
    via = models.CharField(max_length=50)
    citta = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    cap = models.CharField(max_length=50)
    contatto_commerciale = models.CharField(max_length=50)
    agente = models.ForeignKey(Agente)
    telefono = models.CharField(max_length=50)
    cellulare = models.CharField(max_length=50)
    email = models.EmailField(max_length=59)
    note = models.CharField(max_length=50,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "06. Spot -> Clienti"
    def __unicode__(self):
        return self.ragione_sociale

class Fasciapubblicitaria(models.Model):
    canale = models.ForeignKey(Channel)
    orario_previsto = models.TimeField(max_length=50)
    validitasettimanale = models.ManyToManyField(Week)
    class Meta:
        verbose_name_plural = "07. Spot -> Fasce Pubblicitarie"
    def validita_settimanale(self):
        return ', '.join(str(x) for x in self.validitasettimanale.all())
    def __str__(self):
        return "%s %s %s" % (self.canale, self.orario_previsto, ', '.join(str(x) for x in self.validitasettimanale.all()))

class Contratto(models.Model):
    codice_contratto = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente)
    agente = models.ForeignKey(Agente)
    data = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    contratto_digitale = models.FileField(upload_to='contratti')
    servizi_richiesti = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "08. Spot -> Contratti"
    def __unicode__(self):
        return u"%s %s" % (self.codice_contratto, self.cliente, self.data)

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    programmi = models.ManyToManyField(Episode)
    date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    start = models.TimeField('Start')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "09. Scheduling -> Playlists"
    def __unicode__(self):
        return self.start
    def programma(self):
        return ', '.join(str(x) for x in self.programmi.all())
    def __unicode__(self):
        return u"%s - %s - %s" % (self.name, self.start, ', '.join(str(x) for x in self.programmi.all()))

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
    playlist = models.ManyToManyField(Playlist)
    class Meta:
        verbose_name_plural = "10. Scheduling -> Playbacks"
    def playlists(self):
        return ', '.join(str(x) for x in self.playlist.all())
    def __unicode__(self):
        return u"%s - %s - %s" % (self.channel, self.current_state, ', '.join(str(x) for x in self.playlist.all()))
