# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from joomla.models import *
import datetime
def main():
    # for app in JosMemberApplications.objects.filter(app_status='Submitted'):
    #   print app

    for app in JosMemberApplications.objects.filter(app_status='Submitted'):
        org_id = app.crm_contact_id_org
        # print org_id
        info = False
        if CivicrmValue1InstitutionInformation.objects.filter(entity_id=org_id).exists():
            info = CivicrmValue1InstitutionInformation.objects.get(entity_id=org_id)
            # print org_id, info.description.encode('utf-8')

        if not info:
            if CivicrmContact.objects.filter(id=org_id).exists():
                contact = CivicrmContact.objects.get(id=org_id)

                user = app.joomla_user
                # print app.joomla_user, org_id, contact.display_name.encode('utf-8')
                user.block = 1
                user.lastvisitdate = datetime.date(1900, 01, 01)
                user.save()

                app.app_status = 'Spam'
                app.save()


class Command(BaseCommand):
    help = "cleans membership application spam"

    def handle(self, *args, **options):
        main()
