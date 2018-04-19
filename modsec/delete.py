import django
import sys, os
from django.template.defaultfilters import length
sys.path.append("/home/nomis/modsec")
os.environ['DJANGO_SETTINGS_MODULE'] = 'TFG.settings'

django.setup()
from modsec.models import Rule, Log,Category

def delete_everything():
    Rule.objects.all().delete()
    Log.objects.all().delete()
    Category.objects.all().delete()

if __name__ == '__main__':
    delete_everything()
