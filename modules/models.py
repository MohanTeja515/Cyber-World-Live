from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    INTRODUCTION_TO_HACKING = 'introduction to hacking'
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
    IOT_HACKING = 'IOT hacking'
    CLOUD_COMPUTING = 'cloud computing'
    CRYPTOGRAPHY = 'cryptography'


class Module(models.Model):
    module_title = models.CharField(max_length=300, choices=Categories.choices, default=Categories.INTRODUCTION_TO_HACKING)
    module_slug = models.SlugField()
    module_photos = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    module_description = models.TextField()
    module_content = models.TextField()
    module_level = models.IntegerField()
    module_difficulty = models.CharField(max_length=100)
    module_area = models.CharField(max_length=100)
    module_sections = models.IntegerField()
    module_points_add = models.IntegerField()
    module_points_minus = models.IntegerField()
    module_date_created = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.module_title)
        queryset = Module.objects.all().filter(module_slug__iexact=original_slug).count()
        count = 1
        module_slug = original_slug
        while(queryset):
            module_slug = original_slug + '-' + str(count)
            count += 1
            queryset = Module.objects.all().filter(module_slug__iexact=module_slug).count()
        self.module_slug = module_slug
        super(Module, self).save(*args, **kwargs)

    def __str__(self):
        return self.module_title


class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING, related_name='moduletopic', verbose_name=('squadra'),)
    topic_title = models.CharField(max_length=300)
    topic_slug = models.SlugField()
    topic_description = models.TextField()
    topic_content = models.TextField()
    topic_number = models.IntegerField()
    topic_date_created = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.topic_title)
        queryset = Topic.objects.all().filter(topic_slug__iexact=original_slug).count()
        count = 1
        topic_slug = original_slug
        while(queryset):
            topic_slug = original_slug + '-' + str(count)
            count += 1
            queryset = Topic.objects.all().filter(topic_slug__iexact=topic_slug).count()
        self.topic_slug = topic_slug
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.topic_title





