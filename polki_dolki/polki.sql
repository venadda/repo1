
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` integer primary key AUTOINCREMENT,
  `name` varchar(150) NOT NULL,
  UNIQUE (`name`)
);
DROP TABLE IF EXISTS `auth_group_permissions`; 
CREATE TABLE `auth_group_permissions` (
  `id` integer primary key  AUTOINCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  
  UNIQUE(`group_id`,`permission_id`),
   FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
   FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
);
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` integer primary key  AUTOINCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  UNIQUE(`content_type_id`,`codename`),
  FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
);

INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry');
INSERT INTO `auth_permission` VALUES (2,'Can change log entry',1,'change_logentry');
INSERT INTO `auth_permission` VALUES (3,'Can delete log entry',1,'delete_logentry');
INSERT INTO `auth_permission` VALUES (4,'Can view log entry',1,'view_logentry');
INSERT INTO `auth_permission` VALUES (5,'Can add permission',2,'add_permission');
INSERT INTO `auth_permission` VALUES (6,'Can change permission',2,'change_permission');
INSERT INTO `auth_permission` VALUES (7,'Can delete permission',2,'delete_permission');
INSERT INTO `auth_permission` VALUES (8,'Can view permission',2,'view_permission');
INSERT INTO `auth_permission` VALUES (9,'Can add group',3,'add_group');
INSERT INTO `auth_permission` VALUES (10,'Can change group',3,'change_group');
INSERT INTO `auth_permission` VALUES (11,'Can delete group',3,'delete_group');
INSERT INTO `auth_permission` VALUES (12,'Can view group',3,'view_group');
INSERT INTO `auth_permission` VALUES (13,'Can add user',4,'add_user');
INSERT INTO `auth_permission` VALUES (14,'Can change user',4,'change_user');
INSERT INTO `auth_permission` VALUES (15,'Can delete user',4,'delete_user');
INSERT INTO `auth_permission` VALUES (16,'Can view user',4,'view_user');
INSERT INTO `auth_permission` VALUES (17,'Can add content type',5,'add_contenttype');
INSERT INTO `auth_permission` VALUES (18,'Can change content type',5,'change_contenttype');
INSERT INTO `auth_permission` VALUES (19,'Can delete content type',5,'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20,'Can view content type',5,'view_contenttype');
INSERT INTO `auth_permission` VALUES (21,'Can add session',6,'add_session');
INSERT INTO `auth_permission` VALUES (22,'Can change session',6,'change_session');
INSERT INTO `auth_permission` VALUES (23,'Can delete session',6,'delete_session');
INSERT INTO `auth_permission` VALUES (24,'Can view session',6,'view_session');
INSERT INTO `auth_permission` VALUES (25,'Can add vendor',7,'add_vendor');
INSERT INTO `auth_permission` VALUES (26,'Can change vendor',7,'change_vendor');
INSERT INTO `auth_permission` VALUES (27,'Can delete vendor',7,'delete_vendor');
INSERT INTO `auth_permission` VALUES (28,'Can view vendor',7,'view_vendor');
INSERT INTO `auth_permission` VALUES (29,'Can add vendor follow up',8,'add_vendorfollowup');
INSERT INTO `auth_permission` VALUES (30,'Can change vendor follow up',8,'change_vendorfollowup');
INSERT INTO `auth_permission` VALUES (31,'Can delete vendor follow up',8,'delete_vendorfollowup');
INSERT INTO `auth_permission` VALUES (32,'Can view vendor follow up',8,'view_vendorfollowup');

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` integer primary key AUTOINCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  UNIQUE(`username`)
);
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$ph0oRvCe6f5kjuxtlaxnfP$vh9D0XamQZrFG8RNxvs/U10XbDArHeEmVREFHZiyyEc=','2022-05-05 14:21:40.549455',1,'admin','','','addala.venkateswar@polki-dolki.com',1,1,'2022-05-05 10:19:50.077493');
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$260000$HvJL5xMKBozhbujP10dC65$R6s+eGCnko70ydRZyQOYpZPh+L9ELQI79ZvtPLObWdA=','2022-07-23 05:45:52.588722',1,'venkat','','','venkat@gmail.com',1,1,'2022-07-04 11:51:31.455817');
INSERT INTO `auth_user` VALUES (3,'pbkdf2_sha256$260000$VDouEXpieDeIKribmWzsrQ$qH+UNeNxYbCMNC9TxlgxCxb5qQhRxn0aZijij/IBqps=',NULL,0,'venka','venka','venka','ven@gmail.com',0,1,'2022-07-09 06:17:17.247493');
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` integer primary key  AUTOINCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  UNIQUE (`user_id`,`group_id`),
   FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
   FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ;
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` integer primary key AUTOINCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  UNIQUE (`user_id`,`permission_id`),
  FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
   FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
);

DROP TABLE IF EXISTS `colour`;
CREATE TABLE `colour` (
  `product_id` int NOT NULL,
  `colour` varchar(50) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `country`;
CREATE TABLE `country` (
  `id` char(3) primary key,
  `country_name` varchar(20) NOT NULL,
  `country_dail_no` char(4) DEFAULT NULL,
  `country_flag` longblob,
  `mobile_no_size` int DEFAULT '0',
  `country_region` int DEFAULT NULL
  
);
DROP TABLE IF EXISTS `country_state`;
CREATE TABLE `country_state` (
  `id` integer primary key AUTOINCREMENT,
  `state_code` char(3) DEFAULT NULL,
  `state_country_code` char(4) DEFAULT NULL,
  `state_name` varchar(20) NOT NULL,
  `state_longitude` int DEFAULT NULL,
  `state_latitude` int DEFAULT NULL
);

DROP TABLE IF EXISTS `customer_registrations`;
CREATE TABLE `customer_registrations` (
  `id` integer primary key AUTOINCREMENT,
  `cust_firstname` varchar(20) NOT NULL,
  `cust_lastname` varchar(20) NOT NULL,
  `cust_email` varchar(100) NOT NULL,
  `cust_phone` varchar(15) NOT NULL
);
INSERT INTO `customer_registrations` VALUES (1,'mohan','karmchand','mohan.karmchand@gmail.com','9900199001');
INSERT INTO `customer_registrations` VALUES (2,'rajini','kanth','rajini.kanth@gmail.com','9900299002');
INSERT INTO `customer_registrations` VALUES (3,'anil','kumar','anil.kumar@gmail.com','9900399003');
INSERT INTO `customer_registrations` VALUES (4,'kamal','karan','kamal@gmail.com','342342343');
INSERT INTO `customer_registrations` VALUES (5,'naveen','kumar','navi.kumar@gmail.com','9900299002');
INSERT INTO `customer_registrations` VALUES (6,'kamala','karan','kamal.karan@gmail.com','9900299002');
DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `id` integer primary key AUTOINCREMENT,
  `customer_name` varchar(50) NOT NULL,
  `customer_mobile` varchar(15) DEFAULT NULL,
  `customer_email` varchar(100) DEFAULT NULL,
  `customer_password` binary(60) DEFAULT NULL,
  `customer_created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `customer_updated_date` datetime DEFAULT NULL,
  `customer_loggedin_date` datetime DEFAULT NULL,
  `customer_country` char(3) DEFAULT 'IND'
);
DROP TABLE IF EXISTS `design_type`;
CREATE TABLE `design_type` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `design_type` varchar(100) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` integer primary key AUTOINCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL CHECK (`action_flag` >= 0), 
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  
  FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)

);
INSERT INTO `django_admin_log` VALUES (1,'2022-05-05 14:26:20.406564','6','Vendor object (6)',2,'[{\"changed\": {\"fields\": [\"Middle Name\", \"Email Account\", \"Description\", \"Web URL\", \"Created By\", \"Updated By\", \"Updated Date\"]}}]',7,1);
INSERT INTO `django_admin_log` VALUES (2,'2022-05-05 14:27:33.058729','6','Vendor object (6)',2,'[{\"changed\": {\"fields\": [\"Created By\", \"Updated By\", \"Updated Date\"]}}]',7,1);
INSERT INTO `django_admin_log` VALUES (3,'2022-05-05 15:30:09.832301','6','Vendor object (6)',2,'[{\"changed\": {\"fields\": [\"First Name\", \"Created By\", \"Updated By\", \"Updated Date\"]}}]',7,1);
INSERT INTO `django_admin_log` VALUES (4,'2022-07-22 12:24:28.637686','1','test',1,'[{\"added\": {}}]',9,2);
INSERT INTO `django_admin_log` VALUES (5,'2022-07-23 05:47:16.833043','2','VendorFollowUpsModel object (2)',1,'[{\"added\": {}}]',9,2);

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` integer primary key AUTOINCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  UNIQUE (`app_label`,`model`)
);
INSERT INTO `django_content_type` VALUES (1,'admin','logentry');
INSERT INTO `django_content_type` VALUES (3,'auth','group');
INSERT INTO `django_content_type` VALUES (2,'auth','permission');
INSERT INTO `django_content_type` VALUES (4,'auth','user');
INSERT INTO `django_content_type` VALUES (9,'business','vendorfollowupsmodel');
INSERT INTO `django_content_type` VALUES (5,'contenttypes','contenttype');
INSERT INTO `django_content_type` VALUES (7,'management','vendor');
INSERT INTO `django_content_type` VALUES (8,'management','vendorfollowup');
INSERT INTO `django_content_type` VALUES (6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` integer primary key AUTOINCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-04-25 16:21:13.843153');
INSERT INTO `django_migrations` VALUES (2,'auth','0001_initial','2022-04-25 16:21:14.853223');
INSERT INTO `django_migrations` VALUES (3,'admin','0001_initial','2022-04-25 16:21:15.109652');
INSERT INTO `django_migrations` VALUES (4,'admin','0002_logentry_remove_auto_add','2022-04-25 16:21:15.127934');
INSERT INTO `django_migrations` VALUES (5,'admin','0003_logentry_add_action_flag_choices','2022-04-25 16:21:15.147322');
INSERT INTO `django_migrations` VALUES (6,'contenttypes','0002_remove_content_type_name','2022-04-25 16:21:15.343347');
INSERT INTO `django_migrations` VALUES (7,'auth','0002_alter_permission_name_max_length','2022-04-25 16:21:15.511228');
INSERT INTO `django_migrations` VALUES (8,'auth','0003_alter_user_email_max_length','2022-04-25 16:21:15.836434');
INSERT INTO `django_migrations` VALUES (9,'auth','0004_alter_user_username_opts','2022-04-25 16:21:15.861104');
INSERT INTO `django_migrations` VALUES (10,'auth','0005_alter_user_last_login_null','2022-04-25 16:21:15.988218');
INSERT INTO `django_migrations` VALUES (11,'auth','0006_require_contenttypes_0002','2022-04-25 16:21:15.994031');
INSERT INTO `django_migrations` VALUES (12,'auth','0007_alter_validators_add_error_messages','2022-04-25 16:21:16.013840');
INSERT INTO `django_migrations` VALUES (13,'auth','0008_alter_user_username_max_length','2022-04-25 16:21:16.134658');
INSERT INTO `django_migrations` VALUES (14,'auth','0009_alter_user_last_name_max_length','2022-04-25 16:21:16.267019');
INSERT INTO `django_migrations` VALUES (15,'auth','0010_alter_group_name_max_length','2022-04-25 16:21:16.383003');
INSERT INTO `django_migrations` VALUES (16,'auth','0011_update_proxy_permissions','2022-04-25 16:21:16.400181');
INSERT INTO `django_migrations` VALUES (17,'auth','0012_alter_user_first_name_max_length','2022-04-25 16:21:16.510888');
INSERT INTO `django_migrations` VALUES (18,'management','0001_initial','2022-04-25 16:21:16.588206');
INSERT INTO `django_migrations` VALUES (19,'sessions','0001_initial','2022-04-25 16:21:16.652285');
INSERT INTO `django_migrations` VALUES (20,'management','0002_rename_first_name_vendor_first_name_and_more','2022-05-05 10:15:11.932029');
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) primary key ,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
 
);
INSERT INTO `django_session` VALUES ('04tsk79153euy0wst73q3qlqhlfgdf72','.eJxVjEEOwiAQRe_C2pCBAopL956hGWYGqRpISrsy3l2bdKHb_977LzXiupRx7TKPE6uzsurwuyWkh9QN8B3rrWlqdZmnpDdF77Tra2N5Xnb376BgL98aBocBM8Qg4LKXbNh6IRAvbKyzDGQGijEgJ2HChOAoObDG0dHKSb0_-Hw4mw:1o8Kuh:Mz_XmSRGJ1MwW_1KOcDKqpfK9qESpL_EgNZr98k81Bo','2022-07-18 12:10:51.868334');
INSERT INTO `django_session` VALUES ('f0r12250mbnx36fub79kbpfka8tx3jmb','.eJxVjEEOwiAQRe_C2pABDFNcuvcMZGYAqRqalHbVeHdt0oVu_3vvbyrSutS49jzHMamLsur0uzHJM7cdpAe1-6Rlass8st4VfdCub1PKr-vh_h1U6vVbGyCDUhKBNSLgg-PiGCFADoExBUFAR-IHKc4zcaKzLWjJZYODePX-AO9JOFQ:1oB7dB:X_CZ0kvER11VyvrQtBoqsYRcq8UKHrrhcnysBYvrQeY','2022-07-26 04:36:17.648390');
INSERT INTO `django_session` VALUES ('hoto2n5uns5v5fz2bb88ik2raokmrybr','.eJxVjM0OwiAQhN-FsyHCUn48evcZyC5LpWogKe3J-O62SQ96nPm-mbeIuC4lrj3PcWJxEVqcfjvC9Mx1B_zAem8ytbrME8ldkQft8tY4v66H-3dQsJdtDWyMJ-fhnBithzxoUp51CogEYI0mGJgZR0NBuy0HlQFJWwfKjk58vt-zN50:1oErec:mX9OhrVULOexG68sz2niN0RZ-p8UktDg3BUijbIrB8Q','2022-08-05 12:21:14.517567');
INSERT INTO `django_session` VALUES ('ht8e9ngxrvmzvj9p70n7fh2549enzuar','.eJxVjM0OwiAQhN-FsyHCUn48evcZyC5LpWogKe3J-O62SQ96nPm-mbeIuC4lrj3PcWJxEVqcfjvC9Mx1B_zAem8ytbrME8ldkQft8tY4v66H-3dQsJdtDWyMJ-fhnBithzxoUp51CogEYI0mGJgZR0NBuy0HlQFJWwfKjk58vt-zN50:1oF7xY:_Zs2rOeBqQBwINPPVPIa0UhhTmdfaSVFL7dhUDbLwbE','2022-08-06 05:45:52.598728');
INSERT INTO `django_session` VALUES ('ktskhl1c6v407hhxql94l8qydo1fu8ye','.eJxVjL0OwyAQg9-FuUJc-BHp2L3PgC7cUdJWIIVkivruJVKGdrP92d5FwG3NYWu8hJnEVYC4_GYTxheXA9ATy6PKWMu6zJM8KvKkTd4r8ft2dv8OMrbc18ki6BhHD1FrROU8dKWUMxa1S2QNebA8wAgu6cFoZGcTJcBu2IP4fAHLJTco:1nmcMO:5EiNugkC92QdOJrtvT8BqOW2vH87V-onVr_2x4RAJeo','2022-05-19 14:21:40.561458');
INSERT INTO `django_session` VALUES ('uu6pl9a4zncu6vi3v4t5gmhpfnhpl2sk','e30:1oB7kK:1GKmylWUMuQMbAeWl41B0wmuhaN_pAzG58l_KiNt-oI','2022-07-26 04:43:40.138641');
DROP TABLE IF EXISTS `fabric_category`;
CREATE TABLE `fabric_category` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `fabric_category` varchar(100) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `fabric_type`;
CREATE TABLE `fabric_type` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `fabrc_type` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `gender`;
CREATE TABLE `gender` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `gender` varchar(10) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `images` tinyblob NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `vendor_id` int NOT NULL,
  `product_id` int NOT NULL,
  `gender_id` int NOT NULL,
  `sub_product_id` int NOT NULL,
  `category_id` int NOT NULL,
  `fabric_type_id` int NOT NULL,
  `design_type_id` int NOT NULL,
  `pricing_id` int NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `id` integer primary key AUTOINCREMENT,
  `account` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(100) NOT NULL,
  `pwd_question` varchar(200) DEFAULT NULL,
  `pwd_answer` varchar(200) DEFAULT NULL,
  `pwd_question2` varchar(200) DEFAULT NULL,
  `pwd_answer2` varchar(200) DEFAULT NULL,
  `active` tinyint(1) DEFAULT '1',
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` int DEFAULT NULL
);
DROP TABLE IF EXISTS `pricing`;
CREATE TABLE `pricing` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `mrp` int NOT NULL,
  `discount` varchar(10) NOT NULL,
  `actual_price` int NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `vendor_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `type` varchar(100) NOT NULL,
  `status` varchar(30) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
DROP TABLE IF EXISTS `product_category`;
CREATE TABLE `product_category` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `category_type` varchar(100) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` tinyint(1) DEFAULT '1'
);
DROP TABLE IF EXISTS `sub_product`;
CREATE TABLE `sub_product` (
  `product_id` int NOT NULL,
  `id` integer primary key AUTOINCREMENT,
  `sub_product_type` varchar(50) NOT NULL,
  `created_by` varchar(30) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) NOT NULL,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` tinyint(1) DEFAULT '1'
);
DROP TABLE IF EXISTS `user_roles`;
CREATE TABLE `user_roles` (
  `id` integer primary key AUTOINCREMENT,
  `role_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_by` int NOT NULL DEFAULT '0',
  `updated_by` int DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT NULL
);
DROP TABLE IF EXISTS `vendor`;
CREATE TABLE `vendor` (
  `id` integer primary key AUTOINCREMENT,
  `first_name` varchar(20) NOT NULL,
  `middle_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) NOT NULL,
  `contact_no` varchar(20) NOT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `company` varchar(100) NOT NULL,
  `content` varchar(500) DEFAULT NULL,
  `website_url` varchar(100) DEFAULT NULL,
  `created_by` varchar(30) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(30) DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  `company_phone` varchar(15) DEFAULT NULL,
  `company_email` varchar(100) DEFAULT NULL,
  `product` varchar(100) DEFAULT NULL,
  `prod_specialize` varchar(500) DEFAULT NULL,
  `prod_price_range` varchar(50) DEFAULT NULL,
  `company_gst` varchar(50) DEFAULT NULL
);
INSERT INTO `vendor` VALUES (4,'Dilip',NULL,'Mehta','8045910784',NULL,'Nav Darshan Fabrics',' Exports are a key driver to boost our economy, generate employment and provide bigger markets for growing companies. It?s no wonder our Hon?ble Prime Minister has stressed the need to boost exports from India and highlighted its importance to revive our economy in the post-pandemic world. For the first time in history, India has breached the $400 billion mark in annual merchandise exports in FY 21-22 and this has been made possible due to the unwavering commitment of multiple stakeholders.',NULL,'1','2022-04-25 12:07:09','2','2022-04-25 17:37:09',NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO `vendor` VALUES (5,'Ravi',NULL,'Sutariya','8048845357',NULL,'Somnath Creation',' Exports are a key driver to boost our economy, generate employment and provide bigger markets for growing companies. It?s no wonder our Hon?ble Prime Minister has stressed the need to boost exports from India and highlighted its importance to revive our economy in the post-pandemic world. For the first time in history, India has breached the $400 billion mark in annual merchandise exports in FY 21-22 and this has been made possible due to the unwavering commitment of multiple stakeholders.',NULL,'1','2022-04-25 12:07:55','2','2022-04-25 17:37:55',NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO `vendor` VALUES (6,'Khalid mohamd khalid','seikh','Seikh','8048808427','khalid@gmail.com','SK Sarees Emporium','Exports are a key driver to boost our economy, generate employment and provide bigger markets for growing companies. It’s no wonder our Hon’ble Prime Minister has stressed the need to boost exports from India and highlighted its importance to revive our economy in the post-pandemic world. For the first time in history, India has breached the $400 billion mark in annual merchandise exports in FY 21-22 and this has been made possible due to the unwavering commitment of multiple stakeholders. As In','http://khalid.com','1','2022-04-24 18:30:00','2','2022-04-25 00:00:00',NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO `vendor` VALUES (7,'rajesh','','konda','9922399223','konda.rajesh@gmail.com','rajeshconda and co','testing','www.rajeshkonda.com','1','2022-05-09 18:30:00','2',NULL,'9933344444','rajeshkonda@gmail.com','women products','fashion','3000-5000','1232-123-1232');
INSERT INTO `vendor` VALUES (8,'anil','asdfasd','kumar','9999999','anil.kumar@gmail.com','anil and co','asdfjkd','www.rajeshkonda.com','1','2022-05-10 18:30:00','2',NULL,'88888888','anil@gmail.com','men','men','100-500','1232-123-1232');
INSERT INTO `vendor` VALUES (9,'raghu','m','nadth','9922399223','rag.nadth@gmail.com','verandar and brothers','abcdef','www.rajeshkonda.com','1','2022-05-13 18:30:00','2',NULL,'9933344444','abc@gmail.com','menware','T-shirt','2000-5000','123-123-123');
DROP TABLE IF EXISTS `vendor_addresses`;
CREATE TABLE `vendor_addresses` (
  `id` integer primary key AUTOINCREMENT,
  `vendor_id` int NOT NULL,
  `address` varchar(100) NOT NULL,
  `line1` varchar(100) DEFAULT NULL,
  `line2` varchar(100) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `pincode` varchar(6) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` int DEFAULT NULL
);


DROP TABLE IF EXISTS `vendor_follow_ups`;
CREATE TABLE `vendor_follow_ups` (
  `id` integer primary key AUTOINCREMENT,
  `first_name` varchar(20) NOT NULL,
  `middle_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) NOT NULL,
  `primary_no` varchar(30) NOT NULL,
  `secondary_no` varchar(30) NOT NULL,
  `company_email_id` varchar(50) DEFAULT NULL,
  `company_name` varchar(30) NOT NULL,
  `content` varchar(200) NOT NULL,
  `website_url` varchar(40) DEFAULT NULL,
  `product` varchar(100) NOT NULL,
  `reference` varchar(20) NOT NULL,
  `comments` varchar(200) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `vendor_id` int NOT NULL,
  `created_by` int NOT NULL,
  `updated_by` int DEFAULT NULL,
  FOREIGN KEY (`created_by`) REFERENCES `auth_user` (`id`),
  FOREIGN KEY (`updated_by`) REFERENCES `auth_user` (`id`),
  FOREIGN KEY (`vendor_id`) REFERENCES `vendor` (`id`)
);
INSERT INTO `vendor_follow_ups` VALUES (1,'test','test','test','test','test','test@gmail.com','test','test','abc.com','product','12','asdfk','2022-07-22 12:23:12','2022-07-05 12:24:15',8,1,1);
INSERT INTO `vendor_follow_ups` VALUES (2,'temp','temp','temp','234234','23423','tem@gmail.com','temp','temp','tem.com','temp','temp','temp','2022-07-23 05:45:59','2022-07-23 05:47:07',8,3,3);
