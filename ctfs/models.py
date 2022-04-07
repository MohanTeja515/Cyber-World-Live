from unicodedata import category
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    INTRODUCTION = 'introduction'
    FOOTPRINTING = 'footprinting'
    NETWORK_SCANNING = 'network scaning'
    ENUMERATION = 'enumeration'
    VULNERABILITY_ANALYSIS = 'vulnerability Analysis'
    SYSTEM_HACKING = 'system hacking'
    MALWARE_ANALYSIS = 'malware analysis'
    SNIFFING = 'sniffing'
    SOCIAL_ENGINEERING = 'social engineering'
    DENIEAL_OF_SERVICE_ATTACK = 'denieal of service attack'
    SESSION_HIJACKING = 'session hijacking'
    FIREWALL_IDS_IPS_HONEYPOTS = 'firewall'
    HACKING_WEB_SERVERS = 'hacking web servers'
    HACKING_WEB_APPLICATIONS = 'hacking web applications'
    SQL_INJECTION = 'sql injection'
    HACKING_MOBILE_PLATFORMS = 'hacking mobile platforms'
    WIFI_HACKING = 'wifi hacking'
    IOT = 'iot'
    CLOUD_COMPUTING = 'cloud computing'
    CRYPTOGRAPHY = 'cryptography'
    STEGANOGRAPHY = 'steganography'


class CTFs(models.Model):
    ctfs_title = models.CharField(max_length=300, choices=Categories.choices, default=Categories.INTRODUCTION)
    ctfs_slug = models.SlugField(null=True, blank=True)
    ctfs_photos = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    ctfs_description = models.TextField(null=True, blank=True)
    ctfs_content = models.TextField(null=True, blank=True)
    ctfs_level = models.IntegerField(null=True, blank=True)
    ctfs_difficulty = models.CharField(max_length=100, null=True, blank=True)
    ctfs_area = models.CharField(max_length=100, null=True, blank=True)
    ctfs_sections = models.IntegerField(null=True, blank=True)
    ctfs_points_add = models.IntegerField(null=True, blank=True)
    ctfs_points_minus = models.IntegerField(null=True, blank=True)
    ctfs_date_created = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.ctfs_title)
        queryset = CTFs.objects.all().filter(ctfs_slug__iexact=original_slug).count()
        count = 1
        ctfs_slug = original_slug
        while(queryset):
            ctfs_slug = original_slug + '-' + str(count)
            count += 1
            queryset = CTFs.objects.all().filter(ctfs_slug__iexact=ctfs_slug).count()
        self.ctfs_slug = ctfs_slug
        super(CTFs, self).save(*args, **kwargs)

    def __str__(self):
        return self.ctfs_title

class CTFsTopic(models.Model):
    module = models.ForeignKey(CTFs, on_delete=models.DO_NOTHING)
    ctfs_topic_title = models.CharField(max_length=300, null=True, blank=True)
    ctfs_topic_slug = models.SlugField(null=True, blank=True)
    ctfs_topic_description = models.TextField(null=True, blank=True)
    ctfs_topic_content = models.TextField()
    ctfs_topic_answer = models.TextField(null=True, blank=True)
    ctfs_topic_number = models.IntegerField(null=True, blank=True)
    ctfs_topic_difficulty = models.CharField(max_length=100, null=True, blank=True)
    ctfs_topic_points_add = models.IntegerField(null=True, blank=True)
    ctfs_topic_points_minus = models.IntegerField(null=True, blank=True)
    ctfs_topic_date_created = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.ctfs_topic_title)
        queryset = CTFsTopic.objects.all().filter(ctfs_topic_slug__iexact=original_slug).count()
        count = 1
        ctfs_topic_slug = original_slug
        while(queryset):
            ctfs_topic_slug = original_slug + '-' + str(count)
            count += 1
            queryset = CTFsTopic.objects.all().filter(ctfs_topic_slug__iexact=ctfs_topic_slug).count()
        self.ctfs_topic_slug = ctfs_topic_slug
        super(CTFsTopic, self).save(*args, **kwargs)

    def __str__(self):
        return self.ctfs_topic_title

class CTFFiles(models.Model):
    topic = models.ForeignKey(CTFsTopic, on_delete=models.DO_NOTHING)
    ctffiledescription = models.TextField(null=True, blank=True)
    ctffileupload = models.FileField(upload_to='media', blank=True, null=True)
