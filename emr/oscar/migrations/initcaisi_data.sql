-- default agency
insert into agency (id, intake_quick_state, intake_indepth_state) values (0, "", "");

-- default facility
INSERT INTO Facility (name, description, lastUpdated,hic,disabled,orgId,sectorId,integratorEnabled,enableIntegratedReferrals,enableHealthNumberRegistry,allowSims,enableDigitalSignatures,ocanServiceOrgNumber,enableOcanForms,enableAnonymous,enableGroupNotes,enableEncounterTime,enableEncounterTransportationTime,rxInteractionWarningLevel,enablePhoneEncounter,displayAllVacancies,enableCbiForm) VALUES ('Default Facility', 'Default facility, please modify with a more appropriate name and description', now(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);

insert into provider_facility values (999998, (select id from Facility where name='Default Facility' ));

-- default roles
INSERT INTO `caisi_role` VALUES (1,'doctor',0,'',now()),(2,'nurse',0,'',now()),(3,'counsellor',0,'',now()),(4,'csw',0,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('psychiatrist', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('RN', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('RPN',1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Nurse Manager', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Clinical Social Worker',1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Clinical Case Manager',1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Medical Secretary', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Clinical Assistant', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('secretary', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Case Manager',1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Housing Worker', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Support Worker', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Client Service Worker', 1,'',now());
insert into caisi_role (name,userDefined,oscar_name,update_date) values('Recreation Therapist', 1,'',now());

-- access types
INSERT INTO `access_type` VALUES (1,'write doctor issues','access'),(2,'read doctor issues','access'),(3,'read doctor notes','access'),(4,'read doctor ticklers','access'),
(5,'write nurse issues','access'),(6,'read nurse issues','access'),(7,'read nurse notes','access'),(8,'read nurse ticklers','access'),
(9,'write counsellor issues','access'),(10,'read counsellor issues','access'),(11,'read counsellor notes','access'),(12,'read counsellor ticklers','access'),
(13,'write csw issues','access'),(14,'read csw issues','access'),(15,'read csw notes','access'),(16,'read csw ticklers','access')
;


INSERT INTO `access_type` (name,type) VALUES ('Write Ticklers','Action'),('prescription Write','access'),('billing','access'),('medical encounter','access'),('immunization','access'),('prevention','access'),('oscarcomm','access'),('disease registry','access'),('medical form','access'),('measurements','access'),('eform','access'),('lab','access'),('prescription Read','access'),('read ticklers','access'),('master file','access'),('Service restriction override on referral','access'),('Service restriction override on admission','access'),('Create service restriction','access'),('Disable service restriction','access');

insert into access_type (name, type) values("read ticklers assigned to a doctor","access");

insert into access_type (name, type) values("read ticklers assigned to a psychiatrist","access");
insert into access_type (name, type) values("write psychiatrist issues","access");
insert into access_type (name, type) values("read psychiatrist issues","access");
insert into access_type (name, type) values("read psychiatrist notes","access");

insert into access_type (name, type) values("read ticklers assigned to a RN","access");
insert into access_type (name, type) values("write RN issues","access");
insert into access_type (name, type) values("read RN issues","access");
insert into access_type (name, type) values("read RN notes","access");

insert into access_type (name, type) values("read ticklers assigned to a RPN","access");
insert into access_type (name, type) values("write RPN issues","access");
insert into access_type (name, type) values("read RPN issues","access");
insert into access_type (name, type) values("read RPN notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Nurse Manager","access");
insert into access_type (name, type) values("write Nurse Manager issues","access");
insert into access_type (name, type) values("read Nurse Manager issues","access");
insert into access_type (name, type) values("read Nurse Manager notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Clinical Social Worker","access");
insert into access_type (name, type) values("write Clinical Social Worker issues","access");
insert into access_type (name, type) values("read Clinical Social Worker issues","access");
insert into access_type (name, type) values("read Clinical Social Worker notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Clinical Case Manager","access");
insert into access_type (name, type) values("write Clinical Case Manager issues","access");
insert into access_type (name, type) values("read Clinical Case Manager issues","access");
insert into access_type (name, type) values("read Clinical Case Manager notes","access");

insert into access_type (name, type) values("read ticklers assigned to a counsellor","access");

insert into access_type (name, type) values("read ticklers assigned to a Case Manager","access");
insert into access_type (name, type) values("write Case Manager issues","access");
insert into access_type (name, type) values("read Case Manager issues","access");
insert into access_type (name, type) values("read Case Manager notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Housing Worker","access");
insert into access_type (name, type) values("write Housing Worker issues","access");
insert into access_type (name, type) values("read Housing Worker issues","access");
insert into access_type (name, type) values("read Housing Worker notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Medical Secretary","access");
insert into access_type (name, type) values("write Medical Secretary issues","access");
insert into access_type (name, type) values("read Medical Secretary issues","access");
insert into access_type (name, type) values("read Medical Secretary notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Clinical Assistant","access");
insert into access_type (name, type) values("write Clinical Assistant issues","access");
insert into access_type (name, type) values("read Clinical Assistant issues","access");
insert into access_type (name, type) values("read Clinical Assistant notes","access");

insert into access_type (name, type) values("read ticklers assigned to a secretary","access");
insert into access_type (name, type) values("write secretary issues","access");
insert into access_type (name, type) values("read secretary issues","access");
insert into access_type (name, type) values("read secretary notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Support Worker","access");
insert into access_type (name, type) values("write Support Worker issues","access");
insert into access_type (name, type) values("read Support Worker issues","access");
insert into access_type (name, type) values("read Support Worker notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Client Service Worker","access");
insert into access_type (name, type) values("write Client Service Worker issues","access");
insert into access_type (name, type) values("read Client Service Worker issues","access");
insert into access_type (name, type) values("read Client Service Worker notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Recreation Therapist","access");
insert into access_type (name, type) values("write Recreation Therapist issues","access");
insert into access_type (name, type) values("read Recreation Therapist issues","access");
insert into access_type (name, type) values("read Recreation Therapist notes","access");

insert into access_type (name, type) values("read ticklers assigned to a property staff","access");
insert into access_type (name, type) values("write property staff issues","access");
insert into access_type (name, type) values("read property staff issues","access");
insert into access_type (name, type) values("read property staff notes","access");

insert into access_type (name, type) values("read ticklers assigned to a Support Counsellor","access");
insert into access_type (name, type) values("write Support Counsellor issues","access");
insert into access_type (name, type) values("read Support Counsellor issues","access");
insert into access_type (name, type) values("read Support Counsellor notes","access");
insert into access_type (name, type) values("read ticklers assigned to a Counselling Intern","access");
insert into access_type (name, type) values("write Counselling Intern issues","access");
insert into access_type (name, type) values("read Counselling Intern issues","access");
insert into access_type (name, type) values("read Counselling Intern notes","access");

-- access types for quatro shelter
insert into access_type (name, type) values("Sex restriction override on referral","access");
insert into access_type (name, type) values("Sex restriction override on admission","access");
insert into access_type (name, type) values("Gender restriction override on referral","access");
insert into access_type (name, type) values("Gender restriction override on admission","access");
insert into access_type (name, type) values("Age restriction override on referral","access");
insert into access_type (name, type) values("Age restriction override on admission","access");
insert into access_type (name, type) values("Allow duplicate client merge","access");
insert into access_type (name, type) values("Perform program registration intake","access");
insert into access_type (name, type) values("perform registration intake","access");
insert into access_type (name, type) values("perform admissions","access");
insert into access_type (name, type) values("perform discharges","access");
insert into access_type (name, type) values("perform bed assignments","access");
insert into access_type (name, type) values("print bed rosters and reports","access");
insert into access_type	(name, type) values("Run Report Runner","access");
insert into access_type	(name, type) values("Design Reports","access");

insert into access_type (name,type) values('read receptionist notes','access');
insert into access_type (name,type) values('write receptionist notes','access');
insert into access_type (name,type) values('write receptionist issues','access');
insert into access_type (name,type) values('read receptionist issues','access');
insert into access_type (name,type) values('read receptionist ticklers','access');


-- default role access (global) (doctor gets all)
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Recreation Therapist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read Support Counsellor notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read property staff notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='prescription Write'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='billing'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='medical encounter'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='lab'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='Run Report Runner'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='Design Reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read nurse issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write nurse issues'));


insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read receptionist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='read receptionist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write receptionist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='doctor'),(select access_id from access_type where name='write receptionist notes'));


insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Recreation Therapist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read Support Counsellor notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read property staff notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='prescription Write'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='billing'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='medical encounter'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='lab'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='read nurse issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='psychiatrist'),(select access_id from access_type where name='write nurse issues'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Recreation Therapist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read Support Counsellor notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read property staff notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='read nurse issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RN'),(select access_id from access_type where name='write nurse issues'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Recreation Therapist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read Support Counsellor notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read property staff notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='read nurse issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='RPN'),(select access_id from access_type where name='write nurse issues'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Recreation Therapist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read Support Counsellor notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read property staff notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='read nurse issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Nurse Manager'),(select access_id from access_type where name='write nurse issues'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Recreation Therapist notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read Support Counsellor notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read property staff notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Social Worker'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Social Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read Recreation Therapist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Case Manager'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Housing Worker'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Medical Secretary'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Clinical Assistant'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='secretary'),(select access_id from access_type where name='perform bed assignments'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Worker'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Client Service Worker'),(select access_id from access_type where name='print bed rosters and reports'));


insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a doctor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write doctor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read doctor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a psychiatrist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write psychiatrist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read psychiatrist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a RN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write RN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read RN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a RPN'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write RPN issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read RPN notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Nurse Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Nurse Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Nurse Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Recreation Therapist'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Recreation Therapist issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Recreation Therapist notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Clinical Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Clinical Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Clinical Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Clinical Social Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Clinical Social Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Case Manager'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Case Manager issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Case Manager notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Housing Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Housing Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Housing Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='immunization'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='prevention'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='disease registry'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='prescription Read'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Recreation Therapist'),(select access_id from access_type where name='print bed rosters and reports'));


insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='read ticklers assigned to a property staff'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='read property staff issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='write property staff issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='read property staff notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='property staff'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read ticklers assigned to a Support Counsellor'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read Support Counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='write Support Counsellor issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read Support Counsellor notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read ticklers assigned to a Support Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='write Support Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read Support Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read ticklers assigned to a Client Service Worker'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='write Client Service Worker issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read Client Service Worker notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Support Counsellor'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='Counselling Intern'),(select access_id from access_type where name='read ticklers assigned to a Counselling Intern'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='Counselling Intern'),(select access_id from access_type where name='read Counselling Intern issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='Counselling Intern'),(select access_id from access_type where name='write Counselling Intern issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name='Counselling Intern'),(select access_id from access_type where name='read Counselling Intern notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read ticklers assigned to a Counselling Intern'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read Counselling Intern issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='write Counselling Intern issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read Counselling Intern notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read ticklers assigned to a Clinical Assistant'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='write Clinical Assistant issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read Clinical Assistant notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read ticklers assigned to a Medical Secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='write Medical Secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read Medical Secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read ticklers assigned to a secretary'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='write secretary issues'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read secretary notes'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='Write Ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='oscarcomm'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='medical form'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='measurements'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='eform'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='master file'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='read ticklers'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='Perform program registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='perform registration intake'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='perform admissions'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='perform discharges'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='perform bed assignments'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Counselling Intern'),(select access_id from access_type where name='print bed rosters and reports'));

insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='Case Manager'),(select access_id from access_type where name='read Counselling Intern notes'));
insert into default_role_access (role_id,access_id) values ((select role_no from secRole where role_name ='counsellor'),(select access_id from access_type where name='read Counselling Intern notes'));






-- counsellor issues
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM1000','Safety','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM2000','Health','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM3000','Personal ID','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM4000','Financial','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM5000','Legal','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM6000','Housing','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM7000','Education','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM8000','Employment','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM9000','Family','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM10000','Community Support','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM11000','Psycho-social concerns','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM12000','Client feedback / suggestions','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM13000','Physical Health','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM14000','Mental Health','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM15000','Addictions','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM16000','Social Support','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM17000','Respite','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM18000','Counselling Support','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM19000','Recovery/Healing','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM20000','Wellness Program','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM21000','Medication','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM22000','Hygiene/Clothing','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM23000','Increase Community Supports','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM24000','Discharge Planning','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM25000','Re- Admission Update','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM26000','Drug Card','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM27000','Suicidal Tendencies','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM28000','Incident Report','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM29000','Immigration','counsellor',Now(),'userDefined',0);

INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM9500','Intimate Relationships','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM11500','Sexual Expression','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM14500','Client Capacity','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM21500','Self Care','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM22500','Looking After the Home','counsellor',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('CTCMM23500','Transportation','counsellor',Now(),'userDefined',0);


-- CSW issues
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW100','program-client conflict','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW200','difficulties with hygeine','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW300','difficulties with eating','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW301','anorexia, loss of apetite','CSW',Now(),'userDefined',0);

INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW210','requires assistance with grooming/personal hygiene','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW310','requires assistance with eating','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW410','requires assistance of reading (vision problem)','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW420','requires assistance of hearing (hearing aids) ','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW430','requires assistance with seizures','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW440','language barriers','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW450','requires assistance with medical care advocacy','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW460','problems related to sleep pattern','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW400','Requires assistance with bathing','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW500','requires assistance with getting dressed','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW600','requires assistance with getting around floor e.g. dining room','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW700','requires assistance with cleaning of living space','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW800','requires assistance with laundry','CSW',Now(),'userDefined',0);
INSERT INTO issue (code,description,role,update_date,type,sortOrderId) values('ICSW1000','Care provided in Managed Alcohol Program','CSW',Now(),'userDefined',0);


