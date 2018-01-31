from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage
from xml.dom import minidom
from django.http import HttpResponse
from django.template import Context, loader
import xml.etree.ElementTree as ET
import csv
import os

class Index(View):

    def post(self, request):
        pass

    def get(self, request):
        template = loader.get_template('clinicalSearch/index.html')
        tree = ET.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'media/NCT00001193.xml'))
        root = tree.getroot()
        # open a file for writing

        resident_head = []

        count = 0
        cites_list = []
        pmid_list = []

        for elt in tree.iter():
            print("%s: '%s'" % (elt.tag, elt.text))

        for data in root.findall('reference'):
            citation = data.find('citation').text
            pmid = data.find('PMID').text
            cites_list.append(citation)
            pmid_list.append(pmid)

        context = {
            'citation': cites_list,
            'pmid': pmid_list,
        }
        return HttpResponse(template.render(context, request))
