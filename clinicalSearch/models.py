from django.db import models
from django.urls import reverse


class ClinicalStudy(models.Model):
    org_study_id = models.CharField(max_length=100)
    nct_id = models.CharField(max_length=100)
    official_title = models.CharField(max_length=100)
    lead_sponsor_agency = models.CharField(max_length=100)
    lead_sponsor_agency_class = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    brief_summary = models.TextField()
    detail_description = models.TextField()
    overall_status = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100) #string date may be parsed before inserting
    completion_date = models.CharField(max_length=100) #string date may be parsed before inserting
    study_type = models.CharField(max_length=100)
    no_of_arms = models.IntegerField(default=0)


class Outcome(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    outcome_type = models.CharField(max_length=200)  # can be primary or secondary
    measure = models.TextField()
    timeFrame = models.TextField()
    description = models.TextField()


class Condition(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    condition_name = models.CharField(max_length=200)
