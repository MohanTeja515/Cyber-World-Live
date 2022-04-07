from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    INTRODUCTION_TO_ETHICAL_HACKING_LABS = 'introduction to ethical hacking labs'
    FOOTPRINTING_LABS = 'footprinting labs'
    NETWORK_SCANNING_LABS = 'network scaning labs'
    ENUMERATION_LABS = 'enumeration labs'
    VULNERABILITY_ANALYSIS_LABS = 'vulnerability Analysis labs'
    SYSTEM_HACKING_LABS = 'system hacking labs'
    MALWARE_ANALYSIS_LABS = 'malware analysis labs'
    SNIFFING_LABS = 'sniffing labs'
    SOCIAL_ENGINEERING_LABS = 'social engineering labs'
    DENIEAL_OF_SERVICE_ATTACK_LABS = 'denieal of service attack labs'
    SESSION_HIJACKING_LABS = 'session hijacking labs'
    FIREWALL_IDS_IPS_HONEYPOTS_LABS = 'firewall labs'
    HACKING_WEB_SERVERS_LABS = 'hacking web servers labs'
    HACKING_WEB_APPLICATIONS_LABS = 'hacking web applications labs'
    SQL_INJECTION_LABS = 'sql injection labs'
    HACKING_MOBILE_PLATFORMS_LABS = 'hacking mobile platforms labs'
    WIFI_HACKING_LABS = 'wifi hacking labs'
    IOT_LABS = 'iot labs'
    CLOUD_COMPUTING_LABS = 'cloud computing labs'
    CRYPTOGRAPHY_LABS = 'cryptography labs'

class Labs(models.Model):
    lab_title = models.CharField(max_length=300, choices=Categories.choices, default=Categories.INTRODUCTION_TO_ETHICAL_HACKING_LABS)
    lab_slug = models.SlugField()
    lab_photos = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    lab_description = models.TextField()
    lab_content = models.TextField()
    lab_level = models.IntegerField()
    lab_difficulty = models.CharField(max_length=100)
    lab_area = models.CharField(max_length=100)
    lab_sections = models.IntegerField()
    lab_points_add = models.IntegerField()
    lab_points_minus = models.IntegerField()
    lab_date_created = models.DateTimeField(default=datetime.now, null=True, blank=True)


    def save(self, *args, **kwargs):
        original_slug = slugify(self.lab_title)
        queryset = Labs.objects.all().filter(lab_slug__iexact=original_slug).count()
        count = 1
        lab_slug = original_slug
        while(queryset):
            lab_slug = original_slug + '-' + str(count)
            count += 1
            queryset = Labs.objects.all().filter(lab_slug__iexact=lab_slug).count()
        self.lab_slug = lab_slug
        super(Labs, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_title

class LabTopic(models.Model):
    module = models.ForeignKey(Labs, on_delete=models.DO_NOTHING)
    lab_topic_title = models.CharField(max_length=300)
    lab_topic_slug = models.SlugField()
    lab_topic_description = models.TextField()
    lab_topic_content = models.TextField()
    lab_topic_number = models.IntegerField()
    lab_topic_date_created = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.lab_topic_title)
        queryset = LabTopic.objects.all().filter(lab_topic_slug__iexact=original_slug).count()
        count = 1
        lab_topic_slug = original_slug
        while(queryset):
            lab_topic_slug = original_slug + '-' + str(count)
            count += 1
            queryset = LabTopic.objects.all().filter(lab_topic_slug__iexact=lab_topic_slug).count()
        self.lab_topic_slug = lab_topic_slug
        super(LabTopic, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_topic_title

