# Generated by Django 2.0.1 on 2018-02-01 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_study_id', models.CharField(max_length=100)),
                ('nct_id', models.CharField(max_length=100)),
                ('official_title', models.CharField(max_length=100)),
                ('lead_sponsor_agency', models.CharField(max_length=100)),
                ('lead_sponsor_agency_class', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=500)),
                ('brief_summary', models.TextField()),
                ('detail_description', models.TextField()),
                ('overall_status', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100)),
                ('completion_date', models.CharField(max_length=100)),
                ('study_type', models.CharField(max_length=100)),
                ('no_of_arms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome_type', models.CharField(max_length=200)),
                ('measure', models.TextField()),
                ('timeFrame', models.TextField()),
                ('description', models.TextField()),
                ('clinicalStudyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalSearch.ClinicalStudy')),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome_type', models.CharField(max_length=200)),
                ('measure', models.TextField()),
                ('timeFrame', models.TextField()),
                ('description', models.TextField()),
                ('clinicalStudyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicalSearch.ClinicalStudy')),
            ],
        ),
    ]