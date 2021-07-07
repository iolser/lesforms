# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from resources.models import Generaluser, Administrator, Participant, Proponent


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class AuthtokenToken(models.Model):
#     key = models.CharField(primary_key=True, max_length=40)
#     created = models.DateTimeField()
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'authtoken_token'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Form(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     title = models.CharField(max_length=256)
#     form = models.JSONField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     creator = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='creator', blank=True, null=True)
#     type = models.ForeignKey('Formtype', models.DO_NOTHING, db_column='type', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'form'


# class Formanswer(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     content = models.JSONField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     answerer = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='answerer', blank=True, null=True)
#     form = models.ForeignKey(Form, models.DO_NOTHING, db_column='form')

#     class Meta:
#         managed = False
#         db_table = 'formAnswer'


# class Formtype(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     description = models.CharField(max_length=256, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'formType'


# class ResourcesAdministrator(models.Model):
#     generaluser_ptr = models.OneToOneField('ResourcesGeneraluser', models.DO_NOTHING, primary_key=True)
#     gabinete = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'resources_administrator'


# class ResourcesBuilding(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=128)
#     campus = models.ForeignKey('ResourcesCampus', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'resources_building'


# class ResourcesCampus(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=128, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_campus'


# class ResourcesEvent(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     description = models.CharField(max_length=256, blank=True, null=True)
#     state = models.IntegerField()
#     start = models.DateTimeField()
#     end = models.DateTimeField(blank=True, null=True)
#     eventtype = models.ForeignKey('ResourcesEventtype', models.DO_NOTHING)
#     formfeedbackid = models.ForeignKey(Form, models.DO_NOTHING, blank=True, null=True)
#     formsignupid = models.ForeignKey(Form, models.DO_NOTHING, blank=True, null=True)
#     organizer = models.ForeignKey('ResourcesProponent', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_event'


# class ResourcesEventtype(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     description = models.CharField(max_length=256, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_eventtype'


# class ResourcesFeedback(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     feedbackdate = models.DateTimeField(blank=True, null=True)
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('ResourcesParticipant', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_feedback'


# class ResourcesGeneraluser(models.Model):
#     user_ptr = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
#     contact = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'resources_generaluser'


# class ResourcesItem(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     serialnum = models.CharField(max_length=32)
#     storagelocation = models.ForeignKey('ResourcesLocation', models.DO_NOTHING)
#     typeequipment = models.ForeignKey('ResourcesTypeequipment', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'resources_item'


# class ResourcesItemuse(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     processed = models.IntegerField(blank=True, null=True)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING, blank=True, null=True)
#     item = models.ForeignKey(ResourcesItem, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_itemuse'


# class ResourcesLocation(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=32)
#     maxcapacity = models.IntegerField()
#     maxspecialneedscapacity = models.IntegerField()
#     building = models.ForeignKey(ResourcesBuilding, models.DO_NOTHING)
#     campus = models.ForeignKey(ResourcesCampus, models.DO_NOTHING)
#     locationtype = models.ForeignKey('ResourcesLocationtype', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'resources_location'


# class ResourcesLocationtype(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     description = models.CharField(unique=True, max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_locationtype'


# class ResourcesLocationuse(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     satisfies = models.IntegerField(blank=True, null=True)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING, blank=True, null=True)
#     location = models.ForeignKey(ResourcesLocation, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_locationuse'


# class ResourcesParticipant(models.Model):
#     generaluser_ptr = models.OneToOneField(ResourcesGeneraluser, models.DO_NOTHING, primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_participant'


# class ResourcesProponent(models.Model):
#     generaluser_ptr = models.OneToOneField(ResourcesGeneraluser, models.DO_NOTHING, primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_proponent'


# class ResourcesRegister(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     registerdate = models.DateTimeField(blank=True, null=True)
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(ResourcesParticipant, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_register'


# class ResourcesRequestequipment(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     additionalinfo = models.CharField(max_length=128)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING)
#     typeequipment = models.ForeignKey('ResourcesTypeequipment', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_requestequipment'


# class ResourcesRequestlocation(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     additionalinfo = models.CharField(max_length=128)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING)
#     locationtype = models.ForeignKey(ResourcesLocationtype, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_requestlocation'


# class ResourcesRequestservices(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     additionalinfo = models.CharField(max_length=128)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING)
#     servicestype = models.ForeignKey('ResourcesServicestype', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_requestservices'


# class ResourcesRoom(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=128)
#     building = models.ForeignKey(ResourcesBuilding, models.DO_NOTHING, db_column='Building_id')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'resources_room'


# class ResourcesServicestype(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=126, blank=True, null=True)
#     description = models.CharField(max_length=126, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_servicestype'


# class ResourcesServiceuse(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     event = models.ForeignKey(ResourcesEvent, models.DO_NOTHING, blank=True, null=True)
#     servicestype = models.ForeignKey(ResourcesServicestype, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_serviceuse'


# class ResourcesTypeequipment(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(unique=True, max_length=32)
#     image = models.CharField(max_length=128, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'resources_typeequipment'
