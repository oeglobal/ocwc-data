from django.core.management.base import BaseCommand, CommandError
import xlwt
from data.models import *

"""
    $query = "SELECT a.id, e.id as leadid, a.sort_name, cv.description AS description,
                    cv.main_website AS mainweb, cv.ocw_website  AS ocwweb,
                    cv.seal_image__small  AS logo, e.display_name as lead, mt.name as category,
                    m.id as mid, em.email, co.name as country, ma.app_id, ma.app_status,
                    m.join_date, m.membership_type_id  
                FROM civicrm_contact a
                INNER JOIN civicrm_membership m ON m.contact_id = a.id 
                    AND m.status_id = 1
                INNER JOIN civicrm_membership_type mt on mt.id = m.membership_type_id 
                LEFT JOIN civicrm_address adr ON a.id = adr.contact_id
                LEFT JOIN civicrm_country co ON COALESCE(adr.country_id,0) = co.id
                LEFT OUTER JOIN civicrm_value_1_institution_information cv ON a.id = cv.entity_id 
                INNER JOIN civicrm_relationship d ON d.contact_id_b = a.id AND d.relationship_type_id = 6
                INNER JOIN civicrm_contact e on e.id = d.contact_id_a
                INNER JOIN civicrm_email em on em.contact_id = e.id
                    AND em.is_primary = 1
                INNER JOIN jos_member_applications ma ON ma.crm_contact_id_org = a.id 
                WHERE a.id = ".JRequest::getVar( 'orgid', 0 );
"""

def main():
    pass
    # CivicrmMembership
    # CivicrmAddress
    # CivicrmCountry
    # CivicrmValue1InstitutionInformation
    # CivicrmRelationship
    # CivicrmContact 
    # CivicrmEmail
    # JosMemberApplications
    # for app in JosMemberApplications.objects.all():
    #     org_id = app.crm_contact_id_org
    #     # print org_id
    #     if CivicrmValue1InstitutionInformation.objects.filter(entity_id=org_id).exists():
    #         info = CivicrmValue1InstitutionInformation.objects.get(entity_id=org_id)
    #         print org_id, info.description

    #     if CivicrmContact.objects.filter(id=org_id).exists():
    #         contact = CivicrmContact.objects.get(id=org_id)
    #         print org_id, contact.display_name


    # 14821 - 812
    # 15167 - 815
    app = JosMemberApplications.objects.get(app_id=812)
    
    org_id = app.crm_contact_id_org
    ind_id = app.crm_contact_id_ind
    cdate = app.cdate

    # m = CivicrmMembership.objects.get(contact_id=org_id)
    # m.status_id =1
    # m.save()

    # CivicrmMembership.objects.create(
    #     contact_id = org_id,
    #     membership_type_id = 6,
    #     join_date = cdate,
    #     start_date = cdate,
    #     source = 'Queue',
    #     status_id = 2,
    # )

    # print CivicrmMembership.objects.get(contact_id=org_id)


    


class Command(BaseCommand):
  help = "Checks queue in order to ensure that it's consistent"
  args = ''
  
  def handle(self, *args, **options):
      main()
