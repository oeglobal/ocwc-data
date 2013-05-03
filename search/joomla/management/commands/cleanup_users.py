# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db.models import Q

from joomla.models import *
import datetime

def main():
    # grab all joomla users
        # check for last login
        # check for inactivity
        # check for civicrm relations

    qs = JosUsers.objects.filter(
        Q(lastvisitdate=None) | Q(lastvisitdate__lt=(datetime.datetime.now() - datetime.timedelta(days=60))),
        usertype__in=['Registered', '']
    )

    print 'All users:', qs.count()

    rel_count = 0
    mailing_count = 0
    for user in qs:
        # print dir(user)
        if user.civicrmufmatch_set.count():
            # for now skip the 15 users without civicrm contact
            # since it looks like it's a corner case problem with registration

            uf = user.civicrmufmatch_set.all()[0]
            contact = uf.contact
            if CivicrmRelationship.objects.filter(Q(contact_id_a=contact) | Q(contact_id_b=contact)).count():
                rel_count += 1
            elif CivicrmMailingRecipients.objects.filter(contact=contact).exists():
                mailing_count += 1
            else:
                user.delete()
                contact.delete()
                uf.delete()

                #also delete contact and ufmatch?

        else:
            user.delete()

            # also check civicrm mailings maybe?
    print "With relations", rel_count
    print "With mailing", mailing_count


class Command(BaseCommand):
    help = "deletes inactive users from Joomla and CiviCRM"

    def handle(self, *args, **options):
        main()
