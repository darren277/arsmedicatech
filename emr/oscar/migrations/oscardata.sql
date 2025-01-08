-- updated to OSCAR 19 spec Feb 2021
--
-- Dumping data for table `AppDefinition`
--


--
-- Dumping data for table `AppUser`
--


--
-- Dumping data for table `AppointmentDxLink`
--


--
-- Dumping data for table `AppointmentSearch`
--


--
-- Dumping data for table `BORNPathwayMapping`
--


--
-- Dumping data for table `BornTransmissionLog`
--


--
-- Dumping data for table `CVCImmunization`
--


--
-- Dumping data for table `CVCImmunizationName`
--


--
-- Dumping data for table `CVCMapping`
--


--
-- Dumping data for table `CVCMedication`
--


--
-- Dumping data for table `CVCMedicationGTIN`
--


--
-- Dumping data for table `CVCMedicationLotNumber`
--


--
-- Dumping data for table `Consent`
--


--
-- Dumping data for table `Contact`
--


--
-- Dumping data for table `ContactSpecialty`
--

INSERT INTO `ContactSpecialty` (`id`, `specialty`, `description`) VALUES (0,'FAMILY PHYSICIAN',NULL),(1,'DERMATOLOGY',NULL),(2,'NEUROLOGY',NULL),(3,'PSYCHIATRY',NULL),(5,'OBSTETRICS & GYNAECOLOGY',NULL),(6,'OPHTHALMOLOGY',NULL),(7,'OTOLARYNGOLOGY',NULL),(8,'GENERAL SURGERY',NULL),(9,'NEUROSURGERY',NULL),(10,'ORTHOPAEDICS',NULL),(11,'PLASTIC SURGERY',NULL),(12,'CARDIO & THORACIC',NULL),(13,'UROLOGY',NULL),(14,'PAEDIATRICS',NULL),(15,'INTERNAL MEDICINE',NULL),(16,'RADIOLOGY',NULL),(17,'LABORATORY PROCEDURES',NULL),(18,'ANAESTHESIA',NULL),(19,'PAEDIATRIC CARDIOLOGY',NULL),(20,'PHYSICAL MEDICINE AND  REHABILITATION',NULL),(21,'PUBLIC HEALTH',NULL),(22,'PHARMACIST',NULL),(23,'OCCUPATIONAL MEDICINE',NULL),(24,'GERIATRIC MEDICINE',NULL),(25,'UNKNOWN',NULL),(26,'PROCEDURAL CARDIOLOGIST',NULL),(28,'EMERGENCY MEDICINE',NULL),(29,'MEDICAL MICROBIOLOGY',NULL),(30,'CHIROPRACTORS',NULL),(31,'NATUROPATHS',NULL),(32,'PHYSICAL THERAPISTS',NULL),(33,'NUCLEAR MEDICINE',NULL),(34,'OSTEOPATHY',NULL),(35,'ORTHOPTIC',NULL),(37,'ORAL SURGEONS',NULL),(38,'PODIATRISTS',NULL),(39,'OPTOMETRIST',NULL),(40,'DENTAL SURGEONS',NULL),(41,'ORAL MEDICINE',NULL),(42,'ORTHODONTISTS',NULL),(43,'MASSAGE PRACTITIONER',NULL),(44,'RHEUMATOLOGY',NULL),(45,'CLINICAL IMMUNIZATION AND ALLERGY',NULL),(46,'MEDICAL GENETICS',NULL),(47,'VASCULAR SURGERY',NULL),(48,'THORACIC SURGERY',NULL);

--
-- Dumping data for table `CtlRelationships`
--

INSERT INTO `CtlRelationships` (`id`, `value`, `label`, `active`, `maleInverse`, `femaleInverse`) VALUES (1,'Mother','Mother',1,'Son','Daughter'),(2,'Father','Father',1,'Son','Daughter'),(3,'Parent','Parent',1,'Son','Daughter'),(4,'Wife','Wife',1,'Husband','Partner'),(5,'Husband','Husband',1,'Partner','Wife'),(6,'Partner','Partner',1,'Partner','Partner'),(7,'Brother','Brother',1,'Brother','Sister'),(8,'Sister','Sister',1,'Brother','Sister'),(9,'Son','Son',1,'Father','Mother'),(10,'Daughter','Daughter',1,'Father','Mother'),(11,'Aunt','Aunt',1,'Nephew','Niece'),(12,'Uncle','Uncle',1,'Nephew','Niece'),(13,'Nephew','Nephew',1,'Uncle','Aunt'),(14,'Niece','Niece',1,'Uncle','Aunt'),(15,'GrandFather','GrandFather',1,'GrandSon','GrandDaughter'),(16,'GrandMother','GrandMother',1,'GrandSon','GrandDaughter'),(17,'Foster Parent','Foster Parent',1,'Foster Son','Foster Daughter'),(18,'Foster Son','Foster Son',1,'Foster Parent','Foster Parent'),(19,'Foster Daughter','Foster Daughter',1,'Foster Parent','Foster Parent'),(20,'Guardian','Guardian',1,NULL,NULL),(21,'Next of Kin','Next of kin',1,NULL,NULL),(22,'Administrative Staff','Administrative Staff',1,NULL,NULL),(23,'Care Giver','Care Giver',1,NULL,NULL),(24,'Power of Attorney','Power of Attorney',1,NULL,NULL),(25,'Insurance','Insurance',1,NULL,NULL),(26,'Guarantor','Guarantor',1,NULL,NULL),(27,'Other','Other',1,NULL,NULL);

--
-- Dumping data for table `DHIRSubmissionLog`
--


--
-- Dumping data for table `DHIRTransactionLog`
--


--
-- Dumping data for table `DemographicContact`
--


--
-- Dumping data for table `Department`
--


--
-- Dumping data for table `DocumentExtraReviewer`
--


--
-- Dumping data for table `DrugDispensing`
--


--
-- Dumping data for table `DrugDispensingMapping`
--


--
-- Dumping data for table `DrugProduct`
--


--
-- Dumping data for table `DrugProductTemplate`
--


--
-- Dumping data for table `EFormDocs`
--


--
-- Dumping data for table `EFormReportTool`
--


--
-- Dumping data for table `Episode`
--


--
-- Dumping data for table `Eyeform`
--


--
-- Dumping data for table `EyeformConsultationReport`
--


--
-- Dumping data for table `EyeformFollowUp`
--


--
-- Dumping data for table `EyeformMacro`
--


--
-- Dumping data for table `EyeformOcularProcedure`
--


--
-- Dumping data for table `EyeformProcedureBook`
--


--
-- Dumping data for table `EyeformSpecsHistory`
--


--
-- Dumping data for table `EyeformTestBook`
--


--
-- Dumping data for table `Facility`
--


--
-- Dumping data for table `FaxClientLog`
--


--
-- Dumping data for table `FlowSheetUserCreated`
--


--
-- Dumping data for table `Flowsheet`
--


--
-- Dumping data for table `HL7HandlerMSHMapping`
--

INSERT INTO `HL7HandlerMSHMapping` (`id`, `hospital_site`, `facility`, `facility_name`, `notes`) VALUES (1,'Lakeridge Health','.','Lakeridge Health Oshawa',NULL),(2,'Lakeridge Health','MHB','Lakeridge Health Bowmanville',NULL),(3,'Lakeridge Health','NDP','Lakeridge Health Port Perry',NULL),(4,'Lakeridge Health','OE.LHC','Lakeridge Health ',NULL),(5,'Lakeridge Health','RAD.OSG','Lakeridge Health',NULL),(6,'Rouge Valley Health System','RVA','Rouge Valley Ajax and Pickering',NULL),(7,'Rouge Valley Health System','RVC','Rouge Valley Centenary',NULL),(8,'Rouge Valley Health System','RAD.APG','Rouge Valley',NULL),(9,'Peterborough Regional Health Centre','PRH','Peterborough Regional Health Centre',NULL),(10,'Peterborough Regional Health Centre','NHC','Northumberland Hills Hospital',NULL),(11,'Peterborough Regional Health Centre','CMH','Campbellford Memorial Hospital',NULL),(12,'Peterborough Regional Health Centre','RAD.PRH','Peterborough/Northumberland/Campbellford',NULL),(13,'The Scarborough Hospitals','GRA','The Scarborough Hospital - Birchmount Campus',NULL),(14,'The Scarborough Hospitals','SCS','The Scarborough Hospital - General Campus',NULL),(15,'The Scarborough Hospitals','RAD.SCS','The Scarborough Hospital',NULL),(16,'Ontario Shores','WHA','Ontario Shores',NULL),(17,'Rouge Valley Health System','APG','Rouge Valley Ajax and Pickering',NULL);

--
-- Dumping data for table `HRMCategory`
--

INSERT INTO `HRMCategory` (`id`, `categoryName`, `subClassNameMnemonic`) VALUES (1,'Oscar HRM Category Uncategorized','DEFAULT'),(2,'Oscar HRM Category CT:ABDW','CT:ABDW'),(3,'Oscar HRM Category RAD:CSP5','RAD:CSP5'),(4,'Oscar HRM Category NM:THYSAN','NM:THYSAN'),(5,'Oscar HRM Category NM:BLDPOL','NM:BLDPOL'),(6,'Oscar HRM Category US:ABDC','US:ABDC'),(7,'Oscar HRM Category US:PELVLT','US:PELVLT'),(8,'Oscar HRM Category RAD:ABD','RAD:ABD'),(9,'Oscar HRM Category RAD:CXR2','RAD:CXR2'),(10,'Oscar HRM Category RAD:ABD2','RAD:ABD2'),(11,'Oscar HRM Category RAD:ANKB','RAD:ANKB'),(12,'Oscar HRM Category RAD:CSP','RAD:CSP'),(13,'Oscar HRM Category RAD:TSP','RAD:TSP'),(14,'Oscar HRM Category RAD:LSP4ER','RAD:LSP4ER'),(15,'Oscar HRM Category RAD:DIGB','RAD:DIGB'),(16,'Oscar HRM Category RAD:ELBB','RAD:ELBB'),(17,'Oscar HRM Category MAM:MAMMOB','MAM:MAMMOB'),(18,'Oscar HRM Category ECHO:ECHO','ECHO:ECHO'),(19,'Oscar HRM Category ECHOWL:ECH0520','ECHOWL:ECH0520'),(20,'Oscar HRM Category ECHO:MDAB','ECHO:MDAB');

--
-- Dumping data for table `HRMDocument`
--


--
-- Dumping data for table `HRMDocumentComment`
--


--
-- Dumping data for table `HRMDocumentSubClass`
--


--
-- Dumping data for table `HRMDocumentToDemographic`
--


--
-- Dumping data for table `HRMDocumentToProvider`
--


--
-- Dumping data for table `HRMProviderConfidentialityStatement`
--


--
-- Dumping data for table `HRMSubClass`
--


--
-- Dumping data for table `HrmLog`
--


--
-- Dumping data for table `HrmLogEntry`
--


--
-- Dumping data for table `ISO36612`
--


--
-- Dumping data for table `Icd9Synonym`
--

INSERT INTO `Icd9Synonym` (`dxCode`, `patientFriendly`, `id`) VALUES ('172','Skin Cancer',1),('173','basal cell carcinoma',2),('2429','Hyperthyroid',3),('2449','Hypothyroid',4),('2564','polycystic ovarian syndrome',5),('2720','Hypercholesterolemia',6),('2722','Mixed hyperlipidemia',7),('2724','Cholesterol',8),('274','Gout',9),('2768','hypokalemia',10),('2778','Retinitis pigmentosa',11),('2901','Dementia',12),('2963','Depression/Mood',13),('2967','Bipolar',14),('3000','Anxiety',15),('3003','OCD',16),('30981','PTSD',17),('3339','Restless leg syndrome',18),('3540','carpal tunnel syndrome',19),('356','Neuropathy/Neuropathic pain',20),('401','Hypertension',21),('4140','CAD',22),('4273','Atrial Fibrilation',23),('453','Deep vein thrombosis',24),('4781','Nasal congestion',25),('4912','COPD',26),('530','Barret\'s esophagus',27),('53081','GERD/Reflux',28),('555','Cholitis/Crohn\'s',29),('5718','Fatty liver',30),('59651','Overactive bladder',31),('600','Enlarged prostate',32),('607','ED/Libido',33),('627','Menopause',34),('6929','Dermatitis/Eczema',35),('6960','Psoriatic arthritis',36),('715','Arthritis/Osteoarthritis',37),('722','degenerative disc disorder',38),('7245','Back Pain',39),('72885','Muscle Spasms',40),('7291','Fibromyalgia',41),('73390','osteopenia',42),('7506','Hiatis Hernia',43),('7804','Dizziness',44),('7805','sleep',45),('78051','Sleep apnea',46),('78052','insomnia',47),('78605','Difficulty breathing',48),('7865','Chest pain',49),('78841','Frequent Urination',50),('8470','whiplash',51),('O54','Herpes',52),('V433','Aortic valve replacement',53),('V450','Cardiac pace maker',54);

--
-- Dumping data for table `Institution`
--


--
-- Dumping data for table `InstitutionDepartment`
--


--
-- Dumping data for table `IntegratorFileLog`
--


--
-- Dumping data for table `IntegratorProgress`
--


--
-- Dumping data for table `IntegratorProgressItem`
--


--
-- Dumping data for table `IssueGroup`
--


--
-- Dumping data for table `IssueGroupIssues`
--


--
-- Dumping data for table `LookupList`
--

INSERT INTO `LookupList` (`id`, `name`, `listTitle`, `description`, `categoryId`, `active`, `createdBy`, `dateCreated`) VALUES (1,'reasonCode',NULL,'Reason Code',NULL,1,'oscar','2021-02-02 18:16:57'),(2,'consultApptInst','Consultation Request Appointment Instructions List','Select list for the consultation appointment instruction select list',NULL,1,'oscar','2021-02-02 18:33:34');

--
-- Dumping data for table `LookupListItem`
--

INSERT INTO `LookupListItem` (`id`, `lookupListId`, `value`, `label`, `displayOrder`, `active`, `createdBy`, `dateCreated`) VALUES (1,1,'Others','Others',99,1,'oscar','2021-02-02 18:16:57'),(2,1,'Contraception','Contraception',1,1,'oscar','2021-02-02 18:16:57'),(3,1,'Counselling','Counselling',2,1,'oscar','2021-02-02 18:16:57'),(4,1,'ECP','ECP',3,1,'oscar','2021-02-02 18:16:57'),(5,1,'Follow-Up','Follow-Up',4,1,'oscar','2021-02-02 18:16:57'),(6,1,'Genital Warts Treatment','Genital Warts Treatment',5,1,'oscar','2021-02-02 18:16:57'),(7,1,'HIV Testing','HIV Testing',6,1,'oscar','2021-02-02 18:16:57'),(8,1,'Immunization','Immunization',7,1,'oscar','2021-02-02 18:16:57'),(9,1,'IUD Removal','IUD Removal',8,1,'oscar','2021-02-02 18:16:57'),(10,1,'Needle Exchange','Needle Exchange',9,1,'oscar','2021-02-02 18:16:57'),(11,1,'PAP Test','PAP Test',10,1,'oscar','2021-02-02 18:16:57'),(12,1,'Pregnancy Test','Pregnancy Test',11,1,'oscar','2021-02-02 18:16:58'),(13,1,'Repeat PAP Test','Repeat PAP Test',12,1,'oscar','2021-02-02 18:16:58'),(14,1,'Results','Results',13,1,'oscar','2021-02-02 18:16:58'),(15,1,'STI Exam','STI Exam',14,1,'oscar','2021-02-02 18:16:58'),(16,1,'STI Prescription/Treatment','STI Prescription/Treatment',15,1,'oscar','2021-02-02 18:16:58'),(17,1,'Therapeutic Abortion Follow-Up','Therapeutic Abortion Follow-Up',16,1,'oscar','2021-02-02 18:16:58'),(18,2,'285708a4-6585-11eb-9a34-484d7ea6bde1','Please reply to sending facility by fax or phone with appointment',1,1,'oscar','2021-02-02 18:33:34');

--
-- Dumping data for table `MyGroupAccessRestriction`
--


--
-- Dumping data for table `OLISQueryLog`
--


--
-- Dumping data for table `OLISResults`
--


--
-- Dumping data for table `ORNCkdScreeningReportLog`
--


--
-- Dumping data for table `ORNPreImplementationReportLog`
--


--
-- Dumping data for table `OscarCode`
--

INSERT INTO `OscarCode` (`id`, `OscarCode`, `description`) VALUES (1,'CKDSCREEN','Ckd Screening');

--
-- Dumping data for table `OscarJob`
--

INSERT INTO `OscarJob` (`id`, `name`, `description`, `oscarJobTypeId`, `cronExpression`, `providerNo`, `enabled`, `updated`, `config`) VALUES (1,'OSCAR Message Review','',1,'0 0/30 * * * *','999998',0,'2021-02-02 13:33:34',NULL),(2,'OSCAR On-Call Clinic',NULL,2,'0 0 4 * * *','999998',0,'2021-02-02 13:33:34',NULL);

--
-- Dumping data for table `OscarJobType`
--

INSERT INTO `OscarJobType` (`id`, `name`, `description`, `className`, `enabled`, `updated`) VALUES (1,'OSCAR MSG REVIEW','Sends OSCAR Messages to Residents Supervisors when charts need to be reviewed','org.oscarehr.jobs.OscarMsgReviewSender',0,'2021-02-02 13:33:34'),(2,'OSCAR ON CALL CLINIC','Notifies MRP if patient seen during on-call clinic','org.oscarehr.jobs.OscarOnCallClinic',0,'2021-02-02 13:33:33');
INSERT INTO `OscarJobType` (`id`, `name`, `description`, `className`, `enabled`, `updated`) VALUES (\N,'DashboardTrending','','org.oscarehr.integration.dashboard.DashboardTrendingJob',1,now());

--
-- Dumping data for table `PHRVerification`
--


--
-- Dumping data for table `PageMonitor`
--


--
-- Dumping data for table `PreventionReport`
--


--
-- Dumping data for table `PreventionsLotNrs`
--


--
-- Dumping data for table `PrintResourceLog`
--


--
-- Dumping data for table `ProductLocation`
--

INSERT INTO `ProductLocation` (`id`, `name`) VALUES (1,'Default');

--
-- Dumping data for table `ProviderPreference`
--

INSERT INTO `ProviderPreference` (`providerNo`, `startHour`, `endHour`, `everyMin`, `myGroupNo`, `colourTemplate`, `newTicklerWarningWindow`, `defaultServiceType`, `defaultCaisiPmm`, `defaultNewOscarCme`, `printQrCodeOnPrescriptions`, `lastUpdated`, `appointmentScreenLinkNameDisplayLength`, `defaultDoNotDeleteBilling`, `defaultDxCode`, `eRxEnabled`, `eRx_SSO_URL`, `eRxUsername`, `eRxPassword`, `eRxFacility`, `eRxTrainingMode`, `encryptedMyOscarPassword`) VALUES ('999998',8,18,15,'.default','deepblue',NULL,NULL,'disabled','disabled',0,'2021-02-02 13:15:47',3,0,NULL,0,NULL,NULL,NULL,NULL,0,NULL);

--
-- Dumping data for table `ProviderPreferenceAppointmentScreenEForm`
--


--
-- Dumping data for table `ProviderPreferenceAppointmentScreenForm`
--


--
-- Dumping data for table `ProviderPreferenceAppointmentScreenQuickLink`
--


--
-- Dumping data for table `RemoteDataLog`
--


--
-- Dumping data for table `RemoteIntegratedDataCopy`
--


--
-- Dumping data for table `RemoteReferral`
--


--
-- Dumping data for table `ResourceStorage`
--


--
-- Dumping data for table `SecurityArchive`
--


--
-- Dumping data for table `SecurityToken`
--


--
-- Dumping data for table `SentToPHRTracking`
--


--
-- Dumping data for table `ServiceAccessToken`
--


--
-- Dumping data for table `ServiceClient`
--


--
-- Dumping data for table `ServiceRequestToken`
--


--
-- Dumping data for table `SurveillanceData`
--


--
-- Dumping data for table `allergies`
--


--
-- Dumping data for table `appointment`
--


--
-- Dumping data for table `appointmentArchive`
--


--
-- Dumping data for table `appointmentType`
--


--
-- Dumping data for table `appointment_status`
--

INSERT INTO `appointment_status` (`id`, `status`, `description`, `color`, `icon`, `active`, `editable`, `short_letter_colour`, `short_letters`) VALUES (1,'t','To Do','#FDFEC7','starbill.gif',1,0,0,'TODO'),(2,'T','Daysheet Printed','#FDFEC7','todo.gif',1,0,0,'DSPrt'),(3,'H','Here','#00ee00','here.gif',1,1,0,'HERE'),(4,'P','Picked','#FFBBFF','picked.gif',1,1,0,'PICK'),(5,'E','Empty Room','#FFFF33','empty.gif',1,1,0,'EmpRm'),(6,'a','Customized 1','#897DF8','1.gif',1,1,0,'CUST1'),(7,'b','Customized 2','#897DF8','2.gif',1,1,0,'CUST2'),(8,'c','Customized 3','#897DF8','3.gif',0,1,0,'CUST3'),(9,'d','Customized 4','#897DF8','4.gif',1,1,0,'CUST4'),(10,'e','Customized 5','#897DF8','5.gif',1,1,0,'CUST5'),(11,'N','No Show','#cccccc','noshow.gif',1,0,0,'NOSHO'),(12,'C','Cancelled','#999999','cancel.gif',1,0,0,'CAN'),(13,'B','Billed','#3ea4e1','billed.gif',1,0,0,'BILL'),(14,'h','Confirmed','#2fcccf','thumb.png',1,0,0,'CONFI');

--
-- Dumping data for table `batchEligibility`
--


--
-- Dumping data for table `billactivity`
--


--
-- Dumping data for table `billcenter`
--


--
-- Dumping data for table `billing`
--


--
-- Dumping data for table `billing_on_3rdPartyAddress`
--


--
-- Dumping data for table `billing_on_item_payment`
--


--
-- Dumping data for table `billing_on_payment`
--


--
-- Dumping data for table `billing_on_transaction`
--


--
-- Dumping data for table `billing_payment_type`
--

INSERT INTO `billing_payment_type` (`id`, `payment_type`) VALUES (1,'CASH'),(2,'CHEQUE'),(3,'VISA'),(4,'MASTERCARD'),(5,'AMEX'),(6,'ELECTRONIC'),(7,'DEBIT');

--
-- Dumping data for table `billingdetail`
--


--
-- Dumping data for table `billinginr`
--


--
-- Dumping data for table `billingperclimit`
--


--
-- Dumping data for table `billingreferral`
--


--
-- Dumping data for table `billingservice`
--


--
-- Dumping data for table `casemgmt_note_ext`
--


--
-- Dumping data for table `casemgmt_note_link`
--


--
-- Dumping data for table `casemgmt_note_lock`
--


--
-- Dumping data for table `clinic`
--

INSERT INTO `clinic` (`clinic_no`, `clinic_name`, `clinic_address`, `clinic_city`, `clinic_postal`, `clinic_phone`, `clinic_fax`, `clinic_location_code`, `status`, `clinic_province`, `clinic_delim_phone`, `clinic_delim_fax`) VALUES (1234,'McMaster Hospital','Hamilton','Hamilton','L0R 4K3','555-555-5555','555-555-5555','444','A','Ontario','','');

--
-- Dumping data for table `clinic_location`
--

INSERT INTO `clinic_location` (`id`, `clinic_location_no`, `clinic_no`, `clinic_location_name`) VALUES (1,'3642',1,'The Wellington Lodge'),(2,'3831',1,'Maternity Centre of Hamilton'),(3,'1994',1,'McMaster University Medical Center'),(4,'1983',1,'Henderson General'),(5,'1985',1,'Hamilton General'),(6,'2003',1,'St. Joseph\"s Hospital'),(7,'0000',1,'Not Applicable'),(8,'1972',1,'Chedoke Hospital'),(9,'3866',1,'Stonechurch Family Health Center'),(10,'3226',1,'Stonechurch Family Health PCN'),(11,'9999',1,'Home Visit');

--
-- Dumping data for table `clinic_nbr`
--

INSERT INTO `clinic_nbr` (`nbr_id`, `nbr_value`, `nbr_string`, `nbr_status`) VALUES (1,'22','R .  M .  A .','A'),(2,'33','AFP Ham Surgery RMA','A'),(3,'98','Bill Directs','A');

--
-- Dumping data for table `config_Immunization`
--

INSERT INTO `config_Immunization` (`setId`, `setName`, `setXmlDoc`, `createDate`, `providerNo`, `archived`) VALUES (1,'Routine Infants & Children','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<immunizationSet headers=\"true\" name=\"Routine Infants &amp; Children\"><columnList><column name=\"2 months\"/><column name=\"4 months\"/><column name=\"6 months\"/><column name=\"12 months\"/><column name=\"18 months\"/><column name=\"4-6 years\"/><column name=\"14-16 years\"/></columnList><rowList><row name=\"DTP+IPV\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"5\"/><cell index=\"6\"/></row><row name=\"Hib\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"5\"/></row><row name=\"MMR\"><cell index=\"4\"/><cell index=\"6\"/></row><row name=\"Td\"><cell index=\"7\"/></row><row name=\"Hep B&#10;(3 doses)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/></row><row name=\"VariVax&#10;(chickenpox)\"><cell index=\"4\"/></row><row name=\"Prevnar&#10;(pneumococcus)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/></row><row name=\"Menjuvate&#10;(menningococcus)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"7\"/></row></rowList></immunizationSet>','2002-07-30','174',1),(2,'Late Infants & Children','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<immunizationSet headers=\"true\" name=\"Late Infants &amp; Children\"><columnList><column name=\"First visit\"/><column name=\"2 months later\"/><column name=\"2 months later\"/><column name=\"6-12 months later\"/><column name=\"4-6 years old\"/><column name=\"14-16 years old\"/></columnList><rowList><row name=\"DTP+IPV\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/></row><row name=\"Hib\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"4\"/></row><row name=\"MMR\"><cell index=\"1\"/></row><row name=\"Td\"><cell index=\"6\"/></row><row name=\"Hep B&#10;(3 doses)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"4\"/></row><row name=\"Varivax&#10;(chickenpox)\"><cell index=\"1\"/></row><row name=\"Prevnar&#10;(pneumococcus)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"4\"/></row><row name=\"Menjuvate&#10;(meningococcus)\"><cell index=\"1\"/><cell index=\"2\"/></row></rowList></immunizationSet>','2002-07-30','174',0),(3,'>7 year old children','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<immunizationSet headers=\"true\" name=\"&gt;7 year old children\"><columnList><column name=\"First visit\"/><column name=\"2 months later\"/><column name=\"6-12 months later\"/><column name=\"10 years later\"/></columnList><rowList><row name=\"dTap\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/></row><row name=\"IPV\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/></row><row name=\"MMR\"><cell index=\"1\"/></row><row name=\"Hep B\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/></row><row name=\"Varicella\"><cell index=\"1\"/></row><row name=\"Meningococcal&#10;Vaccine\"><cell index=\"1\"/></row></rowList></immunizationSet>','2002-07-30','174',0),(4,'Adult','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<immunizationSet headers=\"true\" name=\"Adult\"><columnList><column name=\"Td (Every 10 years)\"/><column name=\"Influenza (yearly)\"/><column name=\"Pneumococcal&#13;&lt;br&gt;(&gt;65 years + risks)\"/><column name=\"MMR(Adults born 1970 or later)\"/><column name=\"Other\"/><column name=\"Other\"/><column name=\"Other\"/></columnList><rowList><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row><row name=\"Date\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/><cell index=\"5\"/><cell index=\"6\"/><cell index=\"7\"/></row></rowList></immunizationSet>','2002-07-30','174',0),(5,'Routine Infants & Children','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<immunizationSet headers=\"true\" name=\"Routine Infants &amp; Children\"><columnList><column name=\"2 months\"/><column name=\"4 months\"/><column name=\"6 months\"/><column name=\"12 months\"/><column name=\"18 months\"/><column name=\"4-6 years\"/><column name=\"14-16 years\"/></columnList><rowList><row name=\"DTP+IPV\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"5\"/><cell index=\"6\"/></row><row name=\"Hib\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"5\"/></row><row name=\"MMR\"><cell index=\"4\"/><cell index=\"6\"/></row><row name=\"Td\"><cell index=\"7\"/></row><row name=\"Hep B (first visit,&#10;1 month, 6 months)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/></row><row name=\"VariVax&#10;(chickenpox)\"><cell index=\"4\"/></row><row name=\"Prevnar&#10;(pneumococcus)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"4\"/></row><row name=\"Menjugate or others&#10;(meningococcus)\"><cell index=\"1\"/><cell index=\"2\"/><cell index=\"3\"/><cell index=\"7\"/></row></rowList></immunizationSet>','2002-07-30','174',0);

--
-- Dumping data for table `consentType`
--

INSERT INTO `consentType` (`id`, `type`, `name`, `description`, `active`, `providerNo`, `remoteEnabled`) VALUES (1,'default_consent_entry','Demonstraton Consent','This is a demonstration consent. Modify the consentType and Consent tables to replace this message with a desired consent description, or to add new consents.',1,NULL,0);

--
-- Dumping data for table `consultResponseDoc`
--


--
-- Dumping data for table `consultationRequestExt`
--


--
-- Dumping data for table `consultationRequestExtArchive`
--


--
-- Dumping data for table `consultationRequests`
--


--
-- Dumping data for table `consultationRequestsArchive`
--


--
-- Dumping data for table `consultationResponse`
--


--
-- Dumping data for table `consultationServices`
--

INSERT INTO `consultationServices` (`serviceId`, `serviceDesc`, `active`) VALUES (53,'Cardiology','1'),(54,'Dermatology','1'),(55,'Neurology','1'),(56,'Radiology','1'),(57,'SEE NOTES','1'),(58,'Referral Doctor','02');

--
-- Dumping data for table `consultdocs`
--


--
-- Dumping data for table `country_codes`
--

INSERT INTO `country_codes` (`id`, `country_name`, `country_id`, `c_locale`) VALUES (1,'AFGHANISTAN','AF','en'),(2,'LAND ISLANDS','AX','en'),(3,'ALBANIA','AL','en'),(4,'ALGERIA','DZ','en'),(5,'AMERICAN SAMOA','AS','en'),(6,'ANDORRA','AD','en'),(7,'ANGOLA','AO','en'),(8,'ANGUILLA','AI','en'),(9,'ANTARCTICA','AQ','en'),(10,'ANTIGUA AND BARBUDA','AG','en'),(11,'ARGENTINA','AR','en'),(12,'ARMENIA','AM','en'),(13,'ARUBA','AW','en'),(14,'AUSTRALIA','AU','en'),(15,'AUSTRIA','AT','en'),(16,'AZERBAIJAN','AZ','en'),(17,'BAHAMAS','BS','en'),(18,'BAHRAIN','BH','en'),(19,'BANGLADESH','BD','en'),(20,'BARBADOS','BB','en'),(21,'BELARUS','BY','en'),(22,'BELGIUM','BE','en'),(23,'BELIZE','BZ','en'),(24,'BENIN','BJ','en'),(25,'BERMUDA','BM','en'),(26,'BHUTAN','BT','en'),(27,'BOLIVIA','BO','en'),(28,'BOSNIA AND HERZEGOVINA','BA','en'),(29,'BOTSWANA','BW','en'),(30,'BOUVET ISLAND','BV','en'),(31,'BRAZIL','BR','en'),(32,'BRITISH INDIAN OCEAN TERRITORY','IO','en'),(33,'BRUNEI DARUSSALAM','BN','en'),(34,'BULGARIA','BG','en'),(35,'BURKINA FASO','BF','en'),(36,'BURUNDI','BI','en'),(37,'CAMBODIA','KH','en'),(38,'CAMEROON','CM','en'),(39,'CANADA','CA','en'),(40,'CAPE VERDE','CV','en'),(41,'CAYMAN ISLANDS','KY','en'),(42,'CENTRAL AFRICAN REPUBLIC','CF','en'),(43,'CHAD','TD','en'),(44,'CHILE','CL','en'),(45,'CHINA','CN','en'),(46,'CHRISTMAS ISLAND','CX','en'),(47,'COCOS (KEELING) ISLANDS','CC','en'),(48,'COLOMBIA','CO','en'),(49,'COMOROS','KM','en'),(50,'CONGO','CG','en'),(51,'CONGO, THE DEMOCRATIC REPUBLIC OF THE','CD','en'),(52,'COOK ISLANDS','CK','en'),(53,'COSTA RICA','CR','en'),(54,'CïTE D IVOIRE','CI','en'),(55,'CROATIA','HR','en'),(56,'CUBA','CU','en'),(57,'CYPRUS','CY','en'),(58,'CZECH REPUBLIC','CZ','en'),(59,'DENMARK','DK','en'),(60,'DJIBOUTI','DJ','en'),(61,'DOMINICA','DM','en'),(62,'DOMINICAN REPUBLIC','DO','en'),(63,'ECUADOR','EC','en'),(64,'EGYPT','EG','en'),(65,'EL SALVADOR','SV','en'),(66,'EQUATORIAL GUINEA','GQ','en'),(67,'ERITREA','ER','en'),(68,'ESTONIA','EE','en'),(69,'ETHIOPIA','ET','en'),(70,'FALKLAND ISLANDS (MALVINAS)','FK','en'),(71,'FAROE ISLANDS','FO','en'),(72,'FIJI','FJ','en'),(73,'FINLAND','FI','en'),(74,'FRANCE','FR','en'),(75,'FRENCH GUIANA','GF','en'),(76,'FRENCH POLYNESIA','PF','en'),(77,'FRENCH SOUTHERN TERRITORIES','TF','en'),(78,'GABON','GA','en'),(79,'GAMBIA','GM','en'),(80,'GEORGIA','GE','en'),(81,'GERMANY','DE','en'),(82,'GHANA','GH','en'),(83,'GIBRALTAR','GI','en'),(84,'GREECE','GR','en'),(85,'GREENLAND','GL','en'),(86,'GRENADA','GD','en'),(87,'GUADELOUPE','GP','en'),(88,'GUAM','GU','en'),(89,'GUATEMALA','GT','en'),(90,'GUERNSEY','GG','en'),(91,'GUINEA','GN','en'),(92,'GUINEA-BISSAU','GW','en'),(93,'GUYANA','GY','en'),(94,'HAITI','HT','en'),(95,'HEARD ISLAND AND MCDONALD ISLANDS','HM','en'),(96,'HOLY SEE (VATICAN CITY STATE)','VA','en'),(97,'HONDURAS','HN','en'),(98,'HONG KONG','HK','en'),(99,'HUNGARY','HU','en'),(100,'ICELAND','IS','en'),(101,'INDIA','IN','en'),(102,'INDONESIA','ID','en'),(103,'IRAN, ISLAMIC REPUBLIC OF','IR','en'),(104,'IRAQ','IQ','en'),(105,'IRELAND','IE','en'),(106,'ISLE OF MAN','IM','en'),(107,'ISRAEL','IL','en'),(108,'ITALY','IT','en'),(109,'JAMAICA','JM','en'),(110,'JAPAN','JP','en'),(111,'JERSEY','JE','en'),(112,'JORDAN','JO','en'),(113,'KAZAKHSTAN','KZ','en'),(114,'KENYA','KE','en'),(115,'KIRIBATI','KI','en'),(116,'KOREA, DEMOCRATIC PEOPLES REPUBLIC OF','KP','en'),(117,'KOREA, REPUBLIC OF','KR','en'),(118,'KUWAIT','KW','en'),(119,'KYRGYZSTAN','KG','en'),(120,'LAO PEOPLES DEMOCRATIC REPUBLIC','LA','en'),(121,'LATVIA','LV','en'),(122,'LEBANON','LB','en'),(123,'LESOTHO','LS','en'),(124,'LIBERIA','LR','en'),(125,'LIBYAN ARAB JAMAHIRIYA','LY','en'),(126,'LIECHTENSTEIN','LI','en'),(127,'LITHUANIA','LT','en'),(128,'LUXEMBOURG','LU','en'),(129,'MACAO','MO','en'),(130,'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF','MK','en'),(131,'MADAGASCAR','MG','en'),(132,'MALAWI','MW','en'),(133,'MALAYSIA','MY','en'),(134,'MALDIVES','MV','en'),(135,'MALI','ML','en'),(136,'MALTA','MT','en'),(137,'MARSHALL ISLANDS','MH','en'),(138,'MARTINIQUE','MQ','en'),(139,'MAURITANIA','MR','en'),(140,'MAURITIUS','MU','en'),(141,'MAYOTTE','YT','en'),(142,'MEXICO','MX','en'),(143,'MICRONESIA, FEDERATED STATES OF','FM','en'),(144,'MOLDOVA','MD','en'),(145,'MONACO','MC','en'),(146,'MONGOLIA','MN','en'),(147,'MONTENEGRO','ME','en'),(148,'MONTSERRAT','MS','en'),(149,'MOROCCO','MA','en'),(150,'MOZAMBIQUE','MZ','en'),(151,'MYANMAR','MM','en'),(152,'NAMIBIA','NA','en'),(153,'NAURU','NR','en'),(154,'NEPAL','NP','en'),(155,'NETHERLANDS','NL','en'),(156,'NETHERLANDS ANTILLES','AN','en'),(157,'NEW CALEDONIA','NC','en'),(158,'NEW ZEALAND','NZ','en'),(159,'NICARAGUA','NI','en'),(160,'NIGER','NE','en'),(161,'NIGERIA','NG','en'),(162,'NIUE','NU','en'),(163,'NORFOLK ISLAND','NF','en'),(164,'NORTHERN MARIANA ISLANDS','MP','en'),(165,'NORWAY','NO','en'),(166,'OMAN','OM','en'),(167,'PAKISTAN','PK','en'),(168,'PALAU','PW','en'),(169,'PALESTINIAN TERRITORY, OCCUPIED','PS','en'),(170,'PANAMA','PA','en'),(171,'PAPUA NEW GUINEA','PG','en'),(172,'PARAGUAY','PY','en'),(173,'PERU','PE','en'),(174,'PHILIPPINES','PH','en'),(175,'PITCAIRN','PN','en'),(176,'POLAND','PL','en'),(177,'PORTUGAL','PT','en'),(178,'PUERTO RICO','PR','en'),(179,'QATAR','QA','en'),(180,'RƒUNION','RE','en'),(181,'ROMANIA','RO','en'),(182,'RUSSIAN FEDERATION','RU','en'),(183,'RWANDA','RW','en'),(184,'SAINT BARTHƒLEMY','BL','en'),(185,'SAINT HELENA','SH','en'),(186,'SAINT KITTS AND NEVIS','KN','en'),(187,'SAINT LUCIA','LC','en'),(188,'SAINT MARTIN','MF','en'),(189,'SAINT PIERRE AND MIQUELON','PM','en'),(190,'SAINT VINCENT AND THE GRENADINES','VC','en'),(191,'SAMOA','WS','en'),(192,'SAN MARINO','SM','en'),(193,'SAO TOME AND PRINCIPE','ST','en'),(194,'SAUDI ARABIA','SA','en'),(195,'SENEGAL','SN','en'),(196,'SERBIA','RS','en'),(197,'SEYCHELLES','SC','en'),(198,'SIERRA LEONE','SL','en'),(199,'SINGAPORE','SG','en'),(200,'SLOVAKIA','SK','en'),(201,'SLOVENIA','SI','en'),(202,'SOLOMON ISLANDS','SB','en'),(203,'SOMALIA','SO','en'),(204,'SOUTH AFRICA','ZA','en'),(205,'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS','GS','en'),(206,'SPAIN','ES','en'),(207,'SRI LANKA','LK','en'),(208,'SUDAN','SD','en'),(209,'SURINAME','SR','en'),(210,'SVALBARD AND JAN MAYEN','SJ','en'),(211,'SWAZILAND','SZ','en'),(212,'SWEDEN','SE','en'),(213,'SWITZERLAND','CH','en'),(214,'SYRIAN ARAB REPUBLIC','SY','en'),(215,'TAIWAN, PROVINCE OF CHINA','TW','en'),(216,'TAJIKISTAN','TJ','en'),(217,'TANZANIA, UNITED REPUBLIC OF','TZ','en'),(218,'THAILAND','TH','en'),(219,'TIMOR-LESTE','TL','en'),(220,'TOGO','TG','en'),(221,'TOKELAU','TK','en'),(222,'TONGA','TO','en'),(223,'TRINIDAD AND TOBAGO','TT','en'),(224,'TUNISIA','TN','en'),(225,'TURKEY','TR','en'),(226,'TURKMENISTAN','TM','en'),(227,'TURKS AND CAICOS ISLANDS','TC','en'),(228,'TUVALU','TV','en'),(229,'UGANDA','UG','en'),(230,'UKRAINE','UA','en'),(231,'UNITED ARAB EMIRATES','AE','en'),(232,'UNITED KINGDOM','GB','en'),(233,'UNITED STATES','US','en'),(234,'UNITED STATES MINOR OUTLYING ISLANDS','UM','en'),(235,'URUGUAY','UY','en'),(236,'UZBEKISTAN','UZ','en'),(237,'VANUATU','VU','en'),(238,'VATICAN CITY STATE','VA','en'),(239,'VENEZUELA','VE','en'),(240,'VIET NAM','VN','en'),(241,'VIRGIN ISLANDS, BRITISH','VG','en'),(242,'VIRGIN ISLANDS, U.S.','VI','en'),(243,'WALLIS AND FUTUNA','WF','en'),(244,'WESTERN SAHARA','EH','en'),(245,'YEMEN','YE','en'),(246,'ZAMBIA','ZM','en'),(247,'ZIMBABWE','ZW','en');

--
-- Dumping data for table `criteria`
--


--
-- Dumping data for table `criteria_selection_option`
--


--
-- Dumping data for table `criteria_type`
--

INSERT INTO `criteria_type` (`CRITERIA_TYPE_ID`, `FIELD_NAME`, `FIELD_TYPE`, `DEFAULT_VALUE`, `ACTIVE`, `WL_PROGRAM_ID`, `CAN_BE_ADHOC`) VALUES (1,'Agency','select_multiple',NULL,1,1,0),(2,'Age','select_one',NULL,1,1,0),(3,'Area','select_multiple',NULL,1,1,0),(4,'Serious and Persistent Mental Illness','select_one',NULL,1,1,0),(5,'Serious and Persistent Mental Illness Diagnosis','select_multiple',NULL,1,1,0),(6,'Serious and Persistent Mental Illness Hospitalization','number','0',1,1,0),(7,'Type of Program','select_multiple',NULL,1,1,0),(8,'Referral Source','select_one',NULL,1,1,0),(9,'Legal History','select_multiple',NULL,1,1,0),(10,'Residence','select_one',NULL,1,1,0),(11,'Other Health Issues','select_multiple',NULL,1,1,0),(12,'Language','select_multiple',NULL,1,1,0),(13,'Gender','select_one',NULL,1,1,0),(14,'Gender','select_one',NULL,1,2,0),(15,'Homeless','select_one',NULL,1,2,0),(16,'Mental health diagnosis','select_multiple',NULL,1,2,0),(17,'Housing type','select_one',NULL,1,2,0),(18,'Referral source','select_one',NULL,1,2,0),(19,'Support level','select_one',NULL,1,2,0),(20,'Geographic location','select_one',NULL,1,2,0),(21,'Age category','select_one',NULL,1,2,0),(22,'Current involvement with Criminal Justice system','select_one',NULL,1,2,0),(23,'SHPPSU criteria','select_one',NULL,1,2,0),(24,'Accessible unit','select_one',NULL,1,2,0);

--
-- Dumping data for table `criteria_type_option`
--

INSERT INTO `criteria_type_option` (`OPTION_ID`, `CRITERIA_TYPE_ID`, `DISPLAY_ORDER_NUMBER`, `OPTION_LABEL`, `OPTION_VALUE`, `RANGE_START_VALUE`, `RANGE_END_VALUE`) VALUES (1,2,1,'Youth – 14 – 22',NULL,14,22),(2,2,2,'Youth  - 16-24',NULL,16,24),(3,3,1,'North York','North York',NULL,NULL),(4,3,2,'Scarborough','Scarborough',NULL,NULL),(5,3,3,'East York','East York',NULL,NULL),(6,3,4,'Old City of York','Old City of York',NULL,NULL),(7,3,5,'North Etobicoke','North Etobicoke',NULL,NULL),(8,3,6,'South Etobicoke','South Etobicoke',NULL,NULL),(9,3,7,'Downtown Toronto','Downtown Toronto',NULL,NULL),(10,3,8,'East of Yonge','East of Yonge',NULL,NULL),(11,3,9,'West of Yonge','West of Yonge',NULL,NULL),(12,3,10,'Toronto','Toronto',NULL,NULL),(13,2,3,'16 Years of age or older',NULL,16,120),(14,2,4,'18 years of age or older',NULL,18,120),(15,4,1,'Formal Diagnosis','Formal Diagnosis',NULL,NULL),(16,4,2,'No formal Diagnosis','No formal Diagnosis',NULL,NULL),(19,5,1,'Test diagnosis 1','Test diagnosis 1',NULL,NULL),(20,5,2,'Test diagnosis 2','Test diagnosis 2',NULL,NULL),(21,7,1,'Long-Term Case Management','Long-Term Case Management',NULL,NULL),(22,7,2,'Short-term case management','Short-term case management',NULL,NULL),(23,7,3,'Emergency Department Diversion Program','Emergency Department Diversion Program',NULL,NULL),(24,7,4,'Assertive Community Treatment Team','Assertive Community Treatment Team',NULL,NULL),(25,7,5,'Mental Health Outreach Program','Mental Health Outreach Program',NULL,NULL),(26,7,6,'Language Specific Service (Across Boundaries, CRCT, WRAP, Pathways, Passages)','Language Specific Service',NULL,NULL),(27,7,7,'Youth Programs','Youth Programs',NULL,NULL),(28,7,8,'Early Intervention Programs','Early Intervention Programs',NULL,NULL),(29,7,9,'Mental Health Prevention Program (short-term case management)','Mental Health Prevention Program (short-term case management)',NULL,NULL),(30,7,10,'Seniors Case Management','Seniors Case Management',NULL,NULL),(31,7,11,'TCAT (Addictions case management)','TCAT (Addictions case management)',NULL,NULL),(32,7,12,'CATCH','CATCH',NULL,NULL),(33,7,13,'CATCH - ED','CATCH - ED',NULL,NULL),(34,1,1,'Across Boundaries','Across Boundaries',NULL,NULL),(35,1,2,'Bayview Community Services','Bayview Community Services',NULL,NULL),(36,8,1,'Organizational Referral Source','Organizational Referral Source',NULL,NULL),(37,8,2,'Accredited Professional (i.e. private psychiatrist, family doctor etc)','Accredited Professional',NULL,NULL),(38,8,3,' Self',' Self',NULL,NULL),(39,8,4,'Family/Friend','Family/Friend',NULL,NULL),(40,8,5,'Hospital (List of all hospitals)','Hospital',NULL,NULL),(41,8,6,'Ontario Review Board','Ontario Review Board',NULL,NULL),(42,8,7,'Alternative Access Route (i.e. internal referral, pre-existing agreement, alternate access route)','Alternative Access Route',NULL,NULL),(43,9,1,'Test legal history 1','Test legal history 1',NULL,NULL),(44,9,2,'Test legal history 2','Test legal history 2',NULL,NULL),(45,10,1,'Housed','Housed',NULL,NULL),(46,10,2,'Homeless','Homeless',NULL,NULL),(47,10,3,'Transitional','Transitional',NULL,NULL),(48,11,1,'Concurrent Disorder','Concurrent Disorder',NULL,NULL),(49,11,2,'Dual Diagnosis','Dual Diagnosis',NULL,NULL),(50,11,3,'Acquired brain injury','Acquired brain injury',NULL,NULL),(51,11,4,'Psycho-geriatric  issues','Psycho-geriatric  issues',NULL,NULL),(52,12,1,'English','English',NULL,NULL),(53,12,2,'French','French',NULL,NULL),(54,12,3,'Other','Other',NULL,NULL),(55,13,1,'Male','Male',NULL,NULL),(56,13,2,'Female','Female',NULL,NULL),(57,14,1,'Male','Male',NULL,NULL),(58,14,2,'Female','Female',NULL,NULL),(59,15,1,'Homeless','Homeless',NULL,NULL),(60,15,2,'At risk','At risk',NULL,NULL),(61,15,3,'Housed','Housed',NULL,NULL),(62,16,1,'Formal Diagnosis','Formal Diagnosis',NULL,NULL),(63,16,2,'No formal Diagnosis','No formal Diagnosis',NULL,NULL),(65,17,1,'Shared','Shared',NULL,NULL),(66,17,2,'Independent','Independent',NULL,NULL),(67,18,1,'Organizational Referral Source','Organizational Referral Source',NULL,NULL),(68,18,2,'Accredited Professional (i.e. private psychiatrist, family doctor etc)','Accredited Professional',NULL,NULL),(69,19,1,'Test level 1','Test level 1',NULL,NULL),(70,19,2,'Test level 2','Test level 2',NULL,NULL),(75,22,1,'Test involvement 1','Test involvement 1',NULL,NULL),(76,22,2,'Test involvement 2','Test involvement 2',NULL,NULL),(77,23,1,'Test SHPPSU criteria 1','Test SHPPSU criteria 1',NULL,NULL),(78,23,2,'Test SHPPSU criteria 2','Test SHPPSU criteria 2',NULL,NULL),(79,24,1,'Accessible unit required','Accessible unit required',NULL,NULL),(80,24,2,'Accessible unit not required','Accessible unit not required',NULL,NULL),(82,1,3,'CMHA (Toronto East)','CMHA (Toronto East)',NULL,NULL),(83,1,4,'CMHA (Toronto West)','CMHA (Toronto West)',NULL,NULL),(84,1,5,'COTA Health','COTA Health',NULL,NULL),(85,1,6,'Community Resource Connections of Toronto','Community Resource Connections of Toronto',NULL,NULL),(86,1,7,'Griffin Centre & Community Support Network','Griffin Centre & Community Support Network',NULL,NULL),(87,1,8,'North York General Hospital','North York General Hospital',NULL,NULL),(88,1,9,'Reconnect Mental Health Services','Reconnect Mental Health Services',NULL,NULL),(89,1,10,'Saint Elizabeth Health Care','Saint Elizabeth Health Care',NULL,NULL),(90,1,11,'Scarborough Hospital','Scarborough Hospital',NULL,NULL),(91,1,12,'Sunnybrook Hospital','Sunnybrook Hospital',NULL,NULL),(92,1,13,'Toronto North Support Services','Toronto North Support Services',NULL,NULL),(93,13,3,'Transgender','Transgender',NULL,NULL),(94,13,4,'Transsexual','Transsexual',NULL,NULL),(95,13,5,'Other','Other',NULL,NULL),(96,14,3,'Transgender','Transgender',NULL,NULL),(97,14,4,'Transsexual','Transsexual',NULL,NULL),(98,14,5,'Other','Other',NULL,NULL),(99,18,3,' Self',' Self',NULL,NULL),(100,18,4,'Family/Friend','Family/Friend',NULL,NULL),(101,18,5,'Hospital (List of all hospitals)','Hospital',NULL,NULL),(102,18,6,'Ontario Review Board','Ontario Review Board',NULL,NULL),(103,18,7,'Alternative Access Route (i.e. internal referral, pre-existing agreement, alternate access route)','Alternative Access Route',NULL,NULL),(104,20,1,'West End of Toronto (Bathurst to Islington, Lawrence to Lakeshore) ','West End of Toronto',NULL,NULL),(105,20,1,'East End of Toronto (Don Valley to Victoria Park, Lawrence to Lakeshore)','East End of Toronto',NULL,NULL),(106,20,1,'Downtown Core of Toronto (Bathurst to Don Valley, Lawrence to Lakeshore)','Downtown Core of Toronto',NULL,NULL),(107,20,1,'North York East (North of Lawrence, East of Yonge to Victoria Park) ','North York East',NULL,NULL),(108,20,1,'North York West (North of Lawrence, West of Yonge to Islington)','North York West',NULL,NULL),(109,20,1,'Etobicoke (West of Islington) ','Etobicoke',NULL,NULL),(110,20,1,'Scarborough (East of Victoria Park)','Scarborough',NULL,NULL),(111,21,1,'Youth – 14 – 22',NULL,14,22),(112,21,2,'Youth  - 16-24',NULL,16,24),(113,21,3,'16 Years of age or older',NULL,16,120),(114,21,4,'18 years of age or older',NULL,18,120);

--
-- Dumping data for table `cssStyles`
--


--
-- Dumping data for table `ctl_billingservice`
--


--
-- Dumping data for table `ctl_billingservice_premium`
--


--
-- Dumping data for table `ctl_diagcode`
--


--
-- Dumping data for table `ctl_doc_class`
--

INSERT INTO `ctl_doc_class` (`id`, `reportclass`, `subclass`) VALUES (1,'Diagnostic Imaging Report','Abdomen X-Ray'),(2,'Diagnostic Imaging Report','Barium Enema'),(3,'Diagnostic Imaging Report','Bone Densitometry'),(4,'Diagnostic Imaging Report','Bone Scan'),(5,'Diagnostic Imaging Report','Brain Scan'),(6,'Diagnostic Imaging Report','Carotid Angiography'),(7,'Diagnostic Imaging Report','Carotid Doppler Ultrasound'),(8,'Diagnostic Imaging Report','Cervical Spine X-Ray'),(9,'Diagnostic Imaging Report','Chest X-Ray'),(10,'Diagnostic Imaging Report','Coronary Angiography'),(11,'Diagnostic Imaging Report','CT Scan Body'),(12,'Diagnostic Imaging Report','CT Scan Head'),(13,'Diagnostic Imaging Report','Echocardiogram'),(14,'Diagnostic Imaging Report','ERCP X-Ray'),(15,'Diagnostic Imaging Report','Hysterosalpingogram'),(16,'Diagnostic Imaging Report','IVP'),(17,'Diagnostic Imaging Report','Liver-Spleen Scan'),(18,'Diagnostic Imaging Report','Lumbar Spine X-Ray'),(19,'Diagnostic Imaging Report','Lung Scan'),(20,'Diagnostic Imaging Report','Mammogram'),(21,'Diagnostic Imaging Report','Misc. CT Scan'),(22,'Diagnostic Imaging Report','Misc. MRI Scan'),(23,'Diagnostic Imaging Report','Misc. Nuclear Scan'),(24,'Diagnostic Imaging Report','Misc. Ultrasound'),(25,'Diagnostic Imaging Report','Misc. X-Ray'),(26,'Diagnostic Imaging Report','MRI Scan Body'),(27,'Diagnostic Imaging Report','MRI Scan Head'),(28,'Diagnostic Imaging Report','Myelogram'),(29,'Diagnostic Imaging Report','Myoview)'),(30,'Diagnostic Imaging Report','Other Angiography'),(31,'Diagnostic Imaging Report','Retinal Angiography'),(32,'Diagnostic Imaging Report','Retinal Tomograph'),(33,'Diagnostic Imaging Report','Sestamibi'),(34,'Diagnostic Imaging Report','Sonohistogram'),(35,'Diagnostic Imaging Report','Stress Heart Scan (Thallium'),(36,'Diagnostic Imaging Report','UGI with Small Bowel'),(37,'Diagnostic Imaging Report','Ultrasound Abdomen'),(38,'Diagnostic Imaging Report','Ultrasound Breast'),(39,'Diagnostic Imaging Report','Ultrasound Obstetrical'),(40,'Diagnostic Imaging Report','Ultrasound Pelvis'),(41,'Diagnostic Imaging Report','Ultrasound Thyroid'),(42,'Diagnostic Imaging Report','Upper GI Series'),(43,'Diagnostic Imaging Report','Venous Doppler Ultrasound'),(44,'Diagnostic Test Report','Ambulatory BP Monitoring'),(45,'Diagnostic Test Report','Arterial Segmental Pressures (ABI)'),(46,'Diagnostic Test Report','Audiogram'),(47,'Diagnostic Test Report','Bronchoscopy'),(48,'Diagnostic Test Report','Colonoscopy'),(49,'Diagnostic Test Report','Colposcopy'),(50,'Diagnostic Test Report','Cystoscopy'),(51,'Diagnostic Test Report','Dobutamine)'),(52,'Diagnostic Test Report','ECG'),(53,'Diagnostic Test Report','EEG'),(54,'Diagnostic Test Report','EGD-oscopy'),(55,'Diagnostic Test Report','EMG'),(56,'Diagnostic Test Report','Holter Monitor'),(57,'Diagnostic Test Report','Loop Recorder'),(58,'Diagnostic Test Report','Mantoux Test'),(59,'Diagnostic Test Report','Misc. Diagnostic Test'),(60,'Diagnostic Test Report','Pap Test Report'),(61,'Diagnostic Test Report','Persantine'),(62,'Diagnostic Test Report','Pulmonary Function Testing'),(63,'Diagnostic Test Report','Sigmoidoscopy'),(64,'Diagnostic Test Report','Sleep Study'),(65,'Diagnostic Test Report','Stress Test (Exercise'),(66,'Diagnostic Test Report','Urodynamic Testing'),(67,'Cardio Respiratory Report','Echocardiography Bubble Study'),(68,'Cardio Respiratory Report','Pericardiocentesis'),(69,'Cardio Respiratory Report','Echocardiography Esophageal'),(70,'Other Letter','Authorization from Patient'),(71,'Other Letter','Consent from Patient'),(72,'Other Letter','Disability Report'),(73,'Other Letter','Letter from Insurance Company'),(74,'Other Letter','Letter from Lawyer'),(75,'Other Letter','Letter from Patient'),(76,'Other Letter','Letter from WSIB'),(77,'Other Letter','Living Will'),(78,'Other Letter','Miscellaneous Letter'),(79,'Other Letter','Power of Attorney for Health Care'),(80,'Consultant ReportA','Allergy & Immunology'),(81,'Consultant ReportA','Anaesthesiology'),(82,'Consultant ReportA','Audiology'),(83,'Consultant ReportA','Cardiology'),(84,'Consultant ReportA','Cardiovascular Surgery'),(85,'Consultant ReportA','Chiropody / Podiatry'),(86,'Consultant ReportA','Chiropractic'),(87,'Consultant ReportA','Clinical Biochemistry'),(88,'Consultant ReportA','Dentistry'),(89,'Consultant ReportA','Dermatology'),(90,'Consultant ReportA','Diagnostic Radiology'),(91,'Consultant ReportA','Dietitian'),(92,'Consultant ReportA','Emergency Medicine'),(93,'Consultant ReportA','Emergency Physician'),(94,'Consultant ReportA','Endocrinology'),(95,'Consultant ReportA','Family Practice'),(96,'Consultant ReportA','Gastroenterology'),(97,'Consultant ReportA','General Surgery'),(98,'Consultant ReportA','Genetics'),(99,'Consultant ReportA','Geriatrics'),(100,'Consultant ReportA','Hematology'),(101,'Consultant ReportA','Hospitalis'),(102,'Consultant ReportA','Infectious Disease'),(103,'Consultant ReportA','Internal Medicine'),(104,'Consultant ReportA','Kinesiology'),(105,'Consultant ReportA','Microbiology'),(106,'Consultant ReportA','Midwifery'),(107,'Consultant ReportA','Naturopathy'),(108,'Consultant ReportA','Neonatology'),(109,'Consultant ReportA','Nephrology'),(110,'Consultant ReportA','Neurology'),(111,'Consultant ReportA','Neurosurgery'),(112,'Consultant ReportA','Nuclear Medicine'),(113,'Consultant ReportA','Nurse Practitioner'),(114,'Consultant ReportA','Nursing'),(115,'Consultant ReportA','Obstetrics & Gynecology'),(116,'Consultant ReportA','Occupational Therapy'),(117,'Consultant ReportA','On-Call Nurse'),(118,'Consultant ReportA','On-Call Physician'),(119,'Consultant ReportA','Oncology / Chemotherapy'),(120,'Consultant ReportA','Ophthalmology'),(121,'Consultant ReportA','Optometry'),(122,'Consultant ReportA','Oral Surgery'),(123,'Consultant ReportA','Orthopedic Surgery'),(124,'Consultant ReportA','Osteopathy'),(125,'Consultant ReportA','Other Consultant ReportAnt'),(126,'Consultant ReportA','Other Therapy'),(127,'Consultant ReportA','Otolaryngology (ENT)'),(128,'Consultant ReportA','Paediatrics'),(129,'Consultant ReportA','Palliative Care'),(130,'Consultant ReportA','Pathology'),(131,'Consultant ReportA','Pharmacology'),(132,'Consultant ReportA','Physical Medicine'),(133,'Consultant ReportA','Physiotherapy'),(134,'Consultant ReportA','Plastic Surgery'),(135,'Consultant ReportA','Psychiatry'),(136,'Consultant ReportA','Psychology'),(137,'Consultant ReportA','Respiratory Technology'),(138,'Consultant ReportA','Respirology'),(139,'Consultant ReportA','Rheumatology'),(140,'Consultant ReportA','Social Work'),(141,'Consultant ReportA','Speech Therapy'),(142,'Consultant ReportA','Sports Medicine'),(143,'Consultant ReportA','Therapeutic Radiology'),(144,'Consultant ReportA','Thoracic Surgery'),(145,'Consultant ReportA','Urgent Care/Walk-In Clinic Physician'),(146,'Consultant ReportA','Uro-Gynecology'),(147,'Consultant ReportA','Urology'),(148,'Consultant ReportA','Vascular Surgery'),(149,'Consultant ReportB','Admission History'),(150,'Consultant ReportB','Consultant ReportAtion'),(151,'Consultant ReportB','Discharge Summary'),(152,'Consultant ReportB','Encounter Report'),(153,'Consultant ReportB','Operative Report'),(154,'Consultant ReportB','Progress Report');

--
-- Dumping data for table `ctl_doctype`
--

INSERT INTO `ctl_doctype` (`id`, `module`, `doctype`, `status`) VALUES (1,'demographic','lab','A'),(2,'demographic','consult','A'),(3,'demographic','insurance','A'),(4,'demographic','legal','A'),(5,'demographic','oldchart','A'),(6,'demographic','radiology','A'),(7,'demographic','pathology','A'),(8,'demographic','others','A'),(9,'demographic','photo','A'),(10,'provider','resource','A'),(11,'provider','desktop','A'),(12,'provider','handout','A'),(13,'provider','forms','A'),(14,'provider','others','A'),(15,'provider','share','A'),(16,'provider','photo','A'),(17,'provider','invoice letterhead','A'),(18,'demographic','econsult','A');

--
-- Dumping data for table `ctl_document`
--

INSERT INTO `ctl_document` (`module`, `module_id`, `document_no`, `status`) VALUES ('provider',999998,4953,'A'),('provider',999998,4954,'H'),('demographic',2147483647,4955,'A');

--
-- Dumping data for table `ctl_frequency`
--

INSERT INTO `ctl_frequency` (`freqid`, `freqcode`, `dailymin`, `dailymax`) VALUES (1,'OD','1','1'),(2,'BID','2','2'),(3,'TID','3','3'),(4,'QID','4','4'),(5,'Q1H','24','24'),(6,'Q2H','12','12'),(7,'Q1-2H','12','24'),(8,'Q3-4H','6','8'),(9,'Q4H','6','6'),(10,'Q4-6H','4','6'),(11,'Q6H','4','4'),(12,'Q8H','3','3'),(13,'Q12H','2','2'),(14,'QAM','1','1'),(15,'QPM','1','1'),(16,'QHS','1','1'),(17,'Q1Week','1/7','1/7'),(18,'Q2Week','1/14','1/14'),(19,'Q1Month','1/30','1/30'),(20,'Q3Month','1/90','1/90');

--
-- Dumping data for table `ctl_specialinstructions`
--

INSERT INTO `ctl_specialinstructions` (`id`, `description`) VALUES (1,'as needed'),(2,'as needed for pain'),(3,'on an empty stomach'),(4,'until gone'),(5,'before meals'),(6,'after meals'),(7,'with meals'),(8,'before meals and at bedtime'),(9,'as directed'),(10,'in the morning'),(11,'in the evening'),(12,'at bedtime'),(13,'as needed for pain or itching'),(14,'as needed for fever'),(15,'as needed for wheezing'),(16,'while awake'),(17,'1 hour before or 2 hours after'),(18,'with food'),(19,'Apply to affected areas'),(20,'Apply sparingly'),(21,'Insert in left ear'),(22,'Insert in right ear'),(23,'Insert in both ears'),(24,'Insert in left eye'),(25,'Insert in right eye'),(26,'Insert in both eyes');

--
-- Dumping data for table `dashboard`
--


--
-- Dumping data for table `dataExport`
--


--
-- Dumping data for table `default_issue`
--


--
-- Dumping data for table `demographic`
--


--
-- Dumping data for table `demographicArchive`
--


--
-- Dumping data for table `demographicExt`
--


--
-- Dumping data for table `demographicExtArchive`
--


--
-- Dumping data for table `demographicPharmacy`
--


--
-- Dumping data for table `demographicQueryFavourites`
--


--
-- Dumping data for table `demographicSets`
--


--
-- Dumping data for table `demographic_merged`
--


--
-- Dumping data for table `demographicaccessory`
--


--
-- Dumping data for table `demographiccust`
--


--
-- Dumping data for table `demographiccustArchive`
--


--
-- Dumping data for table `demographicstudy`
--


--
-- Dumping data for table `desannualreviewplan`
--


--
-- Dumping data for table `desaprisk`
--


--
-- Dumping data for table `diagnosticcode`
--


--
-- Dumping data for table `diseases`
--


--
-- Dumping data for table `doc_category`
--


--
-- Dumping data for table `doc_manager`
--


--
-- Dumping data for table `document`
--


--
-- Dumping data for table `documentDescriptionTemplate`
--

INSERT INTO `documentDescriptionTemplate` (`id`, `doctype`, `description`, `descriptionShortcut`, `provider_no`, `lastUpdated`) VALUES (1,'lab','Hematology','Hema',NULL,'2021-02-02 18:16:58'),(2,'lab','Biochemistry','Bio',NULL,'2021-02-02 18:16:58'),(3,'lab','ECG','ECG',NULL,'2021-02-02 18:16:58'),(4,'radiology','Ultrasound','US',NULL,'2021-02-02 18:16:58'),(5,'radiology','MRI','MRI',NULL,'2021-02-02 18:16:58'),(6,'radiology','CT-SCAN','Scan',NULL,'2021-02-02 18:16:58'),(7,'radiology','X-Ray','XRay',NULL,'2021-02-02 18:16:58');

--
-- Dumping data for table `document_storage`
--


--
-- Dumping data for table `drugReason`
--


--
-- Dumping data for table `drugs`
--


--
-- Dumping data for table `dsGuidelineProviderMap`
--


--
-- Dumping data for table `dsGuidelines`
--


--
-- Dumping data for table `dx_associations`
--


--
-- Dumping data for table `dxresearch`
--


--
-- Dumping data for table `eChart`
--


--
-- Dumping data for table `eform`
--

INSERT INTO `eform` (`fid`, `form_name`, `file_name`, `subject`, `form_date`, `form_time`, `form_creator`, `status`, `form_html`, `showLatestFormOnly`, `patient_independent`, `roleType`) VALUES (1,'letter','','letter generator','2010-05-02','10:00:00',NULL,1,'<html><head>\r\n<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\r\n\r\n<title>Rich Text Letter</title>\r\n<style type=\"text/css\">\r\n.butn {width: 140px;}\r\n</style>\r\n\r\n<style type=\"text/css\" media=\"print\">\r\n.DoNotPrint {display: none;}\r\n\r\n</style>\r\n\r\n<script language=\"javascript\">\r\nvar needToConfirm = false;\r\n\r\n//keypress events trigger dirty flag for the iFrame and the subject line\r\ndocument.onkeyup=setDirtyFlag\r\n\r\n\r\nfunction setDirtyFlag() {\r\n	needToConfirm = true; \r\n}\r\n\r\nfunction releaseDirtyFlag() {\r\n	needToConfirm = false; //Call this function if dosent requires an alert.\r\n	//this could be called when save button is clicked\r\n}\r\n\r\n\r\nwindow.onbeforeunload = confirmExit;\r\n\r\nfunction confirmExit() {\r\n	if (needToConfirm)\r\n	return \"You have attempted to leave this page. If you have made any changes without clicking the Submit button, your changes will be lost. Are you sure you want to exit this page?\";\r\n}\r\n\r\n</script>\r\n\r\n\r\n\r\n</head><body onload=\"Start()\" bgcolor=\"FFFFFF\">\r\n\r\n\r\n<!-- START OF EDITCONTROL CODE --> \r\n\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_image_path}editControl.js\"></script>\r\n      \r\n<script language=\"javascript\">\r\n\r\n    //put any of the optional configuration variables that you want here\r\n    cfg_width = \'640\';                    //editor control width in pixels\r\n    cfg_height = \'520\';                   //editor control height in pixels\r\n    cfg_editorname = \'edit\';                //the handle for the editor                  \r\n    cfg_isrc = \'${oscar_image_path}\';         //location of the button icon files\r\n    cfg_filesrc = \'${oscar_image_path}\';         //location of the html files\r\n    cfg_template = \'blank.html\';	    //default style and content template\r\n    cfg_formattemplate = \'<option value=\"\">&mdash; template &mdash;</option>  <option value=\"blank\">blank</option>  <option value=\"consult\">consult</option> <option value=\"certificate\">work note</option> <option value=\"narcotic\">narcotic contract</option> <option value=\"MissedAppointment\">missed appt</option> <option value=\"custom\">custom</option></select>\';\r\n    //cfg_layout = \'[all]\';             //adjust the format of the buttons here\r\n    cfg_layout = \r\n\'<table style=\"background-color:#ccccff; width:640px\"><tr id=control1><td>[bold][italic][underlined][strike][subscript][superscript]|[left][center][full][right]|[unordered][ordered][rule]|[undo][redo]|[indent][outdent][select-all][clean]|[table]</td></tr><tr id=control2><td>[select-block][select-face][select-size][select-template]|[image][clock][date][spell][help]</td></tr></table>[edit-area]\';\r\n    insertEditControl(); // Initialise the edit control and sets it at this point in the webpage\r\n\r\n    function Start() {\r\n        // set eventlistener for the iframe to flag changes in the text displayed \r\n	var agent=navigator.userAgent.toLowerCase(); //for non IE browsers\r\n        if ((agent.indexOf(\"msie\") == -1) || (agent.indexOf(\"opera\") != -1)){\r\n		document.getElementById(cfg_editorname).contentWindow.addEventListener(\'keypress\',setDirtyFlag, true);\r\n	}\r\n\r\n	if (document.getElementById(\'recent_rx\').value.length<1){\r\n		//document.RichTextLetter.RecentMedications.style.visibility=\"hidden\";\r\n		document.getElementById(\'RecentMedications\').style.display = \"none\";\r\n	}\r\n\r\n        // reformat values of multiline database values from \\n lines to <br>\r\n        htmlLine(\'label\');\r\n        htmlLine(\'reminders\');\r\n        htmlLine(\'ongoingconcerns\');\r\n        htmlLine(\'medical_history\');document.getElementById(\'allergies_des\').value\r\n        htmlLine(\'other_medications_history\');  //family history  ... don\'t ask\r\n        htmlLine(\'social_family_history\');  //social history\r\n        htmlLine(\'address\');\r\n        htmlLine(\'NameAddress\');\r\n        htmlLine(\'clinic_label\');\r\n        htmlLine(\'clinic_address\');\r\n        htmlLine(\'druglist_generic\');\r\n        htmlLine(\'druglist_trade\');\r\n        htmlLine(\'recent_rx\');\r\n\r\n	var gender=document.getElementById(\'sex\').value; \r\n	if (gender==\'F\'){\r\n		document.getElementById(\'he_she\').value=\'she\'; \r\n		document.getElementById(\'his_her\').value=\'her\';\r\n		document.getElementById(\'gender\').value=\'female\';\r\n	}\r\n	var mySplitResult = document.getElementById(\'referral_name\').value.toString().split(\',\'); \r\n	document.getElementById(\'referral_nameL\').value=mySplitResult[0];\r\n\r\n	document.getElementById(\'letterhead\').value= genericLetterhead();\r\n\r\n	\r\n        // set the HTML contents of this edit control from the value saved in Oscar (if any)\r\n	var contents=document.getElementById(\'Letter\').value\r\n	if (contents.length==0){\r\n		parseTemplate();\r\n	} else {\r\n		seteditControlContents(cfg_editorname,contents);\r\n	}\r\n    }\r\n \r\n    function htmlLine(theelement) { \r\n	var temp = new Array();\r\n	if (document.getElementById(theelement).value.length>0){\r\n		temp=document.getElementById(theelement).value.split(\'\\n\'); \r\n		contents=\'\';\r\n		var x;\r\n		for (x in temp) {\r\n			contents += temp[x]+\'<br>\';\r\n			}\r\n		document.getElementById(theelement).value=contents;\r\n		}\r\n    }\r\n\r\n    function genericLetterhead() {\r\n        // set the HTML contents of the letterhead\r\n	var address = \'<table border=0><tbody><tr><td><font size=6>\'+document.getElementById(\'clinic_name\').value+\'</font></td></tr><tr><td><font size=2>\'+ document.getElementById(\'clinic_addressLineFull\').value+ \' Fax: \'+document.getElementById(\'clinic_fax\').value+\' Phone: \'+document.getElementById(\'clinic_phone\').value+\'</font><hr></td></tr></tbody></table><br>\'\r\n	if ((document.getElementById(\'clinic_name\').value.toLowerCase()).indexOf(\'amily health team\',0)>-1){\r\n		address=fhtLetterhead();\r\n	}\r\n	return address;\r\n    }\r\n\r\n    function fhtLetterhead() {\r\n        // set the HTML contents of the letterhead using FHT colours\r\n	var address = document.getElementById(\'clinic_addressLineFull\').value+ \'<br>Fax:\'+document.getElementById(\'clinic_fax\').value+\' Phone:\'+document.getElementById(\'clinic_phone\').value ;\r\n	if (document.getElementById(\'doctor\').value.indexOf(\'zapski\')>0){address=\'293 Meridian Avenue, Haileybury, ON P0J 1K0<br> Tel 705-672-2442 Fax 705-672-2384\'};\r\n	address=\'<table style=\\\'text-align: right;\\\' border=\\\'0\\\'><tbody><tr style=\\\'font-style: italic; color: rgb(71, 127, 128);\\\'><td><font size=\\\'+2\\\'>\'+document.getElementById(\'clinic_name\').value+\'</font> <hr style=\\\'width: 100%; height: 3px; color: rgb(212, 118, 0); background-color: rgb(212, 118, 0);\\\'></td> </tr> <tr style=\\\'color: rgb(71, 127, 128);\\\'> <td><font size=\\\'+1\\\'>Family Health Team<br> &Eacute;quipe Sant&eacute; Familiale</font></td> </tr> <tr style=\\\'color: rgb(212, 118, 0); \\\'> <td><small>\'+address+\'</small></td> </tr> </tbody> </table>\';\r\n	return address;\r\n    }\r\n</script>\r\n\r\n<!-- END OF EDITCONTROL CODE -->\r\n\r\n\r\n<form method=\"post\" action=\"\" name=\"RichTextLetter\" >\r\n\r\n<!-- START OF DATABASE PLACEHOLDERS -->\r\n\r\n<input type=\"hidden\" name=\"clinic_name\" id=\"clinic_name\" oscarDB=clinic_name>\r\n<input type=\"hidden\" name=\"clinic_address\" id=\"clinic_address\" oscarDB=clinic_address>\r\n<input type=\"hidden\" name=\"clinic_addressLine\" id=\"clinic_addressLine\" oscarDB=clinic_addressLine>\r\n<input type=\"hidden\" name=\"clinic_addressLineFull\" id=\"clinic_addressLineFull\" oscarDB=clinic_addressLineFull>\r\n<input type=\"hidden\" name=\"clinic_label\" id=\"clinic_label\" oscarDB=clinic_label>\r\n<input type=\"hidden\" name=\"clinic_fax\" id=\"clinic_fax\" oscarDB=clinic_fax>\r\n<input type=\"hidden\" name=\"clinic_phone\" id=\"clinic_phone\" oscarDB=clinic_phone>\r\n<input type=\"hidden\" name=\"clinic_city\" id=\"clinic_city\" oscarDB=clinic_city>\r\n<input type=\"hidden\" name=\"clinic_province\" id=\"clinic_province\" oscarDB=clinic_province>\r\n<input type=\"hidden\" name=\"clinic_postal\" id=\"clinic_postal\" oscarDB=clinic_postal>\r\n\r\n<input type=\"hidden\" name=\"patient_name\" id=\"patient_name\" oscarDB=patient_name>\r\n<input type=\"hidden\" name=\"first_last_name\" id=\"first_last_name\" oscarDB=first_last_name>\r\n<input type=\"hidden\" name=\"patient_nameF\" id=\"patient_nameF\" oscarDB=patient_nameF >\r\n<input type=\"hidden\" name=\"patient_nameL\" id=\"patient_nameL\" oscarDB=patient_nameL >\r\n<input type=\"hidden\" name=\"label\" id=\"label\" oscarDB=label>\r\n<input type=\"hidden\" name=\"NameAddress\" id=\"NameAddress\" oscarDB=NameAddress>\r\n<input type=\"hidden\" name=\"address\" id=\"address\" oscarDB=address>\r\n<input type=\"hidden\" name=\"addressline\" id=\"addressline\" oscarDB=addressline>\r\n<input type=\"hidden\" name=\"phone\" id=\"phone\" oscarDB=phone>\r\n<input type=\"hidden\" name=\"phone2\" id=\"phone2\" oscarDB=phone2>\r\n<input type=\"hidden\" name=\"province\" id=\"province\" oscarDB=province>\r\n<input type=\"hidden\" name=\"city\" id=\"city\" oscarDB=city>\r\n<input type=\"hidden\" name=\"postal\" id=\"postal\" oscarDB=postal>\r\n<input type=\"hidden\" name=\"dob\" id=\"dob\" oscarDB=dob>\r\n<input type=\"hidden\" name=\"dobc\" id=\"dobc\" oscarDB=dobc>\r\n<input type=\"hidden\" name=\"dobc2\" id=\"dobc2\" oscarDB=dobc2>\r\n<input type=\"hidden\" name=\"hin\" id=\"hin\" oscarDB=hin>\r\n<input type=\"hidden\" name=\"hinc\" id=\"hinc\" oscarDB=hinc>\r\n<input type=\"hidden\" name=\"hinversion\" id=\"hinversion\" oscarDB=hinversion>\r\n<input type=\"hidden\" name=\"ageComplex\" id=\"ageComplex\" oscarDB=ageComplex >\r\n<input type=\"hidden\" name=\"age\" id=\"age\" oscarDB=age >\r\n<input type=\"hidden\" name=\"sex\" id=\"sex\" oscarDB=sex >\r\n<input type=\"hidden\" name=\"chartno\" id=\"chartno\" oscarDB=chartno >\r\n\r\n<input type=\"hidden\" name=\"medical_history\" id=\"medical_history\" oscarDB=medical_history>\r\n<input type=\"hidden\" name=\"recent_rx\" id=\"recent_rx\" oscarDB=recent_rx>\r\n<input type=\"hidden\" name=\"druglist_generic\" id=\"druglist_generic\" oscarDB=druglist_generic>\r\n<input type=\"hidden\" name=\"druglist_trade\" id=\"druglist_trade\" oscarDB=druglist_trade>\r\n<input type=\"hidden\" name=\"druglist_line\" id=\"druglist_line\" oscarDB=druglist_line>\r\n<input type=\"hidden\" name=\"social_family_history\" id=\"social_family_history\" oscarDB=social_family_history>\r\n<input type=\"hidden\" name=\"other_medications_history\" id=\"other_medications_history\" oscarDB=other_medications_history>\r\n<input type=\"hidden\" name=\"reminders\" id=\"reminders\" oscarDB=reminders>\r\n<input type=\"hidden\" name=\"ongoingconcerns\" id=\"ongoingconcerns\" oscarDB=ongoingconcerns >\r\n\r\n<input type=\"hidden\" name=\"provider_name_first_init\" id=\"provider_name_first_init\" oscarDB=provider_name_first_init >\r\n<input type=\"hidden\" name=\"current_user\" id=\"current_user\" oscarDB=current_user >\r\n<input type=\"hidden\" name=\"doctor_work_phone\" id=\"doctor_work_phone\" oscarDB=doctor_work_phone >\r\n<input type=\"hidden\" name=\"doctor\" id=\"doctor\" oscarDB=doctor >\r\n\r\n<input type=\"hidden\" name=\"today\" id=\"today\" oscarDB=today>\r\n\r\n<input type=\"hidden\" name=\"allergies_des\" id=\"allergies_des\" oscarDB=allergies_des >\r\n\r\n<!-- PLACE REFERRAL PLACEHOLDERS HERE WHEN BC APCONFIG FIXED -->\r\n<input type=\"hidden\" name=\"referral_name\" id=\"referral_name\" oscarDB=referral_name>\r\n<input type=\"hidden\" name=\"referral_address\" id=\"referral_address\" oscarDB=referral_address>\r\n<input type=\"hidden\" name=\"referral_phone\" id=\"referral_phone\" oscarDB=referral_phone>\r\n<input type=\"hidden\" name=\"referral_fax\" id=\"referral_fax\" oscarDB=referral_fax>\r\n\r\n<!-- END OF DATABASE PLACEHOLDERS -->\r\n\r\n\r\n<!-- START OF MEASUREMENTS PLACEHOLDERS -->\r\n\r\n<input type=\"hidden\" name=\"BP\" id=\"BP\" oscarDB=m$BP#value>\r\n<input type=\"hidden\" name=\"WT\" id=\"WT\" oscarDB=m$WT#value>\r\n<input type=\"hidden\" name=\"smoker\" id=\"smoker\" oscarDB=m$SMK#value>\r\n<input type=\"hidden\" name=\"dailySmokes\" id=\"dailySmokes\" oscarDB=m$NOSK#value>\r\n<input type=\"hidden\" name=\"A1C\" id=\"A1C\" oscarDB=m$A1C#value>\r\n\r\n<!-- END OF MEASUREMENTS PLACEHOLDERS -->\r\n\r\n\r\n<!-- START OF DERIVED PLACEHOLDERS -->\r\n\r\n<input type=\"hidden\" name=\"he_she\" id=\"he_she\" value=\"he\">\r\n<input type=\"hidden\" name=\"his_her\" id=\"his_her\" value=\"his\">\r\n<input type=\"hidden\" name=\"gender\" id=\"gender\" value=\"male\">\r\n<input type=\"hidden\" name=\"referral_nameL\" id=\"referral_nameL\" value=\"Referring Doctor\">\r\n<input type=\"hidden\" name=\"letterhead\" id=\"letterhead\" value=\"Letterhead\">\r\n\r\n<!-- END OF DERIVED PLACEHOLDERS -->\r\n\r\n\r\n<textarea name=\"Letter\" id=\"Letter\" style=\"width:600px; display: none;\"></textarea>\r\n\r\n<div class=\"DoNotPrint\" id=\"control3\" style=\"position:absolute; top:20px; left: 660px;\">\r\n<input type=\"button\" class=\"butn\" name=\"AddLetterhead\" id=\"AddLetterhead\" value=\"Letterhead\" \r\n	onclick=\"doHtml(document.getElementById(\'letterhead\').value);\">\r\n\r\n<br>\r\n<!--\r\n<input type=\"button\" class=\"butn\" name=\"certificate\" value=\"Work Note\" \r\n	onclick=\"document.RichTextLetter.AddLetterhead.click();\r\n 	doHtml(\'<p>\'+doDate()+\'<p>This is to certify that I have today examined <p>\');\r\n	document.RichTextLetter.AddLabel.click();\r\n	doHtml(\'In my opinion, \'+document.getElementById(\'he_she\').value+\' will be unfit for \'+document.getElementById(\'his_her\').value+\' normal work from today to * inclusive.\');\r\n	document.RichTextLetter.Closing.click();\">\r\n<br>\r\n\r\n<input type=\"button\" class=\"butn\" name=\"consult\" value=\"Consult Letter\" \r\n	onclick=\"  var ref=document.getElementById(\'referral_name\').value.toString(); var mySplitResult = ref.split(\',\');\r\n	var gender=document.getElementById(\'sex\').value; if (gender==\'M\'){gender=\'male\';}; if (gender==\'F\'){gender=\'female\';};\r\n	var years=document.getElementById(\'ageComplex\').value; if (years==\'\'){years=document.getElementById(\'age\').value + \'yo\';};\r\n	document.RichTextLetter.AddLetterhead.click();\r\n	doHtml(\'<p>\'+doDate()+\'<p>\');\r\n	document.RichTextLetter.AddReferral.click();\r\n	doHtml(\'<p>RE:&nbsp\');\r\n	document.RichTextLetter.AddLabel.click();\r\n	doHtml(\'<p>Dear Dr. \'+mySplitResult[0]+\'<p>Thank you for asking me to see this \'+years+ \' \' +gender);\r\n	document.RichTextLetter.Closing.click(); \">\r\n<br>\r\n-->\r\n<input type=\"button\" class=\"butn\" name=\"AddReferral\" id=\"AddReferral\" value=\"Referring Block\" \r\n	onclick=\"doHtml(document.getElementById(\'referral_name\').value+\'<br>\'+ document.getElementById(\'referral_address\').value +\'<br>CANADA<br> Tel: \'+ document.getElementById(\'referral_phone\').value+\'<br>Fax:  \'+document.getElementById(\'referral_fax\').value);\">\r\n\r\n<br>\r\n\r\n<input type=\"button\" class=\"butn\" name=\"AddLabel\" id=\"AddLabel\" value=\"Patient Block\" \r\n	onclick=\"doHtml(document.getElementById(\'label\').value);\">\r\n\r\n<br>\r\n\r\n<br>\r\n<input type=\"button\"  class=\"butn\" name=\"MedicalHistory\" value=\"Recent History\" width=30\r\n	onclick=\"var hist=parseText(document.getElementById(\'medical_history\').value); doHtml(hist);\">\r\n<br>\r\n<input type=\"button\"  class=\"butn\" name=\"AddMedicalHistory\" value=\"Full History\" width=30\r\n	onclick=\"doHtml(document.getElementById(\'medical_history\').value); \">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"RecentMedications\" id=\"RecentMedications\" value=\"Recent Prescriptions\"\r\n	onclick=\"doHtml(document.getElementById(\'recent_rx\').value);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"Medlist\" id=\"Medlist\" value=\"Medication List\"\r\n	onclick=\"doHtml(document.getElementById(\'druglist_trade\').value);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"Allergies\" id=\"Allergies\" value=\"Meds & Allergies\"\r\n	onclick=\"var allergy=document.getElementById(\'allergies_des\').value; if (allergy.length>0){allergy=\'<br>Allergies: \'+allergy};doHtml(\'Medications: \'+document.getElementById(\'druglist_line\').value+allergy);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"OtherMedicationsHistory\" value=\"Family History\"\r\n	onclick=\"var hist=parseText(document.getElementById(\'other_medications_history\').value); doHtml(hist);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"AddOtherMedicationsHistory\" value=\"Full Family Hx\"\r\n	onclick=\"doHtml(document.getElementById(\'other_medications_history\').value); \">\r\n\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"AddSocialFamilyHistory\" value=\"Social History\" \r\n	onclick=\"var hist=parseText(document.getElementById(\'social_family_history\').value); doHtml(hist);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"AddReminders\" value=\"Reminders\"\r\n	onclick=\"var hist=parseText(document.getElementById(\'reminders\').value); doHtml(hist);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"AddOngoingConcerns\" value=\"Ongoing Concerns\"\r\n	onclick=\"var hist=parseText(document.getElementById(\'ongoingconcerns\').value); doHtml(hist);\">\r\n<br>\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"Patient\" value=\"Patient Name\"\r\n	onclick=\" doHtml(document.getElementById(\'first_last_name\').value);\">\r\n\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"PatientAge\" value=\"Patient Age\"\r\n	onclick=\"var hist=document.getElementById(\'ageComplex\').value; if (hist==\'\'){hist=document.getElementById(\'age\').value;}; doHtml(hist);\">\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"label\" value=\"Patient Label\"\r\n	onclick=\"var hist=document.getElementById(\'label\').value; doHtml(hist);\">\r\n\r\n\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"PatientSex\" value=\"Patient Gender\"\r\n	onclick=\"doHtml(document.getElementById(\'sex\').value);\">\r\n<br>\r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"Closing\" value=\"Closing Salutation\" \r\n	onclick=\" doHtml(\'<p>Yours Sincerely<p>&nbsp;<p>\'+ document.getElementById(\'provider_name_first_init\').value+\', MD\');\">\r\n \r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"User\" value=\"Current User\"\r\n	onclick=\"var hist=document.getElementById(\'current_user\').value; doHtml(hist);\">\r\n \r\n<br>\r\n<input type=\"button\" class=\"butn\" name=\"Doctor\" value=\"Attending Doctor\"\r\n	onclick=\"var hist=document.getElementById(\'doctor\').value; doHtml(hist);\">\r\n<br>\r\n<br>\r\n\r\n\r\n<br>\r\n</div>\r\n\r\n\r\n<div class=\"DoNotPrint\" >\r\n<input onclick=\"viewsource(this.checked)\" type=\"checkbox\">\r\nHTML Source\r\n<input onclick=\"usecss(this.checked)\" type=\"checkbox\">\r\nUse CSS\r\n	<table><tr><td>\r\n		 Subject: <input name=\"subject\" id=\"subject\" size=\"40\" type=\"text\">\r\n		 <input value=\"Submit\" name=\"SubmitButton\" type=\"submit\" onclick=\"needToConfirm=false;document.getElementById(\'Letter\').value=editControlContents(\'edit\');  document.RichTextLetter.submit()\">\r\n		 <input value=\"Reset\" name=\"ResetButton\" type=\"reset\">\r\n		 <input value=\"Print\" name=\"PrintButton\" type=\"button\" onclick=\"document.getElementById(\'edit\').contentWindow.print();\">\r\n		 <input value=\"Print & Save\" name=\"PrintSaveButton\" type=\"button\" onclick=\"document.getElementById(\'edit\').contentWindow.print();needToConfirm=false;document.getElementById(\'Letter\').value=editControlContents(\'edit\');  setTimeout(\'document.RichTextLetter.submit()\',1000);\">\r\n	 </td></tr></table>\r\n </div>\r\n </form>\r\n\r\n</body></html>\r\n',0,0,NULL),(2,'Rich Text Letter',NULL,'Rich Text Letter Generator','2014-02-01','10:00:00',NULL,0,'<html><head>\r\n<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\r\n\r\n<title>Rich Text Letter</title>\r\n<style type=\"text/css\">\r\n.butn {width: 140px;}\r\n</style>\r\n\r\n<style type=\"text/css\" media=\"print\">\r\n.DoNotPrint {display: none;}\r\n\r\n</style>\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}jquery/jquery-1.4.2.js\"></script>\r\n\r\n<script language=\"javascript\">\r\nvar needToConfirm = false;\r\n\r\n//keypress events trigger dirty flag for the iFrame and the subject line\r\ndocument.onkeyup=setDirtyFlag\r\n\r\n\r\nfunction setDirtyFlag() {\r\n	needToConfirm = true; \r\n}\r\n\r\nfunction releaseDirtyFlag() {\r\n	needToConfirm = false; //Call this function if dosent requires an alert.\r\n	//this could be called when save button is clicked\r\n}\r\n\r\n\r\nwindow.onbeforeunload = confirmExit;\r\n\r\nfunction confirmExit() {\r\n	if (needToConfirm){\r\n	return \"You have attempted to leave this page. If you have made any changes without clicking the Submit button, your changes will be lost. Are you sure you want to exit this page?\";\r\n	}\r\n}\r\n\r\n\r\nvar loads=true;\r\n\r\nfunction maximize() {\r\n	window.resizeTo(1030, 865) ;\r\n	loads=false;\r\n}\r\n\r\nfunction saveRTL() {\r\n	needToConfirm=false;\r\n	var theRTL=editControlContents(\'edit\');\r\n	var myNewString = theRTL.replace(/\"/g, \'&quot;\');\r\n	document.getElementById(\'Letter\').value=myNewString.replace(/\'/g, \"&#39;\");\r\n}\r\n</script>\r\n\r\n<!-- START OF EDITCONTROL CODE --> \r\n\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}eforms/editControl.js\"></script>\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}eforms/APCache.js\"></script>\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}eforms/imageControl.js\"></script>\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}eforms/faxControl.js\"></script>\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}eforms/signatureControl.jsp\"></script>\r\n<script language=\"javascript\" type=\"text/javascript\" src=\"${oscar_javascript_path}eforms/printControl.js\"></script>\r\n\r\n<script language=\"javascript\">\r\n	//put any of the optional configuration variables that you want here\r\n	cfg_width = \'840\'; //editor control width in pixels\r\n	cfg_height = \'520\'; //editor control height in pixels\r\n	cfg_editorname = \'edit\'; //the handle for the editor                  \r\n	cfg_isrc = \'../eform/displayImage.do?imagefile=\'; //location of the button icon files\r\n	cfg_filesrc = \'../eform/displayImage.do?imagefile=\'; //location of the html files\r\n	cfg_template = \'blank.rtl\'; //default style and content template\r\n	cfg_formattemplate = \'<option value=\"\"> loading... </option></select>\';\r\n	//cfg_layout = \'[all]\';             //adjust the format of the buttons here\r\n	//cfg_layout = \'<table style=\"background-color:ccccff; width:840px\"><tr id=control1><td>[bold][italic][underlined][strike][subscript][superscript]|[left][center][full][right]|[unordered][ordered][rule]|[undo][redo]|[indent][outdent][select-all][clean]|[table]</td></tr><tr id=control2><td>[select-block][select-face][select-size][select-template]|[image][clock][date][spell][help]</td></tr></table>[edit-area]\';\r\n	cfg_layout = \'<table style=\"background-color:ccccff; width:840px\"><tr id=control1><td align=center>[bold][italic][underlined][strike][subscript][superscript]|[left][center][full][right]|[unordered][ordered][rule]|[undo][redo]|[indent][outdent][select-all][clean]|[table]\\[text-colour][hilight]</td></tr><tr id=control2><td align=center>[select-block][select-face][select-size][select-template]|[image][link]|[clock][date][spell][cut][copy][paste][help]</td></tr></table>[edit-area]\';\r\n	insertEditControl(); // Initialise the edit control and sets it at this point in the webpage\r\n\r\n	\r\n	function gup(name, url)\r\n	{\r\n		if (url == null) { url = window.location.href; }\r\n		name = name.replace(/[\\[]/,\"\\\\\\[\").replace(/[\\]]/,\"\\\\\\]\");\r\n		var regexS = \"[\\\\?&]\"+name+\"=([^&#]*)\";\r\n		var regex = new RegExp(regexS);\r\n		var results = regex.exec(url);\r\n		if (results == null) { return \"\"; }\r\n		else { return results[1]; }\r\n	}\r\n	var demographicNo =\"\";\r\n\r\n	jQuery(document).ready(function(){\r\n		demographicNo = gup(\"demographic_no\");\r\n		if (demographicNo == \"\") { demographicNo = gup(\"efmdemographic_no\", jQuery(\"form\").attr(\'action\')); }\r\n		if (typeof signatureControl != \"undefined\") {\r\n			signatureControl.initialize({\r\n				sigHTML:\"../signature_pad/tabletSignature.jsp?inWindow=true&saveToDB=true&demographicNo=\",\r\n				demographicNo:demographicNo,\r\n				refreshImage: function (e) {\r\n					var html = \"<img src=\'\"+e.storedImageUrl+\"&r=\"+ Math.floor(Math.random()*1001) +\"\'></img>\";\r\n					doHtml(html);		\r\n				},\r\n				signatureInput: \"#signatureInput\"	\r\n			});\r\n		}		\r\n	});\r\n		\r\n	var cache = createCache({\r\n		defaultCacheResponseHandler: function(type) {\r\n			if (checkKeyResponse(type)) {\r\n				doHtml(cache.get(type));\r\n			}			\r\n			\r\n		},\r\n		cacheResponseErrorHandler: function(xhr, error) {\r\n			alert(\"Please contact an administrator, an error has occurred.\");			\r\n			\r\n		}\r\n	});	\r\n	\r\n	function checkKeyResponse(response) {		\r\n		if (cache.isEmpty(response)) {\r\n			alert(\"The requested value has no content.\");\r\n			return false;\r\n		}\r\n		return true;\r\n	}\r\n	\r\n	function printKey (key) {\r\n		var value = cache.lookup(key); \r\n		if (value != null && checkKeyResponse(key)) { doHtml(cache.get(key)); } 		  \r\n	}\r\n	\r\n	function submitFaxButton() {\r\n		document.getElementById(\'faxEForm\').value=true;\r\n		saveRTL();\r\n		setTimeout(\'document.RichTextLetter.submit()\',1000);\r\n	}\r\n	\r\n	cache.addMapping({\r\n		name: \"_SocialFamilyHistory\",\r\n		values: [\"social_family_history\"],\r\n		storeInCacheHandler: function(key,value) {\r\n			cache.put(this.name, cache.get(\"social_family_history\").replace(/(<br>)+/g,\"<br>\"));\r\n		},\r\n		cacheResponseHandler:function () {\r\n			if (checkKeyResponse(this.name)) {				\r\n				doHtml(cache.get(this.name));\r\n			}	\r\n		}\r\n	});\r\n	\r\n	\r\n	cache.addMapping({name: \"template\", cacheResponseHandler: populateTemplate});	\r\n	\r\n	cache.addMapping({\r\n		name: \"_ClosingSalutation\", \r\n		values: [\"provider_name_first_init\"],	\r\n		storeInCacheHandler: function (key,value) {\r\n			if (!cache.isEmpty(\"provider_name_first_init\")) {\r\n				cache.put(this.name, \"<p>Yours Sincerely<p>&nbsp;<p>\" + cache.get(\"provider_name_first_init\") + \", MD\");\r\n			}\r\n		},\r\n		cacheResponseHandler:function () {\r\n			if (checkKeyResponse(this.name)) {				\r\n				doHtml(cache.get(this.name));\r\n			}	\r\n		}\r\n	});\r\n	\r\n	cache.addMapping({\r\n		name: \"_ReferringBlock\", \r\n		values: [\"referral_name\", \"referral_address\", \"referral_phone\", \"referral_fax\"], 	\r\n		storeInCacheHandler: function (key, value) {\r\n			var text = \r\n				(!cache.isEmpty(\"referral_name\") ? cache.get(\"referral_name\") + \"<br>\" : \"\") \r\n			  + (!cache.isEmpty(\"referral_address\") ? cache.get(\"referral_address\") + \"<br>\" : \"\")\r\n			  + (!cache.isEmpty(\"referral_phone\") ? \"Tel: \" + cache.get(\"referral_phone\") + \"<br>\" : \"\")\r\n			  + (!cache.isEmpty(\"referral_fax\") ? \"Fax: \" + cache.get(\"referral_fax\") + \"<br>\" : \"\");\r\n			if (text == \"\") {\r\n				text = \r\n					(!cache.isEmpty(\"bc_referral_name\") ? cache.get(\"bc_referral_name\") + \"<br>\" : \"\") \r\n				  + (!cache.isEmpty(\"bc_referral_address\") ? cache.get(\"bc_referral_address\") + \"<br>\" : \"\")\r\n				  + (!cache.isEmpty(\"bc_referral_phone\") ? \"Tel: \" + cache.get(\"bc_referral_phone\") + \"<br>\" : \"\")\r\n				  + (!cache.isEmpty(\"bc_referral_fax\") ? \"Fax: \" + cache.get(\"bc_referral_fax\") + \"<br>\" : \"\");\r\n			}						 \r\n			cache.put(this.name, text)\r\n		},\r\n		cacheResponseHandler: function () {\r\n			if (checkKeyResponse(this.name)) {\r\n				doHtml(cache.get(this.name));\r\n			}\r\n		}\r\n	});\r\n	\r\n	cache.addMapping({\r\n		name: \"letterhead\", \r\n		values: [\"clinic_name\", \"clinic_fax\", \"clinic_phone\", \"clinic_addressLineFull\", \"doctor\", \"doctor_contact_phone\", \"doctor_contact_fax\", \"doctor_contact_addr\"], \r\n		storeInCacheHandler: function (key, value) {\r\n			var text = genericLetterhead();\r\n			cache.put(\"letterhead\", text);\r\n		},\r\n		cacheResponseHandler: function () {\r\n			if (checkKeyResponse(this.name)) {\r\n				doHtml(cache.get(this.name));\r\n			}\r\n		}\r\n	});\r\n	\r\n	cache.addMapping({\r\n		name: \"referral_nameL\", \r\n		values: [\"referral_name\"], \r\n		storeInCacheHandler: function(_key,_val) { \r\n		if (!cache.isEmpty(\"referral_name\")) {\r\n				var mySplitResult =  cache.get(\"referral_name\").toString().split(\",\");\r\n				cache.put(\"referral_nameL\", mySplitResult[0]);\r\n			} \r\n		}\r\n	});\r\n\r\n	cache.addMapping({\r\n		name: \"medical_historyS\", \r\n		values: [\"medical_history\"], \r\n		storeInCacheHandler: function(_key,_val) { \r\n		if (!cache.isEmpty(\"medical_history\")) {\r\n				var mySplitResult =  cache.get(\"medical_history\").toString().split(\"]]-----\");\r\n				cache.put(\"medical_historyS\", mySplitResult.pop());\r\n			} \r\n		}\r\n	});\r\n\r\n	cache.addMapping({\r\n		name: \"stamp\", \r\n		values: [\"stamp_name\", \"doctor\"], \r\n		storeInCacheHandler: function(_key,_val) { \r\n				var imgsrc=pickStamp();\r\n				cache.put(\"stamp\",imgsrc);\r\n		}\r\n	});\r\n\r\n	\r\n	cache.addMapping({\r\n		name: \"complexAge\", \r\n		values: [\"complexAge\"], \r\n		cacheResponseHandler: function() {\r\n			if (cache.isEmpty(\"complexAge\")) { \r\n				printKey(\"age\"); \r\n			}\r\n			else {\r\n				if (checkKeyResponse(this.name)) {\r\n					doHtml(cache.get(this.name));\r\n				}\r\n			}\r\n		}\r\n	});\r\n	\r\n	// Setting up many to one mapping for derived gender keys.\r\n	var genderKeys = [\"he_she\", \"his_her\", \"gender\"];	\r\n	var genderIndex;\r\n	for (genderIndex in genderKeys) {\r\n		cache.addMapping({ name: genderKeys[genderIndex], values: [\"sex\"]});\r\n	}\r\n	cache.addMapping({name: \"sex\", values: [\"sex\"], storeInCacheHandler: populateGenderInfo});\r\n	\r\n	function isGenderLookup(key) {\r\n		var y;\r\n		for (y in genderKeys) { if (genderKeys[y] == key) { return true; } }\r\n		return false;\r\n	}\r\n	\r\n	function populateGenderInfo(key, val){\r\n		if (val == \'F\') {\r\n			cache.put(\"sex\", \"F\");\r\n			cache.put(\"he_she\", \"she\");\r\n			cache.put(\"his_her\", \"her\");\r\n			cache.put(\"gender\", \"female\");				\r\n		}\r\n		else {\r\n			cache.put(\"sex\", \"M\");\r\n			cache.put(\"he_she\", \"he\");\r\n			cache.put(\"his_her\", \"him\");\r\n			cache.put(\"gender\", \"male\");				\r\n		}\r\n	}\r\n	\r\n	function Start() {\r\n		\r\n			$.ajax({\r\n				url : \"efmformrtl_templates.jsp\",\r\n				success : function(data) {\r\n					$(\"#template\").html(data);\r\n					loadDefaultTemplate();\r\n				}\r\n			});\r\n	\r\n			$(\".cacheInit\").each(function() { \r\n				cache.put($(this).attr(\'name\'), $(this).val());\r\n				$(this).remove();				\r\n			});\r\n			\r\n			// set eventlistener for the iframe to flag changes in the text displayed \r\n			var agent = navigator.userAgent.toLowerCase(); //for non IE browsers\r\n			if ((agent.indexOf(\"msie\") == -1) || (agent.indexOf(\"opera\") != -1)) {\r\n				document.getElementById(cfg_editorname).contentWindow\r\n						.addEventListener(\'keypress\', setDirtyFlag, true);\r\n			}\r\n				\r\n			// set the HTML contents of this edit control from the value saved in Oscar (if any)\r\n			var contents = document.getElementById(\'Letter\').value\r\n			if (contents.length == 0) {\r\n				parseTemplate();\r\n			} else {\r\n				seteditControlContents(cfg_editorname, contents);\r\n				document.getElementById(cfg_editorname).contentWindow.document.designMode = \'on\';\r\n			}\r\n			maximize();\r\n	}\r\n\r\n	function htmlLine(text) {\r\n		return text.replace(/\\r?\\n/g,\"<br>\");\r\n	}\r\n\r\n	function genericLetterhead() {\r\n		// set the HTML contents of the letterhead\r\n		var address = \'<table border=0><tbody><tr><td><font size=6>\'\r\n				+ cache.get(\'clinic_name\')\r\n				+ \'</font></td></tr><tr><td><font size=2>\'\r\n				+ cache.get(\'doctor_contact_addr\')\r\n				+ \' Fax: \' + cache.get(\'doctor_contact_fax\')\r\n				+ \' Phone: \' + cache.get(\'doctor_contact_phone\')\r\n				+ \'</font><hr></td></tr></tbody></table><br>\';\r\n		if ( (cache.get(\'clinic_name\').toLowerCase()).indexOf(\'amily health team\',0)>-1){\r\n		address=fhtLetterhead(); }\r\n		if ( (cache.get(\'clinic_name\').toLowerCase()).indexOf(\'fht\',0)>-1){\r\n		address=fhtLetterhead(); }\r\n		return address;\r\n	}\r\n\r\n	function fhtLetterhead() {\r\n		// set the HTML contents of the letterhead using FHT colours\r\n		var address = cache.get(\'clinic_addressLineFull\')\r\n				+ \'<br>Fax:\' + cache.get(\'clinic_fax\')\r\n				+ \' Phone:\' + cache.get(\'clinic_phone\');\r\n		if (cache.contains(\"doctor\") && cache.get(\'doctor\').indexOf(\'zapski\') > 0) {\r\n			address = \'293 Meridian Avenue, Haileybury, ON P0J 1K0<br> Tel 705-672-2442&nbsp;&nbsp; Fax 866-945-5725\';\r\n		}\r\n		address = \'<table style=\\\'text-align: right;\\\' border=\\\'0\\\'><tbody><tr style=\\\'font-style: italic; color: rgb(71, 127, 128);\\\'><td><font size=\\\'+2\\\'>\'\r\n				+ cache.get(\'clinic_name\')\r\n				+ \'</font> <hr style=\\\'width: 100%; height: 3px; color: rgb(212, 118, 0); background-color: rgb(212, 118, 0);\\\'></td> </tr> <tr style=\\\'color: rgb(71, 127, 128);\\\'> <td><font size=\\\'+1\\\'>Family Health Team<br>Equipe Sante Familiale</font></td> </tr> <tr style=\\\'color: rgb(212, 118, 0); \\\'> <td><small>\'\r\n				+ address + \'</small></td> </tr> </tbody> </table>\';\r\n		return address;\r\n	}\r\n\r\n	function pickStamp() {\r\n		// set the HTML contents of the signature stamp\r\n		var mystamp =\'<img src=\"../eform/displayImage.do?imagefile=stamp.png\">\';\r\n		if (cache.contains(\"doctor\")) {\r\n			if (cache.get(\'doctor\').indexOf(\'zapski\') > 0) {\r\n				mystamp = \'<img src=\"../eform/displayImage.do?imagefile=PHC.png\" width=\"200\" height=\"100\" />\';\r\n				}\r\n			if (cache.get(\'doctor\').indexOf(\'hurman\') > 0) {\r\n				mystamp = \'<img src=\"../eform/displayImage.do?imagefile=MCH.png\" width=\"200\" height=\"100\" />\';\r\n				}\r\n			if (cache.get(\'doctor\').indexOf(\'mith\') > 0) {\r\n				mystamp = \'<img src=\"../eform/displayImage.do?imagefile=PJS.png\" width=\"200\" height=\"100\" />\';\r\n				}\r\n			if (cache.get(\'doctor\').indexOf(\'loko\') > 0) {\r\n				mystamp = \'<img src=\"../eform/displayImage.do?imagefile=FAO.png\" width=\"200\" height=\"100\" />\';\r\n				}\r\n			if (cache.get(\'doctor\').indexOf(\'urrie\') > 0) {\r\n				mystamp = \'<img src=\"../eform/displayImage.do?imagefile=LNC.png\" width=\"200\" height=\"100\" />\';\r\n				}\r\n			if (cache.get(\'doctor\').indexOf(\'cdermot\') > 0) {\r\n				mystamp = \'<img src=\"../eform/displayImage.do?imagefile=TMD.png\" width=\"200\" height=\"100\" />\';\r\n				}\r\n		}\r\n		return mystamp;\r\n	}\r\n	var formIsRTL = true;\r\n\r\n</script>\r\n<!-- END OF EDITCONTROL CODE -->\r\n</head><body bgcolor=\"FFFFFF\" onload=\"Start();\">\r\n<form method=\"post\" action=\"\" name=\"RichTextLetter\" ><textarea name=\"Letter\" id=\"Letter\" style=\"width:600px; display: none;\"></textarea>\r\n\r\n<div class=\"DoNotPrint\" id=\"control3\" style=\"position:absolute; top:20px; left: 860px;\">\r\n\r\n<!-- Letter Head -->\r\n<input type=\"button\" class=\"butn\" name=\"AddLetterhead\" id=\"AddLetterhead\" value=\"Letterhead\" onclick=\"printKey(\'letterhead\');\">\r\n<br>\r\n\r\n<!-- Referring Block -->\r\n<input type=\"button\" class=\"butn\" name=\"AddReferral\" id=\"AddReferral\" value=\"Referring Block\" onclick=\"printKey(\'_ReferringBlock\');\">\r\n<br>\r\n\r\n<!-- Patient Block -->\r\n<input type=\"button\" class=\"butn\" name=\"AddLabel\" id=\"AddLabel\" value=\"Patient Block\" onclick=\"printKey(\'label\');\">\r\n<br>\r\n<br> \r\n\r\n<!-- Social History -->\r\n<input type=\"button\" class=\"butn\" name=\"AddSocialFamilyHistory\" value=\"Social History\" onclick=\"var hist=\'_SocialFamilyHistory\';printKey(hist);\">\r\n<br>\r\n\r\n<!--  Medical History -->\r\n<input type=\"button\"  class=\"butn\" name=\"AddMedicalHistory\" value=\"Medical History\" width=30 onclick=\"var hist=\'medical_historyS\';printKey(hist);\">\r\n<br>\r\n\r\n<!--  Ongoing Concerns -->\r\n<input type=\"button\" class=\"butn\" name=\"AddOngoingConcerns\" value=\"Ongoing Concerns\" onclick=\"var hist=\'ongoingconcerns\'; printKey(hist);\">\r\n<br>\r\n\r\n<!-- Reminders -->\r\n<input type=\"button\" class=\"butn\" name=\"AddReminders\" value=\"Reminders\"\r\n	onclick=\"var hist=\'reminders\'; printKey(hist);\">\r\n<br>\r\n\r\n<!-- Allergies -->\r\n<input type=\"button\" class=\"butn\" name=\"Allergies\" id=\"Allergies\" value=\"Allergies\" onclick=\"printKey(\'allergies_des\');\">\r\n<br>\r\n\r\n<!-- Prescriptions -->\r\n<input type=\"button\" class=\"butn\" name=\"Medlist\" id=\"Medlist\" value=\"Prescriptions\"	onclick=\"printKey(\'druglist_trade\');\">\r\n<br>\r\n\r\n<!-- Other Medications -->\r\n<input type=\"button\" class=\"butn\" name=\"OtherMedicationsHistory\" value=\"Other Medications\" onclick=\"printKey(\'other_medications_history\'); \">\r\n\r\n<br>\r\n\r\n<!-- Risk Factors -->\r\n<input type=\"button\" class=\"butn\" name=\"RiskFactors\" value=\"Risk Factors\" onclick=\"printKey(\'riskfactors\'); \">\r\n<br>\r\n\r\n<!-- Family History -->\r\n<input type=\"button\" class=\"butn\" name=\"FamilyHistory\" value=\"Family History\" onclick=\"printKey(\'family_history\'); \">\r\n<br>\r\n<br>\r\n\r\n<!-- Patient Name --> \r\n<input type=\"button\" class=\"butn\" name=\"Patient\" value=\"Patient Name\" onclick=\"printKey(\'first_last_name\');\">\r\n<br>\r\n\r\n<!-- Patient Age -->\r\n<input type=\"button\" class=\"butn\" name=\"PatientAge\" value=\"Patient Age\" onclick=\"var hist=\'ageComplex\'; printKey(hist);\">\r\n\r\n<br>\r\n\r\n<!-- Patient Label -->\r\n<input type=\"button\" class=\"butn\" name=\"label\" value=\"Patient Label\" onclick=\"hist=\'label\';printKey(hist);\">\r\n<br>\r\n\r\n<input type=\"button\" class=\"butn\" name=\"PatientSex\" value=\"Patient Gender\" onclick=\"printKey(\'gender\');\">\r\n<br>\r\n<br>\r\n\r\n<!-- Closing Salutation -->\r\n<input type=\"button\" class=\"butn\" name=\"Closing\" value=\"Closing Salutation\" onclick=\"printKey(\'_ClosingSalutation\');\">\r\n<br>\r\n\r\n<!-- Signature Stamp -->\r\n<input type=\"button\" class=\"butn\" name=\"stamp\" value=\"Stamp\" onclick=\"printKey(\'stamp\');\">\r\n<br>\r\n<!--  Current User -->\r\n<input type=\"button\" class=\"butn\" name=\"User\" value=\"Current User\" onclick=\"var hist=\'current_user\'; printKey(hist);\">\r\n<br>\r\n\r\n<!-- Attending Doctor -->\r\n<input type=\"button\" class=\"butn\" name=\"Doctor\" value=\"Doctor (MRP)\" onclick=\"var hist=\'doctor\'; printKey(hist);\">\r\n<br>\r\n<br>\r\n\r\n</div>\r\n\r\n\r\n<div class=\"DoNotPrint\" >\r\n<input onclick=\"viewsource(this.checked)\" type=\"checkbox\">\r\nHTML Source\r\n<input onclick=\"usecss(this.checked)\" type=\"checkbox\">\r\nUse CSS	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Subject: <input name=\"subject\" id=\"subject\" size=\"40\" type=\"text\">		 \r\n\r\n<table><tr id=sig>\r\n<td> <div id=\"signatureInput\">&nbsp;</div></td>\r\n<td> <div id=\"faxControl\">&nbsp;</div></td>\r\n</tr></table>\r\n \r\n \r\n<input value=\"Submit\" name=\"SubmitButton\" type=\"submit\" onclick=\"saveRTL();  document.RichTextLetter.submit()\">\r\n<input value=\"Print\" name=\"PrintSaveButton\" type=\"button\" onclick=\"document.getElementById(\'edit\').contentWindow.print();saveRTL();  setTimeout(\'document.RichTextLetter.submit()\',1000);\">\r\n<input value=\"Reset\" name=\"ResetButton\" type=\"reset\">\r\n<input value=\"Print\" name=\"PrintButton\" type=\"button\" onclick=\"document.getElementById(\'edit\').contentWindow.print();\">\r\n\r\n\r\n    	</div>\r\n\r\n</form>\r\n\r\n</body></html>',0,0,NULL);

--
-- Dumping data for table `eform_data`
--


--
-- Dumping data for table `eform_groups`
--


--
-- Dumping data for table `eform_values`
--


--
-- Dumping data for table `encounter`
--


--
-- Dumping data for table `encounterForm`
--

INSERT INTO `encounterForm` (`form_name`, `form_value`, `form_table`, `hidden`) VALUES ('2 Minute Walk','../form/form2minwalk.jsp?demographic_no=','form2MinWalk',0),('ADF','../form/formadf.jsp?demographic_no=','formAdf',0),('ADFv2','../form/formadfv2.jsp?demographic_no=','formAdfV2',0),('ALPHA','../form/formalpha.jsp?demographic_no=','formAlpha',0),('Annual','../form/formannual.jsp?demographic_no=','formAnnual',0),('Annual V2','../form/formannualV2.jsp?demographic_no=','formAnnualV2',0);
INSERT INTO `encounterForm` (`form_name`, `form_value`, `form_table`, `hidden`) VALUES ('Health Passport','../form/formbchp.jsp?demographic_no=','formBCHP',0),('Caregiver','../form/formcaregiver.jsp?demographic_no=','formCaregiver',0),('CESD','../form/formCESD.jsp?demographic_no=','formCESD',0),('CHF','../form/formchf.jsp?demographic_no=','formchf',0),('Letterhead','../form/formConsultant.jsp?demographic_no=','formConsult',0),('Cost Questionnaire','../form/formcostquestionnaire.jsp?demographic_no=','formCostQuestionnaire',0),('Falls History','../form/formfalls.jsp?demographic_no=','formFalls',0),('Grip Strength','../form/formgripstrength.jsp?demographic_no=','formGripStrength',0),('Growth 0-36m','../form/formGrowth0_36.jsp?demographic_no=','formGrowth0_36',0),('HOME FAST','../form/formhomefalls.jsp?demographic_no=','formHomeFalls',0),('ImmunAllergies','../form/formimmunallergy.jsp?demographic_no=','formImmunAllergy',0),('Student Intake Hx','../form/formIntakeHx.jsp?demographic_no=','formIntakeHx',0),('Intake Information','../form/formintakeinfo.jsp?demographic_no=','formIntakeInfo',0);
INSERT INTO `encounterForm` (`form_name`, `form_value`, `form_table`, `hidden`) VALUES ('Lab Req','../form/formlabreq.jsp?demographic_no=','formLabReq',0),('FDI Disability','../form/formlatelifeFDIdisability.jsp?demographic_no=','formLateLifeFDIDisability',0),('FDI Function','../form/formlatelifeFDIfunction.jsp?demographic_no=','formLateLifeFDIFunction',0),('Mental Health','../form/formmentalhealth.jsp?demographic_no=','formMentalHealth',0),('MMSE','../form/formmmse.jsp?demographic_no=','formMMSE',0),('ON AR Enhanced','../form/formonarenhanced.jsp?demographic_no=','formONAREnhancedRecord',0),('Pall. Care','../form/formpalliativecare.jsp?demographic_no=','formPalliativeCare',0),('PeriMenopausal','../form/formperimenopausal.jsp?demographic_no=','formPeriMenopausal',0);
INSERT INTO `encounterForm` (`form_name`, `form_value`, `form_table`, `hidden`) VALUES ('Rourke','../form/formrourke.jsp?demographic_no=','formRourke',0),('Rourke2006','../form/formrourke2006.jsp?demographic_no=','formRourke2006',0),('Risk Assessment','../form/formselfadministered.jsp?demographic_no=','formSelfAdministered',0),('Self Efficacy','../form/formselfefficacy.jsp?demographic_no=','formSelfEfficacy',0),('Self Management','../form/formselfmanagement.jsp?demographic_no=','formSelfManagement',0),('SF36','../form/formSF36.jsp?demographic_no=','formSF36',0),('Caregiver - SF36','../form/formSF36caregiver.jsp?demographic_no=','formSF36Caregiver',0),('Treatment Preference','../form/formtreatmentpref.jsp?demographic_no=','formTreatmentPref',0),('T2Diabetes','../form/formtype2diabete.jsp?demographic_no=','formType2Diabetes',0),('HMP Form','../form/HSFOForm2.do?demographic_no=','form_hsfo2_visit',1),('Patient Encounter Worksheet','../form/patientEncounterWorksheet.jsp?demographic_no=','',0),('Vascular Tracker','../form/SetupForm.do?formName=VTForm&demographic_no=','formVTForm',0);
INSERT INTO `encounterForm` (`form_name`, `form_value`, `form_table`, `hidden`) VALUES ('ON AR 2017','../form/formAR2017Record1.jsp?demographic_no=','formONAR2017',0);
INSERT INTO `encounterForm` (`form_name`, `form_value`, `form_table`, `hidden`) VALUES ('Rourke2017', '../form/formrourke2017complete.jsp?demographic_no=', 'formRourke2017', 0);

--
-- Dumping data for table `encounterWindow`
--


--
-- Dumping data for table `encountertemplate`
--

INSERT INTO `encountertemplate` (`encountertemplate_name`, `createdatetime`, `encountertemplate_value`, `creator`) VALUES ('ABDOMINAL PAIN, NOS','0001-01-01 00:00:00','1. Inquiry re type of pain? \r\n2. Inquiry re duration of pain? \r\n3. Inquiry re location of pain? \r\n4. Inquiry re presence/absence of specific food intolerances? \r\n5. Inquiry re presence/absence of GI symptoms? \r\n6. Inquiry re presence/absence of fever? \r\n7. IF female, inquiry re menstrual history? \r\n8. Chest exam? \r\n9. Abdominal exam? \r\n10. Presence/absence of tenderness noted? \r\n11. IF female AND pelvic pain or lower left or right quadrant pain, pelvic exam? \r\n12. IF male AND pelvic pain or lower left or right quadrant pain, rectal exam? \r\n13. Urinalysis AND micro? \r\n14. IF abnormal urine, C & S? \r\n15. IF 2nd episode of abdominal pain NOS, C & S? ','Unknow'),('ACNE VULGARIS','0001-01-01 00:00:00','1. IF on antibiotics (systemic or topical), duration noted on at least 50% of visits? \r\n2. IF on antibiotics (systemic or topical), type noted of visits? \r\n3. Radiation used in treatment by family physicians? \r\n4. Discussion re causes and treatment with patient? \r\n5. IF systemic antibiotics prescribed, follow-up within 6 weeks? \r\n6. IF \"controlled\", follow-up once per year? \r\n7. IF \"severe\" (failure to respond to treatment by family physician within 6 months), referral? ','Unknow'),('ALCOHOLISM','0001-01-01 00:00:00','1. Alcohol intake, amount per day (when drinking)?\r\n2. Duration of problem?\r\n3. Inquiry re time missed from work?\r\n4. Blood pressure yearly?\r\n5. Chest exam yearly?\r\n6. Yearly comment re condition of skin?\r\n7. Abdominal exam yearly?\r\n8. CPE OR CNS examination within past two years?\r\n9. CBC yearly?\r\n10. Three of following done AT LEAST ONCE; serum protein(AG AND total), SGOT, SGPT, alkaline phosphatase,\r\nprothrombin time, bilirubin?\r\n11. Time since last drink before this office visit noted?\r\n12. Initiate education of patient (AA, Alanon, OR note that counselling was done)?\r\n13. Counselling OR referral to alcohol treatment agency for family member(s)?\r\n14. IF first diagnosis within past 2 years, follow-up within one month?','Unknow'),('ALLERGIC REACTION','0001-01-01 00:00:00','1. Inquiry re type OR description of reaction?\r\n2. Inquiry re site of reaction?\r\n3. Inquiry re severity of reaction?\r\n4. Inquiry re possible causes (eg. food, medications, bites, inhalation)?\r\n5. Examination of affected area(s)?\r\n6. IF \"severe\" reaction, heart rate AND rymthm?\r\n7. Blood pressure?\r\n8. Chest exam?\r\n9. Discussion re allergies OR on chart (3 minute)?\r\n10. IF patient has specific drug allergy, bracelet?\r\n11. IF patient has specific drug allergy, is this recorded in a\r\nconsistent area of the chart?','Unknow'),('AMMENORRHEA - PRIMAR','0001-01-01 00:00:00','1. Family history? \r\n2. Growth history? \r\n3. Sexual development history (secondary sexual characteristics)? \r\n4. No period by age 17? \r\n5. Description of breasts, pubic and axillary hair? \r\n6. Pelvic exam OR referral? \r\n7. Referral by age 18? ','Unknow'),('ANEMIA, NYD','0001-01-01 00:00:00','*** NOTE ***\r\nNon-pregnant \r\n1. Inquiry re blood loss? \r\n2. Inquiry re diet? \r\n3. CPE within 6 months? \r\n4. On presenting visit, at least three of following? \r\nblood pressure \r\npulse \r\nabdominal exam \r\nrectal exam \r\n5. Hb OR hematocrit? \r\n6. IF no history of blood loss as cause, blood smear for indices? \r\n7. IF black patient, sickle cell screen? \r\n8. IF male over 19, hemoglobin OR IF female over 17, hemoglobin \r\n9. IF macrocytic indices OR smear (pancytopenia, macro-ovalocytosis, hypersegmentation of neutrophils), folate AND B12 test? \r\n10. IF microcytic indices OR smear microcytic, hypochromic) AND no obvious cause for bleeding, stool for occult blood? \r\n11. IF melena stool OR occult blood positive, barium enema? \r\n12. IF GI symptoms OR upper GI bleeding, UGI series? \r\n13. IF vitamin B12 injections given, documented B12 deficiency?\r\n14. IF iron therapy used, documented iron deficiency? \r\nSerum ferritin OR hemoglobin microcytic smear OR low indices (MCV and MCHC)? ','Unknow'),('ANIMAL BITES','0001-01-01 00:00:00','1. Inquiry re what kind of animal? \r\n2. Inquiry re animal provoked or not? \r\n3. Description of wound? \r\n4. IF no tetanus toxoid within 10 years, injection given? \r\n5. IF animal unprovoked, comment re rabies risk? ','Unknow'),('ANKYLOSING SPONDYLIT','0001-01-01 00:00:00','1. Inquiry re presence/absence of pain? \r\n2. Inquiry re history of stiffness? \r\n3. Yearly comment re stiffness? \r\n4. Yearly comment re range of movement? \r\n5. Yearly comment re presence/absence of deformity? \r\n6. HLA-B27 positive AND X-ray report positive OR consultant\'s report positive? \r\n7. Oral corticosteroids started in primary care? \r\n8. IF on any medication, follow-up yearly? ','Unknow'),('ANXIETY','0001-01-01 00:00:00','1. Statement re symptoms?\r\n2. Inquiry re duration of symptoms?\r\n3. Inquiry re precipitating factors?\r\n4. IF physical complaints noted, evidence of examination of affected area?\r\n5. IF anxiolytic agents used, amount and duration recorded?\r\n6. IF first prescription for medication, follow-up within 2 weeks?\r\n7. Counselling OR referral?','Unknow'),('ARRHYTHMIA (CARDIAC)','0001-01-01 00:00:00','1. Inquiry re frequency of chest discomfort or pain? \r\n2. Inquiry re duration of chest discomfort or pain? \r\n3. Inquiry re frequency of palpitations? \r\n4. Inquiry re duration of palpitations? \r\n5. Inquiry re precipitating factors (coffee, tea, alcohol)? \r\n6. Inquiry re medications taken prior to occurrence? \r\n7. Blood pressure? \r\n8. Cardiac rate AND rhythm? \r\n9. Chest exam? \r\n10. ECG on first visit for this problem? \r\n11. IF on digoxin OR diuretics, electrolytes? \r\n12. IF on digoxin AND new arrhythmia present, digoxin level? \r\n13. ECG OR description of irregularity on chart? \r\n14. IF arrhythmia present at time of examination, treatment with medication OR reassurance OR referral? \r\n15. Advice re precipitating factors (eg. coffee, tea, alcohol, stress factors)? \r\n16. IF paroxysmal atrial tachycardia, inquiry re stress factors? \r\n17. Follow-up until specific diagnosis made OR referral? ','Unknow'),('ARTHRITIS','0001-01-01 00:00:00','(less than one month - multiple joints)\r\n1. Inquiry re duration of symptoms?\r\n2. Location of joint pains noted?\r\n3. Description of nature OR severity of pain?\r\n4. Inquiry re aggravating OR precipitating factors?\r\n5. Description of inflammation OR swelling?\r\n6. Description of range of movement?\r\n7. On OR before second visit for same problem, CBC?\r\n8. On OR before second visit for same problem, ESR?\r\n9. On OR before second visit for same problem, anti-nuclear factor (i.e. ANF, ANA)?\r\n10. On OR before second visit for same problem, rheumatoid arthritis factor (i.e. RF, RA)?\r\n11. Were systemic steroids prescribed?\r\n12. Advice re rest OR restrict movement of joint?\r\n13. Follow-up within 2 weeks?\r\n14. IF within 1 year of visit for peptic ulcer disease, were anti-inflammatory agents prescribed?','Unknow'),('ARTHRITIS, NYD OR NO','0001-01-01 00:00:00','** NOTE **\r\nless than one month - multiple joints \r\n1. Inquiry re duration of symptoms? \r\n2. Location of joint pains noted? \r\n3. Description of nature OR severity of pain? \r\n4. Inquiry re aggravating OR precipitating factors? \r\n5. Description of inflammation OR swelling? \r\n6. Description of range of movement? \r\n7. On OR before second visit for same problem, CBC? \r\n8. On OR before second visit for same problem, ESR? \r\n9. On OR before second visit for same problem, anti-nuclear factor (i.e. ANF, ANA)? \r\n10. On OR before second visit for same problem, rheumatoid arthritis factor (i.e. RF, RA)? \r\n11. Were systemic steroids prescribed? \r\n12. Advice re rest OR restrict movement of joint? \r\n13. Follow-up within 2 weeks? \r\n14. IF within 1 year of visit for peptic ulcer disease, were anti-inflammatory agents prescribed? ','Unknow'),('ARTHRITIS, RHEUMATOI','0001-01-01 00:00:00','** NOTE **\r\nThese questions apply only to PREVIOUSLY DIAGNOSED rheumatoid arthritis. \r\n1. Inquiry re pain? \r\n2. Inqiury re stiffness? \r\n3. Inquiry re fatigue? \r\n4. Yearly comment re swollen joints? \r\n5. Yearly comment re limitation of movement? \r\n6. Follow-up at least once per year? \r\n7. IF patient on NSAIDS OR chloroquine OR penicillamine OR methotrexate OR gold (myochrysine), follow-up at least 2 times per year? \r\n8. Note at least once yearly re how patient coping? \r\n9. Was methotrexate OR gold OR oral corticosteroids started by family doctor (search back 3 months only)? \r\n10. IF taking chloroquine, ophthamological consultation AND evidence of opthalmological follow-up yearly? ','Unknow'),('ASTHMA','0001-01-01 00:00:00','1. Inquiry re previous episodes? \r\n2. Inquiry re family history OR on chart (3 minute)? \r\n3. Inquiry re occupational history OR on chart (3 minute)? \r\n4. Drugs used for asthma recorded? \r\n5. Amount and duration of asthma drugs recorded? \r\n6. Inquiry re allergies OR on chart (3 minute)? \r\n7. Inquiry re duration of current episode? \r\n8. Description of breathing (eg. wheezing, respiratory distress)? \r\n9. Description of breath sounds? \r\n10. IF steroids used in acute attack, was dosage decreased within 10 days? \r\n11. Wheezing present in history or physical exam? \r\n12. IF smoker, advice re smoking? \r\n13. Advice re avoidance of allergens? \r\n14. Advice re avoidance of precipitating factors? \r\n15. IF on medication for an acute episode, follow-up weekly? \r\n16. Was beta-blocker prescribed? \r\n17. Were parasympathomimetics prescribed? ','Unknow'),('ATROPHIC VAGINITIS','0001-01-01 00:00:00','1. Inquiry re at least one of following? \r\ndyspareunia \r\ndysuria \r\nspotting \r\nvaginal itch \r\n2. Description of vulva AND/OR vagina? \r\n3. Pap smear for karyopyknotic index? \r\n4. IF dysuria, urinalysis AND micro? \r\n5. Vaginal C & S? \r\n6. IF topical agent used, was it Premarin/conjugated estrogen OR dienestrol cream? \r\n7. IF oral estrogen therapy used, follow-up within one year? \r\n8. IF sexual dysfunction OR dyspareunia identified, counselling? ','Unknow'),('BASAL AND SQUAMOUS C','0001-01-01 00:00:00','1. Inquiry re duration of lesion?\r\n2. Location of lesion noted?\r\n3. Size of lesion noted?\r\n4. Surgical pathology biopsy OR referral?\r\n5. IF not referred, pathology report positive?\r\n6. Excision OR dessication OR cryosurgery OR referral?\r\n7. IF not referred, follow-up within 1 month?','Unknow'),('BILIARY COLIC','0001-01-01 00:00:00','1. Inquiry re at least three of following?\r\npain, description\r\nAND\r\nlocation\r\nfood intolerance\r\nrecurrence\r\nfever\r\n2. Abdominal exam?\r\n3. Chest exam?\r\n4. Heart rate AND rhythm?\r\n5. Blood pressure?\r\n6. CBC?\r\n7. SGOT, serum bilirubin, alkaline phosphatase?\r\n8. Gall bladder X-ray OR ultrasound?\r\n9. Advice re low-fat diet?\r\n10. One follow-up within 1 month?\r\n11. IF recurrent (2nd or greater episode), referral?','Unknow'),('BLEPHARITIS','0001-01-01 00:00:00','1. Inquiry re symptoms?\r\n2. Duration of symptoms noted?\r\n3. Fluorinated steroids used?\r\n4. Advice re eye care?','Unknow'),('BREAST LUMP','0001-01-01 00:00:00','1. Inquiry duration? \r\n2. Inquiry re presence/absence of pain? \r\n3. Inquiry re changes relative to menstrual cycle? \r\n4. Size of lump noted? \r\n5. Location of lump noted, specific description OR diagram?\r\n6. Presence/absence of axillary nodes? \r\n7. Referral OR follow-up visit within 4 weeks? \r\n8. IF not previously referred AND lump has not changed OR is larger, one of following done? \r\nreferral \r\naspiration \r\nmammogram \r\nexcision ','Unknow'),('BRONCHITIS,ACUTE','0001-01-01 00:00:00','1. Comment re cough? \r\n2. Comment re sputum? \r\n3. Chest exam? \r\n4. Temperature recorded? \r\n5. IF antibiotics used, dose AND duration recorded (2/3 of the time)? \r\n6. IF smoker, advice re smoking? \r\n7. IF narcotic syrup used, was it prescribed more than once within 30 days? ','Unknow'),('BRONCHITIS,CHRONIC','0001-01-01 00:00:00','1. Occupation on chart (3 minute)? \r\n2. Smoking history on chart (3 minute)? \r\n3. Cough productive OR note re presence/absence of change in amount of sputum? \r\n4. Chest breath sounds? \r\n5. CPE at least every two years with detailed description of chest (3 of 6 respiratory signs)? \r\n6. Chest X-ray (2 views) within 3 years? \r\n7. IF patient fails to improve after 21 days continuous medication, chest X-ray? \r\n8. Does patient produce sputum 6 months of the year? \r\n9. IF antibiotics used, dose AND durtion recorded (2/3 of visits)? \r\n10. IF smoker, advice re smoking? \r\n11. Follow-up twice per year? \r\n12. Sedatives, hypnotics, narcotics or antihistamines used? ','Unknow'),('BRONCHOPNEUMONIA','0001-01-01 00:00:00','1. One of more of following?\r\ncough\r\ndyspnea (shortness of breath)\r\nfever\r\n2. Duration of symptoms noted?\r\n3. Chest exam?\r\n4. Rales in chest?\r\n5. Chest X-ray within one day of diagnosis?\r\n6. IF patient has not improved within 7 days, chest X-ray?\r\n7. IF initial X-ray is positive, repeat within 30 days?\r\n8. Positive X-ray OR rales on examination?\r\n9. IF antibiotics used, dose AND duration recorded, (2/3 of visits)?\r\n10. IF X-ray indicates mycopolasma pneumonia, tetracycline or erythromycin used?\r\n11. Follow-up within one week?','Unknow'),('BURSITIS','0001-01-01 00:00:00','1. Inquiry re pain OR swelling? \r\n2. Inquiry re location? \r\n3. Inquiry re duration? \r\n4. Description of site of lesion (eg. redness, swelling, fluctuation)? \r\n5. IF infected OR if aspirated OR if I&D done, specimen sent for C&S? \r\n6. IF NSAID prescribed, one follow-up within 1 month? ','Unknow'),('CELLULITIS','0001-01-01 00:00:00','1. Inquiry re duration? \r\n2. Site of lesion noted? \r\n3. Extent/size of lesion noted? \r\n4. Temperature recorded? \r\n*** NOTE *** \r\nIF the lesion is larger than 5 inches in diameter OR this is the third or more episode, then questions 5 through 8 apply. \r\n5. IF above, WBC on chart? \r\n6. IF above, urinalysis on chart? \r\n7. IF above, C & S of lesion? \r\n8. IF above, fasting blood sugar within one year? \r\n9. Antibiotics used for at least 7 days? \r\n10. IF antibiotic used, type recorded? \r\n11. IF antibiotic used, amount recorded? \r\n12. Follow-up within 7 days? ','Unknow'),('CEREBRAL CONCUSSION','0001-01-01 00:00:00','1. Type of trauma described? \r\n2. Comment re severity of injury? \r\n3. Time since injury? \r\n4. Presence/absence of change in sensorium since injury? \r\n5. History of loss of consciousness? \r\n6. Neurological exam? \r\n7. Examination of site of injury? \r\n8. Skull X-ray? \r\n9. IF patient not admitted, head injury routine sheet OR instructions? \r\n10. Narcotics or sedatives used? \r\n11. Admission to hospital OR referral? ','Unknow'),('CERVIX, CARCINOMA IN','0001-01-01 00:00:00','1. Inquiry re vaginal discharge, within one month?\r\n2. Inquiry re presence/absence of vaginal spotting, within one month?\r\n3. Description of cervix, within one month?\r\n4. Positive Pap smear?\r\n5. IF class IV smear or worse, referral within one month?','Unknow'),('CHEST PAIN-NYD (>18','0001-01-01 00:00:00','1. Location of pain noted? \r\n2. Duration of pain noted? \r\n3. Response to exercise OR posture noted? \r\n4. History of cough OR response to breathing noted? \r\n5. Response to time of eating OR type of food noted? \r\n6. Chest exam? \r\n7. Blood pressure? \r\n8. Heart rate AND rhythm? \r\n9. Presence/absence of chest wall tenderness noted? \r\n10. IF exercise related AND chest not tender, ECG done within 3 days? \r\n11. IF rales OR rhonchi OR dullness in chest, X-ray ordered within 3 days? \r\n12. Statement that there is no cardiac cause OR ECG normal, on this visit OR follow-up within one month? ','Unknow'),('CHICKEN POX','0001-01-01 00:00:00','1. Inquiry re duration of symptoms? \r\n2. Description of rash? \r\n3. Blister OR papular OR vesicular rash? \r\n4. ASA used? ','Unknow'),('CHRONIC PROSTATITIS','0001-01-01 00:00:00','1. Inquiry re at least 3 of following? \r\ndysuria\r\nfrequency\r\nperineal pain\r\npainful sexual activity\r\nurethral discharge \r\nlow back pain\r\nnocturia \r\n2. Abdominal exam? \r\n3. Rectal exam?\r\n4. Description of prostate (size and consistency)? \r\n5. Urine C & S? \r\n6. Septra OR tetracycline OR ampicillin OR\r\nerythromycin used? \r\n7. Antibiotic used for at least 2 weeks?\r\n8. One follow-up? \r\n9. IF symptoms continue beyond one month OR\r\npyuria for more than one month OR  bacteriuria for more than one month, consultation and/or referral? ','Unknow'),('CLUSTER HEADACHE','0001-01-01 00:00:00','1. History of attacks in clusters? \r\n2. Attacks acute AND short duration AND recurring several times in 24 hours? \r\n3. Description of headache including two of following? \r\nfacial flushing OR sweating \r\nunilateral lacrimation \r\nnasal congestion \r\n4. Blood pressure? \r\n5. Neurological exam, including note re cranial nerves? \r\n6. One follow-up within 6 months? \r\n7. IF on medication, one follow-up within one month? ','Unknow'),('CONGESTIVE HEART FAI','0001-01-01 00:00:00','1. Inquiry re at least two of following? \r\nshortness of breath \r\nswollen ankles \r\nparoxysmal nocturnal dyspnea \r\nexercise intolerance \r\n2. Current medication list? [HA2 ]> \r\n3. Chest exam? \r\n4. Weight recorded on at least 50% of visits? \r\n5. Blood pressure? \r\n6. Comment on ankles OR jugular venous pressure (J.V.P. or J.V.D.)? \r\n7. Heart rate AND rhythm? \r\n8. ECG within 1 year prior OR within 2 weeks after first diagnosis? \r\n9. IF on diuretics, electrolytes done on 50% of visits? \r\n10. BUN done on 50% of visits? \r\n11. Hemoglobin OR indices (hematocrit, MCV, MCHC) done on 50% of visits? \r\n12. Diuretics prescribed? \r\n13. IF on diuretics, amount and duration recorded? \r\n14. Rest recommended? \r\n15. Advice re diet (eg. low salt)? \r\n16. Follow-up weekly until physician notes \"improved\" or \"stable\"? \r\n17. Narcotics prescribed? ','Unknow'),('CONJUNCTIVITIS','0001-01-01 00:00:00','1. Inquiry re itching OR discharge?\r\n2. Inquiry re duration?\r\n3. Description of conjunctiva?\r\n4. IF ophthalmic steroids used, was cornea stained with fluorescein?','Unknow'),('CONSTIPATION, RECURR','0001-01-01 00:00:00','*** NOTE ***\r\nPatient over 30 years old with a prior history of constipation. \r\n1. Inquiry re change in bowel movement? \r\n2. Inquiry re diet? \r\n3. Inquiry re drugs? \r\n4. Abdominal exam? \r\n5. Rectal exam? \r\n6. Stool for occult blood? \r\n7. IF less than 3 months duration, barium enema? \r\n8. Infrequent AND/OR difficult bowel movements? \r\n9. Instructions re increase in roughage OR fibre OR bran? \r\n10. One follow-up OR specific diagnostic statement within 3 months? ','Unknow'),('CONTACT DERMATITIS','0001-01-01 00:00:00','** NOTE **\r\nIncludes poison ivy. \r\n1. Inquiry re duration? \r\n2. Inquiry re itching? \r\n3. Inquiry re exposure to irritants? \r\n4. Location of rash noted? \r\n5. IF oral prednisone used, no more than 7 days? \r\n6. IF oral prednisone used, one follow-up visit or phone call? ','Unknow'),('CORONARY ARTERY DISE','0001-01-01 00:00:00','1. Comment on one of the following with each visit?\r\nangina\r\nshortness of breath\r\nankle edema\r\n2. Yearly comment on pain OR nitroglycerines taken?\r\n3. Yearly comment on exercise tolerance?\r\n4. Blood pressure of each visit for this diagnosis (at least 75%)?\r\n5. One CPE by family physician in 2 years?\r\n6. ECG on chart within 2 years?\r\n7. Drug list every 12 months?\r\n8. Dosage of prescribed drugs every 12 months (at least 75%)?\r\n9. IF obesity noted, advice re weight loss?\r\n10. Follow-up at least twice per year?\r\n11. IF congestive heart failure AND use of non-steroidal anti-inflammatory agents OR beta-blockers OR calcium channel blockers, was there a justification statement?','Unknow'),('CYSTITIS','0001-01-01 00:00:00','1. Inquiry re urinary symptoms, one or more of following? \r\nurgency \r\nfrequency \r\ndysuria \r\nhematuria \r\n2. Inquiry re duration of symptoms? \r\n3. Urine dip for protein AND blood OR urinalysis OR urine culture? \r\n4. Positive culture OR two of following present? \r\nurgency \r\nfrequency \r\ndysuria \r\nhematuria \r\n5. Antibiotic used AND was it one of the sulfas, ampicillin, Septra/Bactrim, or tetracycline? \r\n6. One follow-up AND repeat urinalysis OR\r\nculture? \r\n7. Was a negative culture on chart at end of treatment? \r\n8. Was streptomycin or chloromycetin used? ','Unknow'),('CYSTITIS, RECURRENT','0001-01-01 00:00:00','1. Comment re any urinary symptoms?\r\n2. Urinalysis or dipstick?\r\n3. Urine for C & S?\r\n4. BUN on chart (3 minute)?\r\n5. IF 3 or more episodes within 3 months, urine culture for TB (acid-fast bacilli)?\r\n6. At least one urinary symptom present OR positive culture?\r\n7. IF culture done, do antibiotics reflect culture \r\nsensitivities?\r\n8. IF child with 2 or more UTI, IVP AND voiding cystogram, OR referral?\r\n9. IF adult female with 3 or more culture proven UTI within\r\n2 years, IVP AND (BUN or Creatinine) OR referral?\r\n10. IF abnormal IVP OR (BUN or Creatinine), referral?','Unknow'),('DDD, CERVICAL','0001-01-01 00:00:00','1. Inquiry re neck pain?\r\n2. Inquiry re presence/absence of trauma?\r\n3. Inquiry re one of following?\r\npain referred to shoulder and arm muscle weakness of forearm paresthesia\r\n4. Comment on reflexes in arms?\r\n5. Comment on presence/absence of weakness in upper extremity muscles?\r\n6. Comment re range of movement of neck OR within 1 year?\r\n7. Cervical spine X-ray on chart (3 minute)?\r\n8. Positive X-ray diagnosis?\r\n9. IF first visit for this episode, follow-up within 6 weeks?\r\n10. Cervical collar used continuously for more than 1 month?','Unknow'),('DEAFNESS','0001-01-01 00:00:00','1. Inquiry re duration of hearing loss?\r\n2. Inquiry re trauma OR infection OR industrial exposure, on chart (3 minute)?\r\n3. Comment on ear drums at least once per year?\r\n4. Audiogram OR referral to ENT on chart (3 minute)?','Unknow'),('DEGENERATIVE ARTHRIT','0001-01-01 00:00:00','1. Were oral corticosteroids (steroids) used? ','Unknow'),('DEGENERATIVE DISC DI','0001-01-01 00:00:00','1. Inquiry re low back pain, at least one of following? \r\nduration \r\nlocation \r\nradiation \r\n2. Comment on movement of back, at least one of following? \r\nflexion \r\nextension \r\nlateral flexion \r\nrotation \r\n3. Lumbar X-ray (3 views) on chart (3 minute)? \r\n4. Positive X-ray of lumbar spine on chart (3 minute)? \r\n5. IF narcotic analgesic used, justification statement? \r\n6. Back exercises AND/OR back care instructions? ','Unknow'),('DEPRESSION','0001-01-01 00:00:00','1. Inquiry re medications/drugs taken?\r\n2. Inquiry re duration of problem?\r\n3. Inquiry re suicidal thoughts OR statement that depression is mild or minor?\r\n4. IF physical complaints noted, evidence of examination of affected area?\r\n5. CPE within 2 years?\r\n6. Comment on mood OR appearance OR affect?\r\n7. IF antidepressant given, follow-up within 2 weeks?\r\n8. IF first prescription for antidepressant, was duration noted AND was duration\r\n9. IF no antidepressants given, follow-up within 1 month?\r\n10. IF \"suicidal\", referral OR hospitalization?\r\n11. Discussion re stress factors?\r\n12. Were barbiturates prescribed?','Unknow'),('DERMATOPHYTOSIS - RI','0001-01-01 00:00:00','1. Site noted? \r\n2. Extent noted? \r\n3. IF griseofulvin prescribed, skin scraping for C & S? \r\n4. Topical antifungal agent used? \r\n5. IF griseofulvin used, were topical antifungal agents tried for 1 month first? \r\n6. One follow-up within 3 weeks? \r\n7. IF griseofulvin used, CBC within 3 months? ','Unknow'),('DIABETES MELLITUS, A','0001-01-01 00:00:00','1. Inquiry re family history of diabetes on chart (3 minute)? \r\n2. Duration of disease OR starting date on chart (3 minute)? \r\n3. Inquiry re one of following on each visit? \r\nurine sugars \r\nblood sugars \r\ndietary management \r\npatient feels well or ill \r\n4. Weight recorded (at least 75% of visits)? \r\n5. Urine glucose each visit? \r\n6. Comment re cardiovascular system AND blood pressure yearly? \r\n7. Examination of fundi yearly? \r\n8. IF on oral hypoglycemics, at least one blood sugar recorded yearly? \r\n9. IF on insulin, at least two blood sugars recorded yearly? \r\n10. BUN OR creatinine on chart (3 minute)? \r\n11. IF diabetes first diagnosed within past 2 years, evidence of 2 fasting blood sugars > 8.8 mmol/L OR random sugar > 13.8 mmol/L prior to treatment? \r\n12. Diabetic diet - caloric intake noted on chart (3 minute)? \r\n13. Evidence of dietary counselling by a health professional on chart (3 minute)? \r\n14. IF newly diagnosed, follow-up within one month? \r\n15. IF on diet alone, follow-up at least once yearly? \r\n16. IF on oral hypoglycemic OR insulin, follow-up at least twice yearly? \r\n17. Inquiry re sexual dysfunction on chart (3 minute)? \r\n18. IF acetohexamide or chlorpropramide used (Glyburide and Diabeta are OK), was BUN > 9 mmol/L OR was creatinine > 140 mmol/L? \r\n19. IF no ketones in serum or urine, was dietary therapy tried prior to starting oral hypoglycemic? ','Unknow'),('DIABETES MELLITUS, J','0001-01-01 00:00:00','1. At least every 6 months, comment re one of following? \r\npolyuria \r\npolydipsia \r\nweight loss \r\n2. Description of fundi at least once yearly OR evidence on chart (3 minute) that patient is followed by an opthalmologist? \r\n3. Yearly fasting blood sugar? \r\n4. Urinalysis on at least 75% of visits? \r\n5. Insulin dosage noted at least once yearly? \r\n6. Evidence that home monitoring of urine glucose OR blood glucose is occurring? \r\n7. Evidence of dietary counselling (CDA diet or diabetic education centre referral) on chart (3 minute)? \r\n8. Follow-up at least twice yearly? \r\n9. Evidence of discussion re effects on normal life (eg. family, friends, activities) at least once yearly? ','Unknow'),('DIABETES MELLITUS, T','0001-01-01 00:00:00','1. Inquiry re family history of diabetes on chart (3 minute)?\r\n2. Duration of disease OR starting date on chart (3 minute)?\r\n3. Inquiry re one of following on each visit? \r\nurine sugars blood sugars dietary management patient feels well or ill\r\n4. Weight recorded (at least 75% of visits)?\r\n5. Urine glucose each visit?\r\n6. Comment re cardiovascular system AND blood pressure yearly?\r\n7. Examination of fundi yearly?\r\n8. IF on oral hypoglycemics, at least one blood sugar recorded yearly?\r\n9. IF on insulin, at least two blood sugars recorded yearly?\r\n10. BUN OR creatinine on chart (3 minute)?\r\n11. IF diabetes first diagnosed within past 2 years, evidence of 2 fasting blood sugars > 8.8 mmol/L OR random sugar > 13.8 mmol/L prior to treatment?\r\n12. Diabetic diet - caloric intake noted on chart (3 minute)?\r\n13. Evidence of dietary counselling by a health professional on chart (3 minute)?\r\n14. IF newly diagnosed, follow-up within one month?\r\n15. IF on diet alone, follow-up at least once yearly?\r\n16. IF on oral hypoglycemic OR insulin, follow-up at least twice yearly?\r\n17. Inquiry re sexual dysfunction on chart (3 minute)?\r\n18. IF acetohexamide or chlorpropramide used (Glyburide and Diabeta are OK), was BUN > 9 mmol/L OR was creatinine > 140 mmol/L?\r\n19. IF no ketones in serum or urine, was dietary therapy tried prior to starting oral hypoglycemic?','Unknow'),('DIAPER RASH','0001-01-01 00:00:00','1. Inquiry re duration?\r\n2. Description of rash?\r\n3. IF monilia, comment on mouth?\r\n4. IF monilia, topical antifungal used?\r\n5. Discussion re cleaning at diaper changing?\r\n6. IF \"severe\", follow-up within 1 month?\r\n7. Were fluorinated steroids used?\r\n8. IF thrush also present, oral mycostatin used?','Unknow'),('DIARRHEA, MULTIPLE V','0001-01-01 00:00:00','1. Inquiry re frequency? \r\n2. Inquiry re duration? \r\n3. Inquiry re diet? \r\n4. Inquiry re medications? \r\n5. Inquiry re travel? \r\n6. Inquiry re blood in stool? \r\n7. Inquiry re fever? \r\n8. Inquiry re weight loss? \r\n9. Inquiry re nausea OR abdominal cramps OR pain? \r\n10. Abdominal exam? \r\n11. Rectal exam? \r\n12. Weight noted at least once? \r\n13. Stool for C & S? \r\n14. Stool for ova and parasites? \r\n15. CBC? \r\n16. ESR? \r\n17. Sigmoidoscopy OR colonoscopy OR referral? \r\n18. Barium enema? \r\n19. IF barium enema negative, UGI series with small bowel follow through? \r\n20. IF not improved within 6 months OR specific diagnosis not noted on chart, referral? ','Unknow'),('DIVERTICULITIS','0001-01-01 00:00:00','1. Inquiry re abdominal pain?\r\n2. Inquiry re at least one of following?\r\nconstipation\r\ndiarrhea\r\nrectal bleeding\r\nregularity\r\n3. Inquiry re food intolerances?\r\n4. Abdominal exam?\r\n5. Rectal exam?\r\n6. Stool for occult blood OR within 1 year?\r\n7. Barium enema on chart (3 minute)?','Unknow'),('DIZZINESS, NYD','0001-01-01 00:00:00','1. Inquiry re details of episode?\r\n2. Inquiry re duration of episode?\r\n3. Inquiry re presence/absence of precipitating factors?\r\n4. Inquiry re presence/absence of medications?\r\n5. Blood pressure?\r\n6. Heart rate AND rhythm?\r\n7. Ear exam?\r\n8. Comment on Rhomberg OR reflexes OR nystagmus?\r\n9. IF on diuretics, electrolytes tested?\r\n10. IF problem persists, on second visit blood sugar AND CBC?\r\n11. IF heart irregular, ECG OR Holter monitor?\r\n12. IF condition persists for more than 3 months AND specific diagnosis is made, referral?','Unknow'),('DYSMENORRHEA','0001-01-01 00:00:00','1. Menstrual history?\r\n2. Inquiry re urinary symptoms?\r\n3. Inquiry re painful periods?\r\n4. IF sexually active, pelvic exam with comment on cervix?\r\n5. Abdominal exam?\r\n6. IF vaginal discharge present, C & S?\r\n7. Follow-up once within 4 months?','Unknow'),('DYSPLASIA OF CERVIX','0001-01-01 00:00:00','1. Pap smear at least yearly? \r\n2. IF uterus not removed, yearly follow-up? \r\n3. IF present less than one year, record of follow-up time? ','Unknow'),('ECTOPIC PREGNANCY','0001-01-01 00:00:00','1. Inquiry re presence/absence of lower abdominal pain?\r\n2. Inquiry re date of last menstrual period?\r\n3. Inquiry re presence/absence of vaginal bleeding?\r\n4. Pelvic exam?\r\n5. Blood pressure AND pulse?\r\n6. IF purulent vaginal discharge, C & S?\r\n7. Abdominal exam?\r\n8. Pregnancy test?\r\n9. IF pregnancy test negative, Beta-HCG?\r\n10. IF not referred or admitted, pelvic ultrasound?\r\n11. Positive pregnancy test OR positive Beta-HCG?\r\n12. Referral OR admission?','Unknow'),('ECZEMA, CONTACT DERM','0001-01-01 00:00:00','1. Inquiry re duration? \r\n2. Presence/absence of family history of eczema OR on chart (3 minute)? \r\n3. IF over 5 years, inquiry re stress factors? \r\n4. Description of lesion? \r\n5. Location and extent? \r\n6. Topical steroids used? \r\n7. Systemic steroids initiated by family doctor? \r\n8. Discussion re prognosis of disease? \r\n9. One follow-up? \r\n10. IF acute AND failure to respond within 6 weeks, referral?\r\n11. IF child, occulsive dressing for 8 hours or more per 24 hours? \r\n12. IF systemic corticosteroids used, was it for more than 3 months? \r\n13. Fluorinated steroids used on face? ','Unknow'),('EPICONDYLITIS','0001-01-01 00:00:00','1. Inquiry re duration? \r\n2. Inquiry re causes? \r\n3. Palpation, findings noted? \r\n4. Localized pain present? \r\n5. Tenderness on palpation of site present? \r\n6. Advice re avoidance of activity that caused or precipitated problem? ','Unknow'),('EPILEPSY','0001-01-01 00:00:00','1. Type AND description of seizures? \r\n2. Frequency of seizures noted? \r\n3. Time of occurrence of seizures noted (eg. day, night, at work, at school, etc.)? \r\n4. Inquiry re precipitating factors on chart (3 minute)? \r\n5. Inquiry re family history of seizure disorder on chart (3 minute)? \r\n6. Neurological exam on chart (3 minute)? \r\n7. EEG on chart (3 minute)? \r\n8. IF neurological exam \"abnormal\", CAT scan on chart (3 minute) OR referral? \r\n9. Description of seizure by witness on chart (3 minute)? \r\n10. Names of drug(s) AND dosage? \r\n11. Discussion re dangerous activities (eg. driving car, working with machinery, etc.) on chart (3 minute)? \r\n12. Discussion re precipitating factors? \r\n13. IF seizures persist (more than one per week), referral? ','Unknow'),('FAMILY PLANNING - FE','0001-01-01 00:00:00','1. Inquiry re 3 of following? \r\npregnancies \r\nabortions \r\nmenstrual history \r\ngynecological surgery \r\nhistory of PID \r\nsmoking history (# of cigarettes per day) \r\nthrombophlebitis \r\nheadaches (migraines) OR\r\nno risk factors statement? \r\n2. Blood pressure recorded? \r\n3. Pelvic exam? \r\n4. Pap smear within one year of starting birth control? \r\n5. IF on birth control pill or IUD, pap smear yearly? \r\n6. IF on birth control pill, OR justification statement? \r\n7. IF patient smokes more than 15 cigarettes per day OR is > 35 years old, oral contraceptives used? \r\n8. IF history of PID OR nulliparous, IUD used? \r\n9. IF smoker, advice re smoking? \r\n10. Breast self-examination (BSE) noted? \r\n11. Discussion of all methods of contraception on chart? ','Unknow'),('FATIGUE, NYD (> 15 Y','0001-01-01 00:00:00','1. Inquiry re duration? \r\n2. Inquiry re relation to physical activity? \r\n3. Inquiry re presence/absence of diurnal variation? \r\n4. Inquiry re personal habits (alcohol, drugs)? \r\n5. Inquiry re stress factors? \r\n6. Inquiry re symptoms of depression (early morning wakening, feeling of worthlessness, weight loss, suicidal thoughts)? \r\n7. IF no positive findings in questions 4, 5 and/or 6 above, general assessment within 6 months? \r\n8. Hemoglobin? \r\n9. Urinalysis and micro? \r\n10. IF mention of abnormal thyroid, T4 OR TSH done? \r\n11. IF patient is on diuretics, electrolyte levels recorded? \r\n12. Drug treatment started before definitive diagnosis? \r\n13. One follow-up within 6 weeks? ','Unknow'),('FEBRILE CONVULSION,','0001-01-01 00:00:00','1. Description of convulsion? \r\n2. Total time for convulsion noted? \r\n3. Inquiry re previous history of convulsions? \r\n4. Inquiry re fever in preceding 24 hours? \r\n5. Inquiry re illness in preceding 24 hours? \r\n6. Temperature recorded? \r\n7. Presence/absence of neck stiffness noted? \r\n8. ENT exam? \r\n9. Chest exam? \r\n10. Fever within previous 24 hours? \r\n11. IF temperature > 38 C (100.4 F), antipyretics OR instructions re sponging? \r\n12. IF bacterial cause of fever identified, antibiotics used? \r\n13. Discussion re fever therapy (fluids OR sponging OR antipyretics)? \r\n14. Follow-up within two weeks? \r\n15. IF convulsion lasts more than 20 minutes, admission OR immediate referral? \r\n16. Tetracycline used? ','Unknow'),('FIBROCYSTIC DISEASE','0001-01-01 00:00:00','1. Inquiry re at least 2 of the following? \r\nbreast pain \r\nrelationship of lump to periods \r\nrecurrency of problem \r\nlocation of lump \r\n2. Description of both breasts? \r\n3. Statement of location and size of lumps? \r\n4. Axillary exam? \r\n5. IF lesion diagnosed as non-cystic, mammography? \r\n6. IF suspected cyst, aspiration OR referral? \r\n7. Yearly breast examination by physician following initial diagnosis? \r\n8. Cysts diagnosed by examination OR by mammography? \r\n9. BSE on chart every two years? \r\n10. IF discrete lump persists after aspiration, referral? ','Unknow'),('FIBROMYOSITIS','0001-01-01 00:00:00','1. Inquiry re pain, description AND location?\r\n2. Inquiry re aggrravating AND/OR relieving factors?\r\n3. Inquiry re duration?\r\n4. Inquiry re sleep patterns?\r\n5. Inquiry re symptoms of fatigue AND/OR possible depression?\r\n6. Description of areas of pain?\r\n7. IF trigger point(s) noted, location(s)\r\n8. Hemoglobin AND sed rate within 6 months?\r\n9. Oral steroids used?\r\n10. Discussion re stress factors OR on chart (3 minute)?','Unknow'),('FOLLICULITIS','0001-01-01 00:00:00','1. Inquiry re first or recurrent episode? \r\n2. Description of eruption? \r\n3. Location noted? \r\n4. IF recurrent (3 or more episodes in 1 year), C & S? \r\n5. IF recurrent (3 or more episodes in 1 year), serum glucose OR fasting blood sugar OR glucose tolerance test? \r\n6. IF oral antibiotics used, dosage AND duration recorded? \r\n7. IF folliculitis on face AND male > 16, advice re shaving? \r\n8. IF oral antibiotics used, one follow-up?','Unknow'),('FOREIGN BODY IN NOSE','0001-01-01 00:00:00','1. Inquiry re how foreign body got into nose? \r\n2. Inquiry re which side is affected? \r\n3. IF removed, description of foreign body? \r\n4. IF foreign body not removed, referral to ENT specialist within 24 hours? ','Unknow'),('FRACTURES','0001-01-01 00:00:00','1. Description of accident?\r\n2. Time since accident noted?\r\n3. Place of accident (eg. work related)?\r\n4. Description of fracture including presence/absence of deformity?\r\n5. Presence/absence of swelling?\r\n6. Comment re involvement of neurovascular structures?\r\n7. X-ray of fracture site?\r\n8. IF displaced, evidence of reduction OR referral?\r\n9. Immobilization?\r\n10. IF cast applied to extremity, follow-up within 48 hours?\r\n11. One follow-up?','Unknow'),('GASTRITIS - HYPERACI','0001-01-01 00:00:00','1. Inquiry re location of abdominal pain? \r\n2. Inquiry re duration of abdominal pain? \r\n3. Inquiry re type of abdominal pain? \r\n4. Inquiry re aggravating causes (eg. food, smoking, alcohol, stress, drugs (ASA))? \r\n5. Inquiry re vomiting OR hematemesis? \r\n6. Abdominal exam? \r\n7. Advice re avoidance of aggravating factors (eg. smoking, spices, alcohol, etc.)? \r\n8. Discussion of stress factors? \r\n9. NSAIDs OR ASA OR cortisone used? ','Unknow'),('GASTROENTERITIS AND','0001-01-01 00:00:00','1. Inquiry re presence/absence of vomiting? \r\n2. IF vomiting, frequency AND amount noted? \r\n3. Inquiry re frequency AND consistency AND mucus of stools? \r\n4. Inquiry re presence/absence of blood in stools? \r\n5. Inquiry re duration of symptoms? \r\n6. Inquiry re travel history? \r\n7. Abdominal exam? \r\n8. IF child \r\n9. Comment re presence/absence of dehydration? \r\n10. IF failure to respond in 2 days, CBC? \r\n11. IF failure to respond in 2 days, stool cultures? \r\n12. IF failure to respond in 2 days, electrolytes? \r\n13. IF failure to respond in 2 days, stool for occult blood? \r\n14. IF gastroenteritis, presence of diarrhea and vomiting recorded? \r\n15. Antispasmodics OR narcotic antidiarrheals OR antibiotics used? \r\n16. Discussion re avoidance of citrus juices and milk? ','Unknow'),('GLAUCOMA','0001-01-01 00:00:00','1. Inquiry re vision at each visit? \r\n** NOTE **\r\nIF patient is followed by an ophthalmologist, Questions 2 through 8 are NOT APPLICABLE. \r\n2. Inquiry re compliance with medications? \r\n3. Fundi, yearly statement re optic cup? \r\n4. Visual fields recorded yearly? \r\n5. Intraocular pressure yearly? \r\n6. Medications, dosage recorded? \r\n7. High intraocular pressure ( >30 mm Hg ) recorded on chart (3 minute)? \r\n8. Follow-up yearly? \r\n9. IF ocular pressures are not improved after one month of treatment, referral? ','Unknow'),('GLOMERULONEPHRITIS','0001-01-01 00:00:00','1. Inquiry re urination on each visit?\r\n2. Blood pressure?\r\n3. Weight?\r\n4. Urinalysis, routine AND micro yearly?\r\n5. Creatinine yearly?\r\n6. BUN yearly?\r\n7. Creatinine clearance yearly?\r\n8. Serum proteins yearly?\r\n9. Hemoglobin yearly?\r\n10. One of following?\r\nproteinemia reports on chart\r\ngranular casts\r\nrenal biopsy report on chart\r\n11. Follow-up at least yearly?','Unknow'),('GONORRHEA','0001-01-01 00:00:00','1. Inquiry re time since exposure?\r\n2. Inquiry re sexual contacts?\r\n3. Inquiry re symptoms (discharge, dysuria)?\r\n4. Inquiry re sexual preferences and habits?\r\n5. Genital exam?\r\n6. IF oral sex noted, throat exam?\r\n7. IF anal sex noted, rectal exam?\r\n8. C & S, genital?\r\n9. IF indicated by history, C & S oral AND/OR rectal?\r\n10. Positive culture AND/OR gramstain?\r\n11. Antibiotics according to recommendations of Dept of Health (see list)?\r\n12. One follow-up with repeat cultures within 1 month?\r\n13. Counselling re prevention?\r\n14. Presence/absence of penicillin allergy noted on chart (3 minute)?\r\n15. Refer to Public Health Dept. OR insure follow-up of sexual contacts?\r\n16. VDRL in 6 weeks and 3 months?','Unknow'),('GOUT','0001-01-01 00:00:00','1. Inquiry re at least one of following? \r\nsevere joint pain \r\nhistory of swelling \r\nhistory of inflammation \r\nmonoarticular joint \r\n2. List of drugs being used OR on chart (3 minute)? \r\n3. Presence/absence of swelling of involved joint? \r\n4. Presence/absence of inflammation of involved joint? \r\n5. IF joint aspiration done, report for uric acid crystals? \r\n6. Serum uric acid? \r\n7. One of the following? \r\nserum uric acid greater than lab normal \r\nuric acid crystals in joint aspirate \r\nX-ray diagnosis \r\n8. ASA used? \r\n9. NSAIDs OR Colchicine used? \r\n10. IF thiazides used, statement of justification? \r\n11. IF 3 or more episodes OR uric acid greater than lab normal, recommendation for prophylaxis treatment? \r\n12. Advice re avoidance of precipitating factors (eg. alcohol, high purine foods) \r\n13. IF flare-up occurs AND allopurinal OR uricosurics are being used, Colchicine used? ','Unknow'),('HAY FEVER','0001-01-01 00:00:00','1. Inquiry re seasonal complaint?\r\n2. Inquiry re precipitating factors (e.g. ragweed, grass etc.)?\r\n3. One of following present; sneezing, rhinorrhea, nasal congestion?\r\n4. Examination of nose?\r\n5. Seasonal occurrence of nasal congestion?\r\n6. Discussion re air conditioning OR air filters?\r\n7. Discussion re avoidance of plants and pollen specific to patient?','Unknow'),('HEAD INJURY','0001-01-01 00:00:00','These questions apply only to the INITIAL\r\nPRESENTATION of a head injury.\r\n1. Description of injury?\r\n2. Level of consciousness since injury noted?\r\n3. Cause of injury noted?\r\n4. Mechanism of injury noted?\r\n5. Head and neck exam?\r\n6. ENT exam?\r\n7. Cranial nerves?\r\n8. Neurological exam?\r\n9. Pulse and blood pressure?\r\n10. Level of consciousness and orientation at time of exam?\r\n11. IF depressed consciousness, skull X-ray\r\nOR CAT scan OR referral?\r\n12. IF neck pain\r\nOR tenderness, cervical spine X-ray?\r\n13. Narcotics prescribed (including codeine)?\r\n14. IF sent home, instructions to family or friend re\r\nobservation for change in level of consciousness (i.e.\r\nhead injury sheet)?\r\n15. IF penetrating wound\r\nOR\r\ndeteriorating (i.e. change in sensorium), immediate referral?\r\n16. IF recurrent, discussion re safety measures (eg. helmets)?\r\n17. IF recurrent in child -abuse considered?','Unknow'),('HEADACHE NYD','0001-01-01 00:00:00','1. Inquiry re at least 6 of the following? \r\nseverity \r\nfrequency \r\nlocation \r\nprecipitating factors \r\nmedication history \r\nduration \r\nassociated symptoms (eg. dizziness, blurred vision) \r\nprevious history of headaches \r\nhistory of head injury \r\nhistory of seizures \r\n2. Neurological exam? \r\n3. Blood pressure? \r\n4. One follow-up within 3 months OR referral? \r\n5. IF no definitive diagnosis within 3 months, referral? \r\n6. Inquiry re stress factors? ','Unknow'),('HEMATOMA,','0001-01-01 00:00:00','1. Inquiry re history of trauma, type noted?\r\n2. Inquiry re spontaneous or traumatic?\r\n3. IF spontaneous, inquiry re previous episodes?\r\n4. IF spontaneous, inquiry re family history of bleeding?\r\n5. Description of size?\r\n6. Description of location?\r\n7. IF spontaneous, CBC, platelets, PT, PTT done?\r\n8. IF seen within 48 hours of onset, ice recommended?\r\n9. IF spontaneous OR recurrent, one follow-up?\r\n10. IF child (other recent or old trauma)?\r\n11. IF AND history of repeated trauma (3 or more within 2 years) skeletal survey?','Unknow'),('HEMATOMA,SUBCUTANEOU','0001-01-01 00:00:00','1. Inquiry re history of trauma, type noted? \r\n2. Inquiry re spontaneous or traumatic? \r\n3. IF spontaneous, inquiry re previous episodes? \r\n4. IF spontaneous, inquiry re family history of bleeding? \r\n5. Description of size? \r\n6. Description of location? \r\n7. IF spontaneous, CBC, platelets, PT, PTT done? \r\n8. IF seen within 48 hours of onset, ice recommended? \r\n9. IF spontaneous OR recurrent, one follow-up? \r\n10. IF child (other recent or old trauma)? \r\n11. IF AND history of repeated trauma (3 or more within 2 years) skeletal survey? ','Unknow'),('HEMATURIA','0001-01-01 00:00:00','1. Inquiry re first or recurrent episode?\r\n2. Inquiry re frequency of hematuria?\r\n3. Presence/absence of flank pain noted?\r\n4. Presence/absence of dysuria OR frequency noted?\r\n5. Microscopic or gross hematuria noted?\r\n6. Presence/absence of colicky pain noted?\r\n7. Abdominal exam?\r\n8. Flank percussion, findings noted?\r\n9. IF male, rectal AND genital exam?\r\n10. IF female AND 2nd or more episode within 1 year, pelvic exam?\r\n11. Urinalysis AND micro?\r\n12. Urine C & S?\r\n13. BUN AND/OR Creatinine?\r\n14. IF 2nd episode within 2 years, IVP OR referral?\r\n15. IF > 60 years AND source not identified, referral?','Unknow'),('HEMORRHOIDS','0001-01-01 00:00:00','1. Inquiry re pain?\r\n2. Inquiry re bleeding?\r\n3. Rectal exam?\r\n4. IF rectal bleeding, sigmoidoscopic exam on chart (3 minute)?\r\n5. IF patient >40 and no definitive diagnosis for rectal bleeding found on sigmoidoscopic, barium enema?\r\n6. Description of site and location of hemorrhoids?\r\n7. One or more of the following used? dietary (high fibre, avoid constipation) suppositories sitz baths surgical ligation and banding I & D if acute thrombosed hemorrhoids\r\n8. IF symptoms unchanged for more than 3 months, referral?\r\n9. Discussion re high fibre diet and stool softeners?\r\n10. One follow-up within one month?','Unknow'),('HERPANGINA','0001-01-01 00:00:00','1. Inquiry re duration of sore throat? \r\n2. Examination of throat? \r\n3. Antibiotics used?','Unknow'),('HERPES ZOSTER','0001-01-01 00:00:00','1. Description of lesions? \r\n2. Location of lesions noted? \r\n3. IF lesions on forehead OR physician notes \"ophthalmic distribution\", examination of cornea OR referral? ','Unknow'),('HERPETIC ULCER (EYE)','0001-01-01 00:00:00','1. Inquiry re pain in eye?\r\n2. Red eye noted?\r\n3. Dendrite shaped ulceration noted?\r\n4. Fluorescein staining positive?\r\n5. Referral to ophthalmologist?\r\n6. Steroids used locally?','Unknow'),('HERPETIC ULCER, VULV','0001-01-01 00:00:00','1. Inquiry re history of vaginal complaint? \r\n2. Description of lesion? \r\n3. Location of lesion? \r\n4. Viral culture (scraping)? \r\n5. IF initial culture negative AND patient pregnant OR lesion persists, repeat culture? \r\n6. Positive viral culture? \r\n7. IF present at labour, Caesarian section OR referral? ','Unknow'),('HYPERLIPIDEMIA','0001-01-01 00:00:00','1. Family history OR on chart (3 minute)? \r\n2. Cardiovascular exam? \r\n3. Weight recorded? \r\n4. Abdominal exam? \r\n5. Comment re xanthomas? \r\n6. Blood sugar OR glucose tolerance test? \r\n7. Lipids? \r\n8. Lipid level above lab normal? \r\n9. Discussion re diet? \r\n10. IF obesity noted, discussion re weight reduction? \r\n11. Discussion re alcohol AND/OR exercise? ','Unknow'),('HYPERTENSION (ANY AG','0001-01-01 00:00:00','1. Inquiry re family history of stroke, M.I. OR on chart (3 minute)? \r\n2. Medications taken listed at least twice in 2 year period? \r\n3. One blood pressure per visit (at least 75%)? \r\n4. Yearly comment on heart AND lungs AND fundi AND weight?\r\n5. ECG, on chart (3 minute)? \r\n6. Urinalysis, on chart (3 minute)? \r\n7. IF smoker, advice re smoking? \r\n8. IF obesity noted, advice re weight loss? \r\n9. IF on medication, at least 2 visits per year? \r\n10. IF patient AND diastolic B.P. > 105 on three consecutive visits, referral? \r\n11. Inquiry re stress factors at least once? \r\n12. Inquiry re alcohol intake at least once? \r\n13. IF oral contraceptives used, was justification noted? \r\n14. IF sympathomimetics used, was justification noted?\r\n15. IF diastolic B.P. > 105 on two consecutive occasions, treated with medication? ','Unknow'),('HYPERTENSION, < 75 Y','0001-01-01 00:00:00','1. Inquiry re family history of stroke AND/OR M.I., OR on chart (3 minute)? \r\n2. Right and left arm blood pressure at least once on chart? \r\n3. One blood pressure per visit (at least 75%)? \r\n4. Yearly comment on heart AND lungs AND fundi AND weight? \r\n5. ECG, on chart (3 minute)? \r\n6. Urinalysis, on chart (3 minute)? \r\n7. Were there at least two readings with diastolic greater than 90 OR one reading greater than 105 before drug therapy was started? \r\n8. IF diastolic B.P. > 105 or systolic > 200, first line antihypertensive used (thiazides AND/OR beta blockers)? \r\n9. IF second line antihypertensive were used, were first line antihypertensives tried for at least 3 months? \r\n10. IF smoker, advice re smoking? \r\n11. IF obesity noted, advice re weight loss (eg. diet or exercise)? \r\n12. IF patient on drugs, at least 2 visits per year? \r\n13. IF patient has persistant B.P. > 105, referral after 6 months? \r\n14. Inquiry re stress factors? \r\n15. IF oral contraceptives used, justification noted? \r\n16. IF sympathomimetics used, justification noted? ','Unknow'),('HYPERTHYROIDISM, NEW','0001-01-01 00:00:00','1. Inquiry re one or more of following?\r\nweight loss palpitations\r\ntremulousness restlessness\r\nmuscular weakness\r\nfatigue\r\n2. Thyroid exam?\r\n3. Pulse?\r\n4. Examination of eyes?\r\n5. T4 OR T3 OR resin uptake OR other thyroid tests?\r\n6. T4 AND T3 AND uptake elevated?\r\n7. Follow-up every 6 months?\r\n8. Euthyroid within 6 months OR referral?','Unknow'),('HYPERTHYROIDISM, TRE','0001-01-01 00:00:00','1. Inquiry re at least one of the following at each visit? \r\nenergy \r\nweight \r\nheat sensitivity \r\n2. If new patient to practice within past 2 years, inquiry re duration of disease? \r\n3. If new patient to practice within past 2 years, examination of thyroid and eyes noted? \r\n4. Heart rate OR pulse at each visit? \r\n5. T3 RIA OR TSH yearly? \r\n6. At least one abnormal thyroid test on chart (3 minute), TSH down OR T4 up? \r\n7. Follow-up yearly? ','Unknow'),('HYPOTHROIDISM','0001-01-01 00:00:00','1. Inquiry re previous thyroid treatment? \r\n2. Inquiry re at least one of following? \r\nsensitivity to cold chronic fatigue \r\nmental dullness menses\r\ngeneralized weakness constipation\r\n3. Thyroid exam? \r\n4. Reflex exam? \r\n5. Comment re at least one of the following? \r\ndry skin voice change\r\nmyxedema lethargy\r\n6. T4 done? \r\n7. T4 repeat, every second dosage change? \r\n8. One of; low T4, low T3, or low uptake, or high TSH? \r\n9. IF newly diagnosed (within last two years), extracts used? \r\n10. IF lab test normal? \r\n11. IF >= 60, follow-up every 2 weeks until euthyroid or lab tests normal? \r\n12. Euthyroid within 6 months OR referral? ','Unknow'),('IMPETIGO or PYODERMA','0001-01-01 00:00:00','1. Site noted?\r\n2. IF oral antibiotic used, was it one of penicillins, erythromycins, sulfonamides, tetracyclines, or cephalosporins?\r\n3. IF tetracycline used, was patient','Unknow'),('IMPOTENCE','0001-01-01 00:00:00','1. Inquiry re impotence, constant or intermittant?\r\n2. Inquiry re alcohol use?\r\n3. Inquiry re D.M., or systemic disease?\r\n4. Inquiry re emotional problems?\r\n5. Inquiry re nocturnal erections?\r\n6. Inquiry re medications?\r\n7. Genital exam?\r\n8. Blood pressure?\r\n9. Abdominal exam?\r\n10. Neurological exam?\r\n11. Exam of pulses?\r\n12. Urinalysis?\r\n13. Fasting blood sugar?\r\n14. One follow-up?\r\n15. IF problem persists for > 3 months, referral?\r\n16. Sexual counselling with partner?','Unknow'),('INFANTILE COLIC','0001-01-01 00:00:00','1. Inquiry re at least two of following? \r\nvomiting\r\nbowel movements\r\nburping\r\npassing gas\r\nfluid intake\r\n2. Inquiry re timing of crying? \r\n3. Weight recorded with initial diagnosis? \r\n4. Comment on appearance of baby? \r\n5. Evidence of evening crying after feeding? \r\n6. At least one follow-up with comment on colic status? \r\n7. Evidence of some support for parent(s) by one of following?\r\npublic health nurse\r\nreassurance and/or discussion by family doctor\r\ninvolvement of family members','Unknow'),('INFECTIOUS NOMONUCLE','0001-01-01 00:00:00','1. Inquiry re at least two of following?\r\nsore throat\r\nfever\r\nmalaise\r\nlymphadenopathy\r\nabdominal pain\r\n2. Presence/absence of fever noted?\r\n3. Throat exam?\r\n4. Presence/absence of lymphadenopathy noted?\r\n5. Presence/absence of hepatosplenomegaly noted?\r\n6. WBC AND diff.?\r\n7. Mono screen?\r\n8. Positive mono test OR abnormal WBC\'s?\r\n9. Advice re reduced activity?\r\n10. Ampicillin used?\r\n11. IF splenomegaly present, follow-up within 2 weeks?\r\n12. IF splenomegaly not present, follow-up within 4 weeks?\r\n13. IF splenomegaly present, advice re avoidance of contact sports or activities?','Unknow'),('INFERTILITY, FEMALE','0001-01-01 00:00:00','1. Parity noted?\r\n2. Infertility for more than 2 years?\r\n3. Inquiry re medication history?\r\n4. Inquiry re menstrual history?\r\n5. Pelvic exam?\r\n6. Examination of breasts?\r\n7. CPE within 2 years after initial diagnosis?\r\n8. Pap smear AND/OR referral?\r\n9. Semen analysis (sexual partner/husband) \r\nOR referral?\r\n10. BS within 6 months after initial diagnosis OR referral?\r\n11. T3 AND/OR T4 within 6 months after initial diagnosis OR referral?\r\n12. Plan of action noted OR referral?','Unknow'),('INFLUENZA','0001-01-01 00:00:00','1. Inquiry re three of the following?\r\nmyalgia\r\nfever\r\ncough\r\nphlegm type\r\nmalaise\r\n2. Inquiry re duration of symptoms?\r\n3. ENT exam?\r\n4. IF coughing, chest exam?\r\n5. IF antibiotics prescribed, was there history of secondary infection (coloured phlegm, or fever > 38 for 3 days or more)\r\nOR\r\nhigh risk (cardiac valvular disease or chronic pulmonary disease)?','Unknow'),('INGUINAL HERNIA','0001-01-01 00:00:00','1. Inquiry re presence/absence of vomiting?\r\n2. Inquiry re at least two of following?\r\ninguinal bulge\r\nduration\r\npain\r\n3. Description of inguinal mass including side?\r\n4. Reducible or not noted?\r\n5. IF not reducible AND painful, referral to surgeon within 24 hours?','Unknow'),('INTERMITTENT CLAUDIC','0001-01-01 00:00:00','1. Inquiry re duration of pain? \r\n2. Inquiry re current smoking status? \r\n3. Presence/absence of pulses in legs? \r\n4. Blood pressure? \r\n5. Comment on abdomen OR aneurysm? \r\n6. Comment on legs, warmth OR hair growth OR colour? \r\n7. CPE within 12 months before OR 6 months after presentation?\r\n8. Cholesterol OR triglycerides? \r\n9. Blood sugar? \r\n10. Pain in legs with exercise or walking, relieved by rest? \r\n11. IF smoker, advice re smoking? \r\n12. Discussion re foot care? ','Unknow'),('IRITIS','0001-01-01 00:00:00','1. Inquiry re at least one of following; blurred vision, painful eye, red eye, photophobia? \r\n2. Description of eye? \r\n3. Referral OR phone consultation? ','Unknow'),('IRON DEFICIENCY ANEM','0001-01-01 00:00:00','** NOTE **\r\nNon-pregnant, new presentation \r\n1. Inquiry re bleeding from bowel? \r\n2. Inquiry re bleeding from other sources (eg. nose, vagina) \r\n3. Inquiry re diet? \r\n4. Hemoglobin OR hematocrit? \r\n5. Indices MCV AND MCHC OR smear? \r\n6. Two of following? \r\nSerum ferritin \r\nserum iron \r\ntotal iron binding capacity \r\n7. Stool for occult blood? \r\n8. Serum ferritin OR hemoglobin microcytic smear OR low indices (MCV and MCHC)? \r\n9. Oral iron prescribed? \r\n10. IF poor diet noted, diet counselling? \r\n11. One follow-up within 6 weeks? \r\n12. IF injectable iron used, justification statement?','Unknow'),('IRRITABLE BOWEL','0001-01-01 00:00:00','1. Inquiry re bowel activity OR cramps, once per 6 months? \r\n2. Abdominal exam once per year? \r\n3. Stool for occult blood once per year? \r\n4. Sigmoidoscopic exam OR on chart (3 minute)? \r\n5. UGI series with small bowel follow through OR on chart (3 minute)? \r\n6. Presence of constipation OR diarrhea OR cramps? \r\n7. Barium enema OR on chart (3 minute)? \r\n8. Follow-up at least once within 6 months? \r\n9. Discussion of stress factors? \r\n10. Narcotics used? ','Unknow'),('KERATITIS, INFLAMMAT','0001-01-01 00:00:00','1. Inquiry re at least one of following? \r\nphotophobia \r\npain in eye \r\nocular discharge \r\ntearing of eye \r\n2. Duration of symptoms? \r\n3. Description of cornea? \r\n4. Fluoroscein staining? \r\n5. Corticosteroid eye drops used? \r\n6. Follow-up within 48 hours? \r\n7. IF not improved within 48 hours, referral? ','Unknow'),('KIDNEY OBSTRUCTION','0001-01-01 00:00:00','1. Inquiry re pain? \r\n2. Abdominal exam? \r\n3. Blood pressure? \r\n4. BUN OR creatinine? \r\n5. Urinalysis AND C & S? \r\n6. IVP shows blockage? \r\n7. Referral within 1 week?','Unknow'),('KNEE INJURIES','0001-01-01 00:00:00','1. Description of how injury happened?\r\n2. Duration of discomfort?\r\n3. Presence/absence of locking or collapse?\r\n4. Presence/absence of swelling?\r\n5. Comment on function?\r\n6. Comment on stability of ligaments?\r\n7. IF effusion persists for more than 72 hours, joint aspiration OR referral?\r\n8. IF locking OR instability, referral?','Unknow'),('LACERATIONS','0001-01-01 00:00:00','1. Inquiry re how laceration occurred?\r\n2. Time between injury and visit?\r\n3. Description of wound?\r\n4. IF hand or wrist, comment on function?\r\n5. IF tendons severed, referral?\r\n6. Debridement (washing)?\r\n7. IF sutured, one follow-up?\r\n8. IF no tetanus toxoid within 10 years, injection given?','Unknow'),('LACERATIONS OF SKIN','0001-01-01 00:00:00','** NOTE **\r\nFOR QUESTIONS 1 THROUGH 7, PHYSICIAN MUST FULFILL CONDITION FOR EACH EPISODE OF LACERATION. \r\n1. Inquiry re how laceration occurred? \r\n2. Time between injury and visit? \r\n3. Description of wound? \r\n4. IF hand or wrist, comment on function? \r\n5. IF tendons severed, referral? \r\n6. Debridement (washing)? \r\n7. IF sutured, one follow-up? \r\n8. IF no tetanus toxoid within 10 years, injection given? ','Unknow'),('LARYNGITIS','0001-01-01 00:00:00','1. Inquiry re duration?\r\n2. Inquiry re smoking (or on chart) (3 minute)?\r\n3. Inquiry re specific cause (eg. shouting, occupation)?\r\n4. Exam of pharynx?\r\n5. IF persistant for more than 6 weeks, laryngoscopic exam OR referral?\r\n6. IF smoker, advice re smoking?','Unknow'),('LARYNGITIS OR TRACHE','0001-01-01 00:00:00','1. Duration of symptoms?\r\n2. Presence/absence of cough noted?\r\n3. Throat exam?\r\n4. Chest exam?','Unknow'),('LICE AND SCABIES','0001-01-01 00:00:00','1. Inquiry re itching or pruritis?\r\n2. Location noted?\r\n3. IF scabies, description of skin lesion(s)?\r\n4. Gamma Benzene Hexachloride Lotion OR Shampoo?\r\n5. IF used?\r\n6. Instructions re washing clothing and bed linen?\r\n7. IF scabies, entire family treated?','Unknow'),('LOBAR PNEUMONIA','0001-01-01 00:00:00','1. Inquiry re at least one of following? \r\ncough \r\ndyspnea \r\nchest pain \r\nfever \r\n2. Description of breath sounds? \r\n3. Comment re dullness OR consolidation? \r\n4. Sputum C & S? \r\n5. WBC? \r\n6. Chest X-ray, 2 views? \r\n7. IF X-ray positive, follow-up X-ray within 30 days? \r\n8. Positive culture AND positive X-ray OR consolidation on examination? \r\n9. Oral penicillin or erythromycin or cephalosporin given? \r\n10. Dosage recorded? \r\n11. Amount recorded? \r\n12. Follow-up in 1 week? ','Unknow'),('LOW BACK PAIN, NOS,','0001-01-01 00:00:00','1. Inquiry re duration AND location of pain? \r\n2. Inquiry re presence/absence of one of following? \r\nparesthesia \r\nsensory aberrations \r\nradiation of pain \r\n3. Inquiry re presence/absence of trauma? \r\n4. Inquiry re previous episode(s)? \r\n5. Movement of back (flexion OR extension OR lateral flexion OR rotation) noted? \r\n6. Note on reflexes (one of knee OR ankle)? \r\n7. Note on straight leg raising? \r\n8. IF pain persists for more than 1 month, lumbar spine AP AND lateral X-rays? \r\n9. IF narcotic analgesic (except codeine compounds, 30 mg. codeine max.) used, justification statement? \r\n10. Back exercises AND/OR back care instructions? \r\n11. One follow-up? \r\n12. IF still continuously painful after 3 months, consultation OR referral? ','Unknow'),('LYMPHADENOPATHY NYD','0001-01-01 00:00:00','1. Inquiry re location of enlarged glands? \r\n2. Inquiry re duration? \r\n3. Description of node(s)? \r\n4. IF in axilla OR groin, comment on extremity? \r\n5. IF in neck, ear and throat exam? \r\n6. IF non-neck node AND no obvious cause noted, CBC?\r\n7. IF neck node AND no obvious cause noted, infectious monocucleosis screen (Monospot)? \r\n8. IF lesion persists for one month or more at the same size, chest X-ray? \r\n9. IF lesion persists for two months or longer, biopsy of node OR referral? \r\n10. Antibiotic used AND it was one of the penicillins, erythromycins, sulfonamides, cephalosporins, OR tetracyclines? \r\n11. IF the patient was\r\n12. IF no infectious cause noted, one follow-up? ','Unknow'),('MENOPAUSAL SYNDROME','0001-01-01 00:00:00','1. Inquiry re menstrual history (all of: cycle, flow, LMP)? \r\n2. Inquiry re hot flashes/flushes? \r\n3. CPE within one year after initial diagnosis? \r\n4. Pap smear within one year after initial diagnosis? \r\n5. IF Premarin OR conjugated estrogens used, cyclical use OR progestational agent added (5 days per 3 months)? \r\n6. Discussion re post-menopausal sexual problems (i.e. lack of lubrication) on chart (3 minute)? ','Unknow'),('MENORRHAGIA','0001-01-01 00:00:00','1. Inquiry re bleeding pattern, duration AND amount?\r\n2. IF\r\n3. Pelvic exam on initial visit OR when bleeding stops?\r\n4. Hb?\r\n5. Pap smear on initial visit OR when bleeding stops?\r\n6. Cause established OR referral within 3 months of initial visit for problem?','Unknow'),('MIGRAINE EQUIVALENTS','0001-01-01 00:00:00','1. Inquiry re presence/absence of aura? \r\n2. IF aura present, inquiry re type of aura? \r\n3. Inquiry re location of pain? \r\n4. Inquiry re change in headaches?\r\n5. Neurological exam within last year? \r\n6. Blood pressure within last year? \r\n7. IF medication prescribed, dosage noted? \r\n8. IF medication prescribed, duration noted?','Unknow'),('MONOARTICULAR ARTHRI','0001-01-01 00:00:00','** NOTE **\r\nOne large joint; ankle, knee, hip, wrist, elbow, shoulder. \r\n1. Inquiry re pain? \r\n2. Site noted? \r\n3. Inquiry re duration of symptoms? \r\n4. Inquiry re presence/absence of trauma? \r\n5. Description of joint? \r\n6. Temperature recorded OR history of fever? \r\n7. One large severely painful joint with abnormalities upon examination? \r\n8. Definitive diagnosis on chart within 3 days OR referral? ','Unknow'),('MOUTH LESION','0001-01-01 00:00:00','1. Inquiry re location? \r\n2. Inquiry re duration? [HA2 ]> \r\n3. Description of lesion? \r\n4. IF lesion described as \"ulcer\" or \"plaque\" AND lesion not healed in 2 months, investigation OR referral? ','Unknow'),('MUMPS','0001-01-01 00:00:00','1. Inquiry re duration of symptoms? \r\n2. Swelling in parotid area noted? \r\n3. IF male > 11 years, testicular exam? \r\n4. IF analgesic used, was it ASA or acetaminophen? ','Unknow'),('MYOCARDIAL INFARCTIO','0001-01-01 00:00:00','** NOTE **\r\nQUESTIONS 1 THROUGH 6 SHOULD BE PRESENT ON AT LEAST 75% OF VISITS. \r\n1. Inquiry re chest pain relating to activity? \r\n2. Inquiry re palpitations? \r\n3. Inquiry re dyspnea? \r\n4. Blood pressure? \r\n5. Chest auscultation? \r\n6. Cardiac auscultation (sounds AND rhythm AND murmurs)? \r\n7. Lipids (cholesterol AND triglycerides) within one year of hospital discharge? \r\n8. IF new abnormal rhythm noted, ECG within 2 days? \r\n9. Current medications recorded (name AND dosage)? \r\n10. Inquiry re risk factors (eg. diet, blood pressure, smoking, obesity)? \r\n11. One follow-up by family doctor or specialist within 4 weeks of discharge? \r\n12. Following initial visit after discharge, follow-up at least every 3 months for one year? ','Unknow'),('NASAL INJURY','0001-01-01 00:00:00','1. Description of accident? \r\n2. Description of nose including 2 of following; swelling, amount of bleeding, deformity, lacerations? \r\n3. IF deformity found on examination, X-ray of nasal bones? \r\n4. IF deformity found on examination, referral to ENT specialist? \r\n5. IF unable to control bleeding, referral? ','Unknow'),('NASAL POLYP','0001-01-01 00:00:00','1. Inquiry re nasal symptoms? \r\n2. Inquiry re history of asthma or ASA allergy (or on chart) (3 minute)? \r\n3. Description of polyp? \r\n4. IF no improvement after 6 weeks, referral? ','Unknow'),('NASOPHARYNGITIS OR U','0001-01-01 00:00:00','1. Complaint of at least one of the following? \r\nnasal discharge\r\nsore throat\r\nmalaise \r\ncold \r\n2. Duration of symptoms noted? \r\n3. IF cough in history, chest exam?\r\n4. IF patient \r\n5. IF sore throat in history, throat exam?\r\n6. IF narcotic antitussives prescribed, cough in history? \r\n7. IF antibiotics prescribed, was there history of secondary infection (coloured phlegm, or fever > 38 for 3 days or more)OR\r\nhigh risk (cardiac valvular disease or chronic pulmonary disease)? ','Unknow'),('NASOPHARYNGITIS, CHR','0001-01-01 00:00:00','1. History of one of following? \r\nnasal spray \r\nnasal stuffiness \r\npost-nasal drip \r\ncigarette smoking \r\nexposure to dust or fumes \r\n2. Description of nasal mucosa? \r\n3. Advice re irritants (stop smoking, avoid dust and fumes)? ','Unknow'),('NOCTURNAL ENURESIS','0001-01-01 00:00:00','** NOTE**\r\nAudit only for patients at least 4 years old. \r\n1. Inquiry re family history of enuresis? \r\n2. Inquiry re frequency of bedwetting? \r\n3. Inquiry re remissions and exacerbations? \r\n4. Genital exam, once on chart (3 minute)? \r\n5. Urinalysis, once on chart (3 minute)? \r\n6. Urine C & S, once on chart (3 minute)? \r\n7. IF urine culture positive, IVP OR ultrasound? \r\n8. IF recurrent positive urine culture, voiding cystogram OR referral? \r\n9. History of bedwetting on chart? \r\n10. Follow-up at least once? \r\n11. Family counselling, parents and child? \r\n12. Management plan on chart involving at least one of following? \r\nmedications \r\ncounselling \r\ndry-night record ','Unknow'),('NOSEBLEED, ANTERIOR','0001-01-01 00:00:00','1. Inquiry re frequency? \r\n2. Inquiry re duration? \r\n3. Some estimate of blood loss noted? \r\n4. Examination of nose? \r\n5. IF active bleeding at time of visit, blood pressure recorded? \r\n6. IF > 60 years, hemoglobin? \r\n7. IF recurrent nose bleeder (2 episodes within 6 months), CBC AND platelet count AND PT AND PTT on chart? \r\n8. One of the following? \r\ngross bleeding \r\nphysical evidence of bleeding vessel on examination \r\n9. IF packing performed, follow-up within 2 days? \r\n10. IF Hg \r\n11. IF 3 nosebleeds within past 2 days AND not actively bleeding, cautery OR prescription of ointment? \r\n12. IF acute nosebleed, packing AND/OR cautery AND/OR referral? ','Unknow'),('OBESITY','0001-01-01 00:00:00','1. Inquiry re duration of obesity? \r\n2. Weight recorded? \r\n3. Height recorded? \r\n4. Height AND weight recorded? \r\n5. Anorexiants OR thyroid drugs (if hypothyroidism not diagnosed) OR diuretics used? \r\n6. Diet counselling OR nutritional counselling (physician or dietician)? \r\n7. IF treatment given, follow-up within 6 weeks? ','Unknow'),('ORCHITIS AND EPIDIDY','0001-01-01 00:00:00','1. Inquiry re location of pain?\r\n2. Inquiry re swelling of testes?\r\n3. Examination of testicles?\r\n4. Comment re tenderness?\r\n5. WBC?\r\n6. Urinalysis?\r\n7. Urine C & S?\r\n8. Support to scrotum?\r\n9. IF epididymitis, antibiotics used?\r\n10. IF antibiotics used, amount AND duration noted?\r\n11. Follow-up within one week?','Unknow'),('OSTEOPOROSIS','0001-01-01 00:00:00','\r\n1. Inquiry re presence/absence of pain?\r\n2. Inquiry re dietary history?\r\n3. Inquiry re menopause date?\r\n4. IF pain present, examination of area?\r\n5. Comment re kyphosis?\r\n6. X-ray OR bone density OR cortical thickness?\r\n7. Confirmation of osteoporosis by any of tests in question 6?\r\n8. Increased calcium intake (supplements or dietary)?','Unknow'),('OTITIS EXTERNA','0001-01-01 00:00:00','1. Inquiry re symptoms?\r\n2. Ear exam?\r\n3. Evidence of \"normal drum\"?','Unknow'),('OTITIS MEDIA -SEROUS','0001-01-01 00:00:00','1. Inquiry re at least two of following; hearing, pain, recurrent URI?\r\n2. Comment re fluid in middle ear OR retracted ear drum?\r\n3. Comment re nose AND throat?\r\n4. IF third episode or more, audiometry OR referral?\r\n5. IF physical findings OR hearing test are abnormal, follow-up until resolved OR referral?','Unknow'),('OTITIS MEDIA ACUTE','0001-01-01 00:00:00','1. Description of symptoms? \r\n2. Duration of symptoms? \r\n3. Examination of ears? \r\n4. Comment re one of the following? \r\nred drum \r\nbulging drum \r\nloss of light reflex \r\n5. IF tetracycline or chloramphenicol used, was patient\r\n6. Antibiotics prescribed for at least 10 days? \r\n7. IF > 4 years AND antibiotic used, was it ampicillin, penicillin or erythromycin? \r\n8. IF AND antibiotic used, was it penicillin, amoxicillin, sulfa or erythromycin? \r\n9. One follow-up within 4 weeks of episode with statement of patient\'s condition? ','Unknow'),('PARAPHIMOSIS','0001-01-01 00:00:00','1. Inquiry re pain? \r\n2. Foreskin not reducible by patient? \r\n3. Description of penis? \r\n4. Reduction attempted by physician? \r\n5. Counselling on care of penis? \r\n6. IF physician unable to reduce, follow-up or referral? ','Unknow'),('PELVIC INFLAMMATORY','0001-01-01 00:00:00','1. Inquiry re pelvic pain AND vaginal discharge? \r\n2. Inquiry re previous PID OR venereal disease? \r\n3. Inquiry re menstrual history? \r\n4. Pelvic exam with comment re cervical discharge? \r\n5. Comment re adnexal examination? \r\n6. Comment re pelvic tenderness (cervical excitation)? \r\n7. Presence/absence of fever noted? \r\n8. WBC? \r\n9. Urinalysis? \r\n10. Micro? \r\n11. VDRL? \r\n12. Cervical/vaginal C & S? \r\n13. IF bleeding, pregnancy test? \r\n14. Antibiotic used? \r\n15. Follow-up within 10 days? ','Unknow'),('PEPTIC ULCER','0001-01-01 00:00:00','1. Inquiry re epigastric pain?\r\n2. Inquiry re past history of similar symptoms?\r\n3. Inquiry re relief from antacid or milk?\r\n4. Abdominal exam?\r\n5. UGI series\r\nOR\r\ngastroscopy done?\r\n6. UGI series\r\nOR\r\ngastroscopy demonstrates ulcer crater\r\nAND/OR scarring?\r\n7. IF GASTRIC ulcer demonstrated by UGI series\r\nOR\r\ngastroscopy, procedure repeated within 6 weeks?\r\n8. Instruction re diet?\r\n9. IF smoker, advice re smoking?\r\n10. Instruction re alcohol?\r\n11. Counselling re stress factors?\r\n12. Were any of the following drugs used?\r\noral steroids\r\nnonsteroidal anti-inflammatories\r\nASA\r\ncolchicine\r\n13. Follow-up at least every 6 weeks until asymptomatic\r\nOR\r\nhealing demonstrated by UGI series\r\nOR\r\ngastroscopy?','Unknow'),('PERFORATION TYMPANIC','0001-01-01 00:00:00','1. Inquiry re cause? \r\n2. Inquiry re pain? \r\n3. Inquiry re discharge? \r\n4. Location of perforation? \r\n5. Size of perforation? \r\n6. Follow-up until resolved or referral? ','Unknow'),('PERITONISILLAR ABSCE','0001-01-01 00:00:00','1. Inquiry re sore throat? \r\n2. Inquiry re swallowing difficulties? \r\n3. Throat exam? \r\n4. Description of mass? \r\n5. Referral or hospitalization? ','Unknow'),('PHARYNGITIS','0001-01-01 00:00:00','1. Inquiry re sore throat? \r\n2. Inquiry re duration? \r\n3. Examination of pharynx? \r\n4. IF white membrane OR lot of exudate noted, mono test AND C & S? \r\n5. Red (inflamed, injected) throat? \r\n6. IF AND positive strep culture, amoxil or ampicillin or erythromycin given for at least 7 days? \r\n7. IF 5 years or older AND positive strep culture, penicillin or erythromycin for at least 7 days? ','Unknow'),('PINWORMS','0001-01-01 00:00:00','1. Inquiry re pruritis of anus or vulva? \r\n2. Examination for eggs AND/OR worms on anus? \r\n3. Pinworm test? \r\n4. Pyrvinium pamovate OR Vanquin used? \r\n5. Whole household treated simultaneously? \r\n6. Positive eggs OR positive worms OR positive pinworm test? ','Unknow'),('PITYRIASIS ROSEA','0001-01-01 00:00:00','1. Inquiry re duration of rash? \r\n2. Inquiry re herald patch? \r\n3. Description of distribution? \r\n4. VDRL? \r\n5. Oral steroids used? \r\n6. Counselling re duration? ','Unknow'),('PLEURISY','0001-01-01 00:00:00','1. Inquiry re duration of symptoms? \r\n2. Inquiry re location of pain? \r\n3. Presence/absence of fever noted? \r\n4. Presence/absence of cough noted? \r\n5. Inquiry whether chest pain worse with deep breathing (pleuritic)? \r\n6. Chest exam? \r\n7. Throat exam? \r\n8. CVS exam? \r\n9. Blood pressure? \r\n10. Temperature recorded? \r\n11. IF temperature elevated OR sputum, CBC? \r\n12. IF sputum, C & S? \r\n13. IF rales AND/OR rhonchi present, chest X-ray? \r\n14. IF antibiotics prescribed, C & S of sputum done before use of antibiotic? \r\n15. IF smoker, advice re smoking? \r\n16. Cause stated OR referral? ','Unknow'),('PREGNANCY, DELIVERY,','0001-01-01 00:00:00','1. Ontario antenatal records I AND II? \r\n2. Urinalysis with each visit? \r\n3. Hemoglobin each trimester? \r\n4. IF urinalysis positive for glucose on 2 occasions, blood sugar OR glucose tolerance test OR referral? \r\n5. IF dipstick urinalysis positive, lab report of urinalysis and micro? \r\n6. IF hemoglobin\r\n7. IF any drugs used (except pencillins, vitamins, iron, or antinauseants), comment re teratogenicity? \r\n8. IF blood sugar elevated, discussion of diet with patient? \r\n9. Follow-up monthly for first 7 months, every 2 weeks during the 8th month, and then weekly until delivered? \r\n10. IF X-rays done, pregnancy related OR justification statement? ','Unknow'),('PROSTATE CANCER','0001-01-01 00:00:00','1. Inquiry re urinary symptoms?\r\n2. Rectal exam at least yearly?\r\n3. Serum acid phosphatase yearly?\r\n4. IF new or changed urinary symptoms, C & S AND urinalysis?\r\n5. Pathology report positive?\r\n6. Follow-up every 6 months?','Unknow'),('PROSTATE, BENIGN HYP','0001-01-01 00:00:00','1. Inquiry re urinary symptoms, at least one of following?\r\nnocturia \r\nfrequency\r\nstream\r\nurgency \r\n2. Description of prostate? \r\n3. Urinalysis? \r\n4. C & S? \r\n5. IF bladder distended, drained slowly? \r\n6. IF catheterized or obstructed, referral? ','Unknow'),('PROSTATE, CANCER OF','0001-01-01 00:00:00','1. Inquiry re urinary symptoms? \r\n2. Rectal exam at least yearly? \r\n3. Serum acid phosphatase yearly? \r\n4. IF new or changed urinary symptoms, C & S AND urinalysis?\r\n5. Pathology report positive? \r\n6. Follow-up every 6 months? ','Unknow'),('PROSTATITIS','0001-01-01 00:00:00','1. Inquiry re dysuria? \r\n2. Inquiry re pain? \r\n3. Prostate tender? \r\n4. Urinalysis? \r\n5. Urine C & S? \r\n6. Antibiotics used AND amount noted? \r\n7. Antibiotics used AND duration noted? \r\n8. Counselling re at least one of coffee, alcohol, smoking, spices? \r\n9. Follow-up within 2 weeks? ','Unknow'),('PROSTATITIS CHRONIC','0001-01-01 00:00:00','1. Inquiry re at least 3 of following?\r\ndysuria\r\nfrequency\r\nperineal pain\r\npainful sexual activity\r\nurethral discharge\r\nlow back pain\r\nnocturia\r\n2. Abdominal exam?\r\n3. Rectal exam?\r\n4. Description of prostate (size and consistency)?\r\n5. Urine C & S?\r\n6. Septra\r\nOR\r\ntetracycline\r\nOR\r\nampicillin\r\nOR\r\nerythromycin used?\r\n7. Antibiotic used for at least 2 weeks?\r\n8. One follow-up?\r\n9. IF symptoms continue beyond one month\r\nOR\r\npyuria for more than one month\r\nOR\r\nbacteriuria for more than one month, consultation and/or referral?','Unknow'),('PSORIASIS','0001-01-01 00:00:00','1. Inquiry re duration of lesions OR on chart (3 minute)?\r\n2. Description of lesions (scaly, size, psoriatic etc.) OR on chart (3 minute)? \r\n3. Location of lesions noted OR on chart (3 minute)? \r\n4. IF systemic steroids used, consultant\'s note? \r\n5. IF antimitotic agents used, consultant\'s note? \r\n6. Counselling OR on chart (3 minute)? ','Unknow'),('PULMONARY EMPHYSEMA','0001-01-01 00:00:00','1. Inquiry re chest symptoms each visit, at least two of the following?\r\ncough\r\nsputum\r\nwheezing\r\ndyspnea\r\n2. CPE at least once in 2 years?\r\n3. ECG on chart (3 minute)? \r\n4. Chest X-ray at least once in 2 years?\r\n5. IF smoker, advice re smoking?\r\n6. Follow-up at least once yearly?','Unknow'),('PYELONEPHRITIS, ACUT','0001-01-01 00:00:00','1. Inquiry re at least 3 of following? \r\nurinary frequency \r\nurinary urgency \r\nburning on urination (dysuria) \r\nlumbar back pain \r\nfever \r\nchills \r\n2. Presence/absence of fever noted? \r\n3. Presence/absence of lumbar (CVA) tenderness? \r\n4. Urinalysis AND micro? \r\n5. WBC? \r\n6. Urine C&S prior to treatment? \r\n7. Urine C&S positive? \r\n8. Antibiotic used AND was it one of penicillins, sulfonamides, Septra/Bactrim, cephalosporins, or tetracyclines? \r\n9. IF tetracycline used, was patient \r\n10. Was antibiotic used for 7 days or more initially? \r\n11. IF lab report indicates that organism not sensitive to initial antibiotic used, was antibiotic changed OR did physician indicate \"patient better\"? \r\n12. One follow-up within two weeks? \r\n13. Repeat urine C&S after treatment? ','Unknow'),('PYELONEPHRITIS, CHRO','0001-01-01 00:00:00','1. Inquiry re 3 of following OR on chart (3 minute)? \r\nurinary frequency \r\nurinary urgency \r\nburning on urination (dysuria) \r\nlumbar back pain \r\nfever \r\nchills \r\n2. Blood pressure at least yearly? \r\n3. Urinalysis AND micro at least once in 2 years? \r\n4. Urine C&S at least once in 2 years? \r\n5. Urine C&S for acid-fast bacilli on chart (3 minute)? \r\n6. BUN OR creatinine at least once in 2 years? \r\n7. IVP on chart (3 minute)? \r\n8. Follow-up at least yearly? ','Unknow'),('PYODERMA (INC. IMPET','0001-01-01 00:00:00','1. Site noted? \r\n2. IF oral antibiotic used, was it one of penicillins, erythromycins, sulfonamides, tetracyclines, or cephalosporins? \r\n3. IF tetracycline used, was patient ','Unknow'),('RECTAL BLEEDING','0001-01-01 00:00:00','1. Inquiry re at least 2 of following? \r\namount \r\ntype of bleeding \r\nduration of bleeding \r\n2. Inquiry re bowel habits? \r\n3. Abdominal exam? \r\n4. Rectal exam? \r\n5. Hemoglobin within 1 week? \r\n6. Proctoscopic exam within 1 week? \r\n7. Sigmoidoscopic exam OR referral within 2 weeks? \r\n8. IF > 30, barium enema AND air contrast within 1 month? \r\n9. IF 30 years old or less AND no cause found on sigmoidoscopic, barium enema AND air contrast within 1 month? \r\n10. Barium enema AND/OR sigmoidoscopic exam within 1 month? \r\n11. IF no diagnosis established after 1 month, referral/consultation OR statement of justification? \r\n12. IF not hemorrhoids, one follow-up? ','Unknow'),('REFLUX ESOPHAGITIS','0001-01-01 00:00:00','1. Inquiry re duration of symptoms? \r\n2. At least two of following present? \r\nheartburn with bending over recumbency \r\nwater brash \r\nintolerance to rich or spicy foods \r\nintolerance to alcohol \r\ndysphagia \r\nbelching \r\n3. Abdominal exam? \r\n4. IF dysphagia present, endoscopy? \r\n5. IF UGI series performed, reflux demonstrated? \r\n6. Advice re elevation of head of bed? \r\n7. Advice re diet (eg. avoid rich foods, spices, alcohol, coffee, tea, late meals, large meals,)? \r\n8. IF obesity noted, advice re weight reduction? ','Unknow'),('RHEUMATIC HEAR DISEA','0001-01-01 00:00:00','1. Inquiry re at least one of following? \r\ndyspnea on exertion \r\neffort intolerance \r\nchest pain \r\nfatique \r\n2. Description of cardiac sounds, rhythm, murmurs? \r\n3. Blood pressure? \r\n4. IF available in the community, echocardiography? \r\n5. Chest X-ray on chart? \r\n6. IF prophylactic antibiotic used, was it one of the penicillins, cephalosporins, sulfonamides, erythromycins? \r\n7. Advice re antibiotic coverage for instrumentation procedures (eg. dental surgery, urology, gynecology)? ','Unknow'),('RUBELLA','0001-01-01 00:00:00','1. Inquiry re at least one of following? \r\nfatigue enlarged glands \r\nmalaise rhinitis\r\nmyalgia conjunctivitis\r\nfever abdominal pain\r\nsore throat ear pain\r\n2. Inquiry re duration of symptom? \r\n3. Rash noted? \r\n4. Presence of posterior auricular nodes noted? ','Unknow'),('SCARLET FEVER','0001-01-01 00:00:00','','Unknow'),('SCOLIOSIS','0001-01-01 00:00:00','** NOTE **\r\nAudit only presenting visit. \r\n1. Inquiry re how condition found? \r\n2. Description of location (eg. thoracic, lumbar)? \r\n3. Description of extent (degree of angulation)? \r\n4. X-ray of affected area(s) of spine within 3 months of initial diagnosis? \r\n5. X-ray confirms diagnosis of scoliosis? \r\n6. IF 9 to 16 years old AND severe (angulation greater than or equal to 15 degrees, consultation OR referral? \r\n7. IF not referred, follow-up within 3 months? ','Unknow'),('SECONDARY AMMENORRHE','0001-01-01 00:00:00','1. Menstrual history? \r\n2. Duration of problem? \r\n3. Description re onset of problem? \r\n4. History of medications (including oral contraceptives)? \r\n5. Inquiry re changes in diet? \r\n6. Inquiry re stress factors AND/OR athletics? \r\n7. Pelvic exam? \r\n8. Abdominal exam? \r\n9. Pregnancy test? \r\n10. CBC? \r\n11. Thyroid function (at least one of TSH,T3,T4)? \r\n12. Fasting blood sugar on chart (3 minute)? \r\n13. IF more than 3 months duration, prolactin? \r\n14. Pelvic ultrasound on chart (3 minute)? \r\n15. IF more than 3 months duration, X-ray of pituitary? \r\n16. Follow-up until cause found or referral? ','Unknow'),('SEROUS OTITIS MEDIA','0001-01-01 00:00:00','1. Inquiry re at least two of following; hearing, pain, recurrent URI? \r\n2. Comment re fluid in middle ear OR retracted ear drum? \r\n3. Comment re nose AND throat? \r\n4. IF third episode or more, audiometry OR referral? \r\n5. IF physical findings OR hearing test are abnormal, follow-up until resolved OR referral? ','Unknow'),('SINUSITIS','0001-01-01 00:00:00','1. Inquiry re pain in the face and/or head? \r\n2. Inquiry re nasal blockage? \r\n3. Presence/absence of fever noted? \r\n4. Presence/absence of tenderness over sinuses noted? \r\n5. IF recurrent (3 or more visits), X-ray of sinuses? \r\n6. Tenderness over sinuses OR positive X-ray of sinuses? \r\n7. IF antibiotic used, was it one of the penicillins, sulfonamides, erythromycins, cephalosporins, or tetracycline?\r\n8. IF tetracycline used, was patient ','Unknow'),('SKIN ABSCESS','0001-01-01 00:00:00','1. Inquiry re location? \r\n2. Inquiry re recurrent or first attack? \r\n3. Description of size? \r\n4. Presence/absence of fluctuation? \r\n5. Presence/absence of lymphangitis? \r\n6. C & S of pus? \r\n7. IF recurrent, fasting serum glucose? \r\n8. Demonstration of pus? \r\n9. I & D? \r\n10. One follow-up within 10 days? ','Unknow'),('SOAP','0001-01-01 00:00:00','Subject:\n\nObject: \n\nAssessment: \n\nPlan:\n','<table'),('SPONTANEOUS ABORTION','0001-01-01 00:00:00','1. Date of LMP noted?\r\n2. Duration of LMP noted?\r\n3. Uterine cramps noted?\r\n4. Amount AND duration of vaginal bleeding?\r\n5. Passage of tissue?\r\n6. Pelvic exam with comment re cervix open or closed?\r\n7. Blood pressure?\r\n8. Pulse?\r\n9. Presence/absence of fever?\r\n10. Pregnancy test?\r\n11. Hemoglobin?\r\n12. Hematocrit?\r\n13. Rh factors?\r\n14. IF tissue available, specimen sent to lab?\r\n15. IF indicated by Rh factors, RHOGAM/Rh immune globulin?\r\n16. One follow-up within one month?','Unknow'),('SPRAIN OR STRAIN, NY','0001-01-01 00:00:00','1. Inquiry re how injury happened? \r\n2. Inquiry re location of injury? \r\n3. Time of injury? \r\n4. Presence/absence of swelling? \r\n5. Presence/absence of tenderness? \r\n6. Presence/absence of hematoma? \r\n7. IF sports related, advice re prevention of further episodes? ','Unknow'),('STASIS DERMATITIS','0001-01-01 00:00:00','1. Comment on location?\r\n2. Inquiry re duration?\r\n3. Presence/absence of varicose veins noted?\r\n4. Description of lesions?\r\n5. One follow-up within one month?','Unknow'),('STOMATITIS, HERPETIC','0001-01-01 00:00:00','1. Inquiry re pain in mouth? \r\n2. Oral ulcerations noted? ','Unknow'),('STOMATITIS, MONILIAL','0001-01-01 00:00:00','1. Inquiry re location AND duration of oral lesions? \r\n2. IF adult, inquiry re underlying cause (eg. antibiotics diabetes) OR this information on chart (3 minute)? \r\n3. Presence/absence of plaques in mouth noted? \r\n4. IF lesions unresolved within 2 weeks after therapy started, C & S of lesions for monilia? \r\n5. White plaques in mouth? \r\n6. Local antimonilial agent? \r\n7. Antibiotic used? \r\n8. Follow-up within 2 weeks? ','Unknow'),('STREP THROAT','0001-01-01 00:00:00','1. Inquiry re sore throat?\r\n2. Inquiry re presence/absence of fever?\r\n3. Inquiry re cough?\r\n4. Throat exam?\r\n5. Presence/absence of cervical lymphadenopathy noted?\r\n6. Presence/absence of pharyngeal exudate noted?\r\n7. IF fever OR lymphadenopathy OR exudate OR enlarged tonsils, throat swab C & S?\r\n8. Antibiotic used AND was it one of the penicillins, erythromycins, or cephalosporins?\r\n9. IF antibiotic used AND patient antibiotic used for at least 7 days?\r\n10. One follow-up within two weeks?\r\n11. IF positive strep culture, antibiotics used?','Unknow'),('STY','0001-01-01 00:00:00','1. Painful or swollen eyelid? ','Unknow'),('SYNCOPE, NYD','0001-01-01 00:00:00','1. Inquiry re three of the following?\r\nrecurrent or initial episode predisposing factors (stress, pain, hyperventilation) description of event medications taken any associated injuries\r\n2. Inquiry re duration of unconsciousness? \r\n3. Neurological comments (eg. reflexes, pupils, movements)?\r\n4. Blood pressure?\r\n5. Presence/absence of hyperventilation noted?\r\n6. IF > 55 years, ECG?\r\n7. IF 2nd or more episode, blood sugar?\r\n8. IF 2nd or more episode, CBC?\r\n9. IF 2nd or more episode, EEG?\r\n10. IF 2nd or more episode, follow-up within 1 month OR referral?','Unknow'),('SYPHILIS','0001-01-01 00:00:00','1. Inquiry re exposure?\r\n2. IF skin lesion present, inquiry re duration?\r\n3. IF primary syphilis, presence/absence of chancre noted?\r\n4. IF secondary syphilis, presence/absence of rash noted?\r\n5. Presence/absence of lymphadenopathy noted?\r\n6. VDRL OR STS?\r\n7. IF VDRL OR STS negative, repeated within 2 months?\r\n8. Swab for C & S for gonorrhea?\r\n9. IF antibiotic used, was it one of the penicillins, erythromycins, tetracyclines or spectinomycin?\r\n10. Notification of public health authorities?\r\n11. One follow-up within 2 months?','Unknow'),('TENSION HEADACHE','0001-01-01 00:00:00','1. Inquiry re at least five of following? \r\nlocation of pain \r\nduration \r\ntime of onset \r\nfrequency \r\nassociated symptoms (nausea) \r\nfamily history \r\npsychosocial factors \r\n2. Blood pressure within last year? \r\n3. CPE, including neurological exam within last year? \r\n4. Headache is stress related? \r\n5. Stress factors identified AND counselling done? \r\n6. IF on medication, follow-up at least every 3 months? \r\n7. IF narcotic analgesic prescribed, dose AND duration recorded? ','Unknow'),('THERAPEUTIC ABORTION','0001-01-01 00:00:00','1. Obstetrical history? \r\n2. Date of LMP noted? \r\n3. Parity noted? \r\n4. Pelvic exam, findings noted OR referral? \r\n5. Estimate of size of uterus OR weeks of preqnancy OR referral? \r\n6. Rh factor? \r\n7. Pregnancy test done? \r\n8. Pregnancy test positive? \r\n9. IF indicated by Rh factors, RHOGAM/Rh immune globulin? \r\n10. Admit for D & C OR referral? \r\n11. Family planning OR birth control counselling? \r\n12. One follow-up within 6 weeks after abortion? ','Unknow'),('THREATENED ABORTION','0001-01-01 00:00:00','1. Date of LMP noted? \r\n2. Amount of vaginal bleeding? \r\n3. Duration of vaginal bleeding? \r\n4. Uterine cramps? \r\n5. IF heavy bleeding OR continued spotting for one week, pelvic exam? \r\n6. Pregnancy test? \r\n7. Hemoglobin? \r\n8. Hematocrit? \r\n9. Rh factors? \r\n10. Blood type? \r\n11. Positive pregnancy test? \r\n12. Bedrest advised? \r\n13. Progesterone or estrogen used? \r\n14. Follow-up at least once weekly while bleeding? ','Unknow'),('THYROID NODULE','0001-01-01 00:00:00','1. Inquiry re location? \r\n2. Inquiry re duration? \r\n3. Inquiry re one of following? \r\npalpitations \r\ntremor \r\nweight loss \r\n4. Description of size of lesion? \r\n5. Comment on location (midline or lateral)? \r\n6. Referral OR thyroid function tests (T3 and T4 and TSH) AND I-131 uptake/thyroid scan OR ultrasound? \r\n7. Follow-up within 2 months, OR referral? ','Unknow'),('TONSILLITIS, ACUTE','0001-01-01 00:00:00','1. Inquiry re sore throat?\r\n2. Description of tonsils?\r\n3. IF erythromycin, cephalosporin or sulfa used?\r\n4. IF > 4 years and cephalosporin, or sulfa used?\r\n5. IF >= 13 years, was penicillin, erythromycin,\r\ncephalosporin, sulfa, or tetracycline used?\r\n6. IF tetracycline used, was patient','Unknow'),('TONSILLITIS, CHRONIC','0001-01-01 00:00:00','1. Inquiry re recurrent sore throat? \r\n2. Description of tonsils? \r\n3. Presence/absence of cervical glands noted? \r\n4. IF antibiotic used, was it one of the penicillins, erythromycins, cephalosporins, or tetracyclines? \r\n5. IF tonsillectomy OR referral, were there 4 or more episodes within 2 years OR peritonsillar abscess (quinsy) OR unilateral emlargement OR demonstrated hearing loss? \r\n6. IF tetracycline used, was patient ','Unknow'),('TRANSIENT CEREBRAL I','0001-01-01 00:00:00','1. Inquiry re frequency?\r\n2. Inquiry re duration of each episode?\r\n3. Description of symptoms?\r\n4. Neurological exam with description of deficit?\r\n5. Blood pressure?\r\n6. Cardiovascular examination?\r\n7. Presence/absence of bruits in neck?\r\n8. ECG?\r\n9. IF male > 55 years, ASA prescribed as initial medication OR justification noted?\r\n10. IF ASA used, duration AND dosage recorded?\r\n11. IF two or more episodes, referral OR admission to hospital?\r\n12. IF smoker, advice re smoking?\r\n13. One follow-up within one month?\r\n14. Cause (eg. embolus, thrombosis) noted within one month OR referral?','Unknow'),('TRIGEMINAL NEURALGIA','0001-01-01 00:00:00','1. Inquiry re severity of pain?\r\n2. Inquiry re duration of pain?\r\n3. Inquiry re facial pain?\r\n4. Inquiry re initiating stimuli?\r\n5. Neurological exam?\r\n6. IF Tegretol given, liver function tests within 6 weeks?\r\n7. Discussion re natural history of disease OR reassurance?\r\n8. One follow-up within 3 months?','Unknow'),('UMBILICAL HERNIA','0001-01-01 00:00:00','*** Patient under 1 year old\r\n1. Well baby care visits?\r\n2. IF surgery done, was justification noted (eg. thin skin, too large, pain, ulceration)?','Unknow'),('URETHRITIS, NYD','0001-01-01 00:00:00','1. Inquiry re urinary symptoms?\r\n2. Inquiry re sexual contacts OR injury?\r\n3. Comment re presence/absence of urethral discharge?\r\n4. Genital exam?\r\n5. Urinalysis AND micro?\r\n6. Urine C & S?\r\n7. IF discharge present, urethral swab C & S?\r\n8. VDRL OR STS?\r\n9. IF antibiotic used, was it one of the penicillins, erythromycins, sulfonamides, Septra/Bactrim, cephalosporins, or tetracyclines?\r\n10. One follow-up within 2 weeks?\r\n11. IF urine C & S OR urethral swab C & S still positive after antibiotic treatment, antibiotic changed?\r\n12. IF urine C & S OR urethral swab C & S positive, discussion re notification of sexual partner(s)?\r\n13. IF urethral swab C & S positive for gonorrhea or chlamydia, notification of public health authorities?','Unknow'),('URI','0001-01-01 00:00:00','1. Complaint of at least one of the following?\r\nnasal discharge\r\nsore throat\r\nmalaise\r\ncold\r\n2. Duration of symptoms noted?\r\n3. IF cough in history, chest exam?\r\n4. IF patient\r\n5. IF sore throat in history, throat exam?\r\n6. IF narcotic antitussives prescribed, cough in history?\r\n7. IF antibiotics prescribed, was there history of secondary infection (coloured phlegm, or fever > 38 for 3 days or more)\r\nOR\r\nhigh risk (cardiac valvular disease or chronic pulmonary disease)?','Unknow'),('URINARY TRACT INFECT','0001-01-01 00:00:00','1. Inquiry re duration of symptoms? \r\n2. Inquiry re first or recurring episode? \r\n3. Inquiry re at least two of following?\r\nfrequency \r\ndysuria \r\nhematuria\r\nfever \r\n4. Abdominal exam?\r\n5. Presence/absence of flank OR CVA tenderness noted? \r\n6. IF more than 2 infections within one year in female, vaginal exam? \r\n7. Urinalysis AND micro? \r\n8. Urine C & S? \r\n9. IF 3rd or more occurrence (3 minute) in female, IVP? \r\n10. IF 2nd or more occurrence (3 minute) in males, IVP? \r\n11. IF child AND 2nd or more occurrence in chart, voiding cysto-urethrogram? \r\n12. IF antibiotic used, was it one of penicillins, erythromycins, sulfonamides, cephalosporins, Septra/Bactrim, or tetracyclines? \r\n13. IF tetracycline used, was patient\r\n14. IF child OR discussion re causes of UTI\'s? \r\n15. IF condition persists without definitive diagnosis for more than 3 months, referral? \r\n16. One follow-up within one month?','Unknow'),('URTICARIA','0001-01-01 00:00:00','1. Inquiry re duration of rash? \r\n2. Inquiry re location of rash? \r\n3. Inquiry re possible cause (eg. diet, stress, medications)? \r\n4. Description of lesion? \r\n5. IF life threatening (eg. laryngeal edema, circulatory collapse), epinephrine used? \r\n6. IF systemic steroids used, duration \r\n7. IF recurrent (4 or more occasions), consultation OR referral? ','Unknow'),('UTI','0001-01-01 00:00:00','1. Inquiry re duration of symptoms?\r\n2. Inquiry re first or recurring episode?\r\n3. Inquiry re at least two of following?\r\nfrequency\r\ndysuria\r\nhematuria\r\nfever\r\n4. Abdominal exam?\r\n5. Presence/absence of flank OR CVA tenderness noted?\r\n6. IF more than 2 infections within one year in female, vaginal exam?\r\n7. Urinalysis AND micro?\r\n8. Urine C & S?\r\n9. IF 3rd or more occurrence (3 minute) in female, IVP?\r\n10. IF 2nd or more occurrence (3 minute) in males, IVP?\r\n11. IF child AND 2nd or more occurrence in chart, voiding cysto-urethrogram?\r\n12. IF antibiotic used, was it one of penicillins, erythromycins, sulfonamides, cephalosporins, Septra/Bactrim, or tetracyclines?\r\n13. IF tetracycline used, was patient\r\n14. IF child\r\nOR\r\ndiscussion re causes of UTI\'s?\r\n15. IF condition persists without definitive diagnosis for more than 3 months, referral?\r\n16. One follow-up within one month?','Unknow'),('VAGINITIS, VULVITIS','0001-01-01 00:00:00','1. Inquiry re at least one of following; vaginal itch (pruritis) vulvar irritation, vaginal odour?\r\n2. Presence/absence of vaginal discharge?\r\n3. Vaginal exam?\r\n4. Vaginal AND/OR cervical C & S OR office examination of discharge in saline or KOH?\r\n5. IF Monilia (Candida) AND topical agent used, was it mystatin OR miconazole OR cotrimoxazole?\r\n6. IF Trichomonas AND systemic or topical agent used, was it metronidazole?\r\n7. IF Gardnerella AND systemic or topical agent used, was it metronidazole OR sulfonamide OR tetracycline?\r\n8. IF Trichomonas, discussion re simultaneous treatment of sexual partner?','Unknow'),('VENEREAL WARTS (COND','0001-01-01 00:00:00','1. Inquiry re duration of lesions? \r\n2. Description of size AND extent of lesions? \r\n3. VDRL OR syphilis screen? ','Unknow'),('VIRAL WARTS (VERRUCA','0001-01-01 00:00:00','1. Inquiry re duration of symptoms? \r\n2. Site(s) noted? \r\n3. Number noted? \r\n4. Electrodessication (cautery) of plantar warts on weight-bearing surfaces? \r\n5. Surgery on plantar warts? ','Unknow'),('WELL BABY CARE','0001-01-01 00:00:00','1. Inquiry re food/diet? \r\n2. Inquiry re coping/parenting skills? \r\n3. Weight recorded at each visit? \r\n4. Comment re normal/abnormal developmental milestones? \r\n5. Length recorded 3 or more times per year? \r\n6. Head circumference recorded 3 or more times in first year of life? \r\n7. Three doses of DPTP by age 8 months OR justification of alternate course? \r\n8. IF age 1 to 2, MMR at 12-15 months, DPTP at 17-19 months OR justification of alternate course? \r\n9. IF > 1 year old, at least 3 visits in first year? \r\n10. IF > 2 years old, at least 3 visits in second year? \r\n11. IF parenting problems identified, counselling OR referral? \r\n12. MMR given before 12 months of age? ','Unknow');

--
-- Dumping data for table `erefer_attachment`
--


--
-- Dumping data for table `erefer_attachment_data`
--


--
-- Dumping data for table `eyeform_macro_billing`
--


--
-- Dumping data for table `eyeform_macro_def`
--


--
-- Dumping data for table `favorites`
--


--
-- Dumping data for table `favoritesprivilege`
--


--
-- Dumping data for table `fax_config`
--


--
-- Dumping data for table `faxes`
--


--
-- Dumping data for table `fileUploadCheck`
--


--
-- Dumping data for table `flowsheet_customization`
--


--
-- Dumping data for table `flowsheet_drug`
--


--
-- Dumping data for table `flowsheet_dx`
--


--
-- Dumping data for table `form`
--


--
-- Dumping data for table `form2MinWalk`
--


--
-- Dumping data for table `formAR`
--


--
-- Dumping data for table `formAdf`
--


--
-- Dumping data for table `formAdfV2`
--


--
-- Dumping data for table `formAlpha`
--


--
-- Dumping data for table `formAnnual`
--


--
-- Dumping data for table `formAnnualV2`
--


--
-- Dumping data for table `formBCHP`
--


--
-- Dumping data for table `formCESD`
--


--
-- Dumping data for table `formCaregiver`
--


--
-- Dumping data for table `formConsult`
--


--
-- Dumping data for table `formCostQuestionnaire`
--


--
-- Dumping data for table `formCounseling`
--


--
-- Dumping data for table `formFalls`
--


--
-- Dumping data for table `formGripStrength`
--


--
-- Dumping data for table `formGrowth0_36`
--


--
-- Dumping data for table `formGrowthChart`
--


--
-- Dumping data for table `formHomeFalls`
--


--
-- Dumping data for table `formImmunAllergy`
--


--
-- Dumping data for table `formIntakeHx`
--


--
-- Dumping data for table `formIntakeInfo`
--


--
-- Dumping data for table `formInternetAccess`
--


--
-- Dumping data for table `formLabReq`
--


--
-- Dumping data for table `formLateLifeFDIDisability`
--


--
-- Dumping data for table `formLateLifeFDIFunction`
--


--
-- Dumping data for table `formMMSE`
--


--
-- Dumping data for table `formMentalHealth`
--


--
-- Dumping data for table `formNoShowPolicy`
--


--
-- Dumping data for table `formONAREnhancedRecord`
--


--
-- Dumping data for table `formONAREnhancedRecordExt1`
--


--
-- Dumping data for table `formONAREnhancedRecordExt2`
--


--
-- Dumping data for table `formPalliativeCare`
--


--
-- Dumping data for table `formPeriMenopausal`
--


--
-- Dumping data for table `formRhImmuneGlobulin`
--


--
-- Dumping data for table `formRourke`
--


--
-- Dumping data for table `formRourke2006`
--


--
-- Dumping data for table `formSF36`
--


--
-- Dumping data for table `formSF36Caregiver`
--


--
-- Dumping data for table `formSatisfactionScale`
--


--
-- Dumping data for table `formSelfAdministered`
--


--
-- Dumping data for table `formSelfAssessment`
--


--
-- Dumping data for table `formSelfEfficacy`
--


--
-- Dumping data for table `formSelfManagement`
--


--
-- Dumping data for table `formTreatmentPref`
--


--
-- Dumping data for table `formType2Diabetes`
--


--
-- Dumping data for table `formVTForm`
--


--
-- Dumping data for table `form_hsfo2_visit`
--


--
-- Dumping data for table `formchf`
--


--
-- Dumping data for table `groupMembers_tbl`
--


--
-- Dumping data for table `groups_tbl`
--

INSERT INTO `groups_tbl` (`groupID`, `parentID`, `groupDesc`) VALUES (17,0,'doc');

--
-- Dumping data for table `gstControl`
--

INSERT INTO `gstControl` (`gstFlag`, `gstPercent`, `id`) VALUES (0,5,1);

--
-- Dumping data for table `hash_audit`
--


--
-- Dumping data for table `hl7TextInfo`
--


--
-- Dumping data for table `hl7TextMessage`
--


--
-- Dumping data for table `hsfo2_patient`
--


--
-- Dumping data for table `hsfo2_system`
--


--
-- Dumping data for table `hsfo_recommit_schedule`
--


--
-- Dumping data for table `ichppccode`
--

INSERT INTO `ichppccode` (`ichppccode`, `diagnostic_code`, `description`) VALUES ('000','831','Dislocated Shoulder'),('001','002','Typhoid & Paratyphoid Fevers'),('002','009','Diarrhea/Presumed Infect.Intest Dis'),('003','349','Other Diseases Of CNS (CP), Neuralgia'),('004','010','TB skin test conv.Tuberculosis infection, primary'),('005','511','Pleural Effusion NOS'),('006','033','Whooping Cough'),('007','034','Strep Thr, Scarlet Fev, Erysipelas'),('008','045','Polio & CNS Enteroviral Diseases'),('009','052','Chickenpox'),('010','053','Herpes Zoster, Shingles'),('011','054','Herpes Simplex, All Sites'),('012','055','Measles'),('013','056','Rubella'),('014','057','Viral Xanthems'),('015','070','Infectious Hepatitis'),('016','072','Mumps'),('017','075','Infectious Mononucleosis'),('018','372','Viral Conjunctivitis'),('019','078','Warts, All Sites'),('020','079','Viral Infection NOS'),('020.1','799','Sexually transmitted disease, STD'),('021','136','Malaria'),('022','097','Syphilis, All Sites And Stages'),('023','098','Gonococcal Infections'),('024','117','Dermatophytosis & Dermatomycosis, fungal infection/Tinea'),('025','112','Moniliasis Excl Urogenital'),('026','112','Moniliasis, Urogenital, Proven'),('027','131','Trichomonas, Urogenital, Proven'),('028','127','Oxyuriasis, Pinworms, Helminthiasis'),('029','132','Lice, Head Or Body, Pediculosis'),('030','133','Scabies & Other Acariasis'),('031','136','Sepsis/Other Infect/Parasutic Diseases NEC/STD/fungus/coxsackie'),('032','151','Malig Neopl G.I. Tract, Colon Cancer'),('033','162','Malignant Neopl Respiratory Tract, lung cancer'),('034','173','Malig Neo Skin/Subcutaneous Tissue'),('035','174','Malignant Neoplasm Breast'),('036','180','Malig Neoplasm Female Genital Tract'),('037','188','Malig Neop Urinary & Male Genital'),('037.1','185','Prostate cancer'),('038','201','Hodgkins Disease,Lymphoma,Leukemia'),('039','199','Other Malignant Neoplasms NEC'),('040','214','Lipoma, Any Site'),('041','216','Mole, Pigmented Nevus'),('042','217','Benign Neoplasm Breast'),('043','218','Fibroids, Benign Neoplasm Uterus'),('044','228','Hemangioma & Lymphangioma'),('045','229','Other Benign Neoplasms NEC'),('046','239','Neoplasm Nyd As Benign Or Malignant'),('047','240','Nontoxic Goiter & Nodule'),('048','242','Thyrotoxicosis W/WO Goiter,Hyperthyroidism'),('049','244','Hypothyroidism, Myxedema, Cretinism'),('050','250','Diabetes Mellitus, NIDDM, IDDM'),('050.1','251','Glucose Intolerance'),('051','790','Abnormal Unexplained Biochem Test'),('052','269','Avitamin & Nutritional Disorder NEC'),('053','269','Feeding Problem Baby Or Elderly'),('053.1','269','Feeding Problem Baby'),('053.2','269','Elderly Feeding Problem'),('053.3','269','Breast Feeding Difficulties'),('054','274','Gout'),('055','278','Obesity'),('056','272','Lipid Metabolism Disorders/Hypercholesterolemia/Hyperlipidemia'),('057','259','AIDS,HIV,Other Endocr,Nutritn,Metabol Disord,Jaundice,Dehydration,immunity disorders'),('058','280','Iron Deficiency Anemia'),('059','281','Pernicious & Other Deficienc Anemia (B12 deficiency)'),('060','282','Hereditary Hemolytic Anemias'),('061','285','Anemia, Other/Unspecified'),('062','286','Purpura,Hemorrhag & Coagulat Defect'),('063','289','Lymphadenitis, Chronic/Nonspecific'),('064','288','Abnormal White Cell Count'),('065','289','Blood/Blood Forming Organ Disor NEC'),('066','290','Dementia/organic psychosis'),('067','295','Schizophrenia'),('068','296','(DO NOT USE) Manic Depressive Psychosis'),('068.1','296','Bi-polar/bipolar affective disorder'),('069','298','(DO NOT USE) Psychosis, Other/NOS Excl Alcoholic'),('070','300','Anxiety'),('070.1','300','Post-traumatic stress disorder'),('070.2','300','Panic Disorder'),('071','300','Hysterical & Hypochondriac Disorder'),('071.1','300','Somatoform/psychosomatic disturbance'),('072','300','Depression'),('072.1','300','Dysthymia'),('073','300','(DO NOT USE) Neurosis, Other/Unspecified'),('073.1','300','Phobia'),('073.2','300','Obsessive-compulsive disorder'),('074','315','(DO NOT USE) Specified Delays In Development'),('074.1','315','Learning disorder'),('074.2','315','Attention deficit disorder, ADD, ADHD'),('075','307','Sleep Disorders, Insomnia'),('076','307','Tension Headaches'),('077','309','(DO NOT USE) Adjustment Reaction, grief'),('077.1','309','Grief reaction/bereavement'),('077.2','309','Coping with physical illness'),('077.3','309','Adolescent adjustment'),('078','313','(DO NOT USE) Behaviour Disorders, Child/Adolesce, ADD, ADHD'),('078.1','313','Behavioural problem/conduct disorder'),('078.2','313','Discipline, Temper Tantrums, Conduct Disorder'),('078.3','313','Behaviour Problem, Conduct Disorder'),('079','302','Sexual Dysfunction'),('080','303','Alcoholism & Alcohol Problem'),('080.1','303','Alcohol Abuse'),('081','291','Acute Alcoholic Intoxication'),('082','304','Tobacco Abuse/Smoking Cessation'),('082.1','304','Smokestop'),('083','304','Drug Addiction, Dependence'),('083.1','304','Illegal Drug Addiction, Dependence'),('083.2','304','Legal Drug Addiction, Dependence'),('083.3','304','Prescription drug dependence'),('084','301','Personality Disorders'),('084.1','301','(DO NOT USE) Substance/alcohol abuse, not tobacco'),('085','319','(DO NOT USE) Mental Retardation'),('085.1','319','Developmental delay'),('086','298','Other Psychiatric Disorder'),('086.1','301','Self esteem problem'),('086.2','307','Eating disorder'),('086.3','301','Sexual identity problem'),('086.4','299','Autism'),('086.5','300','Self mutilation'),('087','340','Multiple Sclerosis/MS'),('088','332','Parkinsonism'),('089','345','Epilepsy/Seizure, All Types'),('090','346','Migraine Headaches'),('091','343','Other Neurological Disorders/Carpal Tunnel Syndrome/Trigeminal Neuralgia'),('092','372','Conjunctivitis & Ophthalmia'),('093','373','Stye, Chalazion'),('094','367','Myopia,Astigmatism,Other Refrac Dis'),('096','366','Cataract'),('097','365','Glaucoma'),('098','369','Blindness'),('099','379','Other Eye Diseases, Vision Problem'),('100','380','Otitis Externa/OE'),('101','382','Acute Otitis Media/OM'),('102','381','Acute & Chronic Serous Otitis Media'),('103','381','Eustachian Block Or Catarrh'),('104','386','Labyrinthitis, Meniere&#146;s Disease'),('105','389','Deafness, Partial or Complete/ Hearing problem'),('106','388','Wax In Ear'),('107','388','Tinnitus/Ear Pain/Otalgia'),('108','390','Rheumatic Fever/Heart Disease'),('109','410','Acute MI'),('110','413','Acute coronary insufficiency, Angina Pectoris(CAD, Ischemic Heart)/IHD'),('110.1','412','Post MI, Old Myocardial infarction, chronic coronary artery disease'),('111','429','Disease Heart Valve Non-Rheum,NOS,NYD'),('112','428','Congestive Heart Failure (CHF)'),('113','427','Atrial Fibrillation or Flutter'),('114','427','Paroxysmal Tachycardia'),('115','427','Ectopic Beats, All Types'),('116','785','Heart Murmur NEC, NYD'),('117','429','Pulmonary Heart Disease'),('118','429','Other Heart Diseases NEC,cardiomyopathy'),('119','796','Elevated Blood Pressure (BP)'),('120','401','Hypertension - Uncomplicated (HTN)'),('121','402','Hypertension - Target Organ Invl (HTN)'),('123','435','Transient Cerebral Ischemia/TIA'),('124','436','CVA, Stroke'),('125','440','Arteriosclerosis, Atherosclerosis'),('126','447','Other Disorders Of Arteries/claudication'),('127','415','Pulmonary Embolism & Infarction'),('128','451','Phlebitis, Thrombophlebitis (DVT)'),('129','454','Varicose Veins - Legs, venous stasis'),('130','455','Hemorrhoids'),('131','447','Postural Hypotension'),('132','459','Other Periph. Vessel Dis, Aneurysm, CVD'),('133','460','Common Cold, Acute URI, Pharyngitis, URTI'),('134','461','Sinusitis, Acute & Chronic'),('135','463','Tonsilitis And Quinsy'),('136','474','Chronic Infection Tonsils/Adenoids'),('137','464','Laryngitis&Tracheitis, Acute, Croup'),('138','466','Bronchitis & Bronchiolitis, Acute'),('139','487','Influenza'),('140','486','Pneumonia'),('141','511','Pleurisy All Types Excl Tubercul'),('142','491','Chronic Bronchitis'),('143','492','Emphysema & COPD'),('144','493','Asthma'),('145','477','Hay Fever, allergic rhinitis, allergies'),('146','680','Boil In Nose'),('147','519','Other Respiratory, Atelectasis'),('148','521','Dental Disorders'),('149','529','Glossitis/Mouth Disease'),('149.1','529','Thrush'),('149.2','529','Sore Throat'),('150','530','Esophageal Disorder(GERD/esophagitis),Reflux'),('151','532','Duodenal Ulcer/Gastritis/Gastroenteritis'),('152','531','Other Peptic Ulcer, H Pylori, PUD'),('153','536','Other Stomach & Duoden Dis/Disord'),('154','540','Appendicitis, All Types'),('155','550','Inguinal Hernia W/WO Obstruction'),('156','552','Hiatus/Diaphragmatic Hernia'),('157','553','Other Hernias'),('158','562','Diverticular Disease Of Intestine'),('159','787','Irrit Bowel Syndr IBS /Intest Disor NEC'),('160','556','Ulcerative Colitis, Crohn&#146;s, Inflammatory Bowel'),('161','564','Constipation'),('162','565','Anal Fissure/Fistula/Abscess'),('163','564','Proctitis, Rectal & Anal Pain NOS'),('164','569','Rectal Bleeding'),('165','571','Cirrhosis & Other Liver Diseases'),('166','575','Cholecystitis/Gallbladder Disease'),('167','579','Other Digestive Sys. Dis. NEC, Dysphagia'),('168','580','Glumerulonephritis, Acute & Chronic'),('169','590','Pyelonephritis & Pyelitis,Acute/Chr'),('170','595','Cystitis & UTI (Urinary Tract Infection)'),('171','592','Urinary Calculus/ kidney stone'),('172','597','Urethritis'),('173','593','Orthostatic Albuminuria'),('174','598','Other Urinary System Diseases NEC/ RENAL FAILURE'),('175','600','Benign Prostatic Hypertrophy/BPH'),('176','601','Prostatitis & Seminal Vesiculitis'),('177','603','Hydrocele'),('178','604','Orchitis & Epididymitis'),('179','605','Phimosis & Paraphimosis'),('180','608','Other Male Genital Organ Diseases'),('181','610','Chronic cystic breast disease, fibrocystic breast disease, cyst breast benign'),('182','611','Other Breast Diseases(gynecomastia)'),('183','615','PID, Pelvic Inflammatory Disease, Acute Or Chronic Endometritis (PID)'),('184','752','Cervical Hyperplasia'),('185','616','Vaginitis NOS, Vulvitis, Yeast Vaginitis'),('186','618','Cystocele,Rectocele,Uterine Prolaps'),('187','627','Menopausal Symptoms/Menopause,post menopausal bleeding'),('188','625','Premenstrual Tension Syndrome (PMS)'),('189','626','Amenorrhea, Absent, Scanty, Rare Menstruation'),('190','626','Excessive Menstruation'),('191','625','Dysmenorrhea'),('193','626','Disorders Of Menstruation, DUB'),('194','629','Other disorders of female genital organs'),('194.1','640','Bleeding, threatened abor., hemorrhage in early pregnacy'),('195','628','Female Infertility'),('196','633','Ectopic Pregnancy'),('197','641','Abruptio Placenta, Placenta Praevia'),('197.1','640','Bleeding, threatened abortion, hemorrhage in early pregnancy'),('197.2','640','Antepartum bleeding'),('198','646','Urinary Infection, Pregnancy& Postpartum'),('199','642','Pre-eclampsia, eclampsia, toxaemia, Gestational Hypertension, Toxemias of Pregnancy & Puerperium'),('200','635','Therapeutic Abortion'),('201','634','Complete/Incomplete Abortion, Miscarriage'),('201.1','656','Decreased Fetal Movement, Fetal Distress'),('202','646','Other Complications Of Pregnancy'),('202.1','644','False Labour, Threatened Labour'),('202.2','644','Preterm Labour'),('202.3','644','Post-term Labour'),('202.4','645','Prolonged pregnancy'),('203','650','Uncomplicated Pregnancy, normal delivery'),('204','669','Complicated Delivery'),('204.1','651','Multiple Pregnancy'),('204.10','658','Premature rupture of membrane'),('204.11','645','Post Dates'),('204.2','656','Small/Large for Dates'),('204.3','652','Unusual position of fetus, malpresentation'),('204.4','653','Cephalo-pelvic disproportion'),('204.5','660','Obstructed labour'),('204.6','662','Prolonged labour'),('204.7','664','Perineal lacerations'),('204.8','666','Postpartum Hemorrhage, PPH'),('204.9','656','Decreased fetal movement'),('205','675','Mastitis & Lactation Disorders'),('206','669','Other Complication Of Puerperium'),('207','680','Boil/Cellulitis Incl Finger/Toe/Paronychia'),('209','683','Lymphadenitis, Acute'),('210','684','Impetigo'),('211','686','Pyoderma,Pyogenic Granuloma'),('212','690','Seborrhoeic Dermatitis'),('213','691','Eczema And Allergic Dermatitis'),('214','692','Contact Dermatitis'),('215','691','Diaper Rash'),('216','696','Pityriasis Rosea'),('217','696','Psoriasis'),('218','698','Pruritis And Related Conditions'),('219','700','Corns, Calluses'),('220','706','Sebaceous Cyst'),('221','703','Ingrown Toenail/Nail Diseases/Paronychia'),('222','704','Alopecia,folliculitis'),('223','799','Pompholyx & Sweat Gland Disease NEC'),('224','706','Acne, Sebaceous Cyst'),('225','707','Chronic Skin Ulcer'),('226','708','Allergic Urticaria, hives'),('227','709','Other Skin/Subcutaneous Tiss Diseas (Actinic Keratosis)'),('228','714','RH Arthritis, Still&#146;s Disease, Polymyalgia Rheumatica'),('229','715','Osteoarthritis & Allied Conditions'),('230','716','Traumatic Arthritis'),('231','715','Arthritis NEC/Diff Conn Tiss Dis,polymyalgia rheumatica, PMR'),('232','739','Shoulder Syndromes'),('233','727','Other Bursitis & Synovitis, Tendonitis'),('234','781','Muscle Pain/Myalgia/Fibromyalgia'),('235','739','Cervical Spine Syndromes'),('237','715','Osteoarthritis Of Spine'),('238','781','Back Pain (backache)W/O Radiation'),('239','724','Lumbar Strain, Sciatica, back pain with radiation'),('240','737','Scoliosis, Kyphosis, Lordosis'),('241','727','Ganglion Of Joint & Tendon'),('242','732','Osteochondritis'),('243','733','Osteoporosis'),('244','718','Chronic Internal Knee Derangement'),('245','735','Hammer Toe'),('246','739','Other Musculoskel, Connectiv Diseas (DDD)'),('247','746','Congenital Anomaly Heart & Circulat'),('248','754','Congenital Anomalies Of Lower Limb'),('249','608','Undescended Testicle'),('251','743','Blocked Tear Duct'),('252','759','Congenital Anomalies, hip diplasia'),('253','763','All Perinatal Conditions'),('254','780','Convulsions'),('255','781','Abnormal Involuntary Movement(tremor)'),('256','780','Vertigo & Giddiness, Dizzy'),('257','799','Disturbance Of Speech, hoarseness'),('258','780','Headache Except Tension And Migrain'),('259','300','Disturbance Of Sensation/Numbness'),('262','785','Chest Pain'),('263','786','Palpitations'),('264','780','Syncope, Faint, Blackout'),('265','785','Edema'),('266','785','Enlarged Lymph Nodes, Not Infected'),('267','786','Epistaxis'),('268','786','Hemoptysis'),('269','786','Dyspnea/SOB'),('270','786','Cough'),('273','787','(DO NOT USE) Anorexia'),('274','643','Nausea and/or vomiting, hyperemesis gravidarum'),('275','787','Heartburn/dyspepsia'),('276','787','Hematemesis/Melena'),('277','289','Hepatomegaly/Splenomegaly'),('278','787','Flatulence, Bloating, Eructation'),('279','787','Abdominal Pain'),('280','786','Dysuria'),('281','788','Enuresis, Incontinence'),('281.1','788','Toilet Training Problems'),('283','788','Frequency Of Urination'),('286','781','Leg Pain'),('288','781','Pain Or Stiffness In Joint'),('289','781','Swelling Or Effusion Of Joint'),('290','780','Excessive Sweating, Night Sweats'),('291','780','Fever - Undetermined Cause'),('292','691','Rash & Other Non Spec. Skin Erupt.'),('293','799','Weight Loss'),('294','783','Lack Of Expected Physiolog Develop'),('294.1','315','Developmental delay'),('295','780','Fatigue, Malaise, Tiredness'),('296','229','Mass & Localized Swelling NOS/NYD'),('297','797','Senility Without Psychosis'),('298','791','Abnormal Urine Test NEC'),('299','796','Other Unexplained Abnormal Results'),('300','788','Sign, Symptom, Ill Defined Cond NEC'),('301','802','Skull/Facial Fractures'),('302','805','Fracture Vertebral Column'),('303','807','Fractured Ribs'),('304','810','Fractured Clavicle'),('305','812','Fractured Humerus'),('306','813','Fractured Radius/Ulna'),('307','815','Fractured Metacarpals'),('308','816','Fractured Phalanges - Foot/Hand'),('309','821','Fractured Femur'),('310','823','Fractured Tibia/Fibula'),('311','829','Other Fractures'),('312','718','Acute Damage Knee Meniscus'),('313','839','Other Dislocations'),('314','840','Sprain/Strain Shoulder And Arm'),('315','842','Sprain/Strain Wrist, Hand, Fingers'),('316','844','Sprain/Strain Knee, Leg'),('317','845','Sprain/Strain Ankle, Foot, Toes'),('318','845','Sprain/Strain Foot, Toes'),('318.1','845','Heel pain, plantar fasciitis'),('319','847','Sprain/Strain Neck, Low Back,Coccyx'),('320','847','Sprain/Strain Vertebral Excl Neck'),('321','848','Other Sprains And Strains'),('322','850','Head injury, concussion, intracranial injury'),('323','879','Laceration/Open Wound/Traum Amputat/Needlestick injury'),('325','989','Insect Bites / Bee Stings'),('326','919','Abrasion, Scratch, Blister'),('327','919','Bruise, Contusion, Crushing'),('328','949','Burns & Scalds - All Degrees'),('329','930','Foreign Body In Tissues'),('330','930','Foreign Body In Eye'),('331','930','Foreign Body Entering Thru Orifice'),('332','959','Late Effect Of Trauma'),('332.1','959','Motor Vehicle Accident, MVA'),('333','959','Other Injuries & Trauma, Fall, Soft Tissue Injury'),('334','977','Overdose, Poisoning, Accidental Ingestion'),('335','989','Adverse Effects Of Other Chemicals'),('336','998','Surgery & Medical Care Complication'),('337','994','Adverse Effects Of Physical Factors'),('338','650','Well baby, Newborn care, Postnatal care, Postpartum care'),('338.1','917','CPX/Physical, Annual Health Adult/Teen, Well Visit'),('338.2','917','Well child 2-15 years'),('339','136','Contact/Carrier, Infec/Parasit Dis'),('340','896','Prophylactic Immunization'),('341','799','Observ/Care Pt On Medicat (HRT, medication rev)'),('342','799','Observ/Care Other Hi Risk Patient'),('343','895','Sterilization, Male/Female'),('344','895','Contraceptive Advice, Family Plan,contraception/BCP'),('345','895','Intrauterine Devices'),('346','895','Other Contraceptive Methods(IUD)'),('347','895','General Contraceptive Guidance'),('348','799','Letter, Forms, Prescription WO Exam'),('349','799','Referral WO Exam Or Interview'),('350','650','Diagnosing Pregnancy'),('351','799','Prenatal Care'),('352','799','Postnatal Care/Postpartum Care'),('353','799','Med/Surg Procedure WO Diagnosis'),('353.1','609','Circumcision'),('354','799','Advice & Health Instruction'),('354.1','895','Sexual Health'),('355','799','Problems External To Patient'),('356','897','Financial Stress'),('357','909','Housing/Placement Problem'),('358','909','Caregiver Stress'),('359','898','(DO NOT USE) Marital/Relationship Problem'),('360','899','(DO NOT USE) Parent/Child Problem, Child Abuse'),('360.1','899','Parent/child problem'),('360.3','899','Adult Child of Alcoholic'),('361','900','(DO NOT USE) Aged Parent Or In-Law Problem'),('362','901','Separation/divorce'),('362.1','901','Couple problem'),('363','909','(DO NOT USE) Other Family Problems'),('363.1','909','Family Violence'),('363.2','909','Elder abuse'),('363.3','909','Child abuse'),('363.4','899','Family of Origin Issues'),('363.5','901','Sibling Rivalry'),('364','902','Education Problem'),('365','903','Illegitimacy'),('366','904','(DO NOT USE) Social Maladjustment'),('366.1','904','Cultural adjustment'),('367','905','(DO NOT USE) Occupational Problems'),('367.1','905','Unemployment/Work stress'),('368','909','Phase-Of-Life Problem NEC'),('369','909','(DO NOT USE) Other Problems Of Social Adjustment'),('369.1','909','Other social problem'),('370','906','Legal Problem'),('371','909','Problems NEC In Codes 008- To V629'),('372','099','Non-Specific Urethritis'),('373','599','Hematuria NOS'),('374','625','Non-Psych Vaginismus & Dyspareunia'),('375','790','Hematological Abnormality NEC'),('376','629','Non-Specific Abnormal Pap Smear'),('377','977','Allergy To Medications'),('378','998','Other Adverse Effects NEC'),('607','180','(DO NOT USE) Other Male Genital Organ Diseases'),('999','','Other');

--
-- Dumping data for table `immunizations`
--


--
-- Dumping data for table `incomingLabRules`
--


--
-- Dumping data for table `indicatorTemplate`
--


--
-- Dumping data for table `indivoDocs`
--


--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`issue_id`, `code`, `description`, `role`, `update_date`, `priority`, `type`, `sortOrderId`) VALUES (1,'PastOcularHistory','Past Ocular History','nurse','2021-02-02 13:16:35',NULL,'system',0),(2,'DiagnosticNotes','Diagnostic Notes','nurse','2021-02-02 13:16:35',NULL,'system',0),(3,'OcularMedication','Ocular Medication','nurse','2021-02-02 13:16:35',NULL,'system',0),(4,'PatientLog','Patient Log','nurse','2021-02-02 13:16:35',NULL,'system',0),(5,'CurrentHistory','Current History','nurse','2021-02-02 13:16:35',NULL,'system',0),(6,'eyeformFollowUp','Follow-Up Item for Eyeform','nurse','2021-02-02 13:16:35',NULL,'system',0),(7,'eyeformCurrentIssue','Current Presenting Issue Item for Eyeform','nurse','2021-02-02 13:16:35',NULL,'system',0),(8,'eyeformPlan','Plan Item for Eyeform','nurse','2021-02-02 13:16:35',NULL,'system',0),(9,'eyeformImpression','Impression History Item for Eyeform','nurse','2021-02-02 13:16:35',NULL,'system',0),(10,'eyeformProblem','Problem List Item for Eyeform','nurse','2021-02-02 13:16:35',NULL,'system',0),(11,'TicklerNote','Tickler Note','nurse','2021-02-02 13:16:58',NULL,'system',0);

--
-- Dumping data for table `labPatientPhysicianInfo`
--


--
-- Dumping data for table `labRequestReportLink`
--


--
-- Dumping data for table `labTestResults`
--


--
-- Dumping data for table `log`
--


--
-- Dumping data for table `log_letters`
--


--
-- Dumping data for table `lst_orgcd`
--

INSERT INTO `lst_orgcd` (`code`, `description`, `activeyn`, `orderbyindex`, `codetree`) VALUES ('O0000020','Salvation Army','1',30,'R0000001O0000020'),('R0000001','Shelter Management Information System','1',10,'R000001');

--
-- Dumping data for table `mdsMSH`
--


--
-- Dumping data for table `mdsNTE`
--


--
-- Dumping data for table `mdsOBR`
--


--
-- Dumping data for table `mdsOBX`
--


--
-- Dumping data for table `mdsPID`
--


--
-- Dumping data for table `mdsPV1`
--


--
-- Dumping data for table `mdsZCL`
--


--
-- Dumping data for table `mdsZCT`
--


--
-- Dumping data for table `mdsZFR`
--


--
-- Dumping data for table `mdsZLB`
--


--
-- Dumping data for table `mdsZMC`
--


--
-- Dumping data for table `mdsZMN`
--


--
-- Dumping data for table `mdsZRG`
--


--
-- Dumping data for table `measurementCSSLocation`
--


--
-- Dumping data for table `measurementGroup`
--


--
-- Dumping data for table `measurementGroupStyle`
--


--
-- Dumping data for table `measurementMap`
--


--
-- Dumping data for table `measurementType`
--

INSERT INTO `measurementType` (`id`, `type`, `typeDisplayName`, `typeDescription`, `measuringInstruction`, `validation`, `createDate`) VALUES (1,'02','Oxygen Saturation','Oxygen Saturation','percent','4','2013-02-01 00:00:00'),(2,'24UA','24 hour urine albumin','24 hour urine albumin','mg/24h (nnn.n) Range:0-500 Interval:12mo.','14','2013-02-01 00:00:00'),(3,'24UR','24-hr Urine cr clearance & albuminuria','Renal 24-hr Urine cr clearance & albuminuria','q 6-12 months, unit mg','3','2013-02-01 00:00:00'),(4,'5DAA','5 Day Adherence if on ART','5 Day Adherence if on ART','number','4','2013-02-01 00:00:00'),(5,'A1C','A1C','A1C','Range:0.040-0.200','3','2013-02-01 00:00:00'),(6,'AACP','Asthma Action Plan ','Asthma Action Plan ','Provided/Revised/Reviewed','19','2018-11-08 00:00:00'),(7,'ABO','Blood Group','ABO RhD blood type group','Blood Type','11','2014-05-09 00:00:00'),(8,'ACOS','Asthma Coping Strategies','Asthma Coping Strategies','Yes/No','7','2013-02-01 00:00:00'),(9,'ACR','Alb creat ratio','ACR','in mg/mmol','5','2013-02-01 00:00:00'),(10,'ACS','Acute Conronary Syndrome','Acute Conronary Syndrome','Yes/No','7','2013-02-01 00:00:00'),(11,'AEDR','Asthma Education Referral','Asthma Education Referral','Yes/No','7','2013-02-01 00:00:00'),(12,'AELV','Exacerbations since last visit requiring clincal evaluation','Exacerbations since last visit requiring clincal evaluation','Yes/No','7','2013-02-01 00:00:00'),(13,'AENC','Asthma Environmental Control','Asthma Environmental Control','Yes/No','7','2013-02-01 00:00:00'),(14,'AFP','AFP','Alpha Fetoprotein','ug/L Range under 7','5','2014-05-09 00:00:00'),(15,'AHGM','Anit-hypoglycemic Medication','Anit-hypoglycemic Medication','Yes/No','7','2013-02-01 00:00:00'),(16,'AIDU','Active Intravenous Drug Use','Active Intravenous Drug Use','Yes/No','7','2013-02-01 00:00:00'),(17,'ALB','Albumin','Serum Albumin','g/L Range 35-50','5','2014-05-09 00:00:00'),(18,'ALC','Alcohol','Alcohol','Yes/No/X','12','2013-02-01 00:00:00'),(19,'ALP','ALP','Alkaline Phosphatase','U/L Range 50-300','14','2014-05-09 00:00:00'),(20,'ALPA','Asthma Limits Physical Activity','Asthma Limits Physical Activity','Yes/No','7','2013-02-01 00:00:00'),(21,'ALT','ALT','ALT','in U/L','5','2013-02-01 00:00:00'),(22,'ANA','ANA','Antinuclear Antibodies','result','17','2014-05-09 00:00:00'),(23,'Ang','Angina','Angina','Yes/No','7','2013-02-01 00:00:00'),(24,'ANR','Asthma Needs Reliever   ','Asthma Needs Reliever   ','frequency per week','14','2013-02-01 00:00:00'),(25,'ANSY','Asthma Night Time Symtoms','Asthma Night Time Symtoms','frequency per week','14','2013-02-01 00:00:00'),(26,'AORA','ACE-I OR ARB','ACE-I OR ARB','Yes/No','7','2013-02-01 00:00:00'),(27,'APOB','APO B','Apolipoprotein B','g/L Range 0.5-1.2','14','2014-05-09 00:00:00'),(28,'ARAD','Review Asthma Definition','Review Asthma Definition','Review Asthma Definition','7','2013-02-01 00:00:00'),(29,'ARDT','Asthma  Review Device Technique optimal','Asthma  Review Device Technique optimal','Yes/No','7','2013-02-01 00:00:00'),(30,'ARMA','Asthma Review Med Adherence','Asthma Review Med Adherence','Asthma Review Med Adherence','7','2013-02-01 00:00:00'),(31,'ASAU','ASA Use','ASA Use','Yes/No','7','2013-02-01 00:00:00'),(32,'ASPR','Asthma Specialist Referral','Asthma Specialist Referral','Yes/No','7','2013-02-01 00:00:00'),(33,'AST','AST','AST','in U/L','4','2013-02-01 00:00:00'),(34,'ASTA','Asthma Trigger Avoidance','Asthma Trigger Avoidance','Yes/No','7','2013-02-01 00:00:00'),(35,'ASWA','Asthma Absence School Work','Asthma Absence School Work','Yes/No','7','2013-02-01 00:00:00'),(36,'ASWAN','Asthma # of School Work Absence','Asthma # of School Work Absence','Numeric Value greater than or equal to 0','14','2018-10-01 00:00:00'),(37,'ASYM','Asthma Symptoms','Asthma Symptoms','frequency per week','14','2013-02-01 00:00:00'),(38,'BCTR','Birth Control','Birth Control','Yes/No','7','2013-02-01 00:00:00'),(39,'BG','Blood Glucose','Blood Glucose','in mmol/L (nn.n) Range:1.5-30.0','7','2013-02-01 00:00:00'),(40,'BILI','Bilirubin','Total Bilirubin','umol/L Range under 20','14','2014-05-09 00:00:00'),(41,'BMED','Blood Pressure Medication Changes','BP Med Changes','Changed','7','2013-02-01 00:00:00'),(42,'BMI','Body Mass Index','BMI','BMI','4','2013-02-01 00:00:00'),(43,'BP','BP','Blood Pressure','BP Tru','6','2013-02-01 00:00:00'),(44,'BP','BP','Blood Pressure','supine','6','2013-02-01 00:00:00'),(45,'BP','BP','Blood Pressure','standing position','6','2013-02-01 00:00:00'),(46,'BP','BP','Blood Pressure','sitting position','6','2013-02-01 00:00:00'),(47,'BPII','BPI Pain Interference','BPI Pain Interference','null','2','2013-07-25 13:00:00'),(48,'BPIS','BPI Pain Severity','BPI Pain Severity','null','2','2013-07-25 00:00:00'),(49,'BTFT','Brush teeth with fluoride toothpaste','NULL','Yes/No','7','2013-10-25 13:00:00'),(50,'BUN','BUN','Blood Urea Nitrogen','mmol/L Range 2-9','14','2014-05-09 00:00:00'),(51,'C125','CA 125','CA 125','kU/L Range under 36','14','2014-05-09 00:00:00'),(52,'C153','CA 15-3','CA 15-3','kU/L Range under 23','14','2014-05-09 00:00:00'),(53,'C199','CA 19-9','CA 19-9','kU/L Range under 27','14','2014-05-09 00:00:00'),(54,'C3','C3','Complement component 3','umol/L','14','2014-05-09 00:00:00'),(55,'CA','Calcium','Calcium','mmol/L','14','2014-05-09 00:00:00'),(56,'CASA','Consider ASA','Consider ASA','Yes/No','7','2013-02-01 00:00:00'),(57,'CAVD','Calcium and Vitamin D','NULL','Review','16','2014-01-23 13:00:00'),(58,'CD4','CD4','CD4','in x10e9/l','14','2013-02-01 00:00:00'),(59,'CD4P','CD4 Percent','CD4 Percent','in %','4','2013-02-01 00:00:00'),(60,'CDMP','Attended CDM Self Management Program','Attended CDM Self Management Program','Yes/No','7','2013-02-01 00:00:00'),(61,'CEA','CEA','CEA','umol/L','14','2014-05-09 00:00:00'),(62,'CEDE','Education Exercise','Education Exercise','Yes/No','7','2013-02-01 00:00:00'),(63,'CEDM','Education Patient Meds','Education Patient Meds','Yes/No','7','2013-02-01 00:00:00'),(64,'CEDS','Education Salt fluid ','Education Salt fluid ','Yes/No','7','2013-02-01 00:00:00'),(65,'CEDW','Education Daily Weight Monitoring','Education Daily Weight Monitoring','Yes/No','7','2013-02-01 00:00:00'),(66,'CERV','ER visits for HF','ER visits for HF','integer','2','2013-02-01 00:00:00'),(67,'CGSD','Collaborative Goal Setting','Collaborative Goal Setting','Yes/No','7','2013-02-01 00:00:00'),(68,'CHLM','CHLM','Chlamydia','test result','17','2014-05-09 00:00:00'),(69,'CIMF','Child Immunization recall','Child Immunization Follow up','Patient Contacted by Letter or Phone','11','2013-02-01 00:00:00'),(70,'CK','CK','Creatinine Kinase','U/L','14','2014-05-09 00:00:00'),(71,'Clpl','Chloride','Chloride','mmol/L Range 98-106','5','2014-05-09 00:00:00'),(72,'CMBS','Coombs','Coombs','test result','17','2014-05-09 00:00:00'),(73,'CMVI','CMV IgG','CMV IgG','Positive','7','2013-02-01 00:00:00'),(74,'CODC','COD Classification','COD Classification','','11','2013-02-01 00:00:00'),(75,'ACOSY','Cough','Cough','frequency/week','14','2018-11-15 00:00:00'),(76,'COPDC','COPD Classification','COPD Classification','COPD Classification','25','2018-11-15 00:00:00'),(77,'COGA','Cognitive Assessment','NULL','Yes/No','7','2013-10-25 13:00:00'),(78,'COPE','Provide COP Education Materials ','Provide COP Education Materials ','Yes/No','7','2013-02-01 00:00:00'),(79,'COPM','Review COP Med use and Side effects','Review COP Med use and Side effects','Yes/No','7','2013-02-01 00:00:00'),(80,'COPS','COP Specialist Referral','COP Specialist Referral','Yes/No','7','2013-02-01 00:00:00'),(81,'COUM','Warfarin Weekly Dose','WarfarinDose','Total mg Warfarin per week','5','2013-02-01 00:00:00'),(82,'CRCL','Creatinine Clearance','Creatinine Clearance','in ml/h','5','2013-02-01 00:00:00'),(83,'CRP','CRP','C reactive protein','mg/L','14','2014-05-09 00:00:00'),(84,'ACTSY','Chest tightness','Chest tightness','frequency/week','14','2018-11-15 00:00:00'),(85,'CVD','CVD','Cerebrovascular disease','Yes/No','7','2013-02-01 00:00:00'),(86,'CXR','CXR','CXR','Yes/No','7','2013-02-01 00:00:00'),(87,'DARB','ACE AARB','ACE AARB','Yes/No','7','2013-02-01 00:00:00'),(88,'DEPR','Depression','Depression','Yes/No','7','2013-02-01 00:00:00'),(89,'DESM','Dental Exam Every 6 Months','Dental Exam Every 6 Months','Yes/No','7','2013-02-01 00:00:00'),(90,'DiaC','Diabetes Counseling Given','Diabetes Counseling Given','Yes/No','7','2013-02-01 00:00:00'),(91,'DIER','Diet and Exercise','Diet and Exercise','Reviewed','7','2013-02-01 00:00:00'),(92,'DIET','Diet','Diet','Yes/No','7','2013-02-01 00:00:00'),(93,'DIFB','Impaired FB','Impaired FB','Yes/No','7','2013-02-01 00:00:00'),(94,'DIG','Digoxin','Digoxin Level','nmol/L Range 1-2.6','14','2014-05-09 00:00:00'),(95,'DIGT','Impaired GT','Impaired Glucose Tolerance','Yes/No','7','2013-02-01 00:00:00'),(96,'DIL','Dilantin','Dilantin (Phenytoin) level','umol/L Range 40-80','14','2014-05-09 00:00:00'),(97,'DILY','Dentist in the last year','NULL','Yes/No','7','2013-10-25 13:00:00'),(98,'DM','DM','Diabetes','Yes/No','7','2013-02-01 00:00:00'),(99,'DMED','Diabetes Medication Changes','DM Med Changes','Changed','7','2013-02-01 00:00:00'),(100,'DMME','Diabetes Education','Diabetes Education','Discussed','7','2013-02-01 00:00:00'),(101,'DMOE','Daily Morphine Equivalent','Daily Morphine Equivalent','null','11','2014-11-27 13:00:00'),(102,'DMSM','Diabetes Self Management Goals','Diabetes Self Management Goals','Discussed','7','2013-02-01 00:00:00'),(103,'DNFS','DN4 Questionnaire','DN4 Questionnaire','null','2','2013-05-07 00:00:00'),(104,'DOLE','Date of last Exacerbation','Date of last Exacerbation','yyyy-mm-dd','13','2013-02-01 00:00:00'),(105,'DpSc','Depression Screen','Feeling Sad, blue or depressed for 2 weeks or more','Yes/No','7','2013-02-01 00:00:00'),(106,'DRCO','Drug Coverage','Drug Coverage','Yes/No','7','2013-02-01 00:00:00'),(107,'DRPW','Drinks per Week','Drinks per Week','Number of Drinks per week','5','2013-02-01 00:00:00'),(108,'DT1','Type I','Diabetes Type 1','Yes/No','7','2013-02-01 00:00:00'),(109,'DT2','Type II','Diabetes Type 2','Yes/No','7','2013-02-01 00:00:00'),(110,'DTYP','Diabetes Type','Diabetes Type','1 or 2','10','2013-02-01 00:00:00'),(111,'ADYSY','Dyspnea','Dyspnea','frequency/week','14','2018-11-15 00:00:00'),(112,'ECG','ECG','ECG','Yes/No','7','2013-02-01 00:00:00'),(113,'ECHK','Do you have your eyes regularly checked?','NULL','Yes/No','7','2013-12-20 13:00:00'),(114,'EDC','EDC','Expected Date of Confinement','yyyy-mm-dd','13','2013-02-01 00:00:00'),(115,'EDDD','Education Diabetes','Education Diabetes','Yes/No','7','2013-02-01 00:00:00'),(116,'EDF','EDF','Erectile Dysfunction','Yes/No','7','2013-02-01 00:00:00'),(117,'EDGI','Autonomic Neuropathy','Autonomic Neuropathy','Present','7','2013-02-01 00:00:00'),(118,'EDND','Education Nutrition Diabetes','Education Nutrition Diabetes','Yes/No','7','2013-02-01 00:00:00'),(119,'EDNL','Education Nutrition Lipids','Education Nutrition Lipids','Yes/No','7','2013-02-01 00:00:00'),(120,'EGFR','EGFR','EGFR','in ml/min','4','2013-02-01 00:00:00'),(121,'ENA','ENA','Extractable Nuclear Antigens','result','11','2014-05-09 00:00:00'),(122,'EPR','Exacerbation plan in place or reviewed','Exacerbation plan in place or reviewed','Yes/No','7','2013-02-01 00:00:00'),(123,'EPR2','Exacerbation plan in place','Exacerbation plan in place','Provided/Revised/Reviewed','19','2018-10-18 00:00:00'),(124,'ESR','ESR','Erythrocyte sedimentation rate','mm/h Range under 20','14','2014-05-09 00:00:00'),(125,'EXE','Exercise','Exercise','Yes/No','7','2013-02-01 00:00:00'),(126,'ExeC','Exercise Counseling Given','Exercise Counseling Given','Yes/No','7','2013-02-01 00:00:00'),(127,'Exer','Exercise','Exercise','[min/week 0-1200]','14','2013-02-01 00:00:00'),(128,'EYEE','Dilated Eye Exam','Eye Exam','Exam Done','7','2013-02-01 00:00:00'),(129,'FAHS','Risk of Falling','Risk of Falling','Yes/No','7','2013-02-01 00:00:00'),(130,'FAMR','Family/Relationships','NULL','Review','16','2013-12-30 13:00:00'),(131,'FAS','Folic Acid supplementation','NULL','Yes/No','7','2013-10-25 13:00:00'),(132,'FBPC','2 hr PC BG','2 hr PC BG','in mmol/L','3','2013-02-01 00:00:00'),(133,'FBS','FBS','Glucose FBS','FBS','3','2013-02-01 00:00:00'),(134,'FEET','FEET','Feet Check skin','sensation (Yes/No)','7','2013-02-01 00:00:00'),(135,'FEET','FEET','Feet Check skin','vibration (Yes/No)','7','2013-02-01 00:00:00'),(136,'FEET','FEET','Feet Check skin','reflexes (Yes/No)','7','2013-02-01 00:00:00'),(137,'FEET','FEET','Feet Check skin','pulses (Yes/No)','7','2013-02-01 00:00:00'),(138,'FEET','FEET','Feet Check skin','infection (Yes/No)','7','2013-02-01 00:00:00'),(139,'Fer','Ferritin','Ferritin','ug/L Range 15-180','14','2014-05-09 00:00:00'),(140,'FEV1','Forced Expiratory Volume 1 Second','Forced Expiratory Volume 1 Second','Forced Expiratory Volume 1 Second','14','2013-02-01 00:00:00'),(141,'FGLC','Fasting Glucose meter , lab comparison','Fasting glucose meter, lab comparison','Within 20 percent','7','2013-02-01 00:00:00'),(142,'FICO','Financial Concerns','Financial Concerns','Yes/No','7','2013-02-01 00:00:00'),(143,'FIT','FIT','Fecal Immunochemical Test','result','17','2014-05-09 00:00:00'),(144,'FLOS','Floss','NULL','Yes/No','7','2013-10-25 13:00:00'),(145,'FLUF','Flu Recall','Flu Recall Documentation','Patient Contacted by Letter or Phone','11','2013-02-01 00:00:00'),(146,'FOBF','FOBT prevention recall','FOBT Immunization Follow up','Patient Contacted by Letter or Phone','11','2013-02-01 00:00:00'),(147,'FOBT','FOBT','Fecal Occult Blood','result','17','2014-05-09 00:00:00'),(148,'FRAM','Framingham 10 year CAD','Framingham 10 year CAD','percent','11','2013-02-01 00:00:00'),(149,'FT3','FT3','Free T3','pmol/L Range 4-8','14','2014-05-09 00:00:00'),(150,'FT4','FT4','Free T4','pmol/L Range 11-22','14','2014-05-09 00:00:00'),(151,'FTE','Foot Exam','Foot Exam','Normal','7','2013-02-01 00:00:00'),(152,'FTEx','Foot Exam: Significant Pathology','Significant Pathology','Yes/No','7','2013-02-01 00:00:00'),(153,'FTIn','Foot Exam: Infection','Infection','Yes/No','7','2013-02-01 00:00:00'),(154,'FTIs','Foot Exam: Ischemia','Ischemia','Yes/No','7','2013-02-01 00:00:00'),(155,'FTLS','Foot Exam  Test loss of Sensation','Foot Exam  Loss of Sensation','Normal','7','2013-02-01 00:00:00'),(156,'FTNe','Foot Exam: Neuropathy','Neuropathy','Yes/No','7','2013-02-01 00:00:00'),(157,'FTOt','Foot Exam: Other Vascular abnomality','Other Vascular abnomality','Yes/No','7','2013-02-01 00:00:00'),(158,'FTRe','Foot Exam: Referral made','Referral made','Yes/No','7','2013-02-01 00:00:00'),(159,'FTST','Free Testost','Free Testost','in nmol/L','14','2013-02-01 00:00:00'),(160,'FTUl','Foot Exam: Ulcer','Ulcer','Yes/No','7','2013-02-01 00:00:00'),(161,'FUPP','Assessment/Follow-up plans','NULL','Review','16','2013-12-30 13:00:00'),(162,'G','Gravida','Gravida','Gravida','3','2013-02-01 00:00:00'),(163,'G6PD','G6PD','G6PD','Positive','7','2013-02-01 00:00:00'),(164,'GBS','GBS','Group B Strep','test result','17','2014-05-09 00:00:00'),(165,'GC','Gonococcus','Gonococcus','test result','17','2014-05-09 00:00:00'),(166,'GGT','GGT','Gamma-glutamyl transferase','U/L Range 10-58','14','2014-05-09 00:00:00'),(167,'GCT','50g Glucose Challenge','1h 50g Glucose Challenge','mmol/L Range under 7.8','4','2014-05-09 00:00:00'),(168,'GT1','75g OGTT 1h','1h 75g Glucose Tolerance Test','mmol/L Range under 10.6','4','2014-05-09 00:00:00'),(169,'GT2','75g OGTT 2h','2h 75g Glucose Tolerance Test','mmol/L Range under 9','4','2014-05-09 00:00:00'),(170,'Hb','Hb','Hb','in g/L','5','2013-02-01 00:00:00'),(171,'HCON','Do you have any hearing concerns?','NULL','Yes/No','7','2013-12-20 13:00:00'),(172,'HBEB','AntiHBeAg','AntiHBeAg','result','17','2014-05-09 00:00:00'),(173,'HBEG','HBeAg','HBeAg','result','17','2014-05-09 00:00:00'),(174,'HBVD','HBV DNA','HBV DNA','result','17','2014-05-09 00:00:00'),(175,'HCO3','Bicarbonate','Bicarbonate','mmol/L Range 20-29','4','2014-05-09 00:00:00'),(176,'Hchl','Hypercholesterolemia','Hypercholesterolemia','Yes/No','7','2013-02-01 00:00:00'),(177,'HDL','HDL','High Density Lipid','in mmol/L (n.n) Range:0.4-4.0','2','2013-02-01 00:00:00'),(178,'HEAD','Head circumference','Head circumference','in cm (nnn) Range:30-70 Interval:2mo.','4','2013-02-01 00:00:00'),(179,'HFCG','HF Collaorative Goal Setting','HF Collaorative Goal Setting','Yes/No','7','2013-02-01 00:00:00'),(180,'HFCS','HF Self Management Challenge','HF Self Management Challenge','Yes/No','7','2013-02-01 00:00:00'),(181,'HFMD','HF Mod Risk Factor Diabetes','HF Mod Risk Factor Diabetes','Yes/No','7','2013-02-01 00:00:00'),(182,'HFMH','HF Mod Risk Factor Hyperlipidemia','HF Mod Risk Factor Hyperlipidemia','Yes/No','7','2013-02-01 00:00:00'),(183,'HFMO','HF Mod Risk Factor Overweight','HF Mod Risk Factor Overweight','Yes/No','7','2013-02-01 00:00:00'),(184,'HFMS','HF Mod Risk Factor Smoking','HF Mod Risk Factor Smoking','Yes/No','7','2013-02-01 00:00:00'),(185,'HFMT','HF Mod Risk Factor Hypertension','HF Mod Risk Factor Hypertension','Yes/No','7','2013-02-01 00:00:00'),(186,'HIP','Hip Circ.','Hip Circumference','at 2 cm above navel','14','2013-02-01 00:00:00'),(187,'HIVG','HIV genotype','HIV genotype','Yes/No','7','2013-02-01 00:00:00'),(188,'HLA','HLA B5701','HLA B5701','Yes/No','7','2013-02-01 00:00:00'),(189,'HpAI','Hep A IgG','Hep A IgG','Positive','7','2013-02-01 00:00:00'),(190,'HpBA','Hep BS Ab','Hep BS Ab','Positive','7','2013-02-01 00:00:00'),(191,'HPBC','Hep B CAb','Hep B CAb','Yes/No','7','2013-02-01 00:00:00'),(192,'HPBP','Hep B PCR','Hep B PCR','Yes/No','7','2013-02-01 00:00:00'),(193,'HpBS','Hep BS Ag','Hep BS Ag','Positive','7','2013-02-01 00:00:00'),(194,'HpCA','Hep C Ab','Hep C Ab','Positive','7','2013-02-01 00:00:00'),(195,'HPCG','Hep C Genotype','Hep C Genotype','integer Range 1-7','2','2013-02-01 00:00:00'),(196,'HPCP','Hep C PCR','Hep C PCR','Yes/No','7','2013-02-01 00:00:00'),(197,'HPNP','Hearing protection/Noise control programs','NULL','Yes/No','7','2013-10-25 13:00:00'),(198,'HPYL','H Pylori','H Pylori','result','17','2014-05-09 00:00:00'),(199,'HR','P','Heart Rate','in bpm (nnn) Range:40-180','5','2013-02-01 00:00:00'),(200,'HRMS','Review med use and side effects','HTN Review of Medication use and side effects','null','11','2013-02-01 00:00:00'),(201,'HSMC','Self Management Challenges','HTN Self Management Challenges','null','11','2013-02-01 00:00:00'),(202,'HSMG','Self Management Goal','HTN Self Management Goal','null','11','2013-02-01 00:00:00'),(203,'HT','HT','Height','in cm','5','2013-02-01 00:00:00'),(204,'HTN','HTN','Hypertension','Yes/No','7','2013-02-01 00:00:00'),(205,'HYPE','Hypoglycemic Episodes','Number of Hypoglycemic Episodes','since last visit','3','2013-02-01 00:00:00'),(206,'HYPM','Hypoglycemic Management','Hypoglycemic Management','Yes/No','7','2013-02-01 00:00:00'),(207,'IART','Currently On ART','Currently On ART','Yes/No','7','2013-02-01 00:00:00'),(208,'IBPL','Income below poverty line','NULL','Yes/No','7','2013-10-25 13:00:00'),(209,'iDia','Eye Exam: Diabetic Retinopathy','Diabetic Retinopathy','Yes/No','7','2013-02-01 00:00:00'),(210,'iEx','Eye Exam: Significant Pathology','Significant Pathology','Yes/No','7','2013-02-01 00:00:00'),(211,'iHyp','Eye Exam: Hypertensive Retinopathy','Hypertensive Retinopathy','Yes/No','7','2013-02-01 00:00:00'),(212,'INR','INR','INR','INR Blood Work','5','2013-02-01 00:00:00'),(213,'INSL','Insulin','Insulin','Yes/No','7','2013-02-01 00:00:00'),(214,'iOth','Eye Exam: Other Vascular Abnomality','Other Vascular Abnormality','Yes/No','7','2013-02-01 00:00:00'),(215,'iPTH','iPTH','intact Parathyroid Hormone','pmol/L Range 1-6','14','2014-05-09 00:00:00'),(216,'iRef','Eye Exam: Refferal Made','Refferal Made','Yes/No','7','2013-02-01 00:00:00'),(217,'KEEL','Keele Score','Keele Score','null','2','2013-05-07 00:00:00'),(218,'JVPE','JPV Elevation','JPV Elevation','Yes/No','7','2013-02-01 00:00:00'),(219,'Kpl','Potassium','Potassium','in mmol/L','2','2013-02-01 00:00:00'),(220,'LcCt','Locus of Control Screen','Feeling lack of control over daily life','Yes/No','7','2013-02-01 00:00:00'),(221,'LDL','LDL','Low Density Lipid','monitor every 1-3 year','2','2013-02-01 00:00:00'),(222,'LEFP','LEFS Pain','Lower Extremity Functional Scale - Pain','number','5','2013-02-01 00:00:00'),(223,'LETH','Lethargy','Lethargic','Yes/No','7','2013-02-01 00:00:00'),(224,'LHAD','Lung Related Hospital Admission','Lung Related Hospital Admission','Yes/No','7','2013-02-01 00:00:00'),(225,'LITH','Lithium','Lithium','mmol/L Range 0.6-0.8','14','2014-05-09 00:00:00'),(226,'LMED','Lipid Lowering Medication Changes','Lipid Med Changes','Changed','7','2013-02-01 00:00:00'),(227,'LMP','Last Menstral Period','LMP','date','13','2013-02-01 00:00:00'),(228,'LUCR','Lung Crackles','Lung Crackles','Yes/No','7','2013-02-01 00:00:00'),(229,'MACA','Macroalbuminuria','Renal Macrobalbumnuria','q 3-6 months','3','2013-02-01 00:00:00'),(230,'MACC','MAC culture','MAC culture','Yes/No','7','2013-02-01 00:00:00'),(231,'MAMF','MAM Recall','Mammogram Recall Documentation','Patient Contacted by Letter or Phone','11','2013-02-01 00:00:00'),(232,'MCCE','Motivation Counseling Compeleted Exercise','Motivation Counseling Compeleted Exercise','Yes/No','7','2013-02-01 00:00:00'),(233,'MCCN','Motivation Counseling Compeleted Nutrition','Motivation Counseling Compeleted Nutrition','Yes/No','7','2013-02-01 00:00:00'),(234,'MCCO','Motivation Counseling Compeleted Other','Motivation Counseling Compeleted Other','Yes/No','7','2013-02-01 00:00:00'),(235,'MCCS','Motivation Counseling Compeleted Smoking Cessation','Motivation Counseling Compeleted Smoking Cessation','Yes/No','7','2013-02-01 00:00:00'),(236,'MCV','MCV','Mean corpuscular volume','fL Range 82-98','14','2014-05-09 00:00:00'),(237,'MedA','Medication adherence access barriers','Difficulty affording meds or getting refills on time','Yes/No','7','2013-02-01 00:00:00'),(238,'MedG','Medication adherence general problem','Any missed days or doses of meds','Yes/No','7','2013-02-01 00:00:00'),(239,'MedN','Medication adherence negative beliefs','Concerns about side effects or medication is not working','Yes/No','7','2013-02-01 00:00:00'),(240,'MedR','Medication adherence recall barriers','Difficulty remembering to take meds','Yes/No','7','2013-02-01 00:00:00'),(241,'MG','Mg','Magnesium','mmol/L Range 0.7-1.2','14','2014-05-09 00:00:00'),(242,'MI','MI','MI','Yes/No','7','2013-02-01 00:00:00'),(243,'Napl','Sodium','Sodium','in mmol/L','5','2013-02-01 00:00:00'),(244,'NDIP','CMCC NDI Pain','CMCC Neck Disability Index - Pain','number','5','2013-02-01 00:00:00'),(245,'NDIS','CMCC NDI Score','CMCC Neck Disability Index - Score','number','5','2013-02-01 00:00:00'),(246,'NERF','Neuropathic Features?','Neuropathic Features?','null','15','2013-05-07 00:00:00'),(247,'NOSK','Number of Cigarettes per day','Smoking','Cigarettes per day','5','2013-02-01 00:00:00'),(248,'NOVS','Need for nocturnal ventilated support','Need for nocturnal ventilated support','Yes/No','7','2013-02-01 00:00:00'),(249,'NtrC','Diet/Nutrition Counseling Given','Diet/Nutrition Counseling Given','Yes/No','7','2013-02-01 00:00:00'),(250,'NYHA','NYHA Functional Capacity Classification','NYHA Functional Capacity Classification','NYHA Class I-IV','24','2018-11-08 00:00:00'),(251,'OPAE','Opioid Adverse Effects','Opioid Adverse Effects','null','17','2014-11-27 13:00:00'),(252,'OPAB','Opioid Aberrant Behaviour','Opioid Aberrant Behaviour','null','17','2014-11-27 13:00:00'),(253,'OPUS','Opioid Urine Drug Screen','Opioid Urine Drug Screen','null','17','2014-11-27 13:00:00'),(254,'ORSK','Opioid Risk','NULL','Score 0-26','3','2013-12-27 13:00:00'),(255,'OSWP','Oswestry BDI Pain','Oswestry Back Disability Index - Pain','number','5','2013-02-01 00:00:00'),(256,'OSWS','Oswestry BDI Score','Oswestry Back Disability Index - Score','number','5','2013-02-01 00:00:00'),(257,'OTCO','Other Concerns','Other Concerns','Yes/No','7','2013-02-01 00:00:00'),(258,'OthC','Other Counseling Given','Other Counseling Given','Yes/No','7','2013-02-01 00:00:00'),(259,'OUTR','Outside Spirometry Referral','Outside Spirometry Referral','Yes/No','7','2013-02-01 00:00:00'),(260,'P','Para','Para','Para','3','2013-02-01 00:00:00'),(261,'PANE','Painful Neuropathy','Painful Neuropathy','Present','7','2013-02-01 00:00:00'),(262,'PAPF','Pap Recall','Pap Recall Documentation','Patient Contacted by Letter or Phone','11','2013-02-01 00:00:00'),(263,'PB19','Parvovirus','Parvovirus B19','result','11','2014-05-09 00:00:00'),(264,'PEDE','Pitting Edema','Pitting Edema','Yes/No','7','2013-02-01 00:00:00'),(265,'PEFR','PEFR value','PEFR value','null','14','2013-02-01 00:00:00'),(266,'PHIN','Pharmacological Intolerance','Pharmacological Intolerance','Yes/No','7','2013-02-01 00:00:00'),(267,'PHOS','Phosphate','Phosphate','mmol/L Range 0.8-1.4','14','2014-05-09 00:00:00'),(268,'PHQS','PHQ4 Depression Anxiety Score','PHQ4 Depression Anxiety Score','null','3','2013-05-07 00:00:00'),(269,'PIDU','Previous Intravenous Drug Use','Previous Intravenous Drug Use','Yes/No','7','2013-02-01 00:00:00'),(270,'PLT','Platelets','Platelets','x10 9/L Range 150-400','14','2014-05-09 00:00:00'),(271,'PPD','PPD','PPD','Yes/No','7','2013-02-01 00:00:00'),(272,'PROT','Protein','Total Protein Serum','g/L Range 60-80','14','2014-05-09 00:00:00'),(273,'PRRF','Pulmonary Rehabilitation Referral','Pulmonary Rehabilitation Referral','Yes/No','7','2013-02-01 00:00:00'),(274,'PSA','PSA','Prostatic specific antigen','ug/L Range under 5','14','2014-05-09 00:00:00'),(275,'PSPA','Patient Sets physical Activity Goal','Patient Sets physical Activity Goal','Yes/No','7','2013-02-01 00:00:00'),(276,'PSQS','PSQ3 Sleep Score','PSQ3 Sleep Score','null','5','2013-05-07 00:00:00'),(277,'PSSC','Psychosocial Screening','Psychosocial Screening','Yes/No','7','2013-02-01 00:00:00'),(278,'PsyC','Psychosocial Counseling Given','Psychosocial Counseling Given','Yes/No','7','2013-02-01 00:00:00'),(279,'PTSD','PC PTSD Trauma Score','PC PTSD Trauma Score','null','2','2013-05-07 00:00:00'),(280,'PVD','PVD','Peripheral vascular disease','Yes/No','7','2013-02-01 00:00:00'),(281,'PXAM','Physical Exam','NULL','Review','16','2013-12-30 13:00:00'),(282,'QDSH','QuickDASH Score','Disabilities of the Arm, Shoulder and Hand - Score','number','5','2013-02-01 00:00:00'),(283,'RABG','Recommend ABG','Recommend ABG','Yes/No','7','2013-02-01 00:00:00'),(284,'RABG2','Recommend ABG','Recommend ABG','Yes/Not Applicable','7','2018-10-18 00:00:00'),(285,'REBG','Review Blood Glucose Records','Review Glucose Records','Reviewed','7','2013-02-01 00:00:00'),(286,'RESP','RR','Respiratory Rate','Breaths per minute','4','2013-02-01 00:00:00'),(287,'RETI','Retinopathy','null','Discussed','7','2013-02-01 00:00:00'),(288,'RF','RF','Rheumatoid Factor','result','17','2014-05-09 00:00:00'),(289,'Rh','Rh','RhD blood type group','result','11','2014-05-09 00:00:00'),(290,'RPHR','Review PHR','Review PHR','Yes/No','7','2013-02-01 00:00:00'),(291,'RPPT','Review Pathophysiology, Prognosis, Treatment with Patient','Review Pathophysiology, Prognosis, Treatment with Patient','Yes/No','7','2013-02-01 00:00:00'),(292,'RUB','Rubella','Rubella titre','titre','11','2014-05-09 00:00:00'),(293,'RVTN','Revascularization','Revascularization','Yes/No','7','2013-02-01 00:00:00'),(294,'SBLT','Seat belts','NULL','Yes/No','7','2013-10-25 13:00:00'),(295,'SCR','Serum Creatinine','Creatinine','in umol/L','14','2013-02-01 00:00:00'),(296,'SDET','Smoke detector that works','NULL','Yes/No','7','2013-10-25 13:00:00'),(297,'SDUS','Street Drug Use','NULL','Review','16','2013-12-30 13:00:00'),(298,'SEXF','Sexual Function','Sexual Function','Yes/No','7','2013-02-01 00:00:00'),(299,'SEXH','Sexual History','NULL','Review','16','2013-12-30 13:00:00'),(300,'SHAB','Sleep Habits','NULL','Review','16','2013-12-30 13:00:00'),(301,'SKST','Smoking Status','Smoking Status','Yes/No','7','2013-02-01 00:00:00'),(302,'SMBG','Self monitoring BG','Self Monitoring Blood Glucose','Yes/No','7','2013-02-01 00:00:00'),(303,'SmCC','Smoking Cessation Counseling Given','Smoking Cessation Counseling Given','Yes/No','7','2013-02-01 00:00:00'),(304,'SMCD','Self Management Challenges','Self Management Challenges','Yes/No','7','2013-02-01 00:00:00'),(305,'SMCP','Smoking Cessation Program','Smoking Cessation Program','null','11','2013-02-01 00:00:00'),(306,'SMCS','Smoking Cessation','Smoking Cessation','Yes/No','7','2013-02-01 00:00:00'),(307,'SMK','Smoking','Smoking','Yes/No/X','12','2013-02-01 00:00:00'),(308,'SmkA','Smoking Advice','Advised to Quid','Yes/No','7','2013-02-01 00:00:00'),(309,'SmkC','Cigarette Smoking Cessation','Cigarette Smoking Cessation','Date last quit (yyyy-MM-dd)','13','2013-02-01 00:00:00'),(310,'SmkD','Daily Packs','Packs of Cigarets Daily','fraction or integer','11','2013-02-01 00:00:00'),(311,'SmkF','Smoking Followup','Followup Requested','Yes/No','7','2013-02-01 00:00:00'),(312,'SmkPY','Cigarette Smoking History','Cigarette Smoking History','[Cum. pack yrs 0-110]','5','2013-02-01 00:00:00'),(313,'SmkS','Cigarette Smoking Status','Cigarette Smoking Status','[cig/day 0-80]','4','2013-02-01 00:00:00'),(314,'SODI','Salt Intake','Salt Intake','On Low Sodium Diet','7','2013-02-01 00:00:00'),(315,'SOHF','Symptoms of Heart Failure','Symptoms of Heart Failure','Yes/No','7','2013-02-01 00:00:00'),(316,'HFSFT','Heart Failure Symptom: Fatigue','Heart Failure Symptom: Fatigue','Frequency/week','14','2018-10-18 00:00:00'),(317,'HFSDZ','Heart Failure Symptom: Dizziness','Heart Failure Symptom: Dizziness','Frequency/week','14','2018-10-18 00:00:00'),(318,'HFSSC','Heart Failure Symptom: Syncope','Heart Failure Symptom: Syncope','Frequency/week','14','2018-10-18 00:00:00'),(319,'HFSDE','Heart Failure Symptom: Dyspnea on Exertion','Heart Failure Symptom: Dyspnea on Exertion','Frequency/week','14','2018-10-18 00:00:00'),(320,'HFSDR','Heart Failure Symptom: Dyspnea at Rest','Heart Failure Symptom: Dyspnea at Rest','Frequency/week','14','2018-10-18 00:00:00'),(321,'HFSON','Heart Failure Symptom: Orthopnea','Heart Failure Symptom: Orthopnea','Frequency/week','14','2018-10-18 00:00:00'),(322,'HFSDP','Heart Failure Symptom: Paroxysmal Nocturnal Dyspnea','Heart Failure Symptom: Paroxysmal Nocturnal Dyspnea','Frequency/week','14','2018-10-18 00:00:00'),(323,'SPIR','Spirometry','Spirometry','','14','2013-02-01 00:00:00'),(324,'SPIRT','Spirometry Test','Spirometry Test','Yes or none','22','2018-10-18 00:00:00'),(325,'SSEX','Practicing Safe Sex','Practicing Safe Sex','Yes/No','7','2013-02-01 00:00:00'),(326,'SSXC','Safe Sex Counselling','NULL','Review','16','2014-01-23 13:00:00'),(327,'STIS','STI Screening','Sexual Transmitted Infections','Review','16','2014-01-23 13:00:00'),(328,'STRE','Stress Testing','Stress Testing','Yes/No','7','2013-02-01 00:00:00'),(329,'StSc','Stress Screen','Several periods of irritability, feeling filled with anxiety, or difficulty sleeping b/c of stress','Yes/No','7','2013-02-01 00:00:00'),(330,'SUAB','Substance Use','Substance Use','Yes/No','7','2013-02-01 00:00:00'),(331,'SUNP','Sun protection','NULL','Yes/No','7','2013-10-25 13:00:00'),(332,'SUO2','Need for supplemental oxygen','Need for supplemental oxygen','Yes/No','7','2013-02-01 00:00:00'),(333,'TCHD','TC/HDL','LIPIDS TD/HDL','monitor every 1-3 year','3','2013-02-01 00:00:00'),(334,'TCHL','Total Cholestorol','Total Cholestorol','in mmol/L (nn.n) Range:2.0-12.0','2','2013-02-01 00:00:00'),(335,'TEMP','Temp','Temperature','degrees celcius','3','2013-02-01 00:00:00'),(336,'TG','TG','LIPIDS TG','monitor every 1-3 year','3','2013-02-01 00:00:00'),(337,'TOXP','Toxoplasma IgG','Toxoplasma IgG','Positive','7','2013-02-01 00:00:00'),(338,'TRIG','Triglycerides','Triglycerides','in mmol/L (nn.n) Range:0.0-12.0','3','2013-02-01 00:00:00'),(339,'TSAT','Transferrin Saturation','Transferrin Saturation','percent Range 20-50','4','2014-05-09 00:00:00'),(340,'TSH','TSH','Thyroid Stimulating Hormone','null','4','2013-02-01 00:00:00'),(341,'TUG','Timed Up and Go','Timed Up and Go','Number of Seconds','14','2013-02-01 00:00:00'),(342,'UAIP','Update AIDS defining illness in PMH','Update AIDS defining illness in PMH','Changed','7','2013-02-01 00:00:00'),(343,'UDUS','Update Drug Use','Update Drug Use','Changed','7','2013-02-01 00:00:00'),(344,'UHTP','Update HIV Test History in PMH','Update HIV Test History in PMH','Changed','7','2013-02-01 00:00:00'),(345,'URBH','Update Risk Behaviours','Update Risk Behaviours','Changed','7','2013-02-01 00:00:00'),(346,'URIC','Uric Acid','Uric Acid','umol/L Range 230-530','14','2014-05-09 00:00:00'),(347,'USSH','Update Sexual Identity in Social History','Update Sexual Identity in Social History','Changed','7','2013-02-01 00:00:00'),(348,'VB12','Vit B12','Vitamin B12','Range >0 pmol/l','14','2013-02-01 00:00:00'),(349,'VDRL','VDRL','VDRL','Positive','7','2013-02-01 00:00:00'),(350,'VLOA','Viral Load','Viral Load','in x10e9/L','14','2013-02-01 00:00:00'),(351,'VZV','Zoster','Varicella Zoster','result','17','2014-05-09 00:00:00'),(352,'WAIS','Waist','Waist','Waist Circum in cm','5','2013-02-01 00:00:00'),(353,'WBC','WBC','White Cell Count','x10 9/L Range 4-11','14','2014-05-09 00:00:00'),(354,'AWHSY','Wheeze','Wheeze','frequency/week','14','2018-10-31 00:00:00'),(355,'WHR','Waist:Hip','Waist Hip Ratio','Range:0.5-2 Interval:3mo.','2','2013-02-01 00:00:00'),(356,'WKED','Work/Education','NULL','Review','16','2013-12-30 13:00:00'),(357,'WT','WT','Weight','in kg','5','2013-02-01 00:00:00'),(358,'UMS','Urinary Microalbumin Screen','Urinary Microalbumin Screen','Records the value of the Urinary Microalbumin test: mg/L','14','2018-09-14 00:00:00'),(359,'FEV1BF','FEV1 (before puff)','FEV1 (before puff)','Forced Expiratory Volume: the volume of air that has been exhaled by the patient at the end of the first second of forced expiration','14','2018-09-14 00:00:00'),(360,'FVCBF','FVC (before puff)','FVC (before puff)','Forced Vital Capacity: the volume of air that has been forcibly and maximally exhaled out by the patient until no more can be expired','14','2018-09-14 00:00:00'),(361,'FEV1PCBF','FEV1% (before puff)','FEV1% (before puff)','The ratio of FEV1 to FVC calculated for the patient','14','2018-09-14 00:00:00'),(362,'FEV1PRE','FEV1 predicted','FEV1 predicted','The FEV1 calculated in the population with similar characteristics (e.g. height, age, sex, race, weight, etc.)','14','2018-09-14 00:00:00'),(363,'FVCPRE','FVC predicted','FVC predicted','Forced Vital Capacity predicted: calculated in the population with similar characteristics (height, age, sex, and sometimes race and weight)','14','2018-09-14 00:00:00'),(364,'FEV1PCPRE','FEV1% predicted','FEV1% predicted','The ratio of FEV1 predicted to FVC predicted, calculated in the population with similar characteristics (height, age, sex, and sometimes race and weight)','14','2018-09-14 00:00:00'),(365,'FEV1PCOFPREBF','FEV1% of predicted (before puff)','FEV1% of predicted (before puff)','FEV1% (before puff) of the patient divided by the average FEV1% predicted in the population with similar characteristics (e.g. height, age, sex, race, weight, etc.)','14','2018-09-14 00:00:00'),(366,'FVCRTBF','FVC ratio (before puff)','FVC ratio (before puff)','FVC actual (before puff) / FVC predicted','14','2018-09-14 00:00:00'),(367,'FEV1FVCRTBF','FEV1 / FVC ratio (before puff)','FEV1 / FVC ratio (before puff)','FEV1 / FVC (before puff) actual divided by FEV1 / FVC predicted','14','2018-09-14 00:00:00'),(368,'PEFRBF','PEF personal (before puff)','PEF personal (before puff)','Peak Expiratory Flow: the maximal flow (or speed) achieved during the maximally forced expiration initiated at full inspiration','14','2018-09-14 00:00:00'),(369,'FEV1AFT','FEV1 (after puff)','FEV1 (after puff)','Forced Expiratory Volume: the volume of air that has been exhaled by the patient at the end of the first second of forced expiration','14','2018-09-14 00:00:00'),(370,'FVCAFT','FVC (after puff)','FVC (after puff)','Forced Vital Capacity: the volume of air that has been forcibly and maximally exhaled out by the patient until no more can be expired','14','2018-09-14 00:00:00'),(371,'FEV1PCAFT','FEV1% (after puff)','FEV1% (after puff)','The ratio of FEV1 to FVC calculated for the patient','14','2018-09-14 00:00:00'),(372,'FEV1PCOFPREAFT','FEV1% of predicted (after puff)','FEV1% of predicted (after puff)','FEV1% (after puff) of the patient divided by the average FEV1% predicted in the population with similar characteristics (e.g. height, age, sex, race, weight, etc.)','14','2018-09-14 00:00:00'),(373,'FVCRTAFT','FVC ratio (after puff)','FVC ratio (after puff)','FVC actual (after puff) / FVC predicted','14','2018-09-14 00:00:00'),(374,'FEV1FVCRTAFT','FEV1 / FVC ratio (after puff)','FEV1 / FVC ratio (after puff)','FEV1 / FVC (after puff) actual divided by FEV1 / FVC predicted','14','2018-09-14 00:00:00'),(375,'PEFRAFT','PEF personal (after puff)','PEF personal (after puff)','Peak Expiratory Flow: the maximal flow (or speed) achieved during the maximally forced expiration initiated at full inspiration','14','2018-09-14 00:00:00'),(376,'ANELV','Asthma: # Of Exacerbations Requiring Clinical Evaluation since last assessment','Asthma: # Of Exacerbations Requiring Clinical Evaluation since last assessment','The number of exacerbations since the last assessment requiring clinical evaluations reported by the patient','14','2018-09-14 00:00:00'),(377,'CNOLE','COPD: # of Exacerbations since last assessment','COPD: # of Exacerbations since last assessment','The number of exacerbations due to COPD since last visit, as reported by the patient','14','2018-09-14 00:00:00'),(378,'WHE','Wheezing','Wheezing','Records whether the patient is wheezing or not','18','2018-09-14 00:00:00'),(379,'HFMR','HF Medication Review','Heart Failure Medication Review','Records whether medication adherence for Heart Failure \npurpose has been discussed with the patient','18','2018-09-14 00:00:00'),(380,'MDRC','Med Rec','Med Rec','Completed','18','2018-09-14 00:00:00');

--
-- Dumping data for table `measurementTypeDeleted`
--


--
-- Dumping data for table `measurements`
--


--
-- Dumping data for table `measurementsDeleted`
--


--
-- Dumping data for table `measurementsExt`
--


--
-- Dumping data for table `messageFolder`
--


--
-- Dumping data for table `messagelisttbl`
--


--
-- Dumping data for table `messagetbl`
--


--
-- Dumping data for table `msgDemoMap`
--


--
-- Dumping data for table `msgIntegratorDemoMap`
--


--
-- Dumping data for table `mygroup`
--

INSERT INTO `mygroup` (`mygroup_no`, `provider_no`, `last_name`, `first_name`, `vieworder`, `default_billing_form`) VALUES ('IT Support','88888','Support','IT',NULL,NULL);

--
-- Dumping data for table `onCallClinicDates`
--


--
-- Dumping data for table `oscarKeys`
--


--
-- Dumping data for table `oscar_annotations`
--


--
-- Dumping data for table `oscar_msg_type`
--

INSERT INTO `oscar_msg_type` (`type`, `description`, `code`) VALUES (1,'OSCAR Resident Review','OSCAR_REVIEW_TYPE'),(2,'General','GENERAL_TYPE'),(3,'Integrator Message','INTEGRATOR_TYPE');

--
-- Dumping data for table `oscarcommlocations`
--

INSERT INTO `oscarcommlocations` (`locationId`, `locationDesc`, `locationAuth`, `current1`, `addressBook`, `remoteServerURL`) VALUES (145,'Oscar Users',NULL,1,'<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<addressBook><group><group desc=\"doc\" id=\"17\"><address desc=\"Chan, David\" id=\"174\"/><address desc=\"oscardoc, doctor\" id=\"999998\"/></group><group desc=\"receptionist\" id=\"18\"><address desc=\"oscarrep, receptionist\" id=\"999999\"/><address desc=\"Support, IT\" id=\"88888\"/></group><group desc=\"admin\" id=\"19\"><address desc=\"oscaradmin, admin\" id=\"999997\"/></group><address desc=\"Chan, David\" id=\"174\"/><address desc=\"oscaradmin, admin\" id=\"999997\"/><address desc=\"oscardoc, doctor\" id=\"999998\"/><address desc=\"oscarrep, receptionist\" id=\"999999\"/><address desc=\"Support, IT\" id=\"88888\"/></group></addressBook>',NULL);

--
-- Dumping data for table `other_id`
--


--
-- Dumping data for table `partial_date`
--


--
-- Dumping data for table `patientLabRouting`
--


--
-- Dumping data for table `pharmacyInfo`
--


--
-- Dumping data for table `prescribe`
--


--
-- Dumping data for table `prescription`
--


--
-- Dumping data for table `preventions`
--


--
-- Dumping data for table `preventionsExt`
--


--
-- Dumping data for table `professionalSpecialists`
--


--
-- Dumping data for table `program`
--


--
-- Dumping data for table `property`
--


--
-- Dumping data for table `provider`
--

INSERT INTO `provider` (`provider_no`, `last_name`, `first_name`, `provider_type`, `supervisor`, `specialty`, `team`, `sex`, `dob`, `address`, `phone`, `work_phone`, `ohip_no`, `rma_no`, `billing_no`, `hso_no`, `status`, `comments`, `provider_activity`, `practitionerNo`, `init`, `job_title`, `email`, `title`, `lastUpdateUser`, `lastUpdateDate`, `signed_confidentiality`, `practitionerNoType`) VALUES ('999998','oscardoc','doctor','doctor',NULL,'','','','0001-01-01','','','','','','','','1','','','','','','','','','2021-02-02 13:15:47','0001-01-01 00:00:00','');

--
-- Dumping data for table `providerArchive`
--


--
-- Dumping data for table `providerExt`
--


--
-- Dumping data for table `providerLabRouting`
--


--
-- Dumping data for table `providerLabRoutingFavorites`
--


--
-- Dumping data for table `provider_facility`
--


--
-- Dumping data for table `providerbillcenter`
--


--
-- Dumping data for table `providersite`
--


--
-- Dumping data for table `providerstudy`
--


--
-- Dumping data for table `publicKeys`
--


--
-- Dumping data for table `queue`
--

INSERT INTO `queue` (`id`, `name`) VALUES (1,'default');

--
-- Dumping data for table `queue_document_link`
--


--
-- Dumping data for table `quickList`
--

INSERT INTO `quickList` (`id`, `quickListName`, `createdByProvider`, `dxResearchCode`, `codingSystem`) VALUES (1,'default','999997','000','ichppc'),(2,'default','999997','204','ichppc'),(3,'default','999997','288','ichppc'),(4,'default','999997','053','ichppc'),(5,'default','999997','235','ichppc'),(6,'List1','999998','235','ichppc'),(7,'List1','999998','376','ichppc'),(8,'List1','999998','246','ichppc'),(9,'List1','999998','105','ichppc'),(10,'List1','999998','231','ichppc');

--
-- Dumping data for table `quickListUser`
--


--
-- Dumping data for table `radetail`
--


--
-- Dumping data for table `raheader`
--


--
-- Dumping data for table `recycle_bin`
--


--
-- Dumping data for table `recyclebin`
--


--
-- Dumping data for table `rehabStudy2004`
--


--
-- Dumping data for table `relationships`
--


--
-- Dumping data for table `remoteAttachments`
--


--
-- Dumping data for table `reportByExamples`
--


--
-- Dumping data for table `reportByExamplesFavorite`
--


--
-- Dumping data for table `reportConfig`
--


--
-- Dumping data for table `reportFilter`
--


--
-- Dumping data for table `reportItem`
--


--
-- Dumping data for table `reportTableFieldCaption`
--


--
-- Dumping data for table `reportTemplates`
--


--
-- Dumping data for table `report_letters`
--

-- INSERT INTO `report_letters` (`ID`, `provider_no`, `report_name`, `file_name`, `report_file`, `date_time`, `archive`) VALUES (1,'999998','PAP 1 - 2019','pap-initial.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"pap-initial\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"guardian_label2\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Guardian name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"pap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient Name and Address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"158\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n				</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n		</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"28\" y=\"82\" width=\"181\" height=\"72\"/>\n				<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[Our records show you are due for a PAP test.  A PAP test can help screen a patient for cervical cancer.  This is a vital check to catch it in early stages.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-1\" x=\"35\" y=\"47\" width=\"488\" height=\"24\">\n					<printWhenExpression><![CDATA[Boolean.valueOf($P{pap_immunization_date} != \"\")]]></printWhenExpression>\n				</reportElement>\n				<textFieldExpression><![CDATA[\"According to our records, \" + $P{patient_nameF} + \"\'s last PAP occurred on \" + $P{pap_immunization_date} + \".\"]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"76\" width=\"490\" height=\"83\"/><textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:14:43','0'),(2,'999998','PAP 2 - 2019','pap-second.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"pap-second\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"dtap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[date of last dtap-ipv-hib]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/><field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"183\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n				</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"82\" width=\"128\" height=\"95\"/>\n			<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n		</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[To follow up our first letter, please consider making an appointment for a PAP test.  The PAP test is important to help detect cervical cancer early]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"53\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:15:01','0'),(3,'999998','Imm 1 - 2019','Immunization-Initial.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"Immunization-Initial\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"guardian_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Guardian name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"dtap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[date of last dtap-ipv-hib]]></parameterDescription>\n	</parameter>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient Label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"315\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n				</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"82\" width=\"128\" height=\"95\"/>\n				<textFieldExpression><![CDATA[$P{guardian_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"210\" width=\"128\" height=\"99\"/>\n				<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<staticText>\n				<reportElement key=\"staticText-3\" x=\"37\" y=\"193\" width=\"128\" height=\"15\"/>\n			<text><![CDATA[Re:]]></text>\n			</staticText>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n	<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[The Dtap-IPV-Hib immunization is important to your child.  It prevents tetnus and diptheria.  Your child should have it at 2 months , 4 months, 6 months and 18 months of age.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-1\" x=\"35\" y=\"47\" width=\"488\" height=\"24\">\n					<printWhenExpression><![CDATA[Boolean.valueOf($P{dtap_immunization_date} != \"\")]]></printWhenExpression>\n				</reportElement>\n				<textFieldExpression><![CDATA[\"According to our records, \" + $P{patient_nameF} + \"\'s last immunization occured on \" + $P{dtap_immunization_date} + \".\"]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n			<reportElement key=\"textField-4\" x=\"35\" y=\"77\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n		</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:15:29','0'),(4,'999998','Imm 2 - 2019','dtap-ipv-hib-second.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"dtap-ipv-hib-second\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"guardian_label2\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Guardian name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"dtap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[date of last dtap-ipv-hib]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"289\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n				</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"82\" width=\"128\" height=\"95\"/>\n				<textFieldExpression><![CDATA[$P{guardian_label2}]]></textFieldExpression>\n			</textField>\n		<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-4\" x=\"37\" y=\"181\" width=\"128\" height=\"106\"/>\n				<textFieldExpression><![CDATA[\"Re:\\n\" + $P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n		<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[Following up our first letter, please consider making an appointment for the Dtap immunization.  The Dtap-IPV-Hib immunization is important to your child.  It prevents tetnus and diptheria.  Your child should have it at 2 months , 4 months, 6 months and 18 months of age.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"49\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:15:43','0'),(5,'999998','MAM 1 - 2019','mammogram-initial.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"mammogram-initial\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"guardian_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n	<parameterDescription><![CDATA[Guardian name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"mam_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient Name and Address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/><background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"158\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\"/>\n			<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"28\" y=\"82\" width=\"181\" height=\"72\"/>\n				<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[Our records show you are due for a Mammogram. A Mammogram can help screen a patient for breast cancer.  This is a vital check to catch it in early stages.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-1\" x=\"35\" y=\"47\" width=\"488\" height=\"24\">\n					<printWhenExpression><![CDATA[Boolean.valueOf($P{mam_immunization_date} != \"\")]]></printWhenExpression>\n				</reportElement>\n				<textFieldExpression><![CDATA[\"According to our records, \" + $P{patient_nameF} + \"\'s last Mammogram occurred on \" + $P{mam_immunization_date} + \".\"]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n			<reportElement key=\"textField-3\" x=\"37\" y=\"77\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n		</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:15:58','0'),(6,'999998','MAM 2 - 2019','mammogram-second.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"mammogram-second\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"dtap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[date of last dtap-ipv-hib]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"183\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"70\" width=\"219\" height=\"82\"/>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n		<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"82\" width=\"128\" height=\"95\"/>\n				<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n			<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[To follow up our first letter, please consider making an appointment for a Mammogram test.  The Mammogram test is important to help detect breast cancer early]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"46\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:16:13','0'),(7,'999998','FOBT 1 - 2019','fobt-initial.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"fobt-initial\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"guardian_label2\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Guardian name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"fobt_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient Name and Address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/><field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/><field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"158\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n			<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n				</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"28\" y=\"82\" width=\"181\" height=\"72\"/>\n				<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n	<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[Our records show you are due for a FOBT Test.  An FOBT Test can help screen a patient for colon cancer.  This is a vital check to catch it in early stages.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-1\" x=\"35\" y=\"47\" width=\"488\" height=\"24\">\n					<printWhenExpression><![CDATA[Boolean.valueOf($P{fobt_immunization_date} != \"\")]]></printWhenExpression>\n				</reportElement>\n				<textFieldExpression><![CDATA[\"According to our records, \" + $P{patient_nameF} + \"\'s last FOBT Test occurred on \" + $P{fobt_immunization_date} + \".\"]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-4\" x=\"37\" y=\"76\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:16:30','0'),(8,'999998','FOBT 2 - 2019','fobt-second.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"fobt-second\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"dtap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[date of last dtap-ipv-hib]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/><background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"183\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n			<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n					</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n		</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"82\" width=\"128\" height=\"95\"/>\n				<textFieldExpression><![CDATA[$P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[To follow up our first letter, please consider making an appointment for the FOBT test.  The FOBT test is important to help detect colon cancer early.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"48\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:16:43','0'),(9,'999998','Flu 1 - 2019','flu-initial.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"flu-initial\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"guardian_label2\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Guardian name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"flu_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/><field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/>\n	<field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"268\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n				</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"82\" width=\"128\" height=\"95\"/>\n				<textFieldExpression><![CDATA[$P{guardian_label2}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-4\" x=\"37\" y=\"181\" width=\"127\" height=\"82\"/>\n				<textFieldExpression><![CDATA[\"Re:\\n\" + $P{label}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n				<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[Every year the flu can keep you from enjoying your regular activities.  It is important to be vaccinated against the common strain of the flu virus which can minimize your risk.]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-1\" x=\"35\" y=\"47\" width=\"488\" height=\"24\">\n					<printWhenExpression><![CDATA[Boolean.valueOf($P{flu_immunization_date} != \"\")]]></printWhenExpression>\n				</reportElement>\n				<textFieldExpression><![CDATA[\"According to our records, \" + $P{patient_nameF} + \"\'s last immunization occured on \" + $P{flu_immunization_date} + \".\"]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"35\" y=\"77\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:17:26','0'),(10,'999998','Flu 2 - 2019','flu-second.jrxml','<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Created with Jaspersoft Studio version 6.8.0.final using JasperReports Library version 4.1.3  -->\n<jasperReport xmlns=\"http://jasperreports.sourceforge.net/jasperreports\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd\" name=\"flu-second\" pageWidth=\"612\" pageHeight=\"792\" whenNoDataType=\"NoPages\" columnWidth=\"552\" leftMargin=\"30\" rightMargin=\"30\" topMargin=\"20\" bottomMargin=\"20\">\n	<property name=\"ireport.scriptlethandling\" value=\"0\"/>\n	<property name=\"ireport.encoding\" value=\"UTF-8\"/>\n	<import value=\"net.sf.jasperreports.engine.*\"/>\n	<import value=\"java.util.*\"/>\n	<import value=\"net.sf.jasperreports.engine.data.*\"/>\n	<parameter name=\"clinic_label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[clinic name and address]]></parameterDescription>\n	</parameter>\n	<parameter name=\"label\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[Patient name and address label]]></parameterDescription>\n	</parameter>\n	<parameter name=\"patient_nameF\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[patient\'s first name]]></parameterDescription>\n	</parameter>\n	<parameter name=\"dtap_immunization_date\" class=\"java.lang.String\" isForPrompting=\"false\">\n		<parameterDescription><![CDATA[date of last dtap-ipv-hib]]></parameterDescription>\n	</parameter>\n	<parameter name=\"clinic_phone\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"provider_name_first_init\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"guardian_label2\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<parameter name=\"clinic_name\" class=\"java.lang.String\" isForPrompting=\"false\"/>\n	<field name=\"clinic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"clinic_address\" class=\"java.lang.String\"/>\n	<field name=\"clinic_city\" class=\"java.lang.String\"/>\n	<field name=\"clinic_postal\" class=\"java.lang.String\"/>\n	<field name=\"clinic_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_location_code\" class=\"java.lang.String\"/>\n	<field name=\"status\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_phone\" class=\"java.lang.String\"/>\n	<field name=\"clinic_delim_fax\" class=\"java.lang.String\"/>\n	<field name=\"clinic_province\" class=\"java.lang.String\"/>\n	<field name=\"demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"title\" class=\"java.lang.String\"/>\n	<field name=\"last_name\" class=\"java.lang.String\"/>\n	<field name=\"first_name\" class=\"java.lang.String\"/>\n	<field name=\"address\" class=\"java.lang.String\"/>\n	<field name=\"city\" class=\"java.lang.String\"/>\n	<field name=\"province\" class=\"java.lang.String\"/>\n	<field name=\"postal\" class=\"java.lang.String\"/>\n	<field name=\"phone\" class=\"java.lang.String\"/>\n	<field name=\"phone2\" class=\"java.lang.String\"/>\n	<field name=\"year_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"month_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"date_of_birth\" class=\"java.lang.String\"/>\n	<field name=\"hin\" class=\"java.lang.String\"/>\n	<field name=\"ver\" class=\"java.lang.String\"/>\n	<field name=\"roster_status\" class=\"java.lang.String\"/>\n	<field name=\"patient_status\" class=\"java.lang.String\"/>\n	<field name=\"date_joined\" class=\"java.sql.Date\"/>\n	<field name=\"chart_no\" class=\"java.lang.String\"/>\n	<field name=\"official_lang\" class=\"java.lang.String\"/><field name=\"spoken_lang\" class=\"java.lang.String\"/>\n	<field name=\"provider_no\" class=\"java.lang.String\"/>\n	<field name=\"sex\" class=\"java.lang.String\"/>\n	<field name=\"end_date\" class=\"java.sql.Date\"/>\n	<field name=\"eff_date\" class=\"java.sql.Date\"/>\n	<field name=\"pcn_indicator\" class=\"java.lang.String\"/>\n	<field name=\"hc_type\" class=\"java.lang.String\"/>\n	<field name=\"hc_renew_date\" class=\"java.sql.Date\"/>\n	<field name=\"family_doctor\" class=\"java.lang.String\"/>\n	<field name=\"pin\" class=\"java.lang.String\"/>\n	<field name=\"email\" class=\"java.lang.String\"/>\n	<field name=\"alias\" class=\"java.lang.String\"/>\n	<field name=\"previousAddress\" class=\"java.lang.String\"/>\n	<field name=\"children\" class=\"java.lang.String\"/>\n	<field name=\"sourceOfIncome\" class=\"java.lang.String\"/>\n	<field name=\"citizenship\" class=\"java.lang.String\"/>\n	<field name=\"sin\" class=\"java.lang.String\"/>\n	<field name=\"country_of_origin\" class=\"java.lang.String\"/>\n	<field name=\"newsletter\" class=\"java.lang.String\"/>\n	<field name=\"anonymous\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateUser\" class=\"java.lang.String\"/>\n	<field name=\"lastUpdateDate\" class=\"java.sql.Date\"/>\n	<field name=\"roster_date\" class=\"java.sql.Date\"/>\n	<field name=\"id\" class=\"java.lang.Integer\"/>\n	<field name=\"facility_id\" class=\"java.lang.Integer\"/>\n	<field name=\"relation_demographic_no\" class=\"java.lang.Integer\"/>\n	<field name=\"relation\" class=\"java.lang.String\"/>\n	<field name=\"creation_date\" class=\"java.sql.Timestamp\"/>\n	<field name=\"creator\" class=\"java.lang.String\"/>\n	<field name=\"sub_decision_maker\" class=\"java.lang.String\"/>\n	<field name=\"emergency_contact\" class=\"java.lang.String\"/>\n	<field name=\"notes\" class=\"java.lang.String\"/>\n	<field name=\"deleted\" class=\"java.lang.String\"/>\n	<field name=\"prevention_date\" class=\"java.sql.Date\"/>\n	<field name=\"provider_name\" class=\"java.lang.String\"/>\n	<field name=\"prevention_type\" class=\"java.lang.String\"/>\n	<field name=\"refused\" class=\"java.lang.String\"/>\n	<field name=\"next_date\" class=\"java.sql.Date\"/>\n	<field name=\"never\" class=\"java.lang.String\"/>\n	<background>\n		<band splitType=\"Stretch\"/>\n	</background>\n	<title>\n		<band height=\"281\" splitType=\"Stretch\">\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField\" x=\"290\" y=\"72\" width=\"219\" height=\"82\">\n					<property name=\"com.jaspersoft.studio.unit.x\" value=\"px\"/>\n					<property name=\"com.jaspersoft.studio.unit.y\" value=\"px\"/>\n	</reportElement>\n				<textFieldExpression><![CDATA[$P{clinic_label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-2\" x=\"37\" y=\"176\" width=\"128\" height=\"95\"/>\n				<textFieldExpression><![CDATA[\"Re:\\n\" + $P{label}]]></textFieldExpression>\n			</textField>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-4\" x=\"37\" y=\"81\" width=\"128\" height=\"85\"/>\n			<textFieldExpression><![CDATA[$P{guardian_label2}]]></textFieldExpression>\n			</textField>\n			<textField>\n				<reportElement x=\"1\" y=\"6\" width=\"490\" height=\"30\"/>\n				<textElement>\n					<font size=\"16\"/>\n				</textElement>\n				<textFieldExpression><![CDATA[$P{clinic_name}]]></textFieldExpression>\n			</textField>\n			<line>\n				<reportElement x=\"0\" y=\"40\" width=\"551\" height=\"1\"/>\n			</line>\n		</band>\n	</title>\n	<pageHeader>\n		<band splitType=\"Stretch\"/>\n	</pageHeader>\n	<columnHeader>\n		<band splitType=\"Stretch\"/>\n	</columnHeader>\n	<detail>\n		<band height=\"186\" splitType=\"Stretch\">\n			<staticText>\n		<reportElement key=\"staticText-1\" x=\"37\" y=\"6\" width=\"484\" height=\"36\"/>\n				<text><![CDATA[To follow up our first letter, please consider making an appointment for the Flu immunization.  The Flu immunization is important to help reduce the likelihood of succumbing to the virus during this flu season]]></text>\n			</staticText>\n			<textField isBlankWhenNull=\"false\">\n				<reportElement key=\"textField-3\" x=\"37\" y=\"50\" width=\"490\" height=\"83\"/>\n				<textFieldExpression><![CDATA[\"Please call me at your earliest convenience at \" + $P{clinic_phone} + \".\\n\\n\" + \n\n\"Sincerely,\\n\\n Dr. \" + $P{provider_name_first_init}]]></textFieldExpression>\n			</textField>\n		</band>\n	</detail>\n	<columnFooter>\n		<band splitType=\"Stretch\"/>\n	</columnFooter>\n	<pageFooter>\n		<band splitType=\"Stretch\"/>\n	</pageFooter>\n	<summary>\n		<band splitType=\"Stretch\"/>\n	</summary>\n</jasperReport>\n','2019-06-18 01:17:38','0');

--
-- Dumping data for table `reportagesex`
--


--
-- Dumping data for table `reportprovider`
--

INSERT INTO `reportprovider` (`id`, `provider_no`, `team`, `action`, `status`) VALUES (1,'174','Docs','billingreport','A');

--
-- Dumping data for table `reporttemp`
--


--
-- Dumping data for table `resident_oscarMsg`
--


--
-- Dumping data for table `rschedule`
--


--
-- Dumping data for table `scheduledate`
--


--
-- Dumping data for table `scheduleholiday`
--

INSERT INTO `scheduleholiday` (`sdate`, `holiday_name`) VALUES ('2002-01-01','New Year\'s Day'),('2002-02-11','2nd Monday in February - Hospital'),('2002-03-29','Good Friday'),('2002-04-01','Easter Monday - Hospital'),('2002-05-20','Victoria Day'),('2002-07-01','Canada Day'),('2002-08-05','Civic Day'),('2002-09-02','Labour Day'),('2002-10-14','Thanksgiving Day'),('2002-11-11','2nd Monday in November - Hospital'),('2002-12-25','Christmas Day'),('2002-12-26','Boxing Day'),('2002-12-27','In Lieu of Day Before Christmas - University'),('2002-12-30','Floating Holiday - University'),('2002-12-31','Floating Holiday - University'),('2003-01-01','New Year\'s Day'),('2003-02-10','2nd Monday in February - Hospital'),('2003-04-18','Good Friday'),('2003-04-21','Easter Monday - Hospital'),('2003-05-19','Victoria Day'),('2003-07-01','Canada Day'),('2003-08-04','Civic Day'),('2003-09-01','Labour Day'),('2003-10-13','Thanksgiving Day'),('2003-11-10','2nd Monday in November - Hospital'),('2003-12-25','Christmas Day'),('2003-12-26','Boxing Day'),('2004-01-01','New Year\'s Day');

--
-- Dumping data for table `scheduletemplate`
--

INSERT INTO `scheduletemplate` (`provider_no`, `name`, `summary`, `timecode`) VALUES ('Public','P:OnCallClinic','Weekends/Holidays','________________________________________CCCCCCCCCCCCCCCC________________________________________');

--
-- Dumping data for table `scheduletemplatecode`
--

INSERT INTO `scheduletemplatecode` (`id`, `code`, `description`, `duration`, `color`, `confirm`, `bookinglimit`) VALUES (1,'A','Academic','',NULL,'N',1),(2,'B','Behavioral Science','15','#BFEFFF','N',1),(3,'2','30 Minute Appointment','30','#BFEFFF','N',1),(4,'3','45 Minute Appointment','45','#BFEFFF','N',1),(5,'P','Phone time','15','#BFEFFF','N',1),(6,'M','Monitoring','','EED2EE','N',1),(7,'6','60 Minute Appointment','60','#BFEFFF','N',1),(8,'C','Chart Audit Rounds','15',NULL,'N',1),(9,'R','Rounds','15',NULL,'N',1),(10,'E','Study Leave','15',NULL,'N',1),(11,'V','Vacation','15','FFF68F','N',1),(12,'G','PBSG Rounds','15',NULL,'N',1),(13,'H','Hospital Rounds','15',NULL,'N',1),(14,'d','Drug Rep (Chief)','15',NULL,'N',1),(15,'U','Urgent','15',NULL,'N',1),(16,'a','Administrative Work','15','#BFEFFF','N',1),(17,'t','Travel','',NULL,'N',1),(18,'m','Meeting','',NULL,'N',1),(19,'1','15 Minute Appointment','15','#BFEFFF','N',1),(20,'s','Same Day','15','FFF68F','Day',1),(21,'S','Same Day - R1','30','FFF68F','Day',1),(22,'W','Same Week','15','FFF68F','Wk',1),(23,'C','On Call Clinic','15','green','Onc',1);

--
-- Dumping data for table `scratch_pad`
--


--
-- Dumping data for table `secObjPrivilege`
--

INSERT INTO `secObjPrivilege` (`roleUserGroup`, `objectName`, `privilege`, `priority`, `provider_no`) VALUES ('-1','_demographic','r',0,'999998'),('-1','_msg','x',0,'999998'),('admin','_admin','x',0,'999998'),('admin','_admin.caisi','x',0,'999998'),('admin','_admin.caisiRoles','x',0,'999998'),('admin','_admin.cookieRevolver','x',0,'999998'),('admin','_admin.demographic','u',0,'999998'),('admin','_admin.document','x',0,'999998'),('admin','_admin.facilityMessage','x',0,'999998'),('admin','_admin.fax','x',0,'999998'),('admin','_admin.hrm','x',0,'999998'),('admin','_admin.issueEditor','x',0,'999998'),('admin','_admin.lookupFieldEditor','x',0,'999998'),('admin','_admin.measurements','x',0,'999998'),('admin','_admin.pmm','x',0,'999998'),('admin','_admin.provider','x',0,'999998'),('admin','_admin.reporting','x',0,'999998'),('admin','_admin.security','x',0,'999998'),('admin','_admin.securityLogReport','x',0,'999998'),('admin','_admin.systemMessage','x',0,'999998'),('admin','_admin.traceability','x',0,'999998'),('admin','_admin.unlockAccount','x',0,'999998'),('admin','_admin.userCreatedForms','x',0,'999998'),('admin','_appDefinition','x',0,'999998'),('admin','_appointment','x',0,'999998'),('admin','_appointment.doctorLink','x',0,'999998'),('admin','_casemgmt.issues','x',0,'999998'),('admin','_casemgmt.notes','x',0,'999998'),('admin','_con','x',0,'999998'),('admin','_dashboardCommonLink','o',0,'999998'),('admin','_demographicExport','x',0,'999998'),('admin','_masterLink','x',0,'999998'),('admin','_msg','x',0,'999998'),('admin','_newCasemgmt.allergies','x',0,'999998'),('admin','_newCasemgmt.apptHistory','x',0,'999998'),('admin','_newCasemgmt.calculators','x',0,'999998'),('admin','_newCasemgmt.consultations','x',0,'999998'),('admin','_newCasemgmt.cpp','x',0,'999998'),('admin','_newCasemgmt.decisionSupportAlerts','x',0,'999998'),('admin','_newCasemgmt.doctorName','x',0,'999998'),('admin','_newCasemgmt.documents','x',0,'999998'),('admin','_newCasemgmt.DxRegistry','x',0,'999998'),('admin','_newCasemgmt.eForms','x',0,'999998'),('admin','_newCasemgmt.familyHistory','x',0,'999998'),('admin','_newCasemgmt.forms','x',0,'999998'),('admin','_newCasemgmt.labResult','x',0,'999998'),('admin','_newCasemgmt.measurements','x',0,'999998'),('admin','_newCasemgmt.medicalHistory','x',0,'999998'),('admin','_newCasemgmt.oscarMsg','x',0,'999998'),('admin','_newCasemgmt.otherMeds','x',0,'999998'),('admin','_newCasemgmt.prescriptions','x',0,'999998'),('admin','_newCasemgmt.preventions','x',0,'999998'),('admin','_newCasemgmt.riskFactors','x',0,'999998'),('admin','_newCasemgmt.templates','x',0,'999998'),('admin','_newCasemgmt.viewTickler','x',0,'999998'),('admin','_pmm.addProgram','x',0,'999998'),('admin','_pmm.caisiRoles','x',0,'999998'),('admin','_pmm.editor','x',0,'999998'),('admin','_pmm.globalRoleAccess','x',0,'999998'),('admin','_pmm.manageFacilities','x',0,'999998'),('admin','_pmm.programList','x',0,'999998'),('admin','_pmm.staffList','x',0,'999998'),('admin','_pmm_agencyList','x',0,'999998'),('admin','_pmm_editProgram.access','x',0,'999998'),('admin','_pmm_editProgram.bedCheck','x',0,'999998'),('admin','_pmm_editProgram.clients','x',0,'999998'),('admin','_pmm_editProgram.clientStatus','x',0,'999998'),('admin','_pmm_editProgram.functionUser','x',0,'999998'),('admin','_pmm_editProgram.general','x',0,'999998'),('admin','_pmm_editProgram.queue','x',0,'999998'),('admin','_pmm_editProgram.serviceRestrictions','x',0,'999998'),('admin','_pmm_editProgram.staff','x',0,'999998'),('admin','_pmm_editProgram.teams','x',0,'999998'),('admin','_pref','x',0,'999998'),('admin','_prevention.updateCVC','x',0,'999998'),('admin','_report','x',0,'999998'),('admin','_resource','x',0,'999998'),('admin','_search','x',0,'999998'),('Case Manager','_appointment','x',0,'999998'),('Case Manager','_casemgmt.issues','x',0,'999998'),('Case Manager','_casemgmt.notes','x',0,'999998'),('Case Manager','_demographic','x',0,'999998'),('Case Manager','_eChart','x',0,'999998'),('Case Manager','_eChart.verifyButton','x',0,'999998'),('Case Manager','_flowsheet','x',0,'999998'),('Case Manager','_masterLink','x',0,'999998'),('Case Manager','_pmm','x',0,'999998'),('Case Manager','_pmm.agencyInformation','x',0,'999998'),('Case Manager','_pmm.caseManagement','x',0,'999998'),('Case Manager','_pmm.clientSearch','x',0,'999998'),('Case Manager','_pmm.mergeRecords','x',0,'999998'),('Case Manager','_pmm.newClient','x',0,'999998'),('Case Manager','_pref','x',0,'999998'),('Case Manager','_tasks','x',0,'999998'),('Client Service Worker','_appointment','x',0,'999998'),('Client Service Worker','_casemgmt.issues','x',0,'999998'),('Client Service Worker','_casemgmt.notes','x',0,'999998'),('Client Service Worker','_demographic','x',0,'999998'),('Client Service Worker','_eChart','x',0,'999998'),('Client Service Worker','_eChart.verifyButton','x',0,'999998'),('Client Service Worker','_masterLink','x',0,'999998'),('Client Service Worker','_pmm','x',0,'999998'),('Client Service Worker','_pmm.agencyInformation','x',0,'999998'),('Client Service Worker','_pmm.caseManagement','x',0,'999998'),('Client Service Worker','_pmm.clientSearch','x',0,'999998'),('Client Service Worker','_pmm.newClient','x',0,'999998'),('Client Service Worker','_pref','x',0,'999998'),('Client Service Worker','_tasks','x',0,'999998'),('Clinical Assistant','_appointment','x',0,'999998'),('Clinical Assistant','_casemgmt.issues','x',0,'999998'),('Clinical Assistant','_casemgmt.notes','x',0,'999998'),('Clinical Assistant','_demographic','x',0,'999998'),('Clinical Assistant','_masterLink','x',0,'999998'),('Clinical Assistant','_pmm','x',0,'999998'),('Clinical Assistant','_pmm.agencyInformation','x',0,'999998'),('Clinical Assistant','_pmm.caisiRoles','x',0,'999998'),('Clinical Assistant','_pmm.caseManagement','x',0,'999998'),('Clinical Assistant','_pmm.clientSearch','x',0,'999998'),('Clinical Assistant','_pmm.mergeRecords','x',0,'999998'),('Clinical Assistant','_pmm.newClient','x',0,'999998'),('Clinical Assistant','_pref','x',0,'999998'),('Clinical Assistant','_tasks','x',0,'999998'),('Clinical Case Manager','_appointment','x',0,'999998'),('Clinical Case Manager','_casemgmt.issues','x',0,'999998'),('Clinical Case Manager','_casemgmt.notes','x',0,'999998'),('Clinical Case Manager','_demographic','x',0,'999998'),('Clinical Case Manager','_eChart','x',0,'999998'),('Clinical Case Manager','_eChart.verifyButton','x',0,'999998'),('Clinical Case Manager','_flowsheet','x',0,'999998'),('Clinical Case Manager','_masterLink','x',0,'999998'),('Clinical Case Manager','_pmm','x',0,'999998'),('Clinical Case Manager','_pmm.agencyInformation','x',0,'999998'),('Clinical Case Manager','_pmm.caseManagement','x',0,'999998'),('Clinical Case Manager','_pmm.clientSearch','x',0,'999998'),('Clinical Case Manager','_pmm.mergeRecords','x',0,'999998'),('Clinical Case Manager','_pmm.newClient','x',0,'999998'),('Clinical Case Manager','_pref','x',0,'999998'),('Clinical Case Manager','_tasks','x',0,'999998'),('Clinical Social Worker','_appointment','x',0,'999998'),('Clinical Social Worker','_casemgmt.issues','x',0,'999998'),('Clinical Social Worker','_casemgmt.notes','x',0,'999998'),('Clinical Social Worker','_demographic','x',0,'999998'),('Clinical Social Worker','_eChart','x',0,'999998'),('Clinical Social Worker','_eChart.verifyButton','x',0,'999998'),('Clinical Social Worker','_flowsheet','x',0,'999998'),('Clinical Social Worker','_masterLink','x',0,'999998'),('Clinical Social Worker','_pmm','x',0,'999998'),('Clinical Social Worker','_pmm.agencyInformation','x',0,'999998'),('Clinical Social Worker','_pmm.caseManagement','x',0,'999998'),('Clinical Social Worker','_pmm.clientSearch','x',0,'999998'),('Clinical Social Worker','_pmm.mergeRecords','x',0,'999998'),('Clinical Social Worker','_pmm.newClient','x',0,'999998'),('Clinical Social Worker','_pref','x',0,'999998'),('Clinical Social Worker','_tasks','x',0,'999998'),('Counselling Intern','_appointment','x',0,'999998'),('Counselling Intern','_casemgmt.issues','x',0,'999998'),('Counselling Intern','_casemgmt.notes','x',0,'999998'),('Counselling Intern','_demographic','x',0,'999998'),('Counselling Intern','_eChart','x',0,'999998'),('Counselling Intern','_eChart.verifyButton','x',0,'999998'),('Counselling Intern','_flowsheet','x',0,'999998'),('Counselling Intern','_masterLink','x',0,'999998'),('Counselling Intern','_pmm','x',0,'999998'),('Counselling Intern','_pmm.agencyInformation','x',0,'999998'),('Counselling Intern','_pmm.caseManagement','x',0,'999998'),('Counselling Intern','_pmm.clientSearch','x',0,'999998'),('Counselling Intern','_pmm.mergeRecords','x',0,'999998'),('Counselling Intern','_pmm.newClient','x',0,'999998'),('Counselling Intern','_pref','x',0,'999998'),('Counselling Intern','_tasks','x',0,'999998'),('counsellor','_appointment','x',0,'999998'),('counsellor','_casemgmt.issues','x',0,'999998'),('counsellor','_casemgmt.notes','x',0,'999998'),('counsellor','_demographic','x',0,'999998'),('counsellor','_eChart','x',0,'999998'),('counsellor','_eChart.verifyButton','x',0,'999998'),('counsellor','_flowsheet','x',0,'999998'),('counsellor','_masterLink','x',0,'999998'),('counsellor','_pmm','x',0,'999998'),('counsellor','_pmm.agencyInformation','x',0,'999998'),('counsellor','_pmm.caseManagement','x',0,'999998'),('counsellor','_pmm.clientSearch','x',0,'999998'),('counsellor','_pmm.mergeRecords','x',0,'999998'),('counsellor','_pmm.newClient','x',0,'999998'),('counsellor','_pref','x',0,'999998'),('counsellor','_tasks','x',0,'999998'),('doctor','_admin.caisi','o',0,'999998'),('doctor','_admin.caisiRoles','o',0,'999998'),('doctor','_admin.cookieRevolver','o',0,'999998'),('doctor','_admin.document','x',0,'999998'),('doctor','_admin.facilityMessage','o',0,'999998'),('doctor','_admin.issueEditor','o',0,'999998'),('doctor','_admin.lookupFieldEditor','o',0,'999998'),('doctor','_admin.provider','o',0,'999998'),('doctor','_admin.reporting','o',0,'999998'),('doctor','_admin.security','o',0,'999998'),('doctor','_admin.securityLogReport','o',0,'999998'),('doctor','_admin.systemMessage','o',0,'999998'),('doctor','_admin.traceability','x',0,'999998'),('doctor','_admin.unlockAccount','o',0,'999998'),('doctor','_admin.userCreatedForms','o',0,'999998'),('doctor','_allergy','x',0,'999998'),('doctor','_appointment','x',0,'999998'),('doctor','_appointment.doctorLink','x',0,'999998'),('doctor','_billing','x',0,'999998'),('doctor','_caseload.A1C','x',0,'999998'),('doctor','_caseload.Access1AdmissionDate','o',0,'999998'),('doctor','_caseload.ACR','x',0,'999998'),('doctor','_caseload.Age','x',0,'999998'),('doctor','_caseload.ApptsLYTD','x',0,'999998'),('doctor','_caseload.BMI','x',0,'999998'),('doctor','_caseload.BP','x',0,'999998'),('doctor','_caseload.CashAdmissionDate','o',0,'999998'),('doctor','_caseload.DisplayMode','x',0,'999998'),('doctor','_caseload.Doc','x',0,'999998'),('doctor','_caseload.EGFR','x',0,'999998'),('doctor','_caseload.EYEE','x',0,'999998'),('doctor','_caseload.HDL','x',0,'999998'),('doctor','_caseload.Lab','x',0,'999998'),('doctor','_caseload.LastAppt','x',0,'999998'),('doctor','_caseload.LastEncounterDate','o',0,'999998'),('doctor','_caseload.LastEncounterType','o',0,'999998'),('doctor','_caseload.LDL','x',0,'999998'),('doctor','_caseload.Msg','x',0,'999998'),('doctor','_caseload.NextAppt','x',0,'999998'),('doctor','_caseload.Sex','x',0,'999998'),('doctor','_caseload.SMK','x',0,'999998'),('doctor','_caseload.TCHD','x',0,'999998'),('doctor','_caseload.Tickler','x',0,'999998'),('doctor','_caseload.WT','x',0,'999998'),('doctor','_casemgmt.issues','x',0,'999998'),('doctor','_casemgmt.notes','x',0,'999998'),('doctor','_con','x',0,'999998'),('doctor','_dashboardCommonLink','o',0,'999998'),('doctor','_day','x',0,'999998'),('doctor','_demographic','x',0,'999998'),('doctor','_dxresearch','x',0,'999998'),('doctor','_eChart','x',0,'999998'),('doctor','_eChart.verifyButton','x',0,'999998'),('doctor','_edoc','x',0,'999998'),('doctor','_eform','x',0,'999998'),('doctor','_eform.doctor','x',0,'999998'),('doctor','_eyeform','x',0,'999998'),('doctor','_flowsheet','x',0,'999998'),('doctor','_form','x',0,'999998'),('doctor','_hrm','x',0,'999998'),('doctor','_lab','x',0,'999998'),('doctor','_masterLink','x',0,'999998'),('doctor','_measurement','x',0,'999998'),('doctor','_month','x',0,'999998'),('doctor','_msg','x',0,'999998'),('doctor','_newCasemgmt.allergies','x',0,'999998'),('doctor','_newCasemgmt.apptHistory','x',0,'999998'),('doctor','_newCasemgmt.calculators','x',0,'999998'),('doctor','_newCasemgmt.consultations','x',0,'999998'),('doctor','_newCasemgmt.cpp','x',0,'999998'),('doctor','_newCasemgmt.decisionSupportAlerts','x',0,'999998'),('doctor','_newCasemgmt.doctorName','x',0,'999998'),('doctor','_newCasemgmt.documents','x',0,'999998'),('doctor','_newCasemgmt.DxRegistry','x',0,'999998'),('doctor','_newCasemgmt.eaaps','x',0,'999998'),('doctor','_newCasemgmt.eForms','x',0,'999998'),('doctor','_newCasemgmt.episode','o',0,'999998'),('doctor','_newCasemgmt.familyHistory','x',0,'999998'),('doctor','_newCasemgmt.forms','x',0,'999998'),('doctor','_newCasemgmt.labResult','x',0,'999998'),('doctor','_newCasemgmt.measurements','x',0,'999998'),('doctor','_newCasemgmt.medicalHistory','x',0,'999998'),('doctor','_newCasemgmt.oscarMsg','x',0,'999998'),('doctor','_newCasemgmt.otherMeds','x',0,'999998'),('doctor','_newCasemgmt.photo','x',0,'999998'),('doctor','_newCasemgmt.pregnancy','o',0,'999998'),('doctor','_newCasemgmt.prescriptions','x',0,'999998'),('doctor','_newCasemgmt.preventions','x',0,'999998'),('doctor','_newCasemgmt.riskFactors','x',0,'999998'),('doctor','_newCasemgmt.templates','x',0,'999998'),('doctor','_newCasemgmt.viewTickler','x',0,'999998'),('doctor','_phr','x',0,'999998'),('doctor','_pmm.addProgram','x',0,'999998'),('doctor','_pmm.agencyInformation','x',0,'999998'),('doctor','_pmm.caisiRoles','x',0,'999998'),('doctor','_pmm.caseManagement','x',0,'999998'),('doctor','_pmm.clientSearch','x',0,'999998'),('doctor','_pmm.globalRoleAccess','x',0,'999998'),('doctor','_pmm.manageFacilities','x',0,'999998'),('doctor','_pmm.mergeRecords','x',0,'999998'),('doctor','_pmm.newClient','x',0,'999998'),('doctor','_pmm.programList','x',0,'999998'),('doctor','_pmm.staffList','x',0,'999998'),('doctor','_pmm_agencyList','x',0,'999998'),('doctor','_pmm_client.BedRoomReservation','x',0,'999998'),('doctor','_pmm_editProgram.access','x',0,'999998'),('doctor','_pmm_editProgram.bedCheck','x',0,'999998'),('doctor','_pmm_editProgram.clients','x',0,'999998'),('doctor','_pmm_editProgram.clientStatus','x',0,'999998'),('doctor','_pmm_editProgram.functionUser','x',0,'999998'),('doctor','_pmm_editProgram.general','x',0,'999998'),('doctor','_pmm_editProgram.queue','x',0,'999998'),('doctor','_pmm_editProgram.serviceRestrictions','x',0,'999998'),('doctor','_pmm_editProgram.staff','x',0,'999998'),('doctor','_pmm_editProgram.teams','x',0,'999998'),('doctor','_pmm_editProgram.vacancies','x',0,'999998'),('doctor','_pref','x',0,'999998'),('doctor','_prevention','x',0,'999998'),('doctor','_report','x',0,'999998'),('doctor','_resource','x',0,'999998'),('doctor','_rx','x',0,'999998'),('doctor','_rx.dispense','x',0,'999998'),('doctor','_search','x',0,'999998'),('doctor','_tasks','x',0,'999998'),('doctor','_tickler','x',0,'999998'),('Field Note Admin','_admin.fieldnote','x',0,'999998'),('Housing Worker','_appointment','x',0,'999998'),('Housing Worker','_casemgmt.issues','x',0,'999998'),('Housing Worker','_casemgmt.notes','x',0,'999998'),('Housing Worker','_demographic','x',0,'999998'),('Housing Worker','_eChart','x',0,'999998'),('Housing Worker','_eChart.verifyButton','x',0,'999998'),('Housing Worker','_flowsheet','x',0,'999998'),('Housing Worker','_masterLink','x',0,'999998'),('Housing Worker','_pmm','x',0,'999998'),('Housing Worker','_pmm.agencyInformation','x',0,'999998'),('Housing Worker','_pmm.caseManagement','x',0,'999998'),('Housing Worker','_pmm.clientSearch','x',0,'999998'),('Housing Worker','_pmm.mergeRecords','x',0,'999998'),('Housing Worker','_pmm.newClient','x',0,'999998'),('Housing Worker','_pref','x',0,'999998'),('Housing Worker','_tasks','x',0,'999998'),('HRMAdmin','_hrm.administrator','x',0,'999998'),('locum','_appointment','x',0,'999998'),('locum','_appointment.doctorLink','x',0,'999998'),('locum','_billing','x',0,'999998'),('locum','_casemgmt.issues','x',0,'999998'),('locum','_casemgmt.notes','x',0,'999998'),('locum','_demographic','x',0,'999998'),('locum','_eChart','x',0,'999998'),('locum','_eChart.verifyButton','x',0,'999998'),('locum','_masterLink','x',0,'999998'),('locum','_pref','x',0,'999998'),('locum','_rx','x',0,'999998'),('locum','_tasks','x',0,'999998'),('Medical Secretary','_appointment','x',0,'999998'),('Medical Secretary','_casemgmt.issues','x',0,'999998'),('Medical Secretary','_casemgmt.notes','x',0,'999998'),('Medical Secretary','_demographic','x',0,'999998'),('Medical Secretary','_masterLink','x',0,'999998'),('Medical Secretary','_pmm','x',0,'999998'),('Medical Secretary','_pmm.agencyInformation','x',0,'999998'),('Medical Secretary','_pmm.caisiRoles','x',0,'999998'),('Medical Secretary','_pmm.caseManagement','x',0,'999998'),('Medical Secretary','_pmm.clientSearch','x',0,'999998'),('Medical Secretary','_pmm.mergeRecords','x',0,'999998'),('Medical Secretary','_pmm.newClient','x',0,'999998'),('Medical Secretary','_pref','x',0,'999998'),('Medical Secretary','_tasks','x',0,'999998'),('nurse','_appointment','x',0,'999998'),('nurse','_casemgmt.issues','x',0,'999998'),('nurse','_casemgmt.notes','x',0,'999998'),('nurse','_demographic','x',0,'999998'),('nurse','_eChart','x',0,'999998'),('nurse','_eChart.verifyButton','x',0,'999998'),('nurse','_flowsheet','x',0,'999998'),('nurse','_masterLink','x',0,'999998'),('nurse','_phr','x',0,'999998'),('nurse','_pmm','x',0,'999998'),('nurse','_pmm.agencyInformation','x',0,'999998'),('nurse','_pmm.caisiRoles','x',0,'999998'),('nurse','_pmm.caseManagement','x',0,'999998'),('nurse','_pmm.clientSearch','x',0,'999998'),('nurse','_pmm.mergeRecords','x',0,'999998'),('nurse','_pmm.newClient','x',0,'999998'),('nurse','_pref','x',0,'999998'),('nurse','_tasks','x',0,'999998'),('nurse','_tickler','x',0,'999998'),('Nurse Manager','_appointment','x',0,'999998'),('Nurse Manager','_casemgmt.issues','x',0,'999998'),('Nurse Manager','_casemgmt.notes','x',0,'999998'),('Nurse Manager','_demographic','x',0,'999998'),('Nurse Manager','_eChart','x',0,'999998'),('Nurse Manager','_eChart.verifyButton','x',0,'999998'),('Nurse Manager','_flowsheet','x',0,'999998'),('Nurse Manager','_masterLink','x',0,'999998'),('Nurse Manager','_pmm','x',0,'999998'),('Nurse Manager','_pmm.agencyInformation','x',0,'999998'),('Nurse Manager','_pmm.caisiRoles','x',0,'999998'),('Nurse Manager','_pmm.caseManagement','x',0,'999998'),('Nurse Manager','_pmm.clientSearch','x',0,'999998'),('Nurse Manager','_pmm.mergeRecords','x',0,'999998'),('Nurse Manager','_pmm.newClient','x',0,'999998'),('Nurse Manager','_pref','x',0,'999998'),('Nurse Manager','_tasks','x',0,'999998'),('psychiatrist','_appointment','x',0,'999998'),('psychiatrist','_appointment.doctorLink','x',0,'999998'),('psychiatrist','_billing','x',0,'999998'),('psychiatrist','_casemgmt.issues','x',0,'999998'),('psychiatrist','_casemgmt.notes','x',0,'999998'),('psychiatrist','_demographic','x',0,'999998'),('psychiatrist','_eChart','x',0,'999998'),('psychiatrist','_eChart.verifyButton','x',0,'999998'),('psychiatrist','_flowsheet','x',0,'999998'),('psychiatrist','_masterLink','x',0,'999998'),('psychiatrist','_pmm','x',0,'999998'),('psychiatrist','_pmm.agencyInformation','x',0,'999998'),('psychiatrist','_pmm.caisiRoles','x',0,'999998'),('psychiatrist','_pmm.caseManagement','x',0,'999998'),('psychiatrist','_pmm.clientSearch','x',0,'999998'),('psychiatrist','_pmm.mergeRecords','x',0,'999998'),('psychiatrist','_pmm.newClient','x',0,'999998'),('psychiatrist','_pref','x',0,'999998'),('psychiatrist','_rx','x',0,'999998'),('psychiatrist','_tasks','x',0,'999998'),('receptionist','_appointment','x',0,'999998'),('receptionist','_billing','x',0,'999998'),('receptionist','_casemgmt.issues','x',0,'999998'),('receptionist','_casemgmt.notes','x',0,'999998'),('receptionist','_demographic','x',0,'999998'),('receptionist','_masterLink','x',0,'999998'),('receptionist','_pref','x',0,'999998'),('Recreation Therapist','_appointment','x',0,'999998'),('Recreation Therapist','_casemgmt.issues','x',0,'999998'),('Recreation Therapist','_casemgmt.notes','x',0,'999998'),('Recreation Therapist','_demographic','x',0,'999998'),('Recreation Therapist','_eChart','x',0,'999998'),('Recreation Therapist','_eChart.verifyButton','x',0,'999998'),('Recreation Therapist','_flowsheet','x',0,'999998'),('Recreation Therapist','_masterLink','x',0,'999998'),('Recreation Therapist','_pmm','x',0,'999998'),('Recreation Therapist','_pmm.agencyInformation','x',0,'999998'),('Recreation Therapist','_pmm.caseManagement','x',0,'999998'),('Recreation Therapist','_pmm.clientSearch','x',0,'999998'),('Recreation Therapist','_pmm.mergeRecords','x',0,'999998'),('Recreation Therapist','_pmm.newClient','x',0,'999998'),('Recreation Therapist','_pref','x',0,'999998'),('Recreation Therapist','_tasks','x',0,'999998'),('RN','_appointment','x',0,'999998'),('RN','_casemgmt.issues','x',0,'999998'),('RN','_casemgmt.notes','x',0,'999998'),('RN','_demographic','x',0,'999998'),('RN','_eChart','x',0,'999998'),('RN','_eChart.verifyButton','x',0,'999998'),('RN','_flowsheet','x',0,'999998'),('RN','_masterLink','x',0,'999998'),('RN','_pmm','x',0,'999998'),('RN','_pmm.agencyInformation','x',0,'999998'),('RN','_pmm.caisiRoles','x',0,'999998'),('RN','_pmm.caseManagement','x',0,'999998'),('RN','_pmm.clientSearch','x',0,'999998'),('RN','_pmm.mergeRecords','x',0,'999998'),('RN','_pmm.newClient','x',0,'999998'),('RN','_pref','x',0,'999998'),('RN','_tasks','x',0,'999998'),('RPN','_appointment','x',0,'999998'),('RPN','_casemgmt.issues','x',0,'999998'),('RPN','_casemgmt.notes','x',0,'999998'),('RPN','_demographic','x',0,'999998'),('RPN','_eChart','x',0,'999998'),('RPN','_eChart.verifyButton','x',0,'999998'),('RPN','_flowsheet','x',0,'999998'),('RPN','_masterLink','x',0,'999998'),('RPN','_pmm','x',0,'999998'),('RPN','_pmm.agencyInformation','x',0,'999998'),('RPN','_pmm.caisiRoles','x',0,'999998'),('RPN','_pmm.caseManagement','x',0,'999998'),('RPN','_pmm.clientSearch','x',0,'999998'),('RPN','_pmm.mergeRecords','x',0,'999998'),('RPN','_pmm.newClient','x',0,'999998'),('RPN','_pref','x',0,'999998'),('RPN','_tasks','x',0,'999998'),('secretary','_appointment','x',0,'999998'),('secretary','_casemgmt.issues','x',0,'999998'),('secretary','_casemgmt.notes','x',0,'999998'),('secretary','_demographic','x',0,'999998'),('secretary','_masterLink','x',0,'999998'),('secretary','_pmm.agencyInformation','x',0,'999998'),('secretary','_pmm.caisiRoles','x',0,'999998'),('secretary','_pmm.caseManagement','x',0,'999998'),('secretary','_pmm.clientSearch','x',0,'999998'),('secretary','_pmm.mergeRecords','x',0,'999998'),('secretary','_pmm.newClient','x',0,'999998'),('secretary','_pref','x',0,'999998'),('secretary','_tasks','x',0,'999998'),('Support Worker','_appointment','x',0,'999998'),('Support Worker','_casemgmt.issues','x',0,'999998'),('Support Worker','_casemgmt.notes','x',0,'999998'),('Support Worker','_demographic','x',0,'999998'),('Support Worker','_eChart','x',0,'999998'),('Support Worker','_eChart.verifyButton','x',0,'999998'),('Support Worker','_masterLink','x',0,'999998'),('Support Worker','_pmm','x',0,'999998'),('Support Worker','_pmm.agencyInformation','x',0,'999998'),('Support Worker','_pmm.caseManagement','x',0,'999998'),('Support Worker','_pmm.clientSearch','x',0,'999998'),('Support Worker','_pmm.newClient','x',0,'999998'),('Support Worker','_pref','x',0,'999998'),('Support Worker','_tasks','x',0,'999998');

--
-- Dumping data for table `secObjectName`
--

INSERT INTO `secObjectName` (`objectName`, `description`, `orgapplicable`) VALUES ('_admin','Administration',0),('_admin.auditLogPurge',NULL,0),('_admin.backup',NULL,0),('_admin.billing',NULL,0),('_admin.consult',NULL,0),('_admin.demographic',NULL,0),('_admin.document',NULL,0),('_admin.eform',NULL,0),('_admin.encounter',NULL,0),('_admin.fax','Configure & Manage Faxes',0),('_admin.hrm',NULL,0),('_admin.measurements','access to customize measurements',0),('_admin.messenger',NULL,0),('_admin.misc',NULL,0),('_admin.reporting',NULL,0),('_admin.resource',NULL,0),('_admin.schedule',NULL,0),('_admin.schedule.curprovider_only','allow provider with non-admin role to create schedule templa',0),('_admin.traceability','Right to generate trace and run traceability report',0),('_admin.userAdmin',NULL,0),('_allergy',NULL,0),('_appDefinition',NULL,0),('_appointment','Appointment',0),('_appointment.doctorLink',NULL,0),('_billing',NULL,0),('_caseload.A1C',NULL,0),('_caseload.Access1AdmissionDate',NULL,0),('_caseload.ACR',NULL,0),('_caseload.Age',NULL,0),('_caseload.ApptsLYTD',NULL,0),('_caseload.BMI',NULL,0),('_caseload.BP',NULL,0),('_caseload.CashAdmissionDate',NULL,0),('_caseload.DisplayMode',NULL,0),('_caseload.Doc',NULL,0),('_caseload.EGFR',NULL,0),('_caseload.EYEE',NULL,0),('_caseload.HDL',NULL,0),('_caseload.Lab',NULL,0),('_caseload.LastAppt',NULL,0),('_caseload.LastEncounterDate',NULL,0),('_caseload.LastEncounterType',NULL,0),('_caseload.LDL',NULL,0),('_caseload.Msg',NULL,0),('_caseload.NextAppt',NULL,0),('_caseload.SCR',NULL,0),('_caseload.Sex',NULL,0),('_caseload.SMK',NULL,0),('_caseload.TCHD',NULL,0),('_caseload.Tickler',NULL,0),('_caseload.WT',NULL,0),('_casemgmt.issues','Access to Case Management Issues',0),('_casemgmt.notes','Permissions for Case Management Notes',0),('_con',NULL,0),('_dashboardChgUser',NULL,0),('_dashboardCommonLink',NULL,0),('_dashboardDisplay',NULL,0),('_dashboardDrilldown',NULL,0),('_dashboardManager',NULL,0),('_day',NULL,0),('_demographic','Client Demographic Info',0),('_demographicExport','Export Demographic',0),('_dxresearch',NULL,0),('_eChart','Encounter',0),('_eChart.verifyButton',NULL,0),('_edoc',NULL,0),('_eform',NULL,0),('_eform.doctor',NULL,0),('_ehr',NULL,0),('_eyeform',NULL,0),('_flowsheet','Flow Sheet',0),('_form',NULL,0),('_formMentalHealth',NULL,0),('_hrm',NULL,0),('_hrm.administrator',NULL,0),('_lab',NULL,0),('_masterlink','Client Master Record',0),('_measurement',NULL,0),('_merge',NULL,0),('_month',NULL,0),('_msg',NULL,0),('_newCasemgmt.allergies',NULL,0),('_newCasemgmt.apptHistory',NULL,0),('_newCasemgmt.calculators',NULL,0),('_newCasemgmt.consultations',NULL,0),('_newCasemgmt.cpp',NULL,0),('_newCasemgmt.decisionSupportAlerts',NULL,0),('_newCasemgmt.doctorName',NULL,0),('_newCasemgmt.documents',NULL,0),('_newCasemgmt.DxRegistry',NULL,0),('_newCasemgmt.eaaps',NULL,0),('_newCasemgmt.eForms',NULL,0),('_newCasemgmt.episode',NULL,0),('_newCasemgmt.familyHistory',NULL,0),('_newCasemgmt.forms',NULL,0),('_newCasemgmt.labResult',NULL,0),('_newCasemgmt.measurements',NULL,0),('_newCasemgmt.medicalHistory',NULL,0),('_newCasemgmt.oscarMsg',NULL,0),('_newCasemgmt.otherMeds',NULL,0),('_newCasemgmt.photo',NULL,0),('_newCasemgmt.pregnancy',NULL,0),('_newCasemgmt.prescriptions',NULL,0),('_newCasemgmt.preventions',NULL,0),('_newCasemgmt.riskFactors',NULL,0),('_newCasemgmt.templates',NULL,0),('_newCasemgmt.viewTickler',NULL,0),('_phr',NULL,0),('_pmm_agencyList',NULL,0),('_pmm_client.BedRoomReservation',NULL,0),('_pmm_editProgram.vacancies',NULL,0),('_pref',NULL,0),('_prevention',NULL,0),('_prevention.updateCVC',NULL,0),('_queue.1','default',0),('_report',NULL,0),('_resource',NULL,0),('_rx',NULL,0),('_rx.dispense',NULL,0),('_search',NULL,0),('_site_access_privacy','restrict access to only the assigned sites of a provider',0),('_tasks',NULL,0),('_team_access_privacy','restrict access to only the same team of a provider',0),('_team_billing_only','Restrict billing access to only login provider and his team',0),('_team_schedule_only','Restrict schedule to only login provider and his team',0),('_tickler',NULL,0);

--
-- Dumping data for table `secPrivilege`
--

INSERT INTO `secPrivilege` (`id`, `privilege`, `description`) VALUES (1,'x','All rights.'),(2,'r','Read'),(3,'w','Write'),(4,'d','Delete'),(5,'o','No rights.'),(6,'u','Update');

--
-- Dumping data for table `secRole`
--

INSERT INTO `secRole` (`role_no`, `role_name`, `description`) VALUES (1,'receptionist','receptionist'),(2,'doctor','doctor'),(3,'admin','admin'),(4,'locum','locum'),(5,'nurse','nurse'),(6,'Vaccine Provider','Vaccine Provider'),(7,'external','External'),(8,'er_clerk','ER Clerk'),(9,'psychiatrist','psychiatrist'),(10,'RN','Registered Nurse'),(11,'RPN','Registered Practical Nurse'),(12,'Nurse Manager','Nurse Manager'),(13,'Clinical Social Worker','Clinical Social Worker'),(14,'Clinical Case Manager','Clinical Case Manager'),(15,'Medical Secretary','Medical Secretary'),(16,'Clinical Assistant','Clinical Assistant'),(17,'secretary','secretary'),(18,'counsellor','counsellor'),(19,'Case Manager','Case Manager'),(20,'Housing Worker','Housing Worker'),(21,'Support Worker','Support Worker'),(22,'Client Service Worker','Client Service Worker'),(23,'CAISI ADMIN','CAISI ADMIN'),(24,'Recreation Therapist','Recreation Therapist'),(25,'property staff','property staff'),(26,'Support Counsellor','Support Counsellor'),(27,'Counselling Intern','Counselling Intern'),(28,'Field Note Admin','Field Note Admin'),(29,'student','Student (OSCAR Learning)'),(30,'moderator','Moderator (OSCAR Learning)'),(31,'Site Manager','Site Manager'),(32,'Partner Doctor','Partner Doctor'),(33,'HRMAdmin','HRM Administator');

--
-- Dumping data for table `secUserRole`
--

INSERT INTO `secUserRole` (`id`, `provider_no`, `role_name`, `orgcd`, `activeyn`, `lastUpdateDate`) VALUES (1,'999998','doctor','R0000001',1,'2021-02-02 13:15:55'),(2,'999998','admin','R0000001',1,'2021-02-02 13:15:55'),(3,'999997','receptionist','R0000001',1,'2021-02-02 13:15:55');

--
-- Dumping data for table `security`
--

INSERT INTO `security` (`security_no`, `user_name`, `password`, `provider_no`, `pin`, `b_ExpireSet`, `date_ExpireDate`, `b_LocalLockSet`, `b_RemoteLockSet`, `forcePasswordReset`, `passwordUpdateDate`, `pinUpdateDate`, `lastUpdateUser`, `lastUpdateDate`, `oneIdKey`, `oneIdEmail`, `delegateOneIdEmail`, `totp_enabled`, `totp_secret`, `totp_algorithm`, `totp_digits`, `totp_period`) VALUES (128,'oscardoc','-51-282443-97-5-9410489-60-1021-45-127-12435464-32','999998','1117',1,'2100-01-01',1,1,1,NULL,NULL,NULL,'2021-02-02 18:15:52',NULL,NULL,NULL,0,'','sha1',6,30);

--
-- Dumping data for table `serviceSpecialists`
--


--
-- Dumping data for table `sharing_acl_definition`
--


--
-- Dumping data for table `sharing_actor`
--


--
-- Dumping data for table `sharing_affinity_domain`
--


--
-- Dumping data for table `sharing_clinic_info`
--


--
-- Dumping data for table `sharing_code_mapping`
--


--
-- Dumping data for table `sharing_code_value`
--


--
-- Dumping data for table `sharing_document_export`
--


--
-- Dumping data for table `sharing_exported_doc`
--


--
-- Dumping data for table `sharing_infrastructure`
--


--
-- Dumping data for table `sharing_mapping_code`
--


--
-- Dumping data for table `sharing_mapping_edoc`
--


--
-- Dumping data for table `sharing_mapping_eform`
--


--
-- Dumping data for table `sharing_mapping_misc`
--


--
-- Dumping data for table `sharing_mapping_site`
--


--
-- Dumping data for table `sharing_patient_document`
--


--
-- Dumping data for table `sharing_patient_network`
--


--
-- Dumping data for table `sharing_patient_policy_consent`
--


--
-- Dumping data for table `sharing_policy_definition`
--


--
-- Dumping data for table `sharing_value_set`
--


--
-- Dumping data for table `site`
--


--
-- Dumping data for table `specialistsJavascript`
--

INSERT INTO `specialistsJavascript` (`id`, `setId`, `javascriptString`) VALUES (1,'1','function makeSpecialistslist(dec){\n if(dec==\'1\') \n{K(-1,\"----Choose a Service-------\");D(-1,\"--------Choose a Specialist-----\");}\nelse\n{K(-1,\"----All Services-------\");D(-1,\"--------All Specialists-----\");}\nK(53,\"Cardiology\");\nD(53,\"297\",\"ss4444\",\"ssss, sss ssss\",\"sss\",\"sssss\");\n\nK(54,\"Dermatology\");\n\nK(55,\"Neurology\");\n\nK(56,\"Radiology\");\n\nK(57,\"SEE NOTES\");\n\n\n}\n');

--
-- Dumping data for table `specialty`
--

INSERT INTO `specialty` (`region`, `specialty`, `specialtydesc`) VALUES ('BC','00',' GENERAL PRACTITIONER'),('BC','00',' GENERAL PRACTITIONER'),('BC','01',' DERMATOLOGY'),('BC','02',' NEUROLOGY'),('BC','03',' PSYCHIATRY'),('BC','05',' OBSTETRICS & GYNAECOLOGY'),('BC','06',' OPHTHALMOLOGY'),('BC','07',' OTOLARYNGOLOGY'),('BC','08',' GENERAL SURGERY'),('BC','09',' NEUROSURGERY'),('BC','10',' ORTHOPAEDICS'),('BC','11',' PLASTIC SURGERY'),('BC','12',' CARDIO & THORACIC'),('BC','13',' UROLOGY'),('BC','14',' PAEDIATRICS'),('BC','15',' INTERNAL MEDICINE'),('BC','16',' RADIOLOGY'),('BC','17',' LABORATORY PROCEDURES'),('BC','18',' ANAESTHESIA'),('BC','19',' PAEDIATRIC CARDIOLOGY'),('BC','20',' PHYSICAL MEDICINE AND  REHABILITATION'),('BC','21',' PUBLIC HEALTH'),('BC','23',' OCCUPATIONAL MEDICINE'),('BC','24',' GERIATRIC MEDICINE          SUB-SPECIALTY OF INTERNAL MED'),('BC','26',' PROCEDURAL CARDIOLOGIST'),('BC','28',' EMERGENCY MEDICINE'),('BC','29',' MEDICAL MICROBIOLOGY'),('BC','30',' CHIROPRACTORS'),('BC','31',' NATUROPATHS'),('BC','32',' PHYSICAL THERAPISTS'),('BC','33',' NUCLEAR MEDICINE'),('BC','34',' OSTEOPATHY'),('BC','35',' ORTHOPTIC'),('BC','37',' ORAL SURGEONS'),('BC','38',' PODIATRISTS'),('BC','39',' OPTOMETRIST'),('BC','40',' DENTAL SURGEONS'),('BC','41',' ORAL MEDICINE'),('BC','42',' ORTHODONTISTS'),('BC','43',' MASSAGE PRACTITIONER'),('BC','44',' RHEUMATOLOGY'),('BC','45',' CLINICAL IMMUNIZATION AND ALLERGY'),('BC','46',' MEDICAL GENETICS'),('BC','47',' VASCULAR SURGERY'),('BC','48',' THORACIC SURGERY');

--
-- Dumping data for table `study`
--


--
-- Dumping data for table `studydata`
--


--
-- Dumping data for table `studylogin`
--


--
-- Dumping data for table `surveyData`
--


--
-- Dumping data for table `table_modification`
--


--
-- Dumping data for table `tickler`
--


--
-- Dumping data for table `tickler_category`
--

INSERT INTO `tickler_category` (`id`, `category`, `description`, `active`) VALUES (1,'To Call In','Call this patient in for a follow-up visit',''),(2,'Reminder Note','Send a reminder note to this patient',''),(3,'Follow-up Billing','Follow-up Additional Billing','');

--
-- Dumping data for table `tickler_link`
--


--
-- Dumping data for table `tickler_text_suggest`
--

INSERT INTO `tickler_text_suggest` (`id`, `creator`, `suggested_text`, `create_date`, `active`) VALUES (1,'-1','Advised Test Results','2021-02-02 18:16:49',1),(2,'-1','Advised RTC see INFO','2021-02-02 18:16:49',1),(3,'-1','Advised RTC see MD','2021-02-02 18:16:49',1),(4,'-1','Advised RTC for Rx','2021-02-02 18:16:49',1),(5,'-1','Advised RTC for Lab Work','2021-02-02 18:16:50',1),(6,'-1','Advised RTC for immunization','2021-02-02 18:16:50',1),(7,'-1','Declined treatment','2021-02-02 18:16:50',1),(8,'-1','Don\'t call','2021-02-02 18:16:50',1),(9,'-1','Letter sent','2021-02-02 18:16:50',1),(10,'-1','Msg on ans. mach. to call clinic','2021-02-02 18:16:50',1),(11,'-1','Msg with roomate to call clinic','2021-02-02 18:16:50',1),(12,'-1','Phone - No Answer','2021-02-02 18:16:50',1),(13,'-1','Notified','2021-02-02 18:16:50',1),(14,'-1','Notified. Patient is asymptomatic.','2021-02-02 18:16:50',1),(15,'-1','Prescription given','2021-02-02 18:16:50',1),(16,'-1','Prescription phoned in to:','2021-02-02 18:16:50',1),(17,'-1','Referral Booked','2021-02-02 18:16:50',1),(18,'-1','Re-Booked for followup','2021-02-02 18:16:51',1),(19,'-1','Returned for Lab Work','2021-02-02 18:16:51',1),(20,'-1','Telephone Busy','2021-02-02 18:16:51',1);

--
-- Dumping data for table `uploadfile_from`
--


--
-- Dumping data for table `user_ds_message_prefs`
--


--
-- Dumping data for table `vacancy`
--


--
-- Dumping data for table `vacancy_client_match`
--


--
-- Dumping data for table `vacancy_template`
--


--
-- Dumping data for table `validations`
--

INSERT INTO `validations` (`id`, `name`, `regularExp`, `maxValue1`, `minValue`, `maxLength`, `minLength`, `isNumeric`, `isTrue`, `isDate`) VALUES (1,'Numeric Value: 0 to 1',NULL,10,0,NULL,NULL,1,NULL,NULL),(2,'Numeric Value: 0 to 10',NULL,10,0,NULL,NULL,1,NULL,NULL),(3,'Numeric Value: 0 to 50',NULL,50,0,NULL,NULL,1,NULL,NULL),(4,'Numeric Value: 0 to 100',NULL,100,0,NULL,NULL,1,NULL,NULL),(5,'Numeric Value: 0 to 300',NULL,300,0,NULL,NULL,1,NULL,NULL),(6,'Blood Pressure','[0-9]{2,3}/{1}[0-9]{2,3}',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,'Yes/No/NA','YES|yes|Yes|Y|NO|no|No|N|NotApplicable|NA',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,'Integer: 1 to 5',NULL,5,1,1,NULL,NULL,NULL,NULL),(9,'Integer: 1 to 4',NULL,4,1,1,NULL,NULL,NULL,NULL),(10,'Integer: 1 to 3',NULL,3,1,1,NULL,NULL,NULL,NULL),(11,'No Validations',NULL,0,0,0,0,0,NULL,0),(12,'Yes/No/X','YES|yes|Yes|Y|NO|no|No|N|X|x',0,0,0,0,0,NULL,0),(13,'Date',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1),(14,'Numeric Value greater than or equal to 0',NULL,0,0,0,0,1,NULL,0),(15,'Yes/No/Maybe','YES|yes|Yes|Y|NO|no|No|N|MAYBE|maybe|Maybe',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(16,'Review','REVIEWED|reviewed|Reviewed',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(17,'pos or neg','pos|neg|positive|negative',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(18,'Yes/No','YES|yes|Yes|Y|NO|no|No|N',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(19,'Provided/Revised/Reviewed','Provided|Revised|Reviewed',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(20,'Mild/Moderate/Severe/Very Severe','Mild|Moderate|Severe|Very Severe',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(21,'Yes/Not Applicable','Yes|Not Applicable',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(22,'Yes','Yes',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(23,'Integer: 0 to 7',NULL,7,0,1,NULL,NULL,NULL,NULL),(24,'NYHA Class I-IV','Class I - no symptoms|Class II - symptoms with ordinary activity|Class III - symptoms with less than ordinary activity|Class IV - symptoms at rest',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(25,'COPD Classification','Mild: FEV1 >= 80% predicted|Moderate:50% <= FEV1 < 80% predicted|Severe:30% <= FEV1 < 50% predicted|Very Severe : FEV1 < 30% predicted',NULL,NULL,NULL,NULL,NULL,NULL,NULL);

--
-- Dumping data for table `view`
--


--
-- Dumping data for table `waitingList`
--


--
-- Dumping data for table `waitingListName`
--


--
-- Dumping data for table `workflow`
--