-- community programs
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10001,1,'Subsidized Housing','Subsidized Housing','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10002,1,'Private Market Housing','Private Market Housing','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10003,1,'Returned to Previous Address','Returned to Previous Address','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10004,1,'Returned To Partner','Returned To Partner','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10005,1,'Returned to Parents','Returned to Parents','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10006,1,'Moved in with Friends or Relatives','Moved in with Friends or Relatives','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10007,1,'Continued at Another Hospital or Treatment','Continued at Another Hospital or Treatment','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10008,1,'Left the City','Left the City','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10009,1,'Whereabouts Unknown (AWOL)','Whereabouts Unknown (AWOL)','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10010,1,'Community, unknown destination','Community, unknown destination','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10011,1,'Incarcerated','Incarcerated','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10012,1,'Deceased','Deceased','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10013,1,'Community Shelter','Community Shelter','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10014,1,'Other','Other','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,exclusiveView,defaultServiceRestrictionDays,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,ageMin,ageMax) VALUES (10015,1,'Outside on Street','Outside on Street','','','','','','','community','',99999,0,0,0,0,'active','no',30,1,0,0,0,0,0,0,0,1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10016,1,'Correctional/Probational Facility','Correctional/Probational Facility','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10017,1,'Domiciliary Hospital','Domiciliary Hospital','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10018,1,'General Hospital','General Hospital','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10019,1,'Psychiatric Hospital','Psychiatric Hospital','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10020,1,'Other Specialty Hospital','Other Specialty Hospital','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10021,1,'No fixed address','No fixed address','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10022,1,'Hostel/Shelter','Hostel/Shelter','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10023,1,'Long-Term Care Facility/Nursing Home','Long-Term Care Facility/Nursing Home','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10024,1,'Municipal Non-Profit Housing','Municipal Non-Profit Housing','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10025,1,'Private House/Apt.- Client Owned/Market','Private House/Apt.- Client Owned/Market','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10026,1,'Rent','Rent','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10027,1,'Private House/Apt.- Other/Subsidized','Private House/Apt.- Other/Subsidized','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10028,1,'Retirement Home/Seniors\' Residence','Retirement Home/Seniors\' Residence','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,exclusiveView,defaultServiceRestrictionDays,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,ageMin,ageMax) VALUES (10029,1,'Rooming/Boarding House','Rooming/Boarding House','','','','','','','community','',99999,0,0,0,0,'active','no',30,1,0,0,0,0,0,0,0,1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10030,1,'Supportive Housing - Congregate Living','Supportive Housing - Congregate Living','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10031,1,'Supportive Housing - Assisted Living (RTF 24 Hr Home and Group Homes)','Supportive Housing - Assisted Living (RTF 24 Hr Home and Group Homes)','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10032,1,'Private Non-Profit Housing','Private Non-Profit Housing','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
INSERT INTO `program` (id,facilityId,name,description,address,phone,fax,url,email,emergencyNumber,type,location,maxAllowed,holdingTank,allowBatchAdmission,allowBatchDischarge,hic,programStatus,userDefined,transgender,firstNation,bedProgramAffiliated,alcohol,physicalHealth,mentalHealth,housing,exclusiveView,ageMin,ageMax) VALUES (10033,1,'Approved Homes & Homes for Special Care','Approved Homes & Homes for Special Care','','','','','','','community','',99999,0,0,0,0,'active',1,0,0,0,0,0,0,0,'no',1,200);
update `program` set enableEncounterTime=0, enableEncounterTransportationTime=0 where id >= 10001 AND id <=10033;
update program set defaultServiceRestrictionDays = 0 where defaultServiceRestrictionDays is null;


update program set enableEncounterTime=0;
update program set enableEncounterTransportationTime=0;


-- DEFAULT BED TYPE
INSERT INTO `bed_type` VALUES (1, 'N/A', 1);

-- DEFAULT ROOM TYPES
INSERT INTO `room_type` VALUES (1, 'N/A', 1);

-- DEFAULT BED DEMOGRAPHIC STATUSES
INSERT INTO `bed_demographic_status` VALUES (1, 'N/A', 0, 1);

-- SYSTEM PROVIDER
insert into `provider` (`provider_no`, `last_name`, `first_name`, `provider_type`, `specialty`, `sex`, `status`,`lastUpdateDate`) values (-1, 'system', 'system', 'system', 'system', 's', 1,now());

--
-- Populate intake node labels
--
INSERT INTO `intake_node_label` VALUES
	(1, ''),
	(2, 'Registration Intake'),
	(3, 'Follow-up Intake'),
	(4, 'Page'),
	(5, 'Section'),
	(6, 'Question'),
	(7, 'Compound Answer'),
	(8, 'Boolean'),
	(9, 'String'),
	(10, 'Date'),
	(11, 'Integer'),
	(12, 'Email'),
	(13, 'Phone'),
	(14, 'Note'),
	(15, 'Program Intake');

--
-- Populate intake node types
--
INSERT INTO `intake_node_type` VALUES
	(1, 'intake'),
	(2, 'page'),
	(3, 'section'),
	(4, 'question'),
	(5, 'answer compound'),
	(6, 'answer scalar choice'),
	(7, 'answer scalar text'),
	(8, 'answer scalar note'),
	(9,'answer date');

--
-- Populate intake node templates
--
INSERT INTO `intake_node_template` VALUES
	(1, 1, 1, 2),
	(2, 2, 1, 3),
	(3, 3, 2, 4),
	(4, 4, 3, 5),
	(5, 5, 4, 6),
	(6, 6, 5, 7),
	(7, 7, 6, 8),
	(8, 8, 7, 9),
	(9, 9, 7, 10),
	(10, 10, 7, 11),
	(11, 11, 7, 12),
	(12, 12, 7, 13),
	(13, 13, 8, 14),
	(14, 14, 1, 15),
	(15, 15, 6, 8),
	(16,16,9,10);

--
-- Populate intake answer validation
--
INSERT INTO `intake_answer_validation` VALUES
	(1, 'date'),
	(2, 'integer'),
	(3, 'email'),
	(4, 'phone');

--
-- Populate intake answer element
--
INSERT INTO `intake_answer_element` VALUES
	(1, 7, NULL, 0, 'T', ''),
	(2, 7, NULL, 1, 'F', ''),
	(3, 8, NULL, 0, '', ''),
	(4, 9, 1, 0, '', ''),
	(5, 10, 2, 0, '', ''),
	(6, 11, 3, 0, '', ''),
	(7, 12, 4, 0, '', ''),
	(8, 13, NULL, 0, '', '');

--
-- Populate intake node
--
INSERT INTO `intake_node` VALUES
	(1, 1, NULL, 0, NULL, false, 1, 0, 1, NULL, NULL, NULL,1,0,NULL),
	(2, 2, NULL, 0, NULL, false, 2, 0, 1, NULL, NULL, NULL,2,0,NULL);

--
-- Cookie Revolver Init
--
INSERT INTO cr_policy (policy_id, static_ip, ip, remote_access, generate_super_certs, administrate_policies, administrate_questions, remove_bans, user_id, role_id, priority, usage_times_before_reverify, max_time_between_usage, expire_cookie, ip_filter, certs_max, certs_current, default_answer)
VALUES ('admin-policy', 0, null, 1, 1, 1, 1, 1, null, 'admin', 10, 10000000, 2592000, 315360000, null, 1000000, 1, null);

INSERT INTO cr_policy (policy_id, static_ip, ip, remote_access, generate_super_certs, administrate_policies, administrate_questions, remove_bans, user_id, role_id, priority, usage_times_before_reverify, max_time_between_usage, expire_cookie, ip_filter, certs_max, certs_current, default_answer)
VALUES ('doctor-policy', 0, null, 1, 0, 0, 0, 0, null, 'doctor', 10, 10000000, 2592000, 315360000, null, 1000000, 1, null);

INSERT INTO cr_policy (policy_id, static_ip, ip, remote_access, generate_super_certs, administrate_policies, administrate_questions, remove_bans, user_id, role_id, priority, usage_times_before_reverify, max_time_between_usage, expire_cookie, ip_filter, certs_max, certs_current, default_answer)
VALUES ('nurse-policy', 0, null, 1, 0, 0, 0, 0, null, 'nurse', 10, 10000000, 2592000, 315360000, null, 1000000, 1, null);

INSERT INTO cr_policy (policy_id, static_ip, ip, remote_access, generate_super_certs, administrate_policies, administrate_questions, remove_bans, user_id, role_id, priority, usage_times_before_reverify, max_time_between_usage, expire_cookie, ip_filter, certs_max, certs_current, default_answer)
VALUES ('remote-access-policy', 0, null, 1, 0, 0, 0, 0, null, 'remote_access', 10, 10000000, 2592000, 315360000, null, 1000000, 1, null);

INSERT INTO cr_policy (policy_id, static_ip, ip, remote_access, generate_super_certs, administrate_policies, administrate_questions, remove_bans, user_id, role_id, priority, usage_times_before_reverify, max_time_between_usage, expire_cookie, ip_filter, certs_max, certs_current, default_answer)
VALUES ('default', 0, null, 1, 0, 0, 0, 0, null, null, 10, 10000000, 2592000, 315360000, null, 1000000, 1, null);

--
-- Sherbourne Summary Discharge Form
--
insert into encounterForm values("Discharge Summary","../form/formDischargeSummary.jsp?demographic_no=","formDischargeSummary",0);


-- quatro group's report runner
insert into lst_gender (code,description,isactive,displayorder) values ('M','Male',1,2);
insert into lst_gender (code,description,isactive,displayorder) values ('F','Female',1,1);
insert into lst_gender (code,description,isactive,displayorder) values ('T','Transgender',1,3);

insert into lst_sector (id,description,isactive,displayorder) values (1,'Men',1,1);
insert into lst_sector (id,description,isactive,displayorder) values (2,'Women',1,2);
insert into lst_sector (id,description,isactive,displayorder) values (3,'Families',1,3);
insert into lst_sector (id,description,isactive,displayorder) values (4,'Youth',1,4);

insert into lst_organization (id,description,isactive,displayorder) values (1,'City of Toronto',1,1);
insert into lst_organization (id,description,isactive,displayorder) values (2,'Salvation Army',1,2);
insert into lst_organization (id,description,isactive,displayorder) values (3,'Fred Victor',1,3);

insert into lst_discharge_reason (id,description,needsecondary,isactive,displayorder)
values (1,'Service restriction',0,1,10);
insert into lst_discharge_reason (id,description,needsecondary,isactive,displayorder)
values (2,'Client Self Discharge',0,1,10);
insert into lst_discharge_reason (id,description,needsecondary,isactive,displayorder)
values (3,'Other Program more appropriate',0,1,10);

insert into lst_field_category (id, description,isactive,displayorder)
values(1,'Agency',	1,	10);
insert into lst_field_category (id, description,isactive,displayorder)
values(2,'Client',  1, 20);
insert into lst_field_category (id, description,isactive,displayorder)
values(3,'Intake',	1,	30);
insert into lst_field_category (id, description,isactive,displayorder)
values(4,'Program', 1, 40);

insert into lst_service_restriction(id,description,isactive,displayorder)
values (1,'Assault of client',1,10);
insert into lst_service_restriction(id,description,isactive,displayorder)
values (2,'Assault of staff',1,20);
insert into lst_service_restriction(id,description,isactive,displayorder)
values (3,'Other',1,30);

insert into lst_admission_status(code,description, isactive, displayorder)
values ('current','Current', 1, 10);
insert into lst_admission_status(code,description, isactive, displayorder)
values ('discharged','Discharged', 1, 20);

insert into lst_program_type values('01','BED',1,1);
insert into lst_program_type values('02','SERVICE',1,2);
insert into lst_program_type values('03','EXTERNAL',1,3);

insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('ORG', '1', 'lst_orgcd', 'Org Chart', 1, 8, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('BTY', '4', 'bed_type', 'Bed Type', 0, 0, 0,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('GEN', '4', 'lst_gender', 'Gender', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('SEC', '2', 'lst_sector', 'Sector', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('OGN', '2', 'lst_organization', 'Organization', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('DRN', '5', 'lst_discharge_reason', 'Discharge Reason', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('SRT', '3', 'lst_service_restriction', 'Service Restriction', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('LKT', '1', 'app_lookuptable', 'Available Fields', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('FCT', '1', 'lst_field_category', 'Field Category', 0, 0, 1,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('PRO', '5', 'program', 'Program', 0, 0, 0,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('FAC', '5', 'facility', 'Facility', 0, 0, 0,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('AST', '5', 'lst_admission_status', 'Admission Status', 0, 0, 0,0);
insert into app_lookuptable (tableid, moduleid, table_name, description, istree, treecode_length, activeyn,readonly)
values ('PTY', '5', 'lst_program_type', 'Program Type', 0, 0, 0,0);
commit;

insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('ORG', 'code', 'CODE', '1', 'S', null, 'code', 1, 1, 1, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('ORG', 'description', 'DESCRIPTION', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('ORG', 'activeyn', 'ACTIVEYN', '1', 'N', null, 'activeyn', 3, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('ORG', 'orderbyindex', 'ORDERBYINDEX', '1', 'N', null, 'orderbyindex', 4, 0, 4, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('ORG', 'codetree', 'CODETREE', '1', 'S', null, 'codetree', 5, 0, 7, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('FCT', 'ID', 'Id', '0', 'N', null, 'id', 1, 1, 1, 1);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('FCT', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('FCT', 'ISACTIVE', 'Active?', '1', 'B', null, 'isactive', 3, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('FCT', 'DISPLAYORDER', 'Dispaly Order', '1', 'N', null, 'displayorder', 4, 0, 4, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('BTY', 'BED_TYPE_ID', 'Id', '0', 'N', null, 'bed_type_id', 1, 1, 1, 1);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('BTY', 'NAME', 'Name', '1', 'S', null, 'name', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('BTY', 'DFLT', 'Default Capacity', '1', 'N', null, 'dflt', 3, 0, 6, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'TABLEID', 'Id', '0', 'S', null, 'tableid', 1, 1, 1, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'MODULEID', 'Category', '1', 'S', 'FCT', 'moduleid', 2, 0, 5, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'TABLE_NAME', 'Table Name', '1', 'S', null, 'table_name', 3, 0, 6, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 4, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'ISTREE', 'Is Tree Structured?', '1', 'B', null, 'istree', 5, 0, 0, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'TREECODE_LENGTH', 'Tree Code Length (if is tree)', '1', 'N', null, 'treecode_length', 6, 0, 0, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('LKT', 'ACTIVEYN', 'Active?', '1', 'B', null, 'activeyn', 7, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('GEN', 'CODE', 'Code', '1', 'S', null, 'code', 1, 1, 1, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('GEN', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('GEN', 'ISACTIVE', 'Active?', '1', 'B', null, 'isactive', 3, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('GEN', 'DISPLAYORDER', 'Dispaly Order', '1', 'N', null, 'displayorder', 4, 0, 4, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SEC', 'ID', 'Id', '0', 'N', null, 'id', 1, 1, 1, 1);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SEC', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SEC', 'ISACTIVE', 'Active?', '1', 'B', null, 'isactive', 3, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SEC', 'DISPLAYORDER', 'Dispaly Order', '1', 'N', null, 'displayorder', 4, 0, 4, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('OGN', 'ID', 'Id', '0', 'N', null, 'id', 1, 1, 1, 1);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('OGN', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('OGN', 'ISACTIVE', 'Active?', '1', 'B', null, 'isactive', 3, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('OGN', 'DISPLAYORDER', 'Dispaly Order', '1', 'N', null, 'displayorder', 4, 0, 4, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('DRN', 'ID', 'Id', '0', 'N', null, 'id', 1, 1, 1, 1);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('DRN', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('DRN', 'NEEDSECONDARY', 'Has Associated Secondary Reason?', '1', 'N', null, 'needsecondary', 3, 0, 6, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('DRN', 'ISACTIVE', 'Active?', '1', 'B', null, 'isactive', 4, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('DRN', 'DISPLAYORDER', 'Dispaly Order', '1', 'N', null, 'displayorder', 5, 0, 4, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SRT', 'ID', 'Id', '0', 'N', null, 'id', 1, 1, 1, 1);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SRT', 'DESCRIPTION', 'Description', '1', 'S', null, 'description', 2, 0, 2, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SRT', 'ISACTIVE', 'Active?', '1', 'B', null, 'isactive', 3, 0, 3, 0);
insert into app_lookuptable_fields (tableid, fieldname, fielddesc, edityn, fieldtype, lookuptable, fieldsql, fieldindex, uniqueyn, genericiDX, AUTOYN)
values ('SRT', 'DISPLAYORDER', 'Dispaly Order', '1', 'N', null, 'displayorder', 4, 0, 4, 0);
commit;

insert into app_module (module_id, description)
values (1, 'Client Management');
insert into app_module (module_id, description)
values (2, 'Shelter Management');
insert into app_module (module_id, description)
values (3, 'Case Management');
insert into app_module (module_id, description)
values (4, 'System Administration');
insert into app_module (module_id, description)
values (5, 'Reports');


insert into report (reportno, title, description, orgapplicable, reporttype, dateoption, datepart, reportgroup, notes, tablename, updatedby, updateddate, sptorun)
values (81, 'Shelter Bed Logs', 'Bed Logs in a given shelter on given dates ', 1, 'RPT', 'B', 'D', 15, null, 'V_REP_BEDLOG', 'oscardoc', '2007-12-07 09:37:47', null);
insert into report (reportno, title, description, orgapplicable, reporttype, dateoption, datepart, reportgroup, notes, tablename, updatedby, updateddate, sptorun)
values (82, 'Client List', 'Under designing, please do not test', 1, 'RPT', 'N', null, 5, null, null, 'mespina', '2007-12-07 09:37:47', null);
insert into report (reportno, title, description, orgapplicable, reporttype, dateoption, datepart, reportgroup, notes, tablename, updatedby, updateddate, sptorun)
values (83, 'Case List', 'Under designing, please do not test', 1, 'RPT', 'N', null, 10, null, null, 'mespina', '2007-12-07 09:37:47', null);
insert into report (reportno, title, description, orgapplicable, reporttype, dateoption, datepart, reportgroup, notes, tablename, updatedby, updateddate, sptorun)
values (200594, 'User List', 'List of Users', 1, 'RPT', 'L', 'M', 90, null, 'V_REP_USERLIST', 'oscardoc', '2008-02-22 23:19:44', null);


insert into report_date_sp (reportno, startdate, enddate, asofdate, startdate_s, enddate_s, asofdate_s, sptorun)
values (88, '2007-12-06', '2008-02-08', '2007-12-06', '20071206', '20080208', '20071206', 'sp_cr_insert_empreghrs_tbl');

insert into report_document (docid, subject, privacycd, ownerid, checkoutyn, checkoutuserid, checkoutdate, doctype, filename, moduleid, refno, filetype, viewid, viewrefno, revdatetime)
values (200696, 'List Of Users', 'P', 'oscardoc', '0', null, null, 'RPT', 'CR_USER_LIST.rpt', 'REPORT', null, null, null, null, '2008-02-27 14:36:13');

insert into report_filter (reportno, fieldno, fieldname, fielddesc, fieldtype, lookup_table, iscrosstabheaders, operator, lookup_tree, fieldsql, lookup_script, note, valueformat)
values (200594, 200618, 'ROLE_NAME', null, 'S', 'ROL', null, 'C', null, 'ROLE_NAME', null, null, null);
insert into report_filter (reportno, fieldno, fieldname, fielddesc, fieldtype, lookup_table, iscrosstabheaders, operator, lookup_tree, fieldsql, lookup_script, note, valueformat)
values (200594, 200599, 'FIRST_NAME', null, 'S', null, null, 'CL', null, 'FIRST_NAME', null, null, null);
insert into report_filter (reportno, fieldno, fieldname, fielddesc, fieldtype, lookup_table, iscrosstabheaders, operator, lookup_tree, fieldsql, lookup_script, note, valueformat)
values (200594, 200600, 'Last Name', null, 'S', null, null, 'CL', null, 'LAST_NAME', null, null, null);
insert into report_filter (reportno, fieldno, fieldname, fielddesc, fieldtype, lookup_table, iscrosstabheaders, operator, lookup_tree, fieldsql, lookup_script, note, valueformat)
values (81, 1, 'Last Name', 'Client Last Name', 'S', 'BED', 'N', 'CL', null, 'LAST_NAME', null, null, null);
insert into report_filter (reportno, fieldno, fieldname, fielddesc, fieldtype, lookup_table, iscrosstabheaders, operator, lookup_tree, fieldsql, lookup_script, note, valueformat)
values (81, 2, 'First Name', 'Client First Name', 'S', 'BED', 'N', 'CL', null, 'FIRST_NAME', null, null, null);
insert into report_filter (reportno, fieldno, fieldname, fielddesc, fieldtype, lookup_table, iscrosstabheaders, operator, lookup_tree, fieldsql, lookup_script, note, valueformat)
values (81, 3, 'Room Name', 'Room Name', 'S', null, 'N', 'CL', null, 'ROOM_NAME', null, null, null);

insert into report_lk_reportgroup (id, description, shortdesc, activeyn, orderbyindex, note)
values (90, 'System Reserved', 'System', 'Y', 1500, 'This code is reserved for QGView use');
insert into report_lk_reportgroup (id, description, shortdesc, activeyn, orderbyindex, note)
values (5, 'Client Management', 'Client', 'Y', 1240, null);
insert into report_lk_reportgroup (id, description, shortdesc, activeyn, orderbyindex, note)
values (10, 'Case Management', 'Case', 'Y', 1241, null);
insert into report_lk_reportgroup (id, description, shortdesc, activeyn, orderbyindex, note)
values (15, 'Facility Management', 'Facility', 'Y', 1246, null);

insert into report_option (reportno, reportoptionid, optiontitle, longdesc, activeyn, defaultyn, datefield, datefielddesc, sqlwhere, sqlorderby, rptfilename, rptfileno, rptversion, datefieldtype)
values (81, 2, 'Bed log by data not works', 'Bed Log by data not works', 1, 0, 'ADMISSION_DATE', 'Admission Date', null, null, 'CR_SHEL_BEDLOG.rpt', 0, null, null);
insert into report_option (reportno, reportoptionid, optiontitle, longdesc, activeyn, defaultyn, datefield, datefielddesc, sqlwhere, sqlorderby, rptfilename, rptfileno, rptversion, datefieldtype)
values (81, 1, 'Bed log by date', 'Bed Log by date', 1, 1, 'ADMISSION_DATE', 'Admission Date', null, null, 'CR_SHEL_BEDLOG.rpt', 0, null, null);
insert into report_option (reportno, reportoptionid, optiontitle, longdesc, activeyn, defaultyn, datefield, datefielddesc, sqlwhere, sqlorderby, rptfilename, rptfileno, rptversion, datefieldtype)
values (200594, 200595, 'List Of Users', 'List f Users', 1, 1, 'PROVIDER_NO', null, null, null, 'CR_USER_LIST.rpt', 200696, null, null);

insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'CLIENT_ID', 1, null, 'N', null, null, 'CLIENT_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'ADMISSION_DATE', 2, null, 'D', null, null, 'ADMISSION_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'DISCHARGE_DATE', 3, null, 'D', null, null, 'DISCHARGE_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'PROGRAM_NAME', 4, null, 'S', null, null, 'PROGRAM_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'PROGRAM_DESCRIPTION', 5, null, 'S', null, null, 'PROGRAM_DESCRIPTION', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'BED_ID', 6, null, 'N', null, null, 'BED_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'BED_NAME', 7, null, 'S', null, null, 'BED_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'ROOM_ID', 8, null, 'N', null, null, 'ROOM_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'ROOM_NAME', 9, null, 'S', null, null, 'ROOM_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'CLIENT_PROG_ST_NAME', 10, null, 'S', null, null, 'CLIENT_PROG_ST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'LAST_NAME', 11, null, 'S', null, null, 'LAST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'FIRST_NAME', 12, null, 'S', null, null, 'FIRST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200549, 'ORGCD', 13, null, 'N', null, null, 'ORGCD', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200554, 'PROVIDER_NO', 1, null, 'S', null, 0, 'PROVIDER.PROVIDER_NO', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200554, 'LAST_NAME', 2, 'Last Name', 'S', null, 0, 'PROVIDER.LAST_NAME', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200554, 'FIRST_NAME', 3, null, 'S', null, 0, 'PROVIDER.FIRST_NAME', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200554, 'ROLE_NAME', 4, null, 'S', null, 0, 'SECUSERROLE.ROLE_NAME', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'PROVIDER_NO', 1, null, 'S', null, null, 'PROVIDER_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'LAST_NAME', 2, null, 'S', null, null, 'LAST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'FIRST_NAME', 3, null, 'S', null, null, 'FIRST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'PROVIDER_TYPE', 4, null, 'S', null, null, 'PROVIDER_TYPE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'SPECIALTY', 5, null, 'S', null, null, 'SPECIALTY', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'TEAM', 6, null, 'S', null, null, 'TEAM', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'SEX', 7, null, 'S', null, null, 'SEX', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'DOB', 8, null, 'D', null, null, 'DOB', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'ADDRESS', 9, null, 'S', null, null, 'ADDRESS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'PHONE', 10, null, 'S', null, null, 'PHONE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'WORK_PHONE', 11, null, 'S', null, null, 'WORK_PHONE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'OHIP_NO', 12, null, 'S', null, null, 'OHIP_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'RMA_NO', 13, null, 'S', null, null, 'RMA_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'BILLING_NO', 14, null, 'S', null, null, 'BILLING_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'HSO_NO', 15, null, 'S', null, null, 'HSO_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'STATUS', 16, null, 'S', null, null, 'STATUS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'COMMENTS', 17, null, 'S', null, null, 'COMMENTS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200555, 'PROVIDER_ACTIVITY', 18, null, 'S', null, null, 'PROVIDER_ACTIVITY', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200556, 'PROVIDER_NO', 1, null, 'S', null, null, 'PROVIDER_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200556, 'ROLE_NAME', 2, null, 'S', null, null, 'ROLE_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'LAST_NAME', 1, null, 'S', null, 0, 'DEMOGRAPHIC.LAST_NAME', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'FIRST_NAME', 2, null, 'S', null, 0, 'DEMOGRAPHIC.FIRST_NAME', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'ADDRESS', 3, null, 'S', null, 0, 'DEMOGRAPHIC.ADDRESS', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'CITY', 4, null, 'S', null, 0, 'DEMOGRAPHIC.CITY', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'PROVINCE', 5, null, 'S', null, 0, 'DEMOGRAPHIC.PROVINCE', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'POSTAL', 6, null, 'S', null, 0, 'DEMOGRAPHIC.POSTAL', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'ALIAS', 7, null, 'S', null, 0, 'DEMOGRAPHIC.ALIAS', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'INTAKE_ID', 8, null, 'N', null, 0, 'INTAKE.INTAKE_ID', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'CLIENT_ID', 9, null, 'N', null, 0, 'INTAKE.CLIENT_ID', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'STAFF_ID', 10, null, 'S', null, 0, 'INTAKE.STAFF_ID', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200611, 'CREATION_DATE', 11, null, 'D', null, 0, 'INTAKE.CREATION_DATE', null, 0, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'DEMOGRAPHIC_NO', 1, null, 'N', null, null, 'DEMOGRAPHIC_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'LAST_NAME', 2, null, 'S', null, null, 'LAST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'FIRST_NAME', 3, null, 'S', null, null, 'FIRST_NAME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'ADDRESS', 4, null, 'S', null, null, 'ADDRESS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'CITY', 5, null, 'S', null, null, 'CITY', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PROVINCE', 6, null, 'S', null, null, 'PROVINCE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'POSTAL', 7, null, 'S', null, null, 'POSTAL', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PHONE', 8, null, 'S', null, null, 'PHONE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PHONE2', 9, null, 'S', null, null, 'PHONE2', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'EMAIL', 10, null, 'S', null, null, 'EMAIL', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PIN', 11, null, 'S', null, null, 'PIN', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'YEAR_OF_BIRTH', 12, null, 'S', null, null, 'YEAR_OF_BIRTH', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'MONTH_OF_BIRTH', 13, null, 'S', null, null, 'MONTH_OF_BIRTH', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'DATE_OF_BIRTH', 14, null, 'S', null, null, 'DATE_OF_BIRTH', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'HIN', 15, null, 'S', null, null, 'HIN', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'VER', 16, null, 'S', null, null, 'VER', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'ROSTER_STATUS', 17, null, 'S', null, null, 'ROSTER_STATUS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PATIENT_STATUS', 18, null, 'S', null, null, 'PATIENT_STATUS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'DATE_JOINED', 19, null, 'D', null, null, 'DATE_JOINED', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'CHART_NO', 20, null, 'S', null, null, 'CHART_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PROVIDER_NO', 21, null, 'S', null, null, 'PROVIDER_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'SEX', 22, null, 'S', null, null, 'SEX', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'END_DATE', 23, null, 'D', null, null, 'END_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'EFF_DATE', 24, null, 'D', null, null, 'EFF_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PCN_INDICATOR', 25, null, 'S', null, null, 'PCN_INDICATOR', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'HC_TYPE', 26, null, 'S', null, null, 'HC_TYPE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'HC_RENEW_DATE', 27, null, 'D', null, null, 'HC_RENEW_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'FAMILY_DOCTOR', 28, null, 'S', null, null, 'FAMILY_DOCTOR', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'ALIAS', 29, null, 'S', null, null, 'ALIAS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'PREVIOUSADDRESS', 30, null, 'S', null, null, 'PREVIOUSADDRESS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'CHILDREN', 31, null, 'S', null, null, 'CHILDREN', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'SOURCEOFINCOME', 32, null, 'S', null, null, 'SOURCEOFINCOME', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'CITIZENSHIP', 33, null, 'S', null, null, 'CITIZENSHIP', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200615, 'SIN', 34, null, 'S', null, null, 'SIN', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200616, 'INTAKE_ID', 1, null, 'N', null, null, 'INTAKE_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200616, 'INTAKE_NODE_ID', 2, null, 'N', null, null, 'INTAKE_NODE_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200616, 'CLIENT_ID', 3, null, 'N', null, null, 'CLIENT_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200616, 'STAFF_ID', 4, null, 'S', null, null, 'STAFF_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200616, 'CREATION_DATE', 5, null, 'D', null, null, 'CREATION_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'AM_ID', 1, null, 'N', null, null, 'AM_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'CLIENT_ID', 2, null, 'N', null, null, 'CLIENT_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'PROGRAM_ID', 3, null, 'N', null, null, 'PROGRAM_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'PROVIDER_NO', 4, null, 'S', null, null, 'PROVIDER_NO', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'ADMISSION_DATE', 5, null, 'D', null, null, 'ADMISSION_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'ADMISSION_NOTES', 6, null, 'S', null, null, 'ADMISSION_NOTES', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'TEMP_ADMISSION', 7, null, 'S', null, null, 'TEMP_ADMISSION', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'DISCHARGE_DATE', 8, null, 'D', null, null, 'DISCHARGE_DATE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'DISCHARGE_NOTES', 9, null, 'S', null, null, 'DISCHARGE_NOTES', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'TEMP_ADMIT_DISCHARGE', 10, null, 'S', null, null, 'TEMP_ADMIT_DISCHARGE', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'ADMISSION_STATUS', 11, null, 'S', null, null, 'ADMISSION_STATUS', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'TEAM_ID', 12, null, 'N', null, null, 'TEAM_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'TEMPORARY_ADMISSION_FLAG', 13, null, 'N', null, null, 'TEMPORARY_ADMISSION_FLAG', 'initial set up', null, null);


insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'AGENCY_ID', 14, null, 'N', null, null, 'AGENCY_ID', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'RADIODISCHARGEREASON', 15, null, 'S', null, null, 'RADIODISCHARGEREASON', 'initial set up', null, null);
insert into report_qgviewfield (qgviewno, fieldname, fieldno, description, fieldtypecode, numbermask, fieldlength, sourcetxt, note, grouprank, lookuptable)
values (200617, 'CLIENTSTATUS_ID', 16, null, 'N', null, null, 'CLIENTSTATUS_ID', 'initial set up', null, null);

insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200615, 'DEMOGRAPHIC', null, '90', 'M', 'oscardoc', '2008-02-22 21:13:31', 'intial setup', '1', '0', 'DEMOGRAPHIC', 'DEMOGRAPHIC', null, null, 'TABLE', null);
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200616, 'INTAKE', null, '90', 'M', 'oscardoc', '2008-02-22', 'intial setup', '1', '0', 'INTAKE', 'INTAKE', null, null, 'TABLE', null);
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200617, 'ADMISSION', null, '90', 'M', 'oscardoc', '2008-02-22', 'intial setup', '1', '0', 'ADMISSION', 'ADMISSION', null, null, 'TABLE', null);
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200549, 'V_REP_BEDLOG', null, '90', 'M', 'oscardoc', '2008-02-20 14:19:40', 'intial setup', '1', '0', 'V_REP_BEDLOG', 'V_REP_BEDLOG', null, null, 'VIEW', null);
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200554, 'V_REP_USERLIST', 'User List', '90', 'N', 'oscardoc', '2008-02-21 15:37:41', null, '0', '0', 'V_REP_USERLIST', 'PROVIDER,SECUSERROLE', 'PROVIDER INNER JOIN SECUSERROLE ON PROVIDER.PROVIDER_NO=SECUSERROLE.PROVIDER_NO', null, 'VIEW', '1');
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200611, 'V_REP_CLIENT', 'List of clients', '5', 'N', 'oscardoc', '2008-02-22 23:00:16', 'This is a master view for clients', '0', '0', 'V_REP_CLIENT', 'DEMOGRAPHIC,INTAKE', 'INTAKE INNER JOIN DEMOGRAPHIC ON INTAKE.CLIENT_ID=DEMOGRAPHIC.DEMOGRAPHIC_NO', null, 'VIEW', null);
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200555, 'PROVIDER', null, '90', 'M', 'oscardoc', '2008-02-21', 'intial setup', '1', '0', 'PROVIDER', 'PROVIDER', null, null, 'TABLE', null);
insert into report_qgviewsummary (qgviewno, qgviewcode, description, groupcode, mastertype, updatedby, updateddate, note, activeyn, secureyn, dbentity, refviews, relations, filters, object_type, distinctyn)
values (200556, 'SECUSERROLE', null, '90', 'M', 'oscardoc', '2008-02-21 12:59:53', 'intial setup', '1', '0', 'SECUSERROLE', 'SECUSERROLE', null, null, 'TABLE', null);


insert into report_role (reportno, rolecode, access_type)
values (82, 'doctor', '1');
insert into report_role (reportno, rolecode, access_type)
values (81, 'doctor', '1');
insert into report_role (reportno, rolecode, access_type)
values (83, 'doctor', '1');
insert into report_role (reportno, rolecode, access_type)
values (200594, 'doctor', '1');
insert into report_role (reportno, rolecode, access_type)
values (200594, 'admin', '1');

insert into report_template (templateno, reportno, reportoptionid, description, startdate, enddate, startpayperiod, endpayperiod, loginid, updatedate, privateyn)
values (200682, 81, 2, 'asdfgh', '2008-02-04', '2008-02-22', null, null, '999998', null, 0);
insert into report_template (templateno, reportno, reportoptionid, description, startdate, enddate, startpayperiod, endpayperiod, loginid, updatedate, privateyn)
values (200686, 81, 1, 'qwert', '2008-02-01', '2008-02-28', null, null, '999998', null, 0);
insert into report_template (templateno, reportno, reportoptionid, description, startdate, enddate, startpayperiod, endpayperiod, loginid, updatedate, privateyn)
values (200622, 200594, 200595, 'List of doctors', '1899-12-30', '1899-12-30', null, null, '999998', '2008-02-22 21:37:02', 0);
insert into report_template (templateno, reportno, reportoptionid, description, startdate, enddate, startpayperiod, endpayperiod, loginid, updatedate, privateyn)
values (313, 83, 7, 'Incident Cost Exception Report - Estimated Costs =$0', '1899-12-30', '1899-12-30', null, null, '999998', '2007-11-07 10:34:00', 0);
insert into report_template (templateno, reportno, reportoptionid, description, startdate, enddate, startpayperiod, endpayperiod, loginid, updatedate, privateyn)
values (312, 83, 6, 'Fatal Public Electrical Incidents', '1899-12-30', '1899-12-30', null, null, '999998', '2007-07-10 15:32:56', 0);



insert into report_template_criteria (counter, templateno, relation, fieldno, operator, operators, val, valdesc, required)
values (200688, 200686, null, 2, '=', null, '200284', 'Bed 10', 0);
insert into report_template_criteria (counter, templateno, relation, fieldno, operator, operators, val, valdesc, required)
values (1, 200622, null, 200618, '=', 'C', 'doctor', 'doctor', 0);
insert into report_template_criteria (counter, templateno, relation, fieldno, operator, operators, val, valdesc, required)
values (1, 200605, null, 200599, 'Like', 'CL', '*doc*', null, 0);
insert into report_template_criteria (counter, templateno, relation, fieldno, operator, operators, val, valdesc, required)
values (1, 200606, null, 200599, 'Like', 'CL', '*doc*', null, 0);
insert into report_template_criteria (counter, templateno, relation, fieldno, operator, operators, val, valdesc, required)
values (200694, 200682, null, 2, '=', null, '200267', 'Bed 1', 0);
insert into report_template_criteria (counter, templateno, relation, fieldno, operator, operators, val, valdesc, required)
values (200695, 200682, 'AND', 1, '<=', null, '200268', 'Bed 2', 0);


insert into report_template_org (counter, templateno, orgcd)
values (200687, 200686, '0');
insert into report_template_org (counter, templateno, orgcd)
values (1, 200622, 'ORG');
insert into report_template_org (counter, templateno, orgcd)
values (200693, 200682, '0');

-- set cpp issues
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('OMeds','Other Meds as part of cpp', 'nurse', now(), 'system',0);
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('SocHistory','Social History as part of cpp', 'nurse', now(), 'system',0);
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('MedHistory','Medical History as part of cpp', 'nurse', now(), 'system',0);
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('Concerns','Ongoing Concerns as part of cpp', 'nurse', now(), 'system',0);
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('Reminders','Reminders as part of cpp', 'nurse', now(), 'system',0);
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('FamHistory','Family History as part of cpp', 'nurse', now(), 'system',0);
insert into issue (`code`,`description`,`role`,`update_date`,`type`,sortOrderId) Values('RiskFactors','Risk Factors as part of cpp', 'nurse', now(), 'system',0);

INSERT INTO encounterForm VALUES("Mental Health Form1","../form/formMentalHealthForm1.jsp?demographic_no=","formMentalHealthForm1",0);
INSERT INTO encounterForm VALUES("Mental Health Form14","../form/formMentalHealthForm14.jsp?demographic_no=","formMentalHealthForm14",0);
insert into encounterForm values("Mental Health Form42","../form/formMentalHealthForm42.jsp?demographic_no=","formMentalHealthForm42",0);

insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K203A','Group3','Group3','A',1);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order)  values('PSYCHIATRIST',	'P01','K204A','Group3','Group3','A',2);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K205A','Group3','Group3','A',3);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K620A','Group3','Group3','A',4);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K623A','Group3','Group3','A',5);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K624A','Group3','Group3','A',6);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K992A','Group3','Group3','A',7);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K994A','Group3','Group3','A',8);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K002A','Group2','Group2','A',1);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K003A','Group2','Group2','A',2);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K005A','Group2','Group2','A',3);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K050A','Group2','Group2','A',4);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K051A','Group2','Group2','A',5);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K052A','Group2','Group2','A',6);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K053A','Group2','Group2','A',7);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K054A','Group2','Group2','A',8);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K055A','Group2','Group2','A',9);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K193A','Group2','Group2','A',10);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K195A','Group2','Group2','A',11);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K197A','Group2','Group2','A',12);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','K198A','Group2','Group2','A',13);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','A194A','Group1','Group1','A',2);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','A193A','Group1','Group1','A',1);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','A195A','Group1','Group1','A',3);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','A395A','Group1','Group1','A',4);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','G497A','Group1','Group1','A',6);
insert into ctl_billingservice (servicetype_name,servicetype,service_code,service_group_name,service_group,status,service_order) values('PSYCHIATRIST',	'P01','A795A','Group1','Group1','A',5);


--
-- source init_cds_form_4_options.sql;
--

insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','007-01','Unique individuals - admitted');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','007-02','Unique individuals - pre-admission');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','007-03','Individuals- not uniquely identified');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','007-04','Multiple Admission for Uniquely Identified Individuals');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','07a-01','Individuals Waiting for Initial Assessment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','07a-02','Days Waited for Initial Assessment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','07a-03','Individuals Waiting for Service Initiation');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','07a-04','Days Waited for Service Initiation');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','008-01','Male');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','008-02','Female');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','008-03','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','008-04','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-01','0-15');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-02','16-17');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-03','18-24');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-04','25-34');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-05','35-44');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-06','45-54');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-07','55-64');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-08','65-74');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-09','75-84');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-10','85 and over');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-11','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-12','Minimum Age');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-13','Maximum Age');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','009-14','Average Age');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-01','Algoma District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-02','Brant');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-03','Bruce');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-04','Cochrane District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-05','Dufferin');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-06','Durham');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-07','Elgin');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-08','Essex');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-09','Frontenac');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-10','Grey');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-11','Haldimand-Norfolk');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-12','Haliburton');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-13','Halton');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-14','Hamilton');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-15','Hastings');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-16','Huron');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-17','Kenora & Kenora P.P.');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-18','Chatham-Kent');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-19','Lambton');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-20','Lanark');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-21','Leeds & Grenville');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-22','Lennox & Addington');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-23','Manitoulin District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-24','Middlesex');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-25','Muskoka District Mun');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-26','Niagara');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-27','Nipissing District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-28','Northumberland');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-29','Ottawa');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-30','Out Of Province');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-31','Oxford');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-32','Parry Sound District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-33','Peel');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-34','Perth');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-35','Peterborough');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-36','Prescott & Russell');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-37','Prince Edward');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-38','Rainy River District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-39','Renfrew');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-40','Simcoe');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-41','Stormont, Dundas & Glengarry');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-42','Sudbury District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-43','Sudbury Region');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-44','Thunder Bay District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-45','Timiskaming District');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-46','Toronto');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-47','Unknown');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-48','Victoria Kawartha Lakes');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-49','Waterloo');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-50','Wellington');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-51','York');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','010-52','Out of Country');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-01','Central');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-02','Central East');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-03','Central West');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-04','Champlain');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-05','Erie-St.Clair');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-06','Hamilton Niagara Haldimand Brant');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-07','Mississauga Halton');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-08','North East');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-09','North Simcoe Muskoka');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-10','North West');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-11','South East');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-12','South West');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-13','Toronto Central');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-14','Waterloo Wellington');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-15','Out of Province');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10a-16','Other/Unknown');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-01','Central');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-02','Central East');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-03','Central West');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-04','Champlain');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-05','Erie-St.Clair');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-06','Hamilton Niagara Haldimand Brant');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-07','Mississauga Halton');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-08','North East');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-09','North Simcoe Muskoka');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-10','North West');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-11','South East');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-12','South West');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-13','Toronto Central');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-14','Waterloo Wellington');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-15','Out of Province');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','10b-16','Other/Unknown');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','011-01','Aboriginal');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','011-02','Non-aboriginal');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','011-03','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','012-01','English');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','012-02','French');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','012-03','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','012-04','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-01','Pre-charge Diversion');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-02','Court Diversion Program');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-03','Awaiting fitness assessment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-04','Awaiting trial (with or without bail)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-05','Awaiting Criminal Responsibility Assessment (NCR)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-06','In community on own recognizance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-07','Unfit to stand trial');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-08','Charges withdrawn');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-09','Stay of proceedings');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-10','Awaiting sentence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-11','NCR');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-12','Conditional discharge');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-13','Conditional sentence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-14','Restraining order');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-15','Peace bond');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-16','Suspended sentence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-17','ORB detained- community access');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-18','ORB conditional discharge');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-19','On parole');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-20','On probation');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-21','No Legal Problems (includes absolute discharge and end of sentence)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','013-24','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-01','Pre-charge Diversion');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-02','Court Diversion Program');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-03','Awaiting fitness assessment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-04','Awaiting trial (with or without bail)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-05','Awaiting Criminal Responsibility Assessment (NCR)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-06','In community on own recognizance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-07','Unfit to stand trial');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-08','Charges withdrawn');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-09','Stay of proceedings');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-10','Awaiting sentence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-11','NCR');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-12','Conditional discharge');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-13','Conditional sentence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-14','Restraining order');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-15','Peace bond');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-16','Suspended sentence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-17','ORB detained- community access');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-18','ORB conditional discharge');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-19','On parole');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-20','On probation');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-21','No Legal Problems (includes absolute discharge and end of sentence)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','014-24','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','015-01','Issued CTO');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','015-02','No CTO');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','015-03','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-01','Adjustment Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-02','Anxiety Disorder');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-03','Delirium, Dementia, and Amnestic and Cognitive Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-04','Disorder of Childhood/Adolescence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-05','Dissociative Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-06','Eating Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-07','Factitious Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-08','Impulse Control Disorders not elsewhere classified');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-09','Mental Disorders due to General Medical Conditions');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-10','Mood Disorder');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-11','Personality Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-12','Schizophrenia and other Psychotic Disorder');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-13','Sexual and Gender Identity Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-14','Sleep Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-15','Somatoform Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-16','Substance Related Disorders');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-17','Developmental Handicap');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','016-18','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','16a-01','Concurrent Disorder (Substance Abuse)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','16a-02','Dual Diagnosis (Developmental Disability)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','16a-03','Other Chronic illnesses and/or physical disabilities');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-01','Threat to others/ attempted suicide');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-02','Specific symptom of Serious Mental Illness');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-03','Physical/ Sexual Abuse');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-04','Educational');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-05','Occupational/ Employment/ Vocational');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-06','Housing');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-07','Financial');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-08','Legal');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-09','Problems with Relationships');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-10','Problems with substance abuse/ addictions');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-11','Activities of daily living');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','017-12','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-01','General Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-02','Psychiatric Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-03','Other Institution');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-04','CMH&A - Case Management');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-05','CMH&A - ACT Teams');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-06','CMH&A - Counseling and Treatment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-08','CMH&A - Early Intervention');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-09','CMH&A - Crisis Intervention');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-10','CMH&A - Supports within Housing');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-11','CMH&A - Short Term Residential Crisis Support Beds (Enter in CJS subcategory) (Data no longer accepted)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-12','CMH&A - Information and Referral');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-13','CMH&A - Other community mental health and addiction services');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-14','Other community agencies');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-15','Family Physicians');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-16','Psychiatrists');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-17','Mental Health Worker');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-18','Criminal Justice System (CJS) - Police');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-19','Criminal Justice System (CJS) - Courts (includes Court Support & Diversion Programs)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-20','Criminal Justice System (CJS) - Correctional Facilities (includes jails and detention centres)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-21','Criminal Justice System (CJS) - Probation/Parole Officers');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-22','Criminal Justice System (CJS) - Short Term Residential Safe Beds');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-23','Criminal Justice System (CJS) - Source breakdown not available (use this category if above detailed breakdown is not available)');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-24','Self, Family or friend');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','018-25','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','019-01','Completion without referral');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','019-02','Completion with referral');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','019-03','Suicides');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','019-04','Death');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','019-05','Relocation');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','019-06','Withdrawal');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','020-01','Not been hospitalized');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','020-02','Total Number of Episodes');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','020-03','Total Number of Hospitalization Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','020-04','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','020-05','Average age at first psychiatric hospitalization');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','020-06','Average age at the onset of mental illness');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-01','Not been hospitalized');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-02','Total Number of Episodes');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-03','Total Number of Hospitalization Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-04','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-05','Year 1 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-06','Year 2 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-07','Year 3 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-08','Year 4 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-09','Year 5 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-10','Year 6 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-11','Year 7 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-12','Year 8 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-13','Year 9 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','021-14','Year 10 Hospital Days');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-01','Self');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-02','Spouse/partner');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-03','Spouse/partner and others');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-04','Children');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-05','Parents');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-06','Relatives');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-07','Non-relatives');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','022-08','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-01','Self');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-02','Spouse/partner');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-03','Spouse/partner and others');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-04','Children');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-05','Parents');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-06','Relatives');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-07','Non-relatives');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','023-08','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-01','Approved Homes & Homes for Special Care');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-02','Correctional/ Probational Facility');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-03','Domiciliary Hostel');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-04','General Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-05','Psychiatric Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-06','Other Specialty Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-07','No fixed address');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-08','Hostel/Shelter');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-09','Long-Term Care Facility/Nursing Home');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-10','Municipal Non-Profit Housing');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-11','Private Non-Profit Housing');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-12','Private House/ Apt. - SR Owned /Market Rent');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-13','Private House/ Apt. - Other / Subsidized');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-14','Retirement Home/Senior\'s Residence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-15','Rooming/ Boarding House');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-16','Supportive Housing - Congregate Living');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-17','Supportive Housing - Assisted Living');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-18','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','024-19','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','24a-01','Independent');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','24a-02','Assisted/Supported');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','24a-03','Supervised Non-facility');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','24a-04','Supervised Facility');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','24a-05','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-01','Approved Homes & Homes for Special Care');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-02','Correctional/ Probational Facility');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-03','Domiciliary Hostel');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-04','General Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-05','Psychiatric Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-06','Other Specialty Hospital');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-07','No fixed address');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-08','Hostel/Shelter');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-09','Long-Term Care Facility/Nursing Home');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-10','Municipal Non-Profit Housing');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-11','Private Non-Profit Housing');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-12','Private House/ Apt. - SR Owned /Market Rent');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-13','Private House/ Apt. - Other / Subsidized');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-14','Retirement Home/Senior\'s Residence');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-15','Rooming/ Boarding House');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-16','Supportive Housing - Congregate Living');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-17','Supportive Housing - Assisted Living');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-18','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','025-19','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','25a-01','Independent');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','25a-02','Assisted/Supported');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','25a-03','Supervised Non-facility');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','25a-04','Supervised Facility');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','25a-05','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-01','Independent/Competitive');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-02','Assisted/Supportive');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-03','Alternative Businesses');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-04','Sheltered Workshop');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-05','Non-Paid Work Experience');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-06','No employment - Other Activity');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-07','Casual / Sporadic');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-08','No employment of any kind');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','026-09','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-01','Independent/Competitive');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-02','Assisted/Supportive');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-03','Alternative businesses');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-04','Sheltered Workshop');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-05','Non-Paid Work Experience');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-06','No employment - Other Activity');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-07','Casual / Sporadic');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-08','No employment of any kind');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-09','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-10','Number of people participating in the program annually');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-11','Number of people completing the program');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-12','Number of people employed as a result of program participation');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','027-13','Number of people experiencing a vocational crisis who were helped to maintain employment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-01','Not in school');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-02','Elementary/Junior High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-03','Secondary/High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-04','Trade School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-05','Vocational/ Training Centre');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-06','Adult Education');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-07','Community College');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-08','University');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-09','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','028-10','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-01','Not in school');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-02','Elementary/Junior High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-03','Secondary/High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-04','Trade School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-05','Vocational/ Training Centre');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-06','Adult Education');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-07','Community College');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-08','University');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-09','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','029-10','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-01','No formal schooling');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-02','Some Elementary/Junior High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-03','Elementary/Junior High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-04','Some Secondary/High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-05','Secondary/High School');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-06','Some College/University');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-07','College/University');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','29a-08','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-01','Employment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-02','Employment insurance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-03','Pension');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-04','ODSP');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-05','Social Assistance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-06','Disability Assistance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-07','Family');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-08','No source of income');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-09','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','030-10','Unknown or Service Recipient Declined');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-01','Employment');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-02','Employment insurance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-03','Pension');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-04','ODSP');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-05','Social Assistance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-06','Disability Assistance');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-07','Family');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-08','No source of income');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-09','Other');
insert into CdsFormOption (cdsFormVersion,cdsDataCategory,cdsDataCategoryName) values ('4','031-10','Unknown or Service Recipient Declined');


--
-- source init_functional_centres.sql;
--

-- there are too many functional centres, add them as needed / upon request or this list will be hundreds long and unusable by anyone.
-- functional centre "headers" should not be added to this list.
-- the list provided here for now is just the starting point, until we get feed back.
-- see the OHRS appendix 7 for a full list of functional centres

insert into FunctionalCentre values ('725 09 76','COM Case Managament Mental Health');
insert into FunctionalCentre values ('725 40 76 30','COM Res. Mental Health Support within housing');

insert into FunctionalCentre values ('725 10 76 81','COM MH Home Care Psychiatric Rehab');
insert into FunctionalCentre values ('725 10 78 30','COM Clinic/Program - Initial Assessment and Treatment Planning');

insert into FunctionalCentre values ('725 51 76 11','Peer/Self Help Initiatives');

