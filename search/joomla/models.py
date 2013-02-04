from django.db import models

# class AjaxChatBans(models.Model):
#     userid = models.IntegerField(db_column='userID') # Field name made lowercase.
#     username = models.CharField(max_length=192, db_column='userName') # Field name made lowercase.
#     datetime = models.DateTimeField(db_column='dateTime') # Field name made lowercase.
#     ip = models.CharField(max_length=16)
#     class Meta:
#         db_table = u'ajax_chat_bans'

# class AjaxChatInvitations(models.Model):
#     userid = models.IntegerField(db_column='userID') # Field name made lowercase.
#     channel = models.IntegerField()
#     datetime = models.DateTimeField(db_column='dateTime') # Field name made lowercase.
#     class Meta:
#         db_table = u'ajax_chat_invitations'

# class AjaxChatMessages(models.Model):
#     id = models.IntegerField(primary_key=True)
#     userid = models.IntegerField(db_column='userID') # Field name made lowercase.
#     username = models.CharField(max_length=192, db_column='userName') # Field name made lowercase.
#     userrole = models.IntegerField(db_column='userRole') # Field name made lowercase.
#     channel = models.IntegerField()
#     datetime = models.DateTimeField(db_column='dateTime') # Field name made lowercase.
#     ip = models.CharField(max_length=16)
#     text = models.TextField(blank=True)
#     class Meta:
#         db_table = u'ajax_chat_messages'

# class AjaxChatOnline(models.Model):
#     userid = models.IntegerField(db_column='userID') # Field name made lowercase.
#     username = models.CharField(max_length=192, db_column='userName') # Field name made lowercase.
#     userrole = models.IntegerField(db_column='userRole') # Field name made lowercase.
#     channel = models.IntegerField()
#     datetime = models.DateTimeField(db_column='dateTime') # Field name made lowercase.
#     ip = models.CharField(max_length=16)
#     class Meta:
#         db_table = u'ajax_chat_online'

class CfGetorgs(models.Model):
    source = models.CharField(max_length=765)
    crmid = models.IntegerField(unique=True, primary_key=True)
    url = models.CharField(max_length=765)
    language = models.CharField(max_length=765)
    last_indexed = models.DateTimeField(null=True, blank=True)
    executed = models.IntegerField()
    class Meta:
        db_table = u'cf_getorgs'

# class CivicrmAcl(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, blank=True)
#     deny = models.IntegerField()
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField(null=True, blank=True)
#     operation = models.CharField(max_length=18)
#     object_table = models.CharField(max_length=192, blank=True)
#     object_id = models.IntegerField(null=True, blank=True)
#     acl_table = models.CharField(max_length=192, blank=True)
#     acl_id = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_acl'

# class CivicrmAclCache(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     acl = models.ForeignKey(CivicrmAcl)
#     modified_date = models.DateField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_acl_cache'

# class CivicrmAclContactCache(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(CivicrmContact, unique=True, null=True, blank=True)
#     contact = models.ForeignKey(CivicrmContact)
#     operation = models.CharField(max_length=18, unique=True)
#     class Meta:
#         db_table = u'civicrm_acl_contact_cache'

# class CivicrmAclEntityRole(models.Model):
#     id = models.IntegerField(primary_key=True)
#     acl_role_id = models.IntegerField()
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_acl_entity_role'

# class CivicrmActivity(models.Model):
#     id = models.IntegerField(primary_key=True)
#     source_contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     source_record_id = models.IntegerField(null=True, blank=True)
#     activity_type_id = models.IntegerField()
#     subject = models.CharField(max_length=765, blank=True)
#     activity_date_time = models.DateTimeField(null=True, blank=True)
#     duration = models.IntegerField(null=True, blank=True)
#     location = models.CharField(max_length=765, blank=True)
#     phone = models.ForeignKey(CivicrmPhone, null=True, blank=True)
#     phone_number = models.CharField(max_length=192, blank=True)
#     details = models.TextField(blank=True)
#     status_id = models.IntegerField(null=True, blank=True)
#     priority_id = models.IntegerField(null=True, blank=True)
#     parent = models.ForeignKey('self', null=True, blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     medium_id = models.IntegerField(null=True, blank=True)
#     is_auto = models.IntegerField(null=True, blank=True)
#     relationship = models.ForeignKey(CivicrmRelationship, null=True, blank=True)
#     is_current_revision = models.IntegerField(null=True, blank=True)
#     original = models.ForeignKey('self', null=True, blank=True)
#     is_deleted = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_activity'

# class CivicrmActivityAssignment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     activity = models.ForeignKey(CivicrmActivity)
#     assignee_contact = models.ForeignKey(CivicrmContact, unique=True)
#     class Meta:
#         db_table = u'civicrm_activity_assignment'

# class CivicrmActivityHistory(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity_id = models.IntegerField()
#     activity_type = models.CharField(max_length=192, blank=True)
#     module = models.CharField(max_length=192, blank=True)
#     callback = models.CharField(max_length=192, blank=True)
#     activity_id = models.IntegerField()
#     activity_summary = models.CharField(max_length=765, blank=True)
#     activity_date = models.DateTimeField(null=True, blank=True)
#     relationship = models.ForeignKey(CivicrmRelationship, null=True, blank=True)
#     group = models.ForeignKey(CivicrmGroup, null=True, blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_activity_history'

# class CivicrmActivityTarget(models.Model):
#     id = models.IntegerField(primary_key=True)
#     activity = models.ForeignKey(CivicrmActivity)
#     target_contact = models.ForeignKey(CivicrmContact, unique=True)
#     class Meta:
#         db_table = u'civicrm_activity_target'

class CivicrmAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey('CivicrmContact', null=True, blank=True)
    location_type_id = models.IntegerField(null=True, blank=True)
    is_primary = models.IntegerField(null=True, blank=True)
    is_billing = models.IntegerField(null=True, blank=True)
    street_address = models.CharField(max_length=288, blank=True)
    street_number = models.IntegerField(null=True, blank=True)
    street_number_suffix = models.CharField(max_length=24, blank=True)
    street_number_predirectional = models.CharField(max_length=24, blank=True)
    street_name = models.CharField(max_length=192, blank=True)
    street_type = models.CharField(max_length=24, blank=True)
    street_number_postdirectional = models.CharField(max_length=24, blank=True)
    street_unit = models.CharField(max_length=48, blank=True)
    supplemental_address_1 = models.CharField(max_length=288, blank=True)
    supplemental_address_2 = models.CharField(max_length=288, blank=True)
    supplemental_address_3 = models.CharField(max_length=288, blank=True)
    city = models.CharField(max_length=192, blank=True)
    county = models.ForeignKey('CivicrmCounty', null=True, blank=True)
    state_province = models.ForeignKey('CivicrmStateProvince', null=True, blank=True)
    postal_code_suffix = models.CharField(max_length=36, blank=True)
    postal_code = models.CharField(max_length=36, blank=True)
    usps_adc = models.CharField(max_length=96, blank=True)
    country = models.ForeignKey('CivicrmCountry', null=True, blank=True)
    geo_code_1 = models.FloatField(null=True, blank=True)
    geo_code_2 = models.FloatField(null=True, blank=True)
    timezone = models.CharField(max_length=24, blank=True)
    name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'civicrm_address'

# class CivicrmCache(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group_name = models.CharField(max_length=96, unique=True)
#     path = models.CharField(max_length=192, unique=True, blank=True)
#     data = models.TextField(blank=True)
#     component = models.ForeignKey(CivicrmComponent, null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     expired_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_cache'

class CivicrmCase(models.Model):
    id = models.IntegerField(primary_key=True)
    case_type_id = models.CharField(max_length=384)
    subject = models.CharField(max_length=384, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    details = models.TextField(blank=True)
    status_id = models.IntegerField()
    is_deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_case'

# class CivicrmCaseActivity(models.Model):
#     id = models.IntegerField(primary_key=True)
#     case = models.ForeignKey(CivicrmCase)
#     activity = models.ForeignKey(CivicrmActivity)
#     class Meta:
#         db_table = u'civicrm_case_activity'

# class CivicrmCaseContact(models.Model):
#     id = models.IntegerField(primary_key=True)
#     case = models.ForeignKey(CivicrmCase, unique=True)
#     contact = models.ForeignKey(CivicrmContact)
#     class Meta:
#         db_table = u'civicrm_case_contact'

# class CivicrmComponent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192)
#     namespace = models.CharField(max_length=384, blank=True)
#     class Meta:
#         db_table = u'civicrm_component'

class CivicrmContact(models.Model):
    nick_name = models.CharField(max_length=384, blank=True)
    legal_name = models.CharField(max_length=384, blank=True)
    contact_type = models.CharField(max_length=192, blank=True)
    do_not_email = models.IntegerField(null=True, blank=True)
    do_not_phone = models.IntegerField(null=True, blank=True)
    do_not_mail = models.IntegerField(null=True, blank=True)
    do_not_sms = models.IntegerField(null=True, blank=True)
    contact_sub_type = models.CharField(max_length=192, blank=True)
    legal_identifier = models.CharField(max_length=96, blank=True)
    external_identifier = models.CharField(max_length=96, unique=True, blank=True)
    sort_name = models.CharField(max_length=384, blank=True)
    display_name = models.CharField(max_length=384, blank=True)
    # home_url = models.CharField(max_length=384, db_column='home_URL', blank=True) # Field name made lowercase.
    image_url = models.CharField(max_length=384, db_column='image_URL', blank=True) # Field name made lowercase.
    preferred_communication_method = models.CharField(max_length=765, blank=True)
    preferred_mail_format = models.CharField(max_length=12, blank=True)
    do_not_trade = models.IntegerField(null=True, blank=True)
    hash = models.CharField(max_length=96, blank=True)
    is_opt_out = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=765, blank=True)
    first_name = models.CharField(max_length=192, blank=True)
    middle_name = models.CharField(max_length=192, blank=True)
    last_name = models.CharField(max_length=192, blank=True)
    prefix_id = models.IntegerField(null=True, blank=True)
    suffix_id = models.IntegerField(null=True, blank=True)
    email_greeting_id = models.IntegerField(null=True, blank=True)
    email_greeting_custom = models.CharField(max_length=384, blank=True)
    email_greeting_display = models.CharField(max_length=765, blank=True)
    postal_greeting_id = models.IntegerField(null=True, blank=True)
    postal_greeting_custom = models.CharField(max_length=384, blank=True)
    postal_greeting_display = models.CharField(max_length=765, blank=True)
    addressee_id = models.IntegerField(null=True, blank=True)
    addressee_custom = models.CharField(max_length=384, blank=True)
    addressee_display = models.CharField(max_length=765, blank=True)
    job_title = models.CharField(max_length=765, blank=True)
    gender_id = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_deceased = models.IntegerField(null=True, blank=True)
    deceased_date = models.DateField(null=True, blank=True)
    # mail_to_household = models.ForeignKey('self', null=True, blank=True, related_name='mail_to_household2')
    household_name = models.CharField(max_length=384, blank=True)
    primary_contact = models.ForeignKey('self', null=True, blank=True, related_name='primary_contact2')
    organization_name = models.CharField(max_length=384, blank=True)
    sic_code = models.CharField(max_length=24, blank=True)
    user_unique_id = models.CharField(max_length=765, blank=True)
    employer = models.ForeignKey('self', null=True, blank=True)
    api_key = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'civicrm_contact'

class CivicrmContactType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, unique=True, blank=True)
    label = models.CharField(max_length=192, blank=True)
    description = models.TextField(blank=True)
    image_url = models.CharField(max_length=765, db_column='image_URL', blank=True) # Field name made lowercase.
    parent = models.ForeignKey('self', null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    is_reserved = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_contact_type'

# class CivicrmContribution(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     contribution_type = models.ForeignKey(CivicrmContributionType, null=True, blank=True)
#     contribution_page = models.ForeignKey(CivicrmContributionPage, null=True, blank=True)
#     payment_instrument_id = models.IntegerField(null=True, blank=True)
#     receive_date = models.DateTimeField(null=True, blank=True)
#     non_deductible_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     total_amount = models.DecimalField(max_digits=22, decimal_places=2)
#     fee_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     net_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     trxn_id = models.CharField(max_length=765, unique=True, blank=True)
#     invoice_id = models.CharField(max_length=765, unique=True, blank=True)
#     currency = models.CharField(max_length=192)
#     cancel_date = models.DateTimeField(null=True, blank=True)
#     cancel_reason = models.TextField(blank=True)
#     receipt_date = models.DateTimeField(null=True, blank=True)
#     thankyou_date = models.DateTimeField(null=True, blank=True)
#     source = models.CharField(max_length=765, blank=True)
#     amount_level = models.TextField(blank=True)
#     contribution_recur = models.ForeignKey(CivicrmContributionRecur, null=True, blank=True)
#     honor_contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     is_pay_later = models.IntegerField(null=True, blank=True)
#     contribution_status_id = models.IntegerField(null=True, blank=True)
#     honor_type_id = models.IntegerField(null=True, blank=True)
#     address = models.ForeignKey(CivicrmAddress, null=True, blank=True)
#     check_number = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_contribution'

# class CivicrmContributionPage(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765, blank=True)
#     intro_text = models.TextField(blank=True)
#     contribution_type = models.ForeignKey(CivicrmContributionType)
#     payment_processor = models.ForeignKey(CivicrmPaymentProcessor, null=True, blank=True)
#     is_credit_card_only = models.IntegerField(null=True, blank=True)
#     is_monetary = models.IntegerField(null=True, blank=True)
#     is_recur = models.IntegerField(null=True, blank=True)
#     recur_frequency_unit = models.CharField(max_length=384, blank=True)
#     is_recur_interval = models.IntegerField(null=True, blank=True)
#     is_pay_later = models.IntegerField(null=True, blank=True)
#     pay_later_text = models.TextField(blank=True)
#     pay_later_receipt = models.TextField(blank=True)
#     is_allow_other_amount = models.IntegerField(null=True, blank=True)
#     default_amount_id = models.IntegerField(null=True, blank=True)
#     min_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     max_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     goal_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     thankyou_title = models.CharField(max_length=765, blank=True)
#     thankyou_text = models.TextField(blank=True)
#     thankyou_footer = models.TextField(blank=True)
#     is_for_organization = models.IntegerField(null=True, blank=True)
#     for_organization = models.TextField(blank=True)
#     is_email_receipt = models.IntegerField(null=True, blank=True)
#     receipt_from_name = models.CharField(max_length=765, blank=True)
#     receipt_from_email = models.CharField(max_length=765, blank=True)
#     cc_receipt = models.CharField(max_length=765, blank=True)
#     bcc_receipt = models.CharField(max_length=765, blank=True)
#     receipt_text = models.TextField(blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     footer_text = models.TextField(blank=True)
#     amount_block_is_active = models.IntegerField(null=True, blank=True)
#     honor_block_is_active = models.IntegerField(null=True, blank=True)
#     honor_block_title = models.CharField(max_length=765, blank=True)
#     honor_block_text = models.TextField(blank=True)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     created = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_contribution_page'

# class CivicrmContributionProduct(models.Model):
#     id = models.IntegerField(primary_key=True)
#     product_id = models.IntegerField()
#     contribution = models.ForeignKey(CivicrmContribution)
#     product_option = models.CharField(max_length=765, blank=True)
#     quantity = models.IntegerField(null=True, blank=True)
#     fulfilled_date = models.DateField(null=True, blank=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     comment = models.TextField(blank=True)
#     class Meta:
#         db_table = u'civicrm_contribution_product'

# class CivicrmContributionRecur(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     amount = models.DecimalField(max_digits=22, decimal_places=2)
#     frequency_unit = models.CharField(max_length=15, blank=True)
#     frequency_interval = models.IntegerField()
#     installments = models.IntegerField(null=True, blank=True)
#     start_date = models.DateTimeField()
#     create_date = models.DateTimeField()
#     modified_date = models.DateTimeField(null=True, blank=True)
#     cancel_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     processor_id = models.CharField(max_length=765, blank=True)
#     trxn_id = models.CharField(max_length=765, unique=True, blank=True)
#     invoice_id = models.CharField(max_length=765, unique=True, blank=True)
#     contribution_status_id = models.IntegerField(null=True, blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     cycle_day = models.IntegerField()
#     next_sched_contribution = models.DateTimeField(null=True, blank=True)
#     failure_count = models.IntegerField(null=True, blank=True)
#     failure_retry_date = models.DateTimeField(null=True, blank=True)
#     auto_renew = models.IntegerField()
#     class Meta:
#         db_table = u'civicrm_contribution_recur'

# class CivicrmContributionSoft(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contribution = models.ForeignKey(CivicrmContribution)
#     contact = models.ForeignKey(CivicrmContact)
#     amount = models.DecimalField(max_digits=22, decimal_places=2)
#     pcp = models.ForeignKey(CivicrmPcp, null=True, blank=True)
#     pcp_display_in_roll = models.IntegerField(null=True, blank=True)
#     pcp_roll_nickname = models.CharField(max_length=765, blank=True)
#     pcp_personal_note = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_contribution_soft'

class CivicrmContributionType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, unique=True, blank=True)
    accounting_code = models.CharField(max_length=192, blank=True)
    description = models.CharField(max_length=765, blank=True)
    is_deductible = models.IntegerField(null=True, blank=True)
    is_reserved = models.IntegerField(null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_contribution_type'

# class CivicrmContributionWidget(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contribution_page = models.ForeignKey(CivicrmContributionPage, null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     title = models.CharField(max_length=765, blank=True)
#     url_logo = models.CharField(max_length=765, blank=True)
#     button_title = models.CharField(max_length=765, blank=True)
#     about = models.TextField(blank=True)
#     url_homepage = models.CharField(max_length=765, blank=True)
#     color_title = models.CharField(max_length=30, blank=True)
#     color_button = models.CharField(max_length=30, blank=True)
#     color_bar = models.CharField(max_length=30, blank=True)
#     color_main_text = models.CharField(max_length=30, blank=True)
#     color_main = models.CharField(max_length=30, blank=True)
#     color_main_bg = models.CharField(max_length=30, blank=True)
#     color_bg = models.CharField(max_length=30, blank=True)
#     color_about_link = models.CharField(max_length=30, blank=True)
#     color_homepage_link = models.CharField(max_length=30, blank=True)
#     class Meta:
#         db_table = u'civicrm_contribution_widget'

class CivicrmCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, unique=True, blank=True)
    iso_code = models.CharField(max_length=6, unique=True, blank=True)
    country_code = models.CharField(max_length=12, blank=True)
    idd_prefix = models.CharField(max_length=12, blank=True)
    ndd_prefix = models.CharField(max_length=12, blank=True)
    region = models.ForeignKey('CivicrmWorldregion', null=True, blank=True)
    developing = models.IntegerField()
    is_province_abbreviated = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_country'

