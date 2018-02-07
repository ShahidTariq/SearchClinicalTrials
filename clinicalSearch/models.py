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
    no_of_enrollment = models.IntegerField(default=0)
    enrollment_type = models.CharField(max_length=100)
    eligibility_study_pop=models.TextField()
    eligibility_sampling_method = models.CharField(max_length=100)
    eligibility_criteria = models.TextField()
    eligibility_gender = models.CharField(max_length=100)
    eligibility_min_age = models.CharField(max_length=100)
    eligibility_max_age =models.CharField(max_length=100)
    overall_official_name = models.CharField(max_length=100)
    overall_official_role = models.CharField(max_length=100)
    overall_official_affiliation = models.CharField(max_length=100)#important dates
    result_first_posted_date = models.CharField(max_length=100)
    last_updated_date = models.CharField(max_length=100)
    verification_date = models.CharField(max_length=100)


class Outcome(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    outcome_type = models.CharField(max_length=200)  # can be primary or secondary
    measure = models.TextField()
    timeFrame = models.TextField()
    description = models.TextField()


class Condition(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    condition_name = models.CharField(max_length=200)
class Intervention(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    intervention_name = models.CharField(max_length=200)
    intervention_type = models.CharField(max_length=200)
    intervention_description = models.CharField(max_length=200)

class Location(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100)
    location_status = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    location_zip = models.CharField(max_length=100)
    location_country = models.CharField(max_length=100)


class Mesh(models.Model):
    clinicalStudyId = models.ForeignKey(ClinicalStudy, on_delete=models.CASCADE)
    mesh_name = models.CharField(max_length=200)
