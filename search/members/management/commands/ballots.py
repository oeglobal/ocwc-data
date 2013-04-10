# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from joomla.models import *
import datetime

def main():
	ballots_ids = [10, 11]

	for bid in ballots_ids:
		ballot = JosElectionBallots.objects.get(pk=bid)
		print ballot.title
		# print dir(ballot)

		voters = []
		for boption in ballot.joselectionballotoptions_set.all():
			# print unicode(boption), boption.joselectionvotes_set.count()

			for vote in boption.joselectionvotes_set.all():
				crmid = int(vote.crm_id.id)
				if crmid not in voters:
					voters.append(crmid)
					print crmid, vote.crm_id.first_name, vote.crm_id.last_name

		print sorted(voters)



class Command(BaseCommand):
    help = "calculates ballots"

    def handle(self, *args, **options):
        main()