class CivicrmCounty(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, unique=True, blank=True)
    abbreviation = models.CharField(max_length=12, blank=True)
    state_province = models.ForeignKey('CivicrmStateProvince')
    class Meta:
        db_table = u'civicrm_county'

# class CivicrmCurrency(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, blank=True)
#     symbol = models.CharField(max_length=24, blank=True)
#     numeric_code = models.CharField(max_length=9, blank=True)
#     full_name = models.CharField(max_length=192, blank=True)
#     class Meta:
#         db_table = u'civicrm_currency'

# class CivicrmCustomField(models.Model):
#     id = models.IntegerField(primary_key=True)
#     custom_group = models.ForeignKey(CivicrmCustomGroup)
#     label = models.CharField(max_length=765, unique=True, blank=True)
#     data_type = models.CharField(max_length=48)
#     html_type = models.CharField(max_length=81)
#     default_value = models.CharField(max_length=765, blank=True)
#     is_required = models.IntegerField(null=True, blank=True)
#     is_searchable = models.IntegerField(null=True, blank=True)
#     is_search_range = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField()
#     help_pre = models.TextField(blank=True)
#     help_post = models.TextField(blank=True)
#     mask = models.CharField(max_length=192, blank=True)
#     attributes = models.CharField(max_length=765, blank=True)
#     javascript = models.CharField(max_length=765, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_view = models.IntegerField(null=True, blank=True)
#     options_per_line = models.IntegerField(null=True, blank=True)
#     text_length = models.IntegerField(null=True, blank=True)
#     start_date_years = models.IntegerField(null=True, blank=True)
#     end_date_years = models.IntegerField(null=True, blank=True)
#     date_format = models.CharField(max_length=192, blank=True)
#     time_format = models.IntegerField(null=True, blank=True)
#     note_columns = models.IntegerField(null=True, blank=True)
#     note_rows = models.IntegerField(null=True, blank=True)
#     column_name = models.CharField(max_length=765, blank=True)
#     option_group_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_custom_field'

# class CivicrmCustomGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, unique=True, blank=True)
#     title = models.CharField(max_length=192, unique=True, blank=True)
#     extends = models.CharField(max_length=36, unique=True, blank=True)
#     extends_entity_column_id = models.IntegerField(null=True, blank=True)
#     extends_entity_column_value = models.CharField(max_length=192, blank=True)
#     style = models.CharField(max_length=18, blank=True)
#     collapse_display = models.IntegerField(null=True, blank=True)
#     help_pre = models.TextField(blank=True)
#     help_post = models.TextField(blank=True)
#     weight = models.IntegerField()
#     is_active = models.IntegerField(null=True, blank=True)
#     table_name = models.CharField(max_length=765, blank=True)
#     is_multiple = models.IntegerField(null=True, blank=True)
#     min_multiple = models.IntegerField(null=True, blank=True)
#     max_multiple = models.IntegerField(null=True, blank=True)
#     collapse_adv_display = models.IntegerField(null=True, blank=True)
#     created = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_custom_group'

# class CivicrmDashboard(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain_id = models.IntegerField()
#     label = models.CharField(max_length=765, blank=True)
#     url = models.CharField(max_length=765, blank=True)
#     content = models.TextField(blank=True)
#     permission = models.CharField(max_length=765, blank=True)
#     permission_operator = models.CharField(max_length=9, blank=True)
#     column_no = models.IntegerField(null=True, blank=True)
#     is_minimized = models.IntegerField(null=True, blank=True)
#     is_fullscreen = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField(null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     is_reserved = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_dashboard'

# class CivicrmDashboardContact(models.Model):
#     id = models.IntegerField(primary_key=True)
#     dashboard_id = models.IntegerField()
#     contact_id = models.IntegerField()
#     column_no = models.IntegerField(null=True, blank=True)
#     is_minimized = models.IntegerField(null=True, blank=True)
#     is_fullscreen = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_dashboard_contact'

# class CivicrmDedupeRule(models.Model):
#     id = models.IntegerField(primary_key=True)
#     dedupe_rule_group = models.ForeignKey(CivicrmDedupeRuleGroup)
#     rule_table = models.CharField(max_length=192)
#     rule_field = models.CharField(max_length=192)
#     rule_length = models.IntegerField(null=True, blank=True)
#     rule_weight = models.IntegerField()
#     class Meta:
#         db_table = u'civicrm_dedupe_rule'

# class CivicrmDedupeRuleGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact_type = models.CharField(max_length=36, blank=True)
#     threshold = models.IntegerField()
#     level = models.CharField(max_length=18, blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=192, blank=True)
#     class Meta:
#         db_table = u'civicrm_dedupe_rule_group'

# class CivicrmDiscount(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity_id = models.IntegerField()
#     option_group = models.ForeignKey(CivicrmOptionGroup)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_discount'

class CivicrmDomain(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, unique=True, blank=True)
    description = models.CharField(max_length=765, blank=True)
    config_backend = models.TextField(blank=True)
    version = models.CharField(max_length=96, blank=True)
    loc_block_id = models.IntegerField(null=True, blank=True)
    locales = models.TextField(blank=True)
    class Meta:
        db_table = u'civicrm_domain'

class CivicrmEmail(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
    location_type_id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=192, blank=True)
    is_primary = models.IntegerField(null=True, blank=True)
    is_billing = models.IntegerField(null=True, blank=True)
    on_hold = models.IntegerField()
    is_bulkmail = models.IntegerField()
    hold_date = models.DateTimeField(null=True, blank=True)
    reset_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_email'

# class CivicrmEntityFile(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity_id = models.IntegerField()
#     file = models.ForeignKey(CivicrmFile)
#     class Meta:
#         db_table = u'civicrm_entity_file'

# class CivicrmEntityTag(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     tag = models.ForeignKey(CivicrmTag)
#     class Meta:
#         db_table = u'civicrm_entity_tag'

# class CivicrmEvent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765, blank=True)
#     summary = models.TextField(blank=True)
#     description = models.TextField(blank=True)
#     event_type_id = models.IntegerField(null=True, blank=True)
#     participant_listing_id = models.IntegerField(null=True, blank=True)
#     is_public = models.IntegerField(null=True, blank=True)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     is_online_registration = models.IntegerField(null=True, blank=True)
#     registration_link_text = models.CharField(max_length=765, blank=True)
#     registration_start_date = models.DateTimeField(null=True, blank=True)
#     registration_end_date = models.DateTimeField(null=True, blank=True)
#     max_participants = models.IntegerField(null=True, blank=True)
#     event_full_text = models.TextField(blank=True)
#     is_monetary = models.IntegerField(null=True, blank=True)
#     contribution_type_id = models.IntegerField(null=True, blank=True)
#     payment_processor = models.ForeignKey(CivicrmPaymentProcessor, null=True, blank=True)
#     is_map = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     fee_label = models.CharField(max_length=765, blank=True)
#     is_show_location = models.IntegerField(null=True, blank=True)
#     loc_block = models.ForeignKey(CivicrmLocBlock, null=True, blank=True)
#     default_role_id = models.IntegerField(null=True, blank=True)
#     intro_text = models.TextField(blank=True)
#     footer_text = models.TextField(blank=True)
#     confirm_title = models.CharField(max_length=765, blank=True)
#     confirm_text = models.TextField(blank=True)
#     confirm_footer_text = models.TextField(blank=True)
#     confirm_email_text = models.TextField(blank=True)
#     confirm_from_name = models.CharField(max_length=765, blank=True)
#     thankyou_title = models.CharField(max_length=765, blank=True)
#     thankyou_text = models.TextField(blank=True)
#     thankyou_footer_text = models.TextField(blank=True)
#     pay_later_text = models.TextField(blank=True)
#     pay_later_receipt = models.TextField(blank=True)
#     is_email_confirm = models.IntegerField(null=True, blank=True)
#     confirm_from_email = models.CharField(max_length=765, blank=True)
#     cc_confirm = models.CharField(max_length=765, blank=True)
#     bcc_confirm = models.CharField(max_length=765, blank=True)
#     default_fee_id = models.IntegerField(null=True, blank=True)
#     default_discount_fee_id = models.IntegerField(null=True, blank=True)
#     is_pay_later = models.IntegerField(null=True, blank=True)
#     is_multiple_registrations = models.IntegerField(null=True, blank=True)
#     allow_same_participant_emails = models.IntegerField(null=True, blank=True)
#     is_template = models.IntegerField(null=True, blank=True)
#     template_title = models.CharField(max_length=765, blank=True)
#     has_waitlist = models.IntegerField(null=True, blank=True)
#     requires_approval = models.IntegerField(null=True, blank=True)
#     expiration_time = models.IntegerField(null=True, blank=True)
#     waitlist_text = models.TextField(blank=True)
#     approval_req_text = models.TextField(blank=True)
#     created = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_event'

# class CivicrmFile(models.Model):
#     id = models.IntegerField(primary_key=True)
#     file_type_id = models.IntegerField(null=True, blank=True)
#     mime_type = models.CharField(max_length=765, blank=True)
#     uri = models.CharField(max_length=765, blank=True)
#     document = models.TextField(blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     upload_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_file'

# class CivicrmFinancialTrxn(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contribution = models.ForeignKey(CivicrmContribution)
#     trxn_date = models.DateTimeField()
#     trxn_type = models.CharField(max_length=18)
#     total_amount = models.DecimalField(max_digits=22, decimal_places=2)
#     fee_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     net_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     currency = models.CharField(max_length=192)
#     payment_processor = models.CharField(max_length=192)
#     trxn_id = models.CharField(max_length=765, unique=True)
#     trxn_result_code = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_financial_trxn'

# class CivicrmGrant(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     application_received_date = models.DateField(null=True, blank=True)
#     decision_date = models.DateField(null=True, blank=True)
#     money_transfer_date = models.DateField(null=True, blank=True)
#     grant_due_date = models.DateField(null=True, blank=True)
#     grant_report_received = models.IntegerField(null=True, blank=True)
#     grant_type_id = models.IntegerField()
#     amount_total = models.DecimalField(max_digits=22, decimal_places=2)
#     amount_requested = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     amount_granted = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     rationale = models.TextField(blank=True)
#     status_id = models.IntegerField()
#     class Meta:
#         db_table = u'civicrm_grant'

# class CivicrmGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, unique=True, blank=True)
#     title = models.CharField(max_length=192, unique=True, blank=True)
#     description = models.TextField(blank=True)
#     source = models.CharField(max_length=192, blank=True)
#     saved_search = models.ForeignKey(CivicrmSavedSearch, null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     visibility = models.CharField(max_length=72, blank=True)
#     where_clause = models.TextField(blank=True)
#     select_tables = models.TextField(blank=True)
#     where_tables = models.TextField(blank=True)
#     group_type = models.CharField(max_length=384, blank=True)
#     cache_date = models.DateTimeField(null=True, blank=True)
#     parents = models.TextField(blank=True)
#     children = models.TextField(blank=True)
#     is_hidden = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_group'

# class CivicrmGroupContact(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(CivicrmGroup)
#     contact = models.ForeignKey(CivicrmContact, unique=True)
#     status = models.CharField(max_length=21, blank=True)
#     email = models.ForeignKey(CivicrmEmail, null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_group_contact'

# class CivicrmGroupContactCache(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(CivicrmGroup)
#     contact = models.ForeignKey(CivicrmContact, unique=True)
#     class Meta:
#         db_table = u'civicrm_group_contact_cache'

# class CivicrmGroupNesting(models.Model):
#     id = models.IntegerField(primary_key=True)
#     child_group = models.ForeignKey(CivicrmGroup)
#     parent_group = models.ForeignKey(CivicrmGroup)
#     class Meta:
#         db_table = u'civicrm_group_nesting'

# class CivicrmGroupOrganization(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(CivicrmGroup)
#     organization = models.ForeignKey(CivicrmContact)
#     class Meta:
#         db_table = u'civicrm_group_organization'

# class CivicrmIm(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     location_type_id = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=192, blank=True)
#     provider_id = models.IntegerField(null=True, blank=True)
#     is_primary = models.IntegerField(null=True, blank=True)
#     is_billing = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_im'

# class CivicrmLineItem(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     price_field = models.ForeignKey(CivicrmPriceField)
#     option_group_id = models.IntegerField()
#     label = models.CharField(max_length=765)
#     qty = models.IntegerField()
#     unit_price = models.DecimalField(max_digits=22, decimal_places=2)
#     line_total = models.DecimalField(max_digits=22, decimal_places=2)
#     class Meta:
#         db_table = u'civicrm_line_item'

# class CivicrmLocBlock(models.Model):
#     id = models.IntegerField(primary_key=True)
#     address = models.ForeignKey(CivicrmAddress, null=True, blank=True)
#     email = models.ForeignKey(CivicrmEmail, null=True, blank=True)
#     phone = models.ForeignKey(CivicrmPhone, null=True, blank=True)
#     im = models.ForeignKey(CivicrmIm, null=True, blank=True)
#     address_2 = models.ForeignKey(CivicrmAddress, null=True, blank=True)
#     email_2 = models.ForeignKey(CivicrmEmail, null=True, blank=True)
#     phone_2 = models.ForeignKey(CivicrmPhone, null=True, blank=True)
#     im_2 = models.ForeignKey(CivicrmIm, null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_loc_block'

# class CivicrmLocationType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, unique=True, blank=True)
#     vcard_name = models.CharField(max_length=192, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     is_reserved = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_location_type'

# class CivicrmLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     data = models.TextField(blank=True)
#     modified = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     modified_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_log'

# class CivicrmMailSettings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain_id = models.IntegerField()
#     name = models.CharField(max_length=765, blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     domain = models.CharField(max_length=765, blank=True)
#     localpart = models.CharField(max_length=765, blank=True)
#     return_path = models.CharField(max_length=765, blank=True)
#     protocol = models.CharField(max_length=765, blank=True)
#     server = models.CharField(max_length=765, blank=True)
#     port = models.IntegerField(null=True, blank=True)
#     username = models.CharField(max_length=765, blank=True)
#     password = models.CharField(max_length=765, blank=True)
#     is_ssl = models.IntegerField(null=True, blank=True)
#     source = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_mail_settings'

# class CivicrmMailing(models.Model):
#     id = models.IntegerField(primary_key=True)
#     header = models.ForeignKey(CivicrmMailingComponent, null=True, blank=True)
#     footer = models.ForeignKey(CivicrmMailingComponent, null=True, blank=True)
#     reply = models.ForeignKey(CivicrmMailingComponent, null=True, blank=True)
#     unsubscribe = models.ForeignKey(CivicrmMailingComponent, null=True, blank=True)
#     resubscribe_id = models.IntegerField(null=True, blank=True)
#     optout = models.ForeignKey(CivicrmMailingComponent, null=True, blank=True)
#     name = models.CharField(max_length=384, blank=True)
#     from_name = models.CharField(max_length=384, blank=True)
#     from_email = models.CharField(max_length=384, blank=True)
#     replyto_email = models.CharField(max_length=384, blank=True)
#     subject = models.CharField(max_length=384, blank=True)
#     body_text = models.TextField(blank=True)
#     body_html = models.TextField(blank=True)
#     url_tracking = models.IntegerField(null=True, blank=True)
#     forward_replies = models.IntegerField(null=True, blank=True)
#     auto_responder = models.IntegerField(null=True, blank=True)
#     open_tracking = models.IntegerField(null=True, blank=True)
#     is_completed = models.IntegerField(null=True, blank=True)
#     msg_template = models.ForeignKey(CivicrmMsgTemplate, null=True, blank=True)
#     override_verp = models.IntegerField(null=True, blank=True)
#     created = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     scheduled = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     is_archived = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_mailing'

# class CivicrmMailingBouncePattern(models.Model):
#     id = models.IntegerField(primary_key=True)
#     bounce_type = models.ForeignKey(CivicrmMailingBounceType)
#     pattern = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_mailing_bounce_pattern'

# class CivicrmMailingBounceType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=24)
#     description = models.CharField(max_length=765, blank=True)
#     hold_threshold = models.IntegerField()
#     class Meta:
#         db_table = u'civicrm_mailing_bounce_type'

# class CivicrmMailingComponent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, blank=True)
#     component_type = models.CharField(max_length=33, blank=True)
#     subject = models.CharField(max_length=765, blank=True)
#     body_html = models.TextField(blank=True)
#     body_text = models.TextField(blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_mailing_component'

# class CivicrmMailingEventBounce(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     bounce_type_id = models.IntegerField(null=True, blank=True)
#     bounce_reason = models.CharField(max_length=765, blank=True)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_bounce'

# class CivicrmMailingEventConfirm(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_subscribe = models.ForeignKey(CivicrmMailingEventSubscribe)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_confirm'

# class CivicrmMailingEventDelivered(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_delivered'

# class CivicrmMailingEventForward(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     dest_queue = models.ForeignKey(CivicrmMailingEventQueue, null=True, blank=True)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_forward'

# class CivicrmMailingEventOpened(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_opened'

# class CivicrmMailingEventQueue(models.Model):
#     id = models.IntegerField(primary_key=True)
#     job = models.ForeignKey(CivicrmMailingJob)
#     email = models.ForeignKey(CivicrmEmail)
#     contact = models.ForeignKey(CivicrmContact)
#     hash = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'civicrm_mailing_event_queue'

# class CivicrmMailingEventReply(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_reply'

# class CivicrmMailingEventSubscribe(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(CivicrmGroup)
#     contact = models.ForeignKey(CivicrmContact)
#     hash = models.CharField(max_length=765)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_subscribe'

# class CivicrmMailingEventTrackableUrlOpen(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     trackable_url = models.ForeignKey(CivicrmMailingTrackableUrl)
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_trackable_url_open'

# class CivicrmMailingEventUnsubscribe(models.Model):
#     id = models.IntegerField(primary_key=True)
#     event_queue = models.ForeignKey(CivicrmMailingEventQueue)
#     org_unsubscribe = models.IntegerField()
#     time_stamp = models.DateTimeField()
#     class Meta:
#         db_table = u'civicrm_mailing_event_unsubscribe'

# class CivicrmMailingGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     mailing = models.ForeignKey(CivicrmMailing)
#     group_type = models.CharField(max_length=21, blank=True)
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     search_id = models.IntegerField(null=True, blank=True)
#     search_args = models.TextField(blank=True)
#     class Meta:
#         db_table = u'civicrm_mailing_group'

# class CivicrmMailingJob(models.Model):
#     id = models.IntegerField(primary_key=True)
#     mailing = models.ForeignKey(CivicrmMailing)
#     scheduled_date = models.DateTimeField(null=True, blank=True)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     status = models.CharField(max_length=27, blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_mailing_job'

# class CivicrmMailingSpool(models.Model):
#     id = models.IntegerField(primary_key=True)
#     job = models.ForeignKey(CivicrmMailingJob)
#     recipient_email = models.TextField(blank=True)
#     headers = models.TextField(blank=True)
#     body = models.TextField(blank=True)
#     added_at = models.DateTimeField(null=True, blank=True)
#     removed_at = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_mailing_spool'

# class CivicrmMailingTrackableUrl(models.Model):
#     id = models.IntegerField(primary_key=True)
#     url = models.CharField(max_length=765)
#     mailing = models.ForeignKey(CivicrmMailing)
#     class Meta:
#         db_table = u'civicrm_mailing_trackable_url'

# class CivicrmMapping(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     mapping_type_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_mapping'

# class CivicrmMappingField(models.Model):
#     id = models.IntegerField(primary_key=True)
#     mapping = models.ForeignKey(CivicrmMapping)
#     name = models.CharField(max_length=192, blank=True)
#     contact_type = models.CharField(max_length=192, blank=True)
#     column_number = models.IntegerField()
#     location_type = models.ForeignKey(CivicrmLocationType, null=True, blank=True)
#     phone_type_id = models.IntegerField(null=True, blank=True)
#     im_provider_id = models.IntegerField(null=True, blank=True)
#     relationship_type = models.ForeignKey(CivicrmRelationshipType, null=True, blank=True)
#     relationship_direction = models.CharField(max_length=18, blank=True)
#     grouping = models.IntegerField(null=True, blank=True)
#     operator = models.CharField(max_length=24, blank=True)
#     value = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_mapping_field'

class CivicrmMembership(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(CivicrmContact)
    membership_type = models.ForeignKey('CivicrmMembershipType')
    join_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=384, blank=True)
    status = models.ForeignKey('CivicrmMembershipStatus')
    is_override = models.IntegerField(null=True, blank=True)
    reminder_date = models.DateField(null=True, blank=True)
    owner_membership = models.ForeignKey('self', null=True, blank=True)
    is_test = models.IntegerField(null=True, blank=True)
    is_pay_later = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_membership'

# class CivicrmMembershipBlock(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity = models.ForeignKey(CivicrmContributionPage)
#     membership_types = models.CharField(max_length=765, blank=True)
#     membership_type_default = models.ForeignKey(CivicrmMembershipType, null=True, db_column='membership_type_default', blank=True)
#     display_min_fee = models.IntegerField(null=True, blank=True)
#     is_separate_payment = models.IntegerField(null=True, blank=True)
#     new_title = models.CharField(max_length=765, blank=True)
#     new_text = models.TextField(blank=True)
#     renewal_title = models.CharField(max_length=765, blank=True)
#     renewal_text = models.TextField(blank=True)
#     is_required = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_membership_block'

# class CivicrmMembershipLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     membership = models.ForeignKey(CivicrmMembership)
#     status = models.ForeignKey(CivicrmMembershipStatus)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     modified = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     modified_date = models.DateField(null=True, blank=True)
#     renewal_reminder_date = models.DateField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_membership_log'

# class CivicrmMembershipPayment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     membership = models.ForeignKey(CivicrmMembership)
#     contribution = models.ForeignKey(CivicrmContribution, unique=True, null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_membership_payment'

class CivicrmMembershipStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=384, blank=True)
    start_event = models.CharField(max_length=30, blank=True)
    start_event_adjust_unit = models.CharField(max_length=15, blank=True)
    start_event_adjust_interval = models.IntegerField(null=True, blank=True)
    end_event = models.CharField(max_length=30, blank=True)
    end_event_adjust_unit = models.CharField(max_length=15, blank=True)
    end_event_adjust_interval = models.IntegerField(null=True, blank=True)
    is_current_member = models.IntegerField(null=True, blank=True)
    is_admin = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    is_default = models.IntegerField(null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    is_reserved = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_membership_status'

class CivicrmMembershipType(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.ForeignKey('CivicrmDomain')
    name = models.CharField(max_length=384, blank=True)
    description = models.CharField(max_length=765, blank=True)
    member_of_contact = models.ForeignKey(CivicrmContact)
    contribution_type = models.ForeignKey('CivicrmContributionType')
    minimum_fee = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
    duration_unit = models.CharField(max_length=24, blank=True)
    duration_interval = models.IntegerField(null=True, blank=True)
    period_type = models.CharField(max_length=21, blank=True)
    fixed_period_start_day = models.IntegerField(null=True, blank=True)
    fixed_period_rollover_day = models.IntegerField(null=True, blank=True)
    relationship_type = models.ForeignKey('CivicrmRelationshipType', null=True, blank=True)
    relationship_direction = models.CharField(max_length=18, blank=True)
    visibility = models.CharField(max_length=192, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    renewal_msg = models.ForeignKey('CivicrmMsgTemplate', null=True, blank=True)
    renewal_reminder_day = models.IntegerField(null=True, blank=True)
    receipt_text_signup = models.CharField(max_length=765, blank=True)
    receipt_text_renewal = models.CharField(max_length=765, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_membership_type'

# class CivicrmMenu(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain)
#     path = models.CharField(max_length=765, unique=True, blank=True)
#     path_arguments = models.TextField(blank=True)
#     title = models.CharField(max_length=765, blank=True)
#     access_callback = models.CharField(max_length=765, blank=True)
#     access_arguments = models.TextField(blank=True)
#     page_callback = models.CharField(max_length=765, blank=True)
#     page_arguments = models.TextField(blank=True)
#     breadcrumb = models.TextField(blank=True)
#     return_url = models.CharField(max_length=765, blank=True)
#     return_url_args = models.CharField(max_length=765, blank=True)
#     component = models.ForeignKey(CivicrmComponent, null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_public = models.IntegerField(null=True, blank=True)
#     is_exposed = models.IntegerField(null=True, blank=True)
#     is_ssl = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField()
#     type = models.IntegerField()
#     page_type = models.IntegerField()
#     skipbreadcrumb = models.IntegerField(null=True, db_column='skipBreadcrumb', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = u'civicrm_menu'

class CivicrmMsgTemplate(models.Model):
    id = models.IntegerField(primary_key=True)
    msg_title = models.CharField(max_length=765, blank=True)
    msg_subject = models.TextField(blank=True)
    msg_text = models.TextField(blank=True)
    msg_html = models.TextField(blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    workflow_id = models.IntegerField(null=True, blank=True)
    is_default = models.IntegerField(null=True, blank=True)
    is_reserved = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_msg_template'

# class CivicrmNavigation(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain)
#     label = models.CharField(max_length=765, blank=True)
#     name = models.CharField(max_length=765, blank=True)
#     url = models.CharField(max_length=765, blank=True)
#     permission = models.CharField(max_length=765, blank=True)
#     permission_operator = models.CharField(max_length=9, blank=True)
#     parent = models.ForeignKey('self', null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     has_separator = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_navigation'

# class CivicrmNote(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     note = models.TextField(blank=True)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     modified_date = models.DateField(null=True, blank=True)
#     subject = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_note'

# class CivicrmOpenid(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     location_type_id = models.IntegerField(null=True, blank=True)
#     openid = models.CharField(max_length=765, blank=True)
#     allowed_to_login = models.IntegerField()
#     is_primary = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_openid'

# class CivicrmOpenidAssociations(models.Model):
#     id = models.IntegerField(primary_key=True)
#     server_url = models.TextField(unique=True, blank=True)
#     handle = models.CharField(max_length=765, unique=True, blank=True)
#     secret = models.TextField(blank=True)
#     issued = models.IntegerField(null=True, blank=True)
#     lifetime = models.IntegerField(null=True, blank=True)
#     assoc_type = models.CharField(max_length=192, blank=True)
#     class Meta:
#         db_table = u'civicrm_openid_associations'

# class CivicrmOpenidNonces(models.Model):
#     id = models.IntegerField(primary_key=True)
#     server_url = models.TextField(unique=True, blank=True)
#     timestamp = models.IntegerField(unique=True, null=True, blank=True)
#     salt = models.CharField(max_length=120, unique=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_openid_nonces'

# class CivicrmOptionGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, unique=True)
#     label = models.CharField(max_length=765, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     is_reserved = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_option_group'

# class CivicrmOptionValue(models.Model):
#     id = models.IntegerField(primary_key=True)
#     option_group = models.ForeignKey(CivicrmOptionGroup)
#     label = models.CharField(max_length=765)
#     value = models.CharField(max_length=192)
#     name = models.CharField(max_length=765, blank=True)
#     grouping = models.CharField(max_length=192, blank=True)
#     filter = models.IntegerField(null=True, blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField()
#     description = models.CharField(max_length=765, blank=True)
#     is_optgroup = models.IntegerField(null=True, blank=True)
#     is_reserved = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     component = models.ForeignKey(CivicrmComponent, null=True, blank=True)
#     domain = models.ForeignKey(CivicrmDomain, null=True, blank=True)
#     visibility_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_option_value'

# class CivicrmParticipant(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     event = models.ForeignKey(CivicrmEvent, null=True, blank=True)
#     status = models.ForeignKey(CivicrmParticipantStatusType)
#     role_id = models.IntegerField(null=True, blank=True)
#     register_date = models.DateTimeField(null=True, blank=True)
#     source = models.CharField(max_length=384, blank=True)
#     fee_level = models.TextField(blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     is_pay_later = models.IntegerField(null=True, blank=True)
#     fee_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     registered_by = models.ForeignKey('self', null=True, blank=True)
#     discount = models.ForeignKey(CivicrmDiscount, null=True, blank=True)
#     fee_currency = models.CharField(max_length=192, blank=True)
#     class Meta:
#         db_table = u'civicrm_participant'

# class CivicrmParticipantPayment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     participant = models.ForeignKey(CivicrmParticipant)
#     contribution = models.ForeignKey(CivicrmContribution, unique=True, null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_participant_payment'

# class CivicrmParticipantStatusType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, blank=True)
#     label = models.CharField(max_length=765, blank=True)
#     class_field = models.CharField(max_length=24, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
#     is_reserved = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_counted = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField()
#     visibility_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_participant_status_type'

# class CivicrmPaymentProcessor(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain)
#     name = models.CharField(max_length=192, unique=True, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     payment_processor_type = models.CharField(max_length=765, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     is_test = models.IntegerField(unique=True, null=True, blank=True)
#     user_name = models.CharField(max_length=765, blank=True)
#     password = models.CharField(max_length=765, blank=True)
#     signature = models.CharField(max_length=765, blank=True)
#     url_site = models.CharField(max_length=765, blank=True)
#     url_api = models.CharField(max_length=765, blank=True)
#     url_recur = models.CharField(max_length=765, blank=True)
#     url_button = models.CharField(max_length=765, blank=True)
#     subject = models.CharField(max_length=765, blank=True)
#     class_name = models.CharField(max_length=765, blank=True)
#     billing_mode = models.IntegerField()
#     is_recur = models.IntegerField(null=True, blank=True)
#     payment_type = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_payment_processor'

# class CivicrmPaymentProcessorType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, unique=True, blank=True)
#     title = models.CharField(max_length=192, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_default = models.IntegerField(null=True, blank=True)
#     user_name_label = models.CharField(max_length=765, blank=True)
#     password_label = models.CharField(max_length=765, blank=True)
#     signature_label = models.CharField(max_length=765, blank=True)
#     subject_label = models.CharField(max_length=765, blank=True)
#     class_name = models.CharField(max_length=765, blank=True)
#     url_site_default = models.CharField(max_length=765, blank=True)
#     url_api_default = models.CharField(max_length=765, blank=True)
#     url_recur_default = models.CharField(max_length=765, blank=True)
#     url_button_default = models.CharField(max_length=765, blank=True)
#     url_site_test_default = models.CharField(max_length=765, blank=True)
#     url_api_test_default = models.CharField(max_length=765, blank=True)
#     url_recur_test_default = models.CharField(max_length=765, blank=True)
#     url_button_test_default = models.CharField(max_length=765, blank=True)
#     billing_mode = models.IntegerField()
#     is_recur = models.IntegerField(null=True, blank=True)
#     payment_type = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_payment_processor_type'

# class CivicrmPcp(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     status_id = models.IntegerField()
#     title = models.CharField(max_length=765, blank=True)
#     intro_text = models.TextField(blank=True)
#     page_text = models.TextField(blank=True)
#     donate_link_text = models.CharField(max_length=765, blank=True)
#     contribution_page = models.ForeignKey(CivicrmContributionPage)
#     is_thermometer = models.IntegerField(null=True, blank=True)
#     is_honor_roll = models.IntegerField(null=True, blank=True)
#     goal_amount = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     referer = models.CharField(max_length=765, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_pcp'

# class CivicrmPcpBlock(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity = models.ForeignKey(CivicrmContributionPage)
#     supporter_profile = models.ForeignKey(CivicrmUfGroup, null=True, blank=True)
#     is_approval_needed = models.IntegerField(null=True, blank=True)
#     is_tellfriend_enabled = models.IntegerField(null=True, blank=True)
#     tellfriend_limit = models.IntegerField(null=True, blank=True)
#     link_text = models.CharField(max_length=765, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     notify_email = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_pcp_block'

# class CivicrmPhone(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     location_type_id = models.IntegerField(null=True, blank=True)
#     is_primary = models.IntegerField(null=True, blank=True)
#     is_billing = models.IntegerField(null=True, blank=True)
#     mobile_provider_id = models.IntegerField(null=True, blank=True)
#     phone = models.CharField(max_length=96, blank=True)
#     phone_type_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_phone'

# class CivicrmPledge(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     contribution_type = models.ForeignKey(CivicrmContributionType, null=True, blank=True)
#     contribution_page = models.ForeignKey(CivicrmContributionPage, null=True, blank=True)
#     amount = models.DecimalField(max_digits=22, decimal_places=2)
#     frequency_unit = models.CharField(max_length=15, blank=True)
#     frequency_interval = models.IntegerField()
#     frequency_day = models.IntegerField()
#     installments = models.IntegerField(null=True, blank=True)
#     start_date = models.DateTimeField()
#     create_date = models.DateTimeField()
#     acknowledge_date = models.DateTimeField(null=True, blank=True)
#     modified_date = models.DateTimeField(null=True, blank=True)
#     cancel_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     honor_contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     honor_type_id = models.IntegerField(null=True, blank=True)
#     max_reminders = models.IntegerField(null=True, blank=True)
#     initial_reminder_day = models.IntegerField(null=True, blank=True)
#     additional_reminder_day = models.IntegerField(null=True, blank=True)
#     status_id = models.IntegerField(null=True, blank=True)
#     is_test = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_pledge'

# class CivicrmPledgeBlock(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity_id = models.IntegerField()
#     pledge_frequency_unit = models.CharField(max_length=384, blank=True)
#     is_pledge_interval = models.IntegerField(null=True, blank=True)
#     max_reminders = models.IntegerField(null=True, blank=True)
#     initial_reminder_day = models.IntegerField(null=True, blank=True)
#     additional_reminder_day = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_pledge_block'

# class CivicrmPledgePayment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     pledge = models.ForeignKey(CivicrmPledge)
#     contribution = models.ForeignKey(CivicrmContribution, unique=True, null=True, blank=True)
#     scheduled_amount = models.DecimalField(max_digits=22, decimal_places=2)
#     scheduled_date = models.DateTimeField()
#     reminder_date = models.DateTimeField(null=True, blank=True)
#     reminder_count = models.IntegerField(null=True, blank=True)
#     status_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_pledge_payment'

# class CivicrmPreferences(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain)
#     contact = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     is_domain = models.IntegerField(null=True, blank=True)
#     contact_view_options = models.CharField(max_length=384, blank=True)
#     contact_edit_options = models.CharField(max_length=384, blank=True)
#     advanced_search_options = models.CharField(max_length=384, blank=True)
#     user_dashboard_options = models.CharField(max_length=384, blank=True)
#     address_options = models.CharField(max_length=384, blank=True)
#     address_format = models.TextField(blank=True)
#     mailing_format = models.TextField(blank=True)
#     address_standardization_provider = models.CharField(max_length=192, blank=True)
#     address_standardization_userid = models.CharField(max_length=192, blank=True)
#     address_standardization_url = models.CharField(max_length=765, blank=True)
#     editor_id = models.IntegerField(null=True, blank=True)
#     mailing_backend = models.TextField(blank=True)
#     navigation = models.TextField(blank=True)
#     contact_autocomplete_options = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_preferences'

# class CivicrmPreferencesDate(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192)
#     description = models.CharField(max_length=765, blank=True)
#     start = models.IntegerField()
#     end = models.IntegerField()
#     date_format = models.CharField(max_length=192, blank=True)
#     time_format = models.CharField(max_length=192, blank=True)
#     class Meta:
#         db_table = u'civicrm_preferences_date'

# class CivicrmPremiums(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     premiums_active = models.IntegerField()
#     premiums_intro_title = models.CharField(max_length=765, blank=True)
#     premiums_intro_text = models.TextField(blank=True)
#     premiums_contact_email = models.CharField(max_length=300, blank=True)
#     premiums_contact_phone = models.CharField(max_length=150, blank=True)
#     premiums_display_min_contribution = models.IntegerField()
#     class Meta:
#         db_table = u'civicrm_premiums'

# class CivicrmPremiumsProduct(models.Model):
#     id = models.IntegerField(primary_key=True)
#     premiums = models.ForeignKey(CivicrmPremiums)
#     product = models.ForeignKey(CivicrmProduct)
#     weight = models.IntegerField()
#     class Meta:
#         db_table = u'civicrm_premiums_product'

# class CivicrmPriceField(models.Model):
#     id = models.IntegerField(primary_key=True)
#     price_set = models.ForeignKey(CivicrmPriceSet)
#     name = models.CharField(max_length=765)
#     label = models.CharField(max_length=765)
#     html_type = models.CharField(max_length=24)
#     is_enter_qty = models.IntegerField(null=True, blank=True)
#     help_pre = models.TextField(blank=True)
#     help_post = models.TextField(blank=True)
#     weight = models.IntegerField(null=True, blank=True)
#     is_display_amounts = models.IntegerField(null=True, blank=True)
#     options_per_line = models.IntegerField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_required = models.IntegerField(null=True, blank=True)
#     active_on = models.DateTimeField(null=True, blank=True)
#     expire_on = models.DateTimeField(null=True, blank=True)
#     javascript = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_price_field'

# class CivicrmPriceSet(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain, null=True, blank=True)
#     name = models.CharField(max_length=765, unique=True)
#     title = models.CharField(max_length=765, unique=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     help_pre = models.TextField(blank=True)
#     help_post = models.TextField(blank=True)
#     javascript = models.CharField(max_length=192, blank=True)
#     extends = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'civicrm_price_set'

# class CivicrmPriceSetEntity(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192, unique=True)
#     entity_id = models.IntegerField(unique=True)
#     price_set = models.ForeignKey(CivicrmPriceSet)
#     class Meta:
#         db_table = u'civicrm_price_set_entity'

# class CivicrmProduct(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765)
#     description = models.TextField(blank=True)
#     sku = models.CharField(max_length=150, blank=True)
#     options = models.TextField(blank=True)
#     image = models.CharField(max_length=765, blank=True)
#     thumbnail = models.CharField(max_length=765, blank=True)
#     price = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     min_contribution = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     cost = models.DecimalField(null=True, max_digits=22, decimal_places=2, blank=True)
#     is_active = models.IntegerField()
#     period_type = models.CharField(max_length=21, blank=True)
#     fixed_period_start_day = models.IntegerField(null=True, blank=True)
#     duration_unit = models.CharField(max_length=15, blank=True)
#     duration_interval = models.IntegerField(null=True, blank=True)
#     frequency_unit = models.CharField(max_length=15, blank=True)
#     frequency_interval = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_product'

# class CivicrmProject(models.Model):
#     id = models.IntegerField(unique=True)
#     title = models.CharField(max_length=192, blank=True)
#     description = models.TextField(blank=True)
#     logo = models.CharField(max_length=765, blank=True)
#     owner_entity_table = models.CharField(max_length=192, unique=True)
#     owner_entity_id = models.IntegerField(unique=True)
#     start_date = models.DateTimeField(null=True, blank=True)
#     end_date = models.DateTimeField(null=True, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     status_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_project'

class CivicrmRelationship(models.Model):
    id = models.IntegerField(primary_key=True)
    contact_id_a = models.ForeignKey(CivicrmContact, db_column='contact_id_a', related_name='contact_id_a_relationship')
    contact_id_b = models.ForeignKey(CivicrmContact, db_column='contact_id_b', related_name='contact_id_b_relationship')
    relationship_type = models.ForeignKey('CivicrmRelationshipType')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=765, blank=True)
    is_permission_a_b = models.IntegerField(null=True, blank=True)
    is_permission_b_a = models.IntegerField(null=True, blank=True)
    case = models.ForeignKey('CivicrmCase', null=True, blank=True)
    class Meta:
        db_table = u'civicrm_relationship'

class CivicrmRelationshipType(models.Model):
    id = models.IntegerField(primary_key=True)
    name_a_b = models.CharField(max_length=192, unique=True, blank=True)
    label_a_b = models.CharField(max_length=192, blank=True)
    name_b_a = models.CharField(max_length=192, unique=True, blank=True)
    label_b_a = models.CharField(max_length=192, blank=True)
    description = models.CharField(max_length=765, blank=True)
    contact_type_a = models.CharField(max_length=36, blank=True)
    contact_type_b = models.CharField(max_length=36, blank=True)
    contact_sub_type_a = models.CharField(max_length=192, blank=True)
    contact_sub_type_b = models.CharField(max_length=192, blank=True)
    is_reserved = models.IntegerField(null=True, blank=True)
    is_active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'civicrm_relationship_type'

# class CivicrmReportInstance(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain)
#     title = models.CharField(max_length=765, blank=True)
#     report_id = models.CharField(max_length=192)
#     description = models.CharField(max_length=765, blank=True)
#     permission = models.CharField(max_length=765, blank=True)
#     form_values = models.TextField(blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     email_subject = models.CharField(max_length=765, blank=True)
#     email_to = models.TextField(blank=True)
#     email_cc = models.TextField(blank=True)
#     header = models.TextField(blank=True)
#     footer = models.TextField(blank=True)
#     navigation = models.ForeignKey(CivicrmNavigation, null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_report_instance'

# class CivicrmSavedSearch(models.Model):
#     id = models.IntegerField(primary_key=True)
#     form_values = models.TextField(blank=True)
#     mapping = models.ForeignKey(CivicrmMapping, null=True, blank=True)
#     search_custom_id = models.IntegerField(null=True, blank=True)
#     where_clause = models.TextField(blank=True)
#     select_tables = models.TextField(blank=True)
#     where_tables = models.TextField(blank=True)
#     class Meta:
#         db_table = u'civicrm_saved_search'

class CivicrmStateProvince(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=192, unique=True, blank=True)
    abbreviation = models.CharField(max_length=12, blank=True)
    country = models.ForeignKey(CivicrmCountry)
    class Meta:
        db_table = u'civicrm_state_province'

# class CivicrmSubscriptionHistory(models.Model):
#     id = models.IntegerField(primary_key=True)
#     contact = models.ForeignKey(CivicrmContact)
#     group = models.ForeignKey(CivicrmGroup, null=True, blank=True)
#     date = models.DateTimeField()
#     method = models.CharField(max_length=15, blank=True)
#     status = models.CharField(max_length=21, blank=True)
#     tracking = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_subscription_history'

# class CivicrmTag(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, unique=True, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     parent = models.ForeignKey('self', null=True, blank=True)
#     is_selectable = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_tag'

# class CivicrmTask(models.Model):
#     id = models.IntegerField(unique=True)
#     title = models.CharField(max_length=192, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     task_type_id = models.IntegerField(null=True, blank=True)
#     owner_entity_table = models.CharField(max_length=192, unique=True)
#     owner_entity_id = models.IntegerField(unique=True)
#     parent_entity_table = models.CharField(max_length=192, unique=True, blank=True)
#     parent_entity_id = models.IntegerField(unique=True, null=True, blank=True)
#     due_date = models.DateTimeField(null=True, blank=True)
#     priority_id = models.IntegerField(null=True, blank=True)
#     task_class = models.CharField(max_length=765, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_task'

# class CivicrmTaskStatus(models.Model):
#     id = models.IntegerField(primary_key=True)
#     task = models.ForeignKey(CivicrmTask)
#     responsible_entity_table = models.CharField(max_length=192)
#     responsible_entity_id = models.IntegerField()
#     target_entity_table = models.CharField(max_length=192)
#     target_entity_id = models.IntegerField()
#     status_detail = models.TextField(blank=True)
#     status_id = models.IntegerField(null=True, blank=True)
#     create_date = models.DateTimeField(null=True, blank=True)
#     modified_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_task_status'

# class CivicrmTellFriend(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_table = models.CharField(max_length=192)
#     entity_id = models.IntegerField()
#     title = models.CharField(max_length=765, blank=True)
#     intro = models.TextField(blank=True)
#     suggested_message = models.TextField(blank=True)
#     general_link = models.CharField(max_length=765, blank=True)
#     thankyou_title = models.CharField(max_length=765, blank=True)
#     thankyou_text = models.TextField(blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_tell_friend'

# class CivicrmTimezone(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=192, blank=True)
#     abbreviation = models.CharField(max_length=9, blank=True)
#     gmt = models.CharField(max_length=192, blank=True)
#     offset = models.IntegerField(null=True, blank=True)
#     country = models.ForeignKey(CivicrmCountry)
#     class Meta:
#         db_table = u'civicrm_timezone'

# class CivicrmUfField(models.Model):
#     id = models.IntegerField(primary_key=True)
#     uf_group = models.ForeignKey(CivicrmUfGroup)
#     field_name = models.CharField(max_length=192, blank=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     is_view = models.IntegerField(null=True, blank=True)
#     is_required = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField()
#     help_post = models.TextField(blank=True)
#     visibility = models.CharField(max_length=75, blank=True)
#     in_selector = models.IntegerField(null=True, blank=True)
#     is_searchable = models.IntegerField(null=True, blank=True)
#     location_type = models.ForeignKey(CivicrmLocationType, null=True, blank=True)
#     phone_type_id = models.IntegerField(null=True, blank=True)
#     label = models.CharField(max_length=765, blank=True)
#     field_type = models.CharField(max_length=765, blank=True)
#     is_reserved = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_uf_field'

# class CivicrmUfGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     group_type = models.CharField(max_length=765, blank=True)
#     title = models.CharField(max_length=192, blank=True)
#     help_pre = models.TextField(blank=True)
#     help_post = models.TextField(blank=True)
#     limit_listings_group = models.ForeignKey(CivicrmGroup, null=True, blank=True)
#     post_url = models.CharField(max_length=765, db_column='post_URL', blank=True) # Field name made lowercase.
#     add_to_group = models.ForeignKey(CivicrmGroup, null=True, blank=True)
#     add_captcha = models.IntegerField(null=True, blank=True)
#     is_map = models.IntegerField(null=True, blank=True)
#     is_edit_link = models.IntegerField(null=True, blank=True)
#     is_uf_link = models.IntegerField(null=True, blank=True)
#     is_update_dupe = models.IntegerField(null=True, blank=True)
#     cancel_url = models.CharField(max_length=765, db_column='cancel_URL', blank=True) # Field name made lowercase.
#     is_cms_user = models.IntegerField(null=True, blank=True)
#     notify = models.CharField(max_length=765, blank=True)
#     is_reserved = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=192, blank=True)
#     created = models.ForeignKey(CivicrmContact, null=True, blank=True)
#     created_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_uf_group'

# class CivicrmUfJoin(models.Model):
#     id = models.IntegerField(primary_key=True)
#     is_active = models.IntegerField(null=True, blank=True)
#     module = models.CharField(max_length=192)
#     entity_table = models.CharField(max_length=192, blank=True)
#     entity_id = models.IntegerField(null=True, blank=True)
#     weight = models.IntegerField()
#     uf_group = models.ForeignKey(CivicrmUfGroup)
#     class Meta:
#         db_table = u'civicrm_uf_join'

# class CivicrmUfMatch(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.ForeignKey(CivicrmDomain)
#     uf_id = models.IntegerField()
#     uf_name = models.CharField(max_length=384, unique=True, blank=True)
#     contact = models.ForeignKey(CivicrmContact, unique=True, null=True, blank=True)
#     language = models.CharField(max_length=15, blank=True)
#     class Meta:
#         db_table = u'civicrm_uf_match'

# class CivicrmValue1AffiliateApplicationQuestions4(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_id = models.IntegerField()
#     legal_status = models.TextField(blank=True)
#     mission_and_goals = models.TextField(blank=True)
#     supporting_ocwc = models.TextField(blank=True)
#     target_audience = models.TextField(blank=True)
#     credentials = models.TextField(blank=True)
#     for_profit = models.IntegerField(null=True, blank=True)
#     revenue_source = models.TextField(blank=True)
#     sell_to_members = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_value_1_affiliate_application_questions_4'

class CivicrmValue1InstitutionInformation(models.Model):
    id = models.IntegerField(primary_key=True)
    entity_id = models.IntegerField()
    main_website = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    ocw_website = models.CharField(max_length=765, blank=True)
    seal_image__large = models.CharField(max_length=765, blank=True)
    seal_image__small = models.CharField(max_length=765, blank=True)
    institution_country = models.ForeignKey('CivicrmCountry', null=True, db_column='institution_country', blank=True)
    signed_by = models.CharField(max_length=765, blank=True)
    rss_course_feed = models.CharField(max_length=765, blank=True)
    agreed_to_terms = models.CharField(max_length=765, blank=True)
    agreed_criteria = models.CharField(max_length=765, blank=True)
    contract_version = models.CharField(max_length=765, blank=True)
    rss_referral_link = models.CharField(max_length=765, blank=True)
    rss_course_feed_language = models.CharField(max_length=765, blank=True)
    ocw_software_platform = models.CharField(max_length=765, blank=True)
    ocw_platform_details = models.TextField(blank=True)
    ocw_site_hosting = models.CharField(max_length=765, blank=True)
    ocw_site_approved = models.IntegerField(null=True, blank=True)
    ocw_published_languages = models.CharField(max_length=765, blank=True)
    ocw_license = models.CharField(max_length=765, blank=True)
    organization_type = models.CharField(max_length=765, blank=True)
    accreditation = models.IntegerField(null=True, blank=True)
    ocw_launch_date = models.DateTimeField(null=True, blank=True)
    featured_member_description = models.TextField(blank=True)
    featured_course_title = models.CharField(max_length=765, blank=True)
    featured_course_link = models.CharField(max_length=765, blank=True)
    featured_course_description = models.TextField(blank=True)
    sponsor_logo = models.CharField(max_length=765, blank=True)
    accreditation_body_53 = models.CharField(max_length=765, blank=True)
    support_commitment_54 = models.TextField(blank=True)
    class Meta:
        db_table = u'civicrm_value_1_institution_information'

# class CivicrmValue1StaffData3(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_id = models.IntegerField()
#     computer_description = models.CharField(max_length=765, blank=True)
#     computer_serial_number = models.CharField(max_length=765, blank=True)
#     computer_purchase_date = models.DateTimeField(null=True, blank=True)
#     computer_warranty_expiration = models.DateTimeField(null=True, blank=True)
#     monitor_description = models.CharField(max_length=765, blank=True)
#     monitor_serial_number = models.CharField(max_length=765, blank=True)
#     monitor_purchase_date = models.DateTimeField(null=True, blank=True)
#     monitor_warranty_expiration = models.DateTimeField(null=True, blank=True)
#     mobile_phone_description = models.CharField(max_length=765, blank=True)
#     mobile_phone_serial_number = models.CharField(max_length=765, blank=True)
#     mobile_phone_purchase_date = models.DateTimeField(null=True, blank=True)
#     mobile_phone_warranty_expiration = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_value_1_staff_data_3'

# class CivicrmValue1TermsAndConditions5(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_id = models.IntegerField()
#     accepted_site_terms = models.IntegerField(null=True, blank=True)
#     over_thirteen = models.IntegerField(null=True, blank=True)
#     language_preference = models.CharField(max_length=765, blank=True)
#     personal_bio_55 = models.TextField(blank=True)
#     personal_photo_56 = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'civicrm_value_1_terms_and_conditions_5'

# class CivicrmValue1VotingAndCertification(models.Model):
#     id = models.IntegerField(primary_key=True)
#     entity_id = models.IntegerField()
#     certification_date = models.DateTimeField(null=True, blank=True)
#     class Meta:
#         db_table = u'civicrm_value_1_voting_and_certification'

class CivicrmWorldregion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=384, blank=True)
    class Meta:
        db_table = u'civicrm_worldregion'

# class CmtyBbForums(models.Model):
#     forum_id = models.IntegerField(primary_key=True)
#     forum_name = models.CharField(max_length=450)
#     forum_slug = models.CharField(max_length=765)
#     forum_desc = models.TextField()
#     forum_parent = models.IntegerField()
#     forum_order = models.IntegerField()
#     topics = models.BigIntegerField()
#     posts = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bb_forums'

# class CmtyBbMeta(models.Model):
#     meta_id = models.BigIntegerField(primary_key=True)
#     object_type = models.CharField(max_length=48)
#     object_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_bb_meta'

# class CmtyBbPosts(models.Model):
#     post_id = models.BigIntegerField(primary_key=True)
#     forum_id = models.IntegerField()
#     topic_id = models.BigIntegerField()
#     poster_id = models.IntegerField()
#     post_text = models.TextField()
#     post_time = models.DateTimeField()
#     poster_ip = models.CharField(max_length=45)
#     post_status = models.IntegerField()
#     post_position = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bb_posts'

# class CmtyBbTermRelationships(models.Model):
#     object_id = models.BigIntegerField(primary_key=True)
#     term_taxonomy_id = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     term_order = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bb_term_relationships'

# class CmtyBbTermTaxonomy(models.Model):
#     term_taxonomy_id = models.BigIntegerField(primary_key=True)
#     term_id = models.BigIntegerField(unique=True)
#     taxonomy = models.CharField(max_length=96)
#     description = models.TextField()
#     parent = models.BigIntegerField()
#     count = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bb_term_taxonomy'

# class CmtyBbTerms(models.Model):
#     term_id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=165)
#     slug = models.CharField(max_length=600, unique=True)
#     term_group = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bb_terms'

# class CmtyBbTopics(models.Model):
#     topic_id = models.BigIntegerField(primary_key=True)
#     topic_title = models.CharField(max_length=300)
#     topic_slug = models.CharField(max_length=765)
#     topic_poster = models.BigIntegerField()
#     topic_poster_name = models.CharField(max_length=120)
#     topic_last_poster = models.BigIntegerField()
#     topic_last_poster_name = models.CharField(max_length=120)
#     topic_start_time = models.DateTimeField()
#     topic_time = models.DateTimeField()
#     forum_id = models.IntegerField()
#     topic_status = models.IntegerField()
#     topic_open = models.IntegerField()
#     topic_last_post_id = models.BigIntegerField()
#     topic_sticky = models.IntegerField()
#     topic_posts = models.BigIntegerField()
#     tag_count = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bb_topics'

# class CmtyBpActivity(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     component = models.CharField(max_length=225)
#     type = models.CharField(max_length=225)
#     action = models.TextField()
#     content = models.TextField()
#     primary_link = models.CharField(max_length=450)
#     item_id = models.CharField(max_length=225)
#     secondary_item_id = models.CharField(max_length=225, blank=True)
#     date_recorded = models.DateTimeField()
#     hide_sitewide = models.IntegerField(null=True, blank=True)
#     mptt_left = models.IntegerField()
#     mptt_right = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bp_activity'

# class CmtyBpActivityMeta(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     activity_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_bp_activity_meta'

# class CmtyBpFriends(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     initiator_user_id = models.BigIntegerField()
#     friend_user_id = models.BigIntegerField()
#     is_confirmed = models.IntegerField(null=True, blank=True)
#     is_limited = models.IntegerField(null=True, blank=True)
#     date_created = models.DateTimeField()
#     class Meta:
#         db_table = u'cmty_bp_friends'

# class CmtyBpGroups(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     creator_id = models.BigIntegerField()
#     name = models.CharField(max_length=300)
#     slug = models.CharField(max_length=600)
#     description = models.TextField()
#     status = models.CharField(max_length=30)
#     enable_forum = models.IntegerField()
#     date_created = models.DateTimeField()
#     class Meta:
#         db_table = u'cmty_bp_groups'

# class CmtyBpGroupsGroupmeta(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     group_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_bp_groups_groupmeta'

# class CmtyBpGroupsMembers(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     group_id = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     inviter_id = models.BigIntegerField()
#     is_admin = models.IntegerField()
#     is_mod = models.IntegerField()
#     user_title = models.CharField(max_length=300)
#     date_modified = models.DateTimeField()
#     comments = models.TextField()
#     is_confirmed = models.IntegerField()
#     is_banned = models.IntegerField()
#     invite_sent = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bp_groups_members'

# class CmtyBpMessagesMessages(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     thread_id = models.BigIntegerField()
#     sender_id = models.BigIntegerField()
#     subject = models.CharField(max_length=600)
#     message = models.TextField()
#     date_sent = models.DateTimeField()
#     class Meta:
#         db_table = u'cmty_bp_messages_messages'

# class CmtyBpMessagesNotices(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     subject = models.CharField(max_length=600)
#     message = models.TextField()
#     date_sent = models.DateTimeField()
#     is_active = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bp_messages_notices'

# class CmtyBpMessagesRecipients(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     thread_id = models.BigIntegerField()
#     unread_count = models.IntegerField()
#     sender_only = models.IntegerField()
#     is_deleted = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bp_messages_recipients'

# class CmtyBpNotifications(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     item_id = models.BigIntegerField()
#     secondary_item_id = models.BigIntegerField(null=True, blank=True)
#     component_name = models.CharField(max_length=225)
#     component_action = models.CharField(max_length=225)
#     date_notified = models.DateTimeField()
#     is_new = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bp_notifications'

# class CmtyBpUserBlogs(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     blog_id = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bp_user_blogs'

# class CmtyBpUserBlogsBlogmeta(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     blog_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_bp_user_blogs_blogmeta'

# class CmtyBpXprofileData(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     field_id = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     value = models.TextField()
#     last_updated = models.DateTimeField()
#     class Meta:
#         db_table = u'cmty_bp_xprofile_data'

# class CmtyBpXprofileFields(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     group_id = models.BigIntegerField()
#     parent_id = models.BigIntegerField()
#     type = models.CharField(max_length=450)
#     name = models.CharField(max_length=450)
#     description = models.TextField()
#     is_required = models.IntegerField()
#     is_default_option = models.IntegerField()
#     field_order = models.BigIntegerField()
#     option_order = models.BigIntegerField()
#     order_by = models.CharField(max_length=45)
#     can_delete = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_bp_xprofile_fields'

# class CmtyBpXprofileGroups(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=450)
#     description = models.TextField()
#     can_delete = models.IntegerField()
#     group_order = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_bp_xprofile_groups'

# class CmtyBpXprofileMeta(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     object_id = models.BigIntegerField()
#     object_type = models.CharField(max_length=450)
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_bp_xprofile_meta'

# class CmtyCommentmeta(models.Model):
#     meta_id = models.BigIntegerField(primary_key=True)
#     comment_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_commentmeta'

# class CmtyComments(models.Model):
#     comment_id = models.BigIntegerField(primary_key=True, db_column='comment_ID') # Field name made lowercase.
#     comment_post_id = models.BigIntegerField(db_column='comment_post_ID') # Field name made lowercase.
#     comment_author = models.TextField()
#     comment_author_email = models.CharField(max_length=300)
#     comment_author_url = models.CharField(max_length=600)
#     comment_author_ip = models.CharField(max_length=300, db_column='comment_author_IP') # Field name made lowercase.
#     comment_date = models.DateTimeField()
#     comment_date_gmt = models.DateTimeField()
#     comment_content = models.TextField()
#     comment_karma = models.IntegerField()
#     comment_approved = models.CharField(max_length=60)
#     comment_agent = models.CharField(max_length=765)
#     comment_type = models.CharField(max_length=60)
#     comment_parent = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_comments'

# class CmtyLinks(models.Model):
#     link_id = models.BigIntegerField(primary_key=True)
#     link_url = models.CharField(max_length=765)
#     link_name = models.CharField(max_length=765)
#     link_image = models.CharField(max_length=765)
#     link_target = models.CharField(max_length=75)
#     link_description = models.CharField(max_length=765)
#     link_visible = models.CharField(max_length=60)
#     link_owner = models.BigIntegerField()
#     link_rating = models.IntegerField()
#     link_updated = models.DateTimeField()
#     link_rel = models.CharField(max_length=765)
#     link_notes = models.TextField()
#     link_rss = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'cmty_links'

# class CmtyOptions(models.Model):
#     option_id = models.BigIntegerField(primary_key=True)
#     blog_id = models.IntegerField()
#     option_name = models.CharField(max_length=192, unique=True)
#     option_value = models.TextField()
#     autoload = models.CharField(max_length=60)
#     class Meta:
#         db_table = u'cmty_options'

# class CmtyPostmeta(models.Model):
#     meta_id = models.BigIntegerField(primary_key=True)
#     post_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_postmeta'

# class CmtyPosts(models.Model):
#     id = models.BigIntegerField(db_column='ID') # Field name made lowercase.
#     post_author = models.BigIntegerField()
#     post_date = models.DateTimeField()
#     post_date_gmt = models.DateTimeField()
#     post_content = models.TextField()
#     post_title = models.TextField()
#     post_excerpt = models.TextField()
#     post_status = models.CharField(max_length=60)
#     comment_status = models.CharField(max_length=60)
#     ping_status = models.CharField(max_length=60)
#     post_password = models.CharField(max_length=60)
#     post_name = models.CharField(max_length=600)
#     to_ping = models.TextField()
#     pinged = models.TextField()
#     post_modified = models.DateTimeField()
#     post_modified_gmt = models.DateTimeField()
#     post_content_filtered = models.TextField()
#     post_parent = models.BigIntegerField()
#     guid = models.CharField(max_length=765)
#     menu_order = models.IntegerField()
#     post_type = models.CharField(max_length=60)
#     post_mime_type = models.CharField(max_length=300)
#     comment_count = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_posts'

# class CmtyTermRelationships(models.Model):
#     object_id = models.BigIntegerField(primary_key=True)
#     term_taxonomy_id = models.BigIntegerField()
#     term_order = models.IntegerField()
#     class Meta:
#         db_table = u'cmty_term_relationships'

# class CmtyTermTaxonomy(models.Model):
#     term_taxonomy_id = models.BigIntegerField(primary_key=True)
#     term_id = models.BigIntegerField(unique=True)
#     taxonomy = models.CharField(max_length=96)
#     description = models.TextField()
#     parent = models.BigIntegerField()
#     count = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_term_taxonomy'

# class CmtyTerms(models.Model):
#     term_id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=600)
#     slug = models.CharField(max_length=600, unique=True)
#     term_group = models.BigIntegerField()
#     class Meta:
#         db_table = u'cmty_terms'

# class CmtyUsermeta(models.Model):
#     umeta_id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'cmty_usermeta'

# class CmtyUsers(models.Model):
#     id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
#     user_login = models.CharField(max_length=180)
#     user_pass = models.CharField(max_length=192)
#     user_nicename = models.CharField(max_length=150)
#     user_email = models.CharField(max_length=300)
#     user_url = models.CharField(max_length=300)
#     user_registered = models.DateTimeField()
#     user_activation_key = models.CharField(max_length=180)
#     user_status = models.IntegerField()
#     display_name = models.CharField(max_length=750)
#     class Meta:
#         db_table = u'cmty_users'

# class CountryCodes(models.Model):
#     iso_2 = models.CharField(max_length=6, blank=True)
#     iso_3 = models.CharField(max_length=9, blank=True)
#     iso_numeric = models.IntegerField(null=True, blank=True)
#     fips = models.CharField(max_length=6, blank=True)
#     country = models.CharField(max_length=765, blank=True)
#     currency = models.CharField(max_length=9, blank=True)
#     class Meta:
#         db_table = u'country_codes'

# class CrmRelationshipRequests(models.Model):
#     id = models.IntegerField(primary_key=True)
#     crm_contact_id_org = models.IntegerField()
#     crm_contact_id_ind = models.IntegerField()
#     cdate = models.DateTimeField()
#     mdate = models.DateTimeField()
#     status = models.CharField(max_length=750)
#     class Meta:
#         db_table = u'crm_relationship_requests'

# class JosBanner(models.Model):
#     bid = models.IntegerField(primary_key=True)
#     cid = models.IntegerField()
#     type = models.CharField(max_length=90)
#     name = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     imptotal = models.IntegerField()
#     impmade = models.IntegerField()
#     clicks = models.IntegerField()
#     imageurl = models.CharField(max_length=300)
#     clickurl = models.CharField(max_length=600)
#     date = models.DateTimeField(null=True, blank=True)
#     showbanner = models.IntegerField(db_column='showBanner') # Field name made lowercase.
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     editor = models.CharField(max_length=150, blank=True)
#     custombannercode = models.TextField(blank=True)
#     catid = models.IntegerField()
#     description = models.TextField()
#     sticky = models.IntegerField()
#     ordering = models.IntegerField()
#     publish_up = models.DateTimeField()
#     publish_down = models.DateTimeField()
#     tags = models.TextField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_banner'

# class JosBannerclient(models.Model):
#     cid = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765)
#     contact = models.CharField(max_length=765)
#     email = models.CharField(max_length=765)
#     extrainfo = models.TextField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.TextField(blank=True) # This field type is a guess.
#     editor = models.CharField(max_length=150, blank=True)
#     class Meta:
#         db_table = u'jos_bannerclient'

# class JosBannertrack(models.Model):
#     track_date = models.DateField()
#     track_type = models.IntegerField()
#     banner_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_bannertrack'

# class JosCategories(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parent_id = models.IntegerField()
#     title = models.CharField(max_length=765)
#     name = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     image = models.CharField(max_length=765)
#     section = models.CharField(max_length=150)
#     image_position = models.CharField(max_length=90)
#     description = models.TextField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     editor = models.CharField(max_length=150, blank=True)
#     ordering = models.IntegerField()
#     access = models.IntegerField()
#     count = models.IntegerField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_categories'

# class JosChronoContact(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField()
#     html = models.TextField()
#     scriptcode = models.TextField()
#     stylecode = models.TextField()
#     redirecturl = models.TextField()
#     emailresults = models.IntegerField()
#     fieldsnames = models.TextField()
#     fieldstypes = models.TextField()
#     onsubmitcode = models.TextField()
#     onsubmitcodeb4 = models.TextField()
#     server_validation = models.TextField()
#     attformtag = models.TextField()
#     submiturl = models.TextField()
#     emailtemplate = models.TextField()
#     useremailtemplate = models.TextField()
#     paramsall = models.TextField()
#     titlesall = models.TextField()
#     extravalrules = models.TextField()
#     dbclasses = models.TextField()
#     autogenerated = models.TextField()
#     chronocode = models.TextField()
#     theme = models.TextField()
#     published = models.IntegerField()
#     extra1 = models.TextField()
#     extra2 = models.TextField()
#     extra3 = models.TextField()
#     extra4 = models.TextField()
#     extra5 = models.TextField()
#     class Meta:
#         db_table = u'jos_chrono_contact'

# class JosChronoContactElements(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765)
#     placeholder = models.CharField(max_length=765)
#     desc = models.TextField()
#     code = models.TextField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_chrono_contact_elements'

# class JosChronoContactEmails(models.Model):
#     emailid = models.IntegerField(primary_key=True)
#     formid = models.IntegerField()
#     to = models.TextField()
#     dto = models.TextField()
#     subject = models.TextField()
#     dsubject = models.TextField()
#     cc = models.TextField()
#     dcc = models.TextField()
#     bcc = models.TextField()
#     dbcc = models.TextField()
#     fromname = models.TextField()
#     dfromname = models.TextField()
#     fromemail = models.TextField()
#     dfromemail = models.TextField()
#     replytoname = models.TextField()
#     dreplytoname = models.TextField()
#     replytoemail = models.TextField()
#     dreplytoemail = models.TextField()
#     enabled = models.IntegerField()
#     params = models.TextField()
#     template = models.TextField()
#     class Meta:
#         db_table = u'jos_chrono_contact_emails'

# class JosChronoContactPlugins(models.Model):
#     id = models.IntegerField(primary_key=True)
#     form_id = models.IntegerField()
#     name = models.CharField(max_length=765)
#     event = models.CharField(max_length=765)
#     params = models.TextField()
#     extra1 = models.TextField()
#     extra2 = models.TextField()
#     extra3 = models.TextField()
#     extra4 = models.TextField()
#     extra5 = models.TextField()
#     extra6 = models.TextField()
#     extra7 = models.TextField()
#     extra8 = models.TextField()
#     extra9 = models.TextField()
#     extra10 = models.TextField()
#     class Meta:
#         db_table = u'jos_chrono_contact_plugins'

# class JosChronoformsAceNomination(models.Model):
#     cf_id = models.IntegerField(primary_key=True)
#     uid = models.CharField(max_length=765)
#     recordtime = models.CharField(max_length=765)
#     ipaddress = models.CharField(max_length=765)
#     cf_user_id = models.CharField(max_length=765)
#     nominator_name = models.CharField(max_length=765)
#     nominator_email = models.CharField(max_length=765)
#     nominator_phone = models.CharField(max_length=765)
#     nominator_institution = models.CharField(max_length=765)
#     nominee_name = models.CharField(max_length=765)
#     nominee_email = models.CharField(max_length=765)
#     nominee_phone = models.CharField(max_length=765)
#     nominee_institution = models.CharField(max_length=765)
#     ocw_url = models.CharField(max_length=765)
#     course_url = models.CharField(max_length=765)
#     feature_tour = models.CharField(max_length=765)
#     award_category = models.CharField(max_length=765)
#     award_year = models.IntegerField()
#     proposed_citation = models.TextField()
#     background = models.TextField()
#     class Meta:
#         db_table = u'jos_chronoforms_ace_nomination'

# class JosComponents(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150)
#     link = models.CharField(max_length=765)
#     menuid = models.IntegerField()
#     parent = models.IntegerField()
#     admin_menu_link = models.CharField(max_length=765)
#     admin_menu_alt = models.CharField(max_length=765)
#     option = models.CharField(max_length=150)
#     ordering = models.IntegerField()
#     admin_menu_img = models.CharField(max_length=765)
#     iscore = models.IntegerField()
#     params = models.TextField()
#     enabled = models.IntegerField()
#     class Meta:
#         db_table = u'jos_components'

# class JosContactDetails(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     con_position = models.CharField(max_length=765, blank=True)
#     address = models.TextField(blank=True)
#     suburb = models.CharField(max_length=300, blank=True)
#     state = models.CharField(max_length=300, blank=True)
#     country = models.CharField(max_length=300, blank=True)
#     postcode = models.CharField(max_length=300, blank=True)
#     telephone = models.CharField(max_length=765, blank=True)
#     fax = models.CharField(max_length=765, blank=True)
#     misc = models.TextField(blank=True)
#     image = models.CharField(max_length=765, blank=True)
#     imagepos = models.CharField(max_length=60, blank=True)
#     email_to = models.CharField(max_length=765, blank=True)
#     default_con = models.IntegerField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     params = models.TextField()
#     user_id = models.IntegerField()
#     catid = models.IntegerField()
#     access = models.IntegerField()
#     mobile = models.CharField(max_length=765)
#     webpage = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'jos_contact_details'

# class JosContent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     title_alias = models.CharField(max_length=765)
#     introtext = models.TextField()
#     fulltext = models.TextField()
#     state = models.IntegerField()
#     sectionid = models.IntegerField()
#     mask = models.IntegerField()
#     catid = models.IntegerField()
#     created = models.DateTimeField()
#     created_by = models.IntegerField()
#     created_by_alias = models.CharField(max_length=765)
#     modified = models.DateTimeField()
#     modified_by = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     publish_up = models.DateTimeField()
#     publish_down = models.DateTimeField()
#     images = models.TextField()
#     urls = models.TextField()
#     attribs = models.TextField()
#     version = models.IntegerField()
#     parentid = models.IntegerField()
#     ordering = models.IntegerField()
#     metakey = models.TextField()
#     metadesc = models.TextField()
#     access = models.IntegerField()
#     hits = models.IntegerField()
#     metadata = models.TextField()
#     class Meta:
#         db_table = u'jos_content'

# class JosContentFrontpage(models.Model):
#     content_id = models.IntegerField(primary_key=True)
#     ordering = models.IntegerField()
#     class Meta:
#         db_table = u'jos_content_frontpage'

# class JosContentRating(models.Model):
#     content_id = models.IntegerField(primary_key=True)
#     rating_sum = models.IntegerField()
#     rating_count = models.IntegerField()
#     lastip = models.CharField(max_length=150)
#     class Meta:
#         db_table = u'jos_content_rating'

# class JosCoreAclAro(models.Model):
#     id = models.IntegerField(primary_key=True)
#     section_value = models.CharField(max_length=720, unique=True)
#     value = models.CharField(max_length=720, unique=True)
#     order_value = models.IntegerField()
#     name = models.CharField(max_length=765)
#     hidden = models.IntegerField()
#     class Meta:
#         db_table = u'jos_core_acl_aro'

# class JosCoreAclAroGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parent_id = models.IntegerField()
#     name = models.CharField(max_length=765)
#     lft = models.IntegerField()
#     rgt = models.IntegerField()
#     value = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'jos_core_acl_aro_groups'

# class JosCoreAclAroMap(models.Model):
#     acl_id = models.IntegerField(primary_key=True)
#     section_value = models.CharField(max_length=690, primary_key=True)
#     value = models.CharField(max_length=300, primary_key=True)
#     class Meta:
#         db_table = u'jos_core_acl_aro_map'

# class JosCoreAclAroSections(models.Model):
#     id = models.IntegerField(primary_key=True)
#     value = models.CharField(max_length=690, unique=True)
#     order_value = models.IntegerField()
#     name = models.CharField(max_length=690)
#     hidden = models.IntegerField()
#     class Meta:
#         db_table = u'jos_core_acl_aro_sections'

# class JosCoreAclGroupsAroMap(models.Model):
#     group_id = models.IntegerField(unique=True)
#     section_value = models.CharField(max_length=720, unique=True)
#     aro_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'jos_core_acl_groups_aro_map'

# class JosCoreLogItems(models.Model):
#     time_stamp = models.DateField()
#     item_table = models.CharField(max_length=150)
#     item_id = models.IntegerField()
#     hits = models.IntegerField()
#     class Meta:
#         db_table = u'jos_core_log_items'

# class JosCoreLogSearches(models.Model):
#     search_term = models.CharField(max_length=384)
#     hits = models.IntegerField()
#     class Meta:
#         db_table = u'jos_core_log_searches'

# class JosDbcache(models.Model):
#     id = models.CharField(max_length=96, primary_key=True)
#     groupname = models.CharField(max_length=96)
#     expire = models.DateTimeField()
#     value = models.TextField()
#     class Meta:
#         db_table = u'jos_dbcache'

# class JosDocman(models.Model):
#     id = models.IntegerField()
#     catid = models.IntegerField()
#     dmname = models.TextField()
#     dmdescription = models.TextField(blank=True)
#     dmdate_published = models.DateTimeField()
#     dmowner = models.IntegerField()
#     dmfilename = models.TextField()
#     published = models.IntegerField()
#     dmurl = models.TextField(blank=True)
#     dmcounter = models.IntegerField(null=True, blank=True)
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     approved = models.IntegerField()
#     dmthumbnail = models.TextField(blank=True)
#     dmlastupdateon = models.DateTimeField(null=True, blank=True)
#     dmlastupdateby = models.IntegerField()
#     dmsubmitedby = models.IntegerField()
#     dmmantainedby = models.IntegerField(null=True, blank=True)
#     dmlicense_id = models.IntegerField(null=True, blank=True)
#     dmlicense_display = models.IntegerField()
#     access = models.IntegerField()
#     attribs = models.TextField()
#     class Meta:
#         db_table = u'jos_docman'

# class JosDocmanGroups(models.Model):
#     groups_id = models.IntegerField(primary_key=True)
#     groups_name = models.TextField()
#     groups_description = models.TextField(blank=True)
#     groups_access = models.IntegerField()
#     groups_members = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_docman_groups'

# class JosDocmanHistory(models.Model):
#     id = models.IntegerField(primary_key=True)
#     doc_id = models.IntegerField()
#     revision = models.IntegerField()
#     his_date = models.DateTimeField()
#     his_who = models.IntegerField()
#     his_obs = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_docman_history'

# class JosDocmanLicenses(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField()
#     license = models.TextField()
#     class Meta:
#         db_table = u'jos_docman_licenses'

# class JosDocmanLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     log_docid = models.IntegerField()
#     log_ip = models.TextField()
#     log_datetime = models.DateTimeField()
#     log_user = models.IntegerField()
#     log_browser = models.TextField(blank=True)
#     log_os = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_docman_log'

# class JosElectionBallotoptions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     ballot_id = models.IntegerField()
#     item_id = models.IntegerField()
#     extra = models.CharField(max_length=765, blank=True)
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     class Meta:
#         db_table = u'jos_election_ballotoptions'

# class JosElectionBallots(models.Model):
#     id = models.IntegerField(primary_key=True)
#     catid = models.IntegerField()
#     type = models.CharField(max_length=765)
#     title = models.CharField(max_length=765)
#     intro = models.TextField()
#     description = models.TextField()
#     min_selections = models.IntegerField()
#     max_selections = models.IntegerField()
#     multiple = models.IntegerField()
#     required_relationships = models.CharField(max_length=765)
#     required_memberships = models.CharField(max_length=765)
#     required_status = models.CharField(max_length=765)
#     beginning = models.DateTimeField()
#     ending = models.DateTimeField()
#     date_added = models.DateTimeField()
#     date_modified = models.DateTimeField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     class Meta:
#         db_table = u'jos_election_ballots'

# class JosElectionCandidates(models.Model):
#     id = models.IntegerField(primary_key=True)
#     crmid_candidate = models.IntegerField()
#     crmid_institution = models.IntegerField()
#     crmid_sponsor = models.IntegerField()
#     bio = models.TextField(blank=True)
#     vision = models.TextField(blank=True)
#     link = models.CharField(max_length=765, blank=True)
#     sponsor_comment = models.TextField(blank=True)
#     alt_phone = models.CharField(max_length=45)
#     alt_email = models.CharField(max_length=765)
#     date_added = models.DateTimeField()
#     date_modified = models.DateTimeField()
#     election_year = models.IntegerField()
#     vetted = models.IntegerField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     archived = models.IntegerField()
#     accepted = models.IntegerField()
#     declined = models.IntegerField()
#     class Meta:
#         db_table = u'jos_election_candidates'

# class JosElectionMultipleVotes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     orgid = models.IntegerField()
#     orgname = models.CharField(max_length=765)
#     vid = models.IntegerField()
#     vname = models.CharField(max_length=765)
#     members = models.IntegerField()
#     votes = models.IntegerField()
#     class Meta:
#         db_table = u'jos_election_multiple_votes'

# class JosElectionPropositions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765)
#     details = models.TextField()
#     intro = models.TextField()
#     date_added = models.DateTimeField()
#     date_modified = models.DateTimeField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     class Meta:
#         db_table = u'jos_election_propositions'

# class JosElectionVotes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     ballotoption_id = models.IntegerField()
#     user_id = models.IntegerField()
#     crm_id = models.IntegerField()
#     org_id = models.IntegerField()
#     date_submitted = models.DateTimeField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     class Meta:
#         db_table = u'jos_election_votes'

# class JosExportCategories(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parent_id = models.IntegerField()
#     title = models.TextField()
#     name = models.TextField()
#     alias = models.CharField(max_length=765)
#     image = models.CharField(max_length=765)
#     section = models.CharField(max_length=450)
#     image_position = models.CharField(max_length=450)
#     description = models.TextField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     editor = models.CharField(max_length=450, blank=True)
#     ordering = models.IntegerField()
#     access = models.IntegerField()
#     count = models.IntegerField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_export_categories'

# class JosExportContent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.TextField()
#     alias = models.CharField(max_length=765)
#     title_alias = models.TextField()
#     introtext = models.TextField()
#     fulltext = models.TextField()
#     state = models.IntegerField()
#     sectionid = models.IntegerField()
#     mask = models.IntegerField()
#     catid = models.IntegerField()
#     created = models.DateTimeField()
#     created_by = models.IntegerField()
#     created_by_alias = models.TextField()
#     modified = models.DateTimeField()
#     modified_by = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     publish_up = models.DateTimeField()
#     publish_down = models.DateTimeField()
#     images = models.TextField()
#     urls = models.TextField()
#     attribs = models.TextField()
#     version = models.IntegerField()
#     parentid = models.IntegerField()
#     ordering = models.IntegerField()
#     metakey = models.TextField()
#     metadesc = models.TextField()
#     access = models.IntegerField()
#     hits = models.IntegerField()
#     metadata = models.TextField()
#     class Meta:
#         db_table = u'jos_export_content'

# class JosExportSections(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.TextField()
#     name = models.TextField()
#     alias = models.CharField(max_length=765)
#     image = models.TextField()
#     scope = models.CharField(max_length=300)
#     image_position = models.CharField(max_length=300)
#     description = models.TextField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     access = models.IntegerField()
#     count = models.IntegerField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_export_sections'

# class JosGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150)
#     class Meta:
#         db_table = u'jos_groups'

# class JosJevUsers(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     published = models.IntegerField()
#     canuploadimages = models.IntegerField()
#     canuploadmovies = models.IntegerField()
#     cancreate = models.IntegerField()
#     canedit = models.IntegerField()
#     canpublishown = models.IntegerField()
#     candeleteown = models.IntegerField()
#     canpublishall = models.IntegerField()
#     candeleteall = models.IntegerField()
#     cancreateown = models.IntegerField()
#     cancreateglobal = models.IntegerField()
#     eventslimit = models.IntegerField()
#     extraslimit = models.IntegerField()
#     created = models.DateTimeField()
#     class Meta:
#         db_table = u'jos_jev_users'

# class JosJeventsCategories(models.Model):
#     id = models.IntegerField(primary_key=True)
#     color = models.CharField(max_length=24)
#     admin = models.IntegerField()
#     class Meta:
#         db_table = u'jos_jevents_categories'

# class JosJeventsException(models.Model):
#     ex_id = models.IntegerField(primary_key=True)
#     rp_id = models.IntegerField()
#     eventid = models.IntegerField()
#     eventdetail_id = models.IntegerField()
#     exception_type = models.IntegerField()
#     startrepeat = models.DateTimeField()
#     class Meta:
#         db_table = u'jos_jevents_exception'

# class JosJeventsIcsfile(models.Model):
#     ics_id = models.IntegerField(primary_key=True)
#     srcurl = models.CharField(max_length=765, db_column='srcURL') # Field name made lowercase.
#     label = models.CharField(max_length=90, unique=True)
#     filename = models.CharField(max_length=360)
#     icaltype = models.IntegerField()
#     isdefault = models.IntegerField()
#     ignoreembedcat = models.IntegerField()
#     state = models.IntegerField()
#     access = models.IntegerField()
#     catid = models.IntegerField()
#     created = models.DateTimeField()
#     created_by = models.IntegerField()
#     created_by_alias = models.CharField(max_length=300)
#     modified_by = models.IntegerField()
#     refreshed = models.DateTimeField()
#     autorefresh = models.IntegerField()
#     class Meta:
#         db_table = u'jos_jevents_icsfile'

# class JosJeventsRepbyday(models.Model):
#     rptday = models.DateField()
#     rp_id = models.IntegerField()
#     catid = models.IntegerField()
#     class Meta:
#         db_table = u'jos_jevents_repbyday'

# class JosJeventsRepetition(models.Model):
#     rp_id = models.IntegerField(primary_key=True)
#     eventid = models.IntegerField()
#     eventdetail_id = models.IntegerField()
#     duplicatecheck = models.CharField(max_length=96, unique=True)
#     startrepeat = models.DateTimeField()
#     endrepeat = models.DateTimeField()
#     class Meta:
#         db_table = u'jos_jevents_repetition'

# class JosJeventsRrule(models.Model):
#     rr_id = models.IntegerField(primary_key=True)
#     eventid = models.IntegerField()
#     freq = models.CharField(max_length=90)
#     until = models.IntegerField()
#     untilraw = models.CharField(max_length=90)
#     count = models.IntegerField()
#     rinterval = models.IntegerField()
#     bysecond = models.CharField(max_length=150)
#     byminute = models.CharField(max_length=150)
#     byhour = models.CharField(max_length=150)
#     byday = models.CharField(max_length=150)
#     bymonthday = models.CharField(max_length=150)
#     byyearday = models.CharField(max_length=150)
#     byweekno = models.CharField(max_length=150)
#     bymonth = models.CharField(max_length=150)
#     bysetpos = models.CharField(max_length=150)
#     wkst = models.CharField(max_length=150)
#     class Meta:
#         db_table = u'jos_jevents_rrule'

# class JosJeventsVevdetail(models.Model):
#     evdet_id = models.IntegerField(primary_key=True)
#     rawdata = models.TextField()
#     dtstart = models.IntegerField()
#     dtstartraw = models.CharField(max_length=90)
#     duration = models.IntegerField()
#     durationraw = models.CharField(max_length=90)
#     dtend = models.IntegerField()
#     dtendraw = models.CharField(max_length=90)
#     dtstamp = models.CharField(max_length=90)
#     class_field = models.CharField(max_length=30, db_column='class') # Field renamed because it was a Python reserved word.
#     categories = models.CharField(max_length=360)
#     color = models.CharField(max_length=60)
#     description = models.TextField()
#     geolon = models.FloatField()
#     geolat = models.FloatField()
#     location = models.CharField(max_length=360)
#     priority = models.IntegerField()
#     status = models.CharField(max_length=60)
#     summary = models.TextField()
#     contact = models.CharField(max_length=360)
#     organizer = models.CharField(max_length=360)
#     url = models.CharField(max_length=360)
#     extra_info = models.CharField(max_length=720)
#     created = models.CharField(max_length=90)
#     sequence = models.IntegerField()
#     state = models.IntegerField()
#     multiday = models.IntegerField()
#     hits = models.IntegerField()
#     noendtime = models.IntegerField()
#     class Meta:
#         db_table = u'jos_jevents_vevdetail'

# class JosJeventsVevent(models.Model):
#     ev_id = models.IntegerField(primary_key=True)
#     icsid = models.IntegerField()
#     catid = models.IntegerField()
#     uid = models.CharField(max_length=765, unique=True)
#     refreshed = models.DateTimeField()
#     created = models.DateTimeField()
#     created_by = models.IntegerField()
#     created_by_alias = models.CharField(max_length=300)
#     modified_by = models.IntegerField()
#     rawdata = models.TextField()
#     recurrence_id = models.CharField(max_length=90)
#     detail_id = models.IntegerField()
#     state = models.IntegerField()
#     access = models.IntegerField()
#     class Meta:
#         db_table = u'jos_jevents_vevent'

# class JosJfContent(models.Model):
#     id = models.IntegerField(primary_key=True)
#     language_id = models.IntegerField()
#     reference_id = models.IntegerField()
#     reference_table = models.CharField(max_length=300)
#     reference_field = models.CharField(max_length=300)
#     value = models.TextField()
#     original_value = models.CharField(max_length=765, blank=True)
#     original_text = models.TextField()
#     modified = models.DateTimeField()
#     modified_by = models.IntegerField()
#     published = models.IntegerField()
#     class Meta:
#         db_table = u'jos_jf_content'

# class JosJfTableinfo(models.Model):
#     id = models.IntegerField(primary_key=True)
#     joomlatablename = models.CharField(max_length=300)
#     tablepkid = models.CharField(max_length=300, db_column='tablepkID') # Field name made lowercase.
#     class Meta:
#         db_table = u'jos_jf_tableinfo'

# class JosLanguages(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=300)
#     active = models.IntegerField()
#     iso = models.CharField(max_length=60, blank=True)
#     code = models.CharField(max_length=60)
#     shortcode = models.CharField(max_length=60, blank=True)
#     image = models.CharField(max_length=300, blank=True)
#     fallback_code = models.CharField(max_length=60)
#     params = models.TextField()
#     ordering = models.IntegerField()
#     class Meta:
#         db_table = u'jos_languages'

# class JosLknanswersAcl(models.Model):
#     cat_id = models.IntegerField()
#     group_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_acl'

# class JosLknanswersAclAttachments(models.Model):
#     cat_id = models.IntegerField()
#     group_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_acl_attachments'

# class JosLknanswersAdmin(models.Model):
#     sid = models.CharField(max_length=90, unique=True)
#     id = models.IntegerField()
#     table_name = models.CharField(max_length=384)
#     created = models.DateTimeField()
#     class Meta:
#         db_table = u'jos_lknanswers_admin'

# class JosLknanswersAttachments(models.Model):
#     id = models.IntegerField(primary_key=True)
#     answer_id = models.IntegerField()
#     question_id = models.IntegerField()
#     file_name = models.CharField(max_length=765)
#     date = models.DateTimeField()
#     class Meta:
#         db_table = u'jos_lknanswers_attachments'

# class JosLknanswersCategories(models.Model):
#     id = models.IntegerField(primary_key=True)
#     parent_id = models.IntegerField()
#     title = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     text = models.TextField()
#     moderator_id = models.CharField(max_length=300)
#     meta_keywords = models.TextField()
#     meta_description = models.TextField()
#     published = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_categories'

# class JosLknanswersPollOptions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     poll_id = models.IntegerField()
#     text = models.TextField()
#     hits = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_poll_options'

# class JosLknanswersPollVotes(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     date = models.DateTimeField()
#     vote_id = models.IntegerField()
#     poll_id = models.IntegerField()
#     user_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_poll_votes'

# class JosLknanswersPolls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     question_id = models.IntegerField(unique=True)
#     title = models.CharField(max_length=765)
#     voters = models.IntegerField()
#     type = models.IntegerField()
#     timefrom = models.DateTimeField()
#     timeto = models.DateTimeField()
#     published = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_polls'

# class JosLknanswersQuestionAnswers(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=150)
#     text = models.TextField()
#     memberid = models.IntegerField()
#     created = models.DateTimeField()
#     question_id = models.IntegerField()
#     published = models.CharField(max_length=3)
#     abuse = models.CharField(max_length=3)
#     ip = models.CharField(max_length=90)
#     best_answer = models.CharField(max_length=3)
#     class Meta:
#         db_table = u'jos_lknanswers_question_answers'

# class JosLknanswersQuestionTags(models.Model):
#     id = models.IntegerField(primary_key=True)
#     tag = models.CharField(max_length=75)
#     cid = models.IntegerField()
#     published = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_question_tags'

# class JosLknanswersQuestions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=300)
#     alias = models.CharField(max_length=300)
#     text = models.TextField()
#     memberid = models.IntegerField()
#     cat_id = models.IntegerField()
#     created = models.DateTimeField()
#     meta_keywords = models.CharField(max_length=450)
#     meta_description = models.CharField(max_length=450)
#     hits = models.IntegerField()
#     published = models.CharField(max_length=3)
#     abuse = models.CharField(max_length=3)
#     ip = models.CharField(max_length=90)
#     solved = models.CharField(max_length=3)
#     class Meta:
#         db_table = u'jos_lknanswers_questions'

# class JosLknanswersSubscriptions(models.Model):
#     question_id = models.IntegerField(unique=True)
#     memberid = models.IntegerField()
#     class Meta:
#         db_table = u'jos_lknanswers_subscriptions'

# class JosLknanswersUsers(models.Model):
#     memberid = models.IntegerField(primary_key=True)
#     image = models.CharField(max_length=150, blank=True)
#     user_points = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'jos_lknanswers_users'

# class JosMailman2(models.Model):
#     id = models.IntegerField(primary_key=True)
#     maildomain = models.CharField(max_length=150, blank=True)
#     domainname = models.CharField(max_length=150)
#     protocol = models.CharField(max_length=24)
#     appdomain = models.CharField(max_length=150)
#     admindir = models.CharField(max_length=150)
#     sitename = models.CharField(max_length=150, blank=True)
#     adminpw = models.CharField(max_length=150)
#     sender = models.CharField(max_length=150)
#     extlist = models.IntegerField()
#     debug = models.IntegerField()
#     communitybuilder = models.IntegerField()
#     communitybuilderstring = models.CharField(max_length=450, blank=True)
#     class Meta:
#         db_table = u'jos_mailman2'

# class JosMemberAppComments(models.Model):
#     comment_id = models.IntegerField(primary_key=True)
#     app_id = models.IntegerField()
#     comment_user_id = models.IntegerField()
#     comment = models.TextField()
#     cdate = models.DateTimeField()
#     sent_email = models.IntegerField()
#     app_status = models.CharField(max_length=750, blank=True)
#     class Meta:
#         db_table = u'jos_member_app_comments'

class JosMemberApplications(models.Model):
    app_id = models.IntegerField(primary_key=True)
    crm_contact_id_org = models.IntegerField()
    crm_contact_id_ind = models.IntegerField()
    joomla_user = models.ForeignKey('JosUsers', db_column='joomla_user_id')
    app_status = models.CharField(max_length=750)
    cdate = models.DateTimeField()
    mdate = models.DateTimeField()
    last_mod_user_id = models.IntegerField()
    class Meta:
        db_table = u'jos_member_applications'

# class JosMenu(models.Model):
#     id = models.IntegerField(primary_key=True)
#     menutype = models.CharField(max_length=225, blank=True)
#     name = models.CharField(max_length=765, blank=True)
#     alias = models.CharField(max_length=765)
#     link = models.TextField(blank=True)
#     type = models.CharField(max_length=150)
#     published = models.IntegerField()
#     parent = models.IntegerField()
#     componentid = models.IntegerField()
#     sublevel = models.IntegerField(null=True, blank=True)
#     ordering = models.IntegerField(null=True, blank=True)
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     pollid = models.IntegerField()
#     browsernav = models.IntegerField(null=True, db_column='browserNav', blank=True) # Field name made lowercase.
#     access = models.IntegerField()
#     utaccess = models.IntegerField()
#     params = models.TextField()
#     lft = models.IntegerField()
#     rgt = models.IntegerField()
#     home = models.IntegerField()
#     class Meta:
#         db_table = u'jos_menu'

# class JosMenuTypes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     menutype = models.CharField(max_length=225, unique=True)
#     title = models.CharField(max_length=765)
#     description = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'jos_menu_types'

# class JosMessages(models.Model):
#     message_id = models.IntegerField(primary_key=True)
#     user_id_from = models.IntegerField()
#     user_id_to = models.IntegerField()
#     folder_id = models.IntegerField()
#     date_time = models.DateTimeField()
#     state = models.IntegerField()
#     priority = models.IntegerField()
#     subject = models.TextField()
#     message = models.TextField()
#     class Meta:
#         db_table = u'jos_messages'

# class JosMessagesCfg(models.Model):
#     user_id = models.IntegerField(unique=True)
#     cfg_name = models.CharField(max_length=300, unique=True)
#     cfg_value = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'jos_messages_cfg'

# class JosMigrationBacklinks(models.Model):
#     itemid = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=300)
#     url = models.TextField()
#     sefurl = models.TextField()
#     newurl = models.TextField()
#     class Meta:
#         db_table = u'jos_migration_backlinks'

# class JosModules(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.TextField()
#     content = models.TextField()
#     ordering = models.IntegerField()
#     position = models.CharField(max_length=150, blank=True)
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     published = models.IntegerField()
#     module = models.CharField(max_length=150, blank=True)
#     numnews = models.IntegerField()
#     access = models.IntegerField()
#     showtitle = models.IntegerField()
#     params = models.TextField()
#     iscore = models.IntegerField()
#     client_id = models.IntegerField()
#     control = models.TextField()
#     class Meta:
#         db_table = u'jos_modules'

# class JosModulesMenu(models.Model):
#     moduleid = models.IntegerField(primary_key=True)
#     menuid = models.IntegerField(primary_key=True)
#     class Meta:
#         db_table = u'jos_modules_menu'

# class JosNewsfeeds(models.Model):
#     catid = models.IntegerField()
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField()
#     alias = models.CharField(max_length=765)
#     link = models.TextField()
#     filename = models.CharField(max_length=600, blank=True)
#     published = models.IntegerField()
#     numarticles = models.IntegerField()
#     cache_time = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     rtl = models.IntegerField()
#     class Meta:
#         db_table = u'jos_newsfeeds'

# class JosNewslinks(models.Model):
#     id = models.IntegerField(primary_key=True)
#     catid = models.IntegerField()
#     sid = models.IntegerField()
#     title = models.CharField(max_length=750)
#     url = models.CharField(max_length=750)
#     linkalias = models.CharField(max_length=750)
#     pubdate = models.DateTimeField()
#     date = models.DateTimeField()
#     hits = models.IntegerField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     archived = models.IntegerField()
#     approved = models.IntegerField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_newslinks'

# class JosOcwCatalogCourses(models.Model):
#     id = models.IntegerField(primary_key=True)
#     crmid = models.IntegerField()
#     linkhash = models.CharField(max_length=96, unique=True)
#     linkurl = models.TextField()
#     title = models.TextField()
#     description = models.TextField()
#     tags = models.TextField()
#     source = models.TextField()
#     language = models.CharField(max_length=300)
#     author = models.CharField(max_length=765)
#     rights = models.TextField()
#     contributors = models.CharField(max_length=765, blank=True)
#     license = models.TextField(blank=True)
#     type = models.CharField(max_length=765, blank=True)
#     format = models.CharField(max_length=765, blank=True)
#     level = models.CharField(max_length=765, blank=True)
#     date_published = models.DateTimeField()
#     date_indexed = models.DateTimeField()
#     date_modified = models.DateTimeField()
#     locked = models.IntegerField()
#     class Meta:
#         db_table = u'jos_ocw_catalog_courses'

# class JosOcwCategories(models.Model):
#     id = models.IntegerField(primary_key=True)
#     category = models.CharField(max_length=765)
#     descriptors = models.TextField(blank=True)
#     parent_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_ocw_categories'

# class JosOcwCourseCategory(models.Model):
#     course_id = models.IntegerField()
#     category_id = models.IntegerField()
#     workerid = models.CharField(max_length=150)
#     assignmentid = models.CharField(max_length=150)
#     class Meta:
#         db_table = u'jos_ocw_course_category'

# class JosOcwCourseOntology(models.Model):
#     course_id = models.IntegerField()
#     category_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_ocw_course_ontology'

class JosOcwCourses(models.Model):
    id = models.IntegerField(primary_key=True)
    crmid = models.ForeignKey(CivicrmContact, db_column='crmid')
    # crmid = models.IntegerField()
    linkhash = models.CharField(max_length=96, unique=True)
    linkurl = models.TextField()
    title = models.TextField()
    description = models.TextField()
    tags = models.TextField()
    source = models.TextField()
    language = models.CharField(max_length=300)
    author = models.CharField(max_length=765, default='')
    rights = models.TextField(default='')
    contributors = models.CharField(max_length=765, blank=True, default='')
    license = models.TextField(blank=True, default='')
    type = models.CharField(max_length=765, blank=True)
    format = models.CharField(max_length=765, blank=True)
    level = models.CharField(max_length=765, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_indexed = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    locked = models.IntegerField(default=0)
    enabled = models.IntegerField()
    is_member = models.IntegerField(default=1)
    class Meta:
        db_table = u'jos_ocw_courses'

# class JosOcwOntology(models.Model):
#     id = models.IntegerField(primary_key=True)
#     category = models.CharField(max_length=765)
#     keywords = models.TextField(blank=True)
#     parent_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_ocw_ontology'

# class JosOcwcsiteterms(models.Model):
#     id = models.IntegerField(primary_key=True)
#     siteterms = models.TextField()
#     coppatext = models.TextField()
#     class Meta:
#         db_table = u'jos_ocwcsiteterms'

# class JosPlugins(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=300)
#     element = models.CharField(max_length=300)
#     folder = models.CharField(max_length=300)
#     access = models.IntegerField()
#     ordering = models.IntegerField()
#     published = models.IntegerField()
#     iscore = models.IntegerField()
#     client_id = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_plugins'

# class JosPollData(models.Model):
#     id = models.IntegerField(primary_key=True)
#     pollid = models.IntegerField()
#     text = models.TextField()
#     hits = models.IntegerField()
#     class Meta:
#         db_table = u'jos_poll_data'

# class JosPollDate(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     date = models.DateTimeField()
#     vote_id = models.IntegerField()
#     poll_id = models.IntegerField()
#     class Meta:
#         db_table = u'jos_poll_date'

# class JosPollMenu(models.Model):
#     pollid = models.IntegerField(primary_key=True)
#     menuid = models.IntegerField(primary_key=True)
#     class Meta:
#         db_table = u'jos_poll_menu'

# class JosPolls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     voters = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     published = models.IntegerField()
#     access = models.IntegerField()
#     lag = models.IntegerField()
#     class Meta:
#         db_table = u'jos_polls'

# class JosSections(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=765)
#     name = models.CharField(max_length=765)
#     alias = models.CharField(max_length=765)
#     image = models.TextField()
#     scope = models.CharField(max_length=150)
#     image_position = models.CharField(max_length=90)
#     description = models.TextField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     access = models.IntegerField()
#     count = models.IntegerField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_sections'

# class JosSession(models.Model):
#     username = models.CharField(max_length=450, blank=True)
#     time = models.CharField(max_length=42, blank=True)
#     session_id = models.CharField(max_length=600, primary_key=True)
#     guest = models.IntegerField(null=True, blank=True)
#     userid = models.IntegerField(null=True, blank=True)
#     usertype = models.CharField(max_length=150, blank=True)
#     gid = models.IntegerField()
#     client_id = models.IntegerField()
#     data = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_session'

# class JosStatsAgents(models.Model):
#     agent = models.CharField(max_length=765)
#     type = models.IntegerField()
#     hits = models.IntegerField()
#     class Meta:
#         db_table = u'jos_stats_agents'

# class JosTemplatesMenu(models.Model):
#     template = models.CharField(max_length=765, primary_key=True)
#     menuid = models.IntegerField(primary_key=True)
#     client_id = models.IntegerField(primary_key=True)
#     class Meta:
#         db_table = u'jos_templates_menu'

class JosUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    username = models.CharField(max_length=450)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    usertype = models.CharField(max_length=75)
    block = models.IntegerField()
    sendemail = models.IntegerField(null=True, db_column='sendEmail', blank=True) # Field name made lowercase.
    gid = models.IntegerField()
    registerdate = models.DateTimeField(db_column='registerDate') # Field name made lowercase.
    lastvisitdate = models.DateTimeField(db_column='lastvisitDate') # Field name made lowercase.
    activation = models.CharField(max_length=300)
    params = models.TextField()
    class Meta:
        db_table = u'jos_users'

# class JosWeblinks(models.Model):
#     id = models.IntegerField(primary_key=True)
#     catid = models.IntegerField()
#     sid = models.IntegerField()
#     title = models.CharField(max_length=750)
#     alias = models.CharField(max_length=765)
#     url = models.CharField(max_length=750)
#     description = models.TextField()
#     date = models.DateTimeField()
#     hits = models.IntegerField()
#     published = models.IntegerField()
#     checked_out = models.IntegerField()
#     checked_out_time = models.DateTimeField()
#     ordering = models.IntegerField()
#     archived = models.IntegerField()
#     approved = models.IntegerField()
#     params = models.TextField()
#     class Meta:
#         db_table = u'jos_weblinks'

# class JosWpCommentmeta(models.Model):
#     meta_id = models.BigIntegerField(primary_key=True)
#     comment_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_wp_commentmeta'

# class JosWpComments(models.Model):
#     comment_id = models.BigIntegerField(primary_key=True, db_column='comment_ID') # Field name made lowercase.
#     comment_post_id = models.BigIntegerField(db_column='comment_post_ID') # Field name made lowercase.
#     comment_author = models.TextField()
#     comment_author_email = models.CharField(max_length=300)
#     comment_author_url = models.CharField(max_length=600)
#     comment_author_ip = models.CharField(max_length=300, db_column='comment_author_IP') # Field name made lowercase.
#     comment_date = models.DateTimeField()
#     comment_date_gmt = models.DateTimeField()
#     comment_content = models.TextField()
#     comment_karma = models.IntegerField()
#     comment_approved = models.CharField(max_length=60)
#     comment_agent = models.CharField(max_length=765)
#     comment_type = models.CharField(max_length=60)
#     comment_parent = models.BigIntegerField()
#     user_id = models.BigIntegerField()
#     class Meta:
#         db_table = u'jos_wp_comments'

# class JosWpJauthenticate(models.Model):
#     user_id = models.IntegerField(primary_key=True)
#     hash = models.CharField(max_length=96)
#     timestamp = models.IntegerField()
#     class Meta:
#         db_table = u'jos_wp_jauthenticate'

# class JosWpLinks(models.Model):
#     link_id = models.BigIntegerField(primary_key=True)
#     link_url = models.CharField(max_length=765)
#     link_name = models.CharField(max_length=765)
#     link_image = models.CharField(max_length=765)
#     link_target = models.CharField(max_length=75)
#     link_category = models.BigIntegerField()
#     link_description = models.CharField(max_length=765)
#     link_visible = models.CharField(max_length=60)
#     link_owner = models.BigIntegerField()
#     link_rating = models.IntegerField()
#     link_updated = models.DateTimeField()
#     link_rel = models.CharField(max_length=765)
#     link_notes = models.TextField()
#     link_rss = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'jos_wp_links'

# class JosWpOptions(models.Model):
#     option_id = models.BigIntegerField(primary_key=True)
#     blog_id = models.IntegerField(primary_key=True)
#     option_name = models.CharField(max_length=192, unique=True)
#     option_value = models.TextField()
#     autoload = models.CharField(max_length=60)
#     class Meta:
#         db_table = u'jos_wp_options'

# class JosWpPostmeta(models.Model):
#     meta_id = models.BigIntegerField(primary_key=True)
#     post_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_wp_postmeta'

# class JosWpPosts(models.Model):
#     id = models.BigIntegerField(db_column='ID') # Field name made lowercase.
#     post_author = models.BigIntegerField()
#     post_date = models.DateTimeField()
#     post_date_gmt = models.DateTimeField()
#     post_content = models.TextField()
#     post_title = models.TextField()
#     post_category = models.IntegerField()
#     post_excerpt = models.TextField()
#     post_status = models.CharField(max_length=60)
#     comment_status = models.CharField(max_length=60)
#     ping_status = models.CharField(max_length=60)
#     post_password = models.CharField(max_length=60)
#     post_name = models.CharField(max_length=600)
#     to_ping = models.TextField()
#     pinged = models.TextField()
#     post_modified = models.DateTimeField()
#     post_modified_gmt = models.DateTimeField()
#     post_content_filtered = models.TextField()
#     post_parent = models.BigIntegerField()
#     guid = models.CharField(max_length=765)
#     menu_order = models.IntegerField()
#     post_type = models.CharField(max_length=60)
#     post_mime_type = models.CharField(max_length=300)
#     comment_count = models.BigIntegerField()
#     class Meta:
#         db_table = u'jos_wp_posts'

# class JosWpTermRelationships(models.Model):
#     object_id = models.BigIntegerField(primary_key=True)
#     term_taxonomy_id = models.BigIntegerField()
#     term_order = models.IntegerField()
#     class Meta:
#         db_table = u'jos_wp_term_relationships'

# class JosWpTermTaxonomy(models.Model):
#     term_taxonomy_id = models.BigIntegerField(primary_key=True)
#     term_id = models.BigIntegerField(unique=True)
#     taxonomy = models.CharField(max_length=96)
#     description = models.TextField()
#     parent = models.BigIntegerField()
#     count = models.BigIntegerField()
#     class Meta:
#         db_table = u'jos_wp_term_taxonomy'

# class JosWpTerms(models.Model):
#     term_id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=600)
#     slug = models.CharField(max_length=600, unique=True)
#     term_group = models.BigIntegerField()
#     class Meta:
#         db_table = u'jos_wp_terms'

# class JosWpUsermeta(models.Model):
#     umeta_id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     meta_key = models.CharField(max_length=765, blank=True)
#     meta_value = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_wp_usermeta'

# class JosWpUsers(models.Model):
#     id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
#     user_login = models.CharField(max_length=180)
#     user_pass = models.CharField(max_length=192)
#     user_nicename = models.CharField(max_length=150)
#     user_email = models.CharField(max_length=300)
#     user_url = models.CharField(max_length=300)
#     user_registered = models.DateTimeField()
#     user_activation_key = models.CharField(max_length=180)
#     user_status = models.IntegerField()
#     display_name = models.CharField(max_length=750)
#     class Meta:
#         db_table = u'jos_wp_users'

# class JosXmap(models.Model):
#     name = models.CharField(max_length=90, primary_key=True)
#     value = models.CharField(max_length=300, blank=True)
#     class Meta:
#         db_table = u'jos_xmap'

# class JosXmapExt(models.Model):
#     id = models.IntegerField(primary_key=True)
#     extension = models.CharField(max_length=300)
#     published = models.IntegerField(null=True, blank=True)
#     params = models.TextField(blank=True)
#     class Meta:
#         db_table = u'jos_xmap_ext'

# class JosXmapItems(models.Model):
#     uid = models.CharField(max_length=300)
#     itemid = models.IntegerField()
#     view = models.CharField(max_length=30)
#     sitemap_id = models.IntegerField(primary_key=True)
#     properties = models.CharField(max_length=900, blank=True)
#     class Meta:
#         db_table = u'jos_xmap_items'

# class JosXmapSitemap(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765, blank=True)
#     expand_category = models.IntegerField(null=True, blank=True)
#     expand_section = models.IntegerField(null=True, blank=True)
#     show_menutitle = models.IntegerField(null=True, blank=True)
#     columns = models.IntegerField(null=True, blank=True)
#     exlinks = models.IntegerField(null=True, blank=True)
#     ext_image = models.CharField(max_length=765, blank=True)
#     menus = models.TextField(blank=True)
#     exclmenus = models.CharField(max_length=765, blank=True)
#     includelink = models.IntegerField(null=True, blank=True)
#     usecache = models.IntegerField(null=True, blank=True)
#     cachelifetime = models.IntegerField(null=True, blank=True)
#     classname = models.CharField(max_length=765, blank=True)
#     count_xml = models.IntegerField(null=True, blank=True)
#     count_html = models.IntegerField(null=True, blank=True)
#     views_xml = models.IntegerField(null=True, blank=True)
#     views_html = models.IntegerField(null=True, blank=True)
#     lastvisit_xml = models.IntegerField(null=True, blank=True)
#     lastvisit_html = models.IntegerField(null=True, blank=True)
#     excluded_items = models.TextField(blank=True)
#     compress_xml = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'jos_xmap_sitemap'

class OcwcStatistics(models.Model):
    id = models.IntegerField(primary_key=True)
    # crm_org_id = models.IntegerField()
    # crm_org = models.ForeignKey(CivicrmMembership, db_column='crm_org_id')
    crm_org = models.ForeignKey(CivicrmContact, db_column='crm_org_id')
    report_month = models.CharField(max_length=6)
    report_year = models.CharField(max_length=12)
    site_visits = models.IntegerField()
    orig_courses = models.IntegerField()
    trans_courses = models.IntegerField()
    orig_course_lang = models.TextField(blank=True)
    trans_course_lang = models.TextField(blank=True)
    report_date = models.DateField()
    last_modified = models.DateTimeField()
    carry_forward = models.IntegerField()
    class Meta:
        db_table = u'ocwc_statistics'

# class WorldLanguages(models.Model):
#     english_name = models.CharField(max_length=765)
#     native_name = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'world_languages'

