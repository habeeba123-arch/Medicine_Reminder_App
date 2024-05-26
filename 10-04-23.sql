/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - medicine_reminder
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`medicine_reminder` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `medicine_reminder`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`b_id`,`schedule_id`,`patient_id`,`date`,`time`,`status`) values 
(1,5,12,'22/03/2023','16:50','pending'),
(2,0,0,'\"++\"','\"++\"','\"++\"');

/*Table structure for table `care_taker` */

DROP TABLE IF EXISTS `care_taker`;

CREATE TABLE `care_taker` (
  `caretaker_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `caretaker_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`caretaker_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=latin1;

/*Data for the table `care_taker` */

insert  into `care_taker`(`caretaker_id`,`lid`,`caretaker_name`,`place`,`email`,`phone_no`) values 
(0,123,'fas','gfdgdf','fas@gmail.com',2147483647),
(124,0,'\"++\"','\"++\"','\"++\"',0);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `replay` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`cid`,`lid`,`user_id`,`complaint`,`status`,`date`,`replay`) values 
(11,10,0,'drgfrdhtjyhujmk','replayed','2023-03-28','whghsev'),
(12,123,0,'uihiugyf','uyuiguyd','2023-03-28','gyufytdrtsdr'),
(13,10,0,'hngngh','pending','2023-04-04','pending'),
(14,10,0,'gvdfgbfvb','pending','2023-04-04','pending'),
(15,10,0,'vgghbhbjb','pending','2023-04-04','pending'),
(16,0,0,'\"++\"','\"++\"','0000-00-00','\"++\"');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `doc_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `doc_name` varchar(50) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `phno` bigint(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `hlid` int(11) DEFAULT NULL,
  PRIMARY KEY (`doc_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`doc_id`,`lid`,`doc_name`,`photo`,`department`,`experience`,`qualification`,`gender`,`DOB`,`place`,`pin`,`phno`,`email`,`hlid`) values 
(8,4,'','','','','','','','','',NULL,NULL,NULL),
(11,3,'nana',NULL,'ENT','3year','md','female','23/3/1986','hhhaa','234245',NULL,NULL,NULL),
(14,10,'nana','/static/doctor_img/20230316165102.jpg','swass','edr','fgyh','Male','23/8/2000','jn','455566',456576,'nn@gamil.com',NULL),
(15,11,'hana','/static/doctor_img/20230316161521.jpg','dwqwe','fvf','decd','Female','23/8/2000','dref','3214',21333,'abc@gmail.com',NULL),
(16,16,'nana','/static/doctor_img/20230329141322.jpg','swass','edr','fgyh','Female','23/8/2000','wef','3214',456576,'nn@gamil.com',13);

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `hospital_id` int(11) NOT NULL,
  `hospital_name` varchar(50) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`lid`,`hospital_id`,`hospital_name`,`photo`,`place`,`email`,`phone_no`) values 
(13,0,'bb@gmail.com','/static/hospital_image/230323-122117.jpg','uk','bb@gmail.com',1234567890);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'','',''),
(3,'','',''),
(4,'hg','ui','doctor'),
(5,'u','i','doctor'),
(10,'nn@gmail.com','1234','doctor'),
(11,'abc@gmail.com','4321','doctor'),
(12,'ss@gamil.com','456','patient'),
(13,'bb@gmail.com','123','hospital'),
(14,'nn@gamil.com','3286','doctor'),
(15,'abc@gmail.com','9672','doctor'),
(16,'nn@gamil.com','7411','doctor'),
(17,'nn@gamil.com','5288','doctor'),
(18,'\"++\"','\"++\"','\"++\"'),
(19,'\"++\"','\"++\"','\"++\"');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `medicine_name` varchar(50) DEFAULT NULL,
  `medicine_type` varchar(50) DEFAULT NULL,
  `dose` varchar(50) DEFAULT NULL,
  KEY `lid` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `medicine` */

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) NOT NULL,
  `patient_name` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone_no` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

insert  into `patient`(`lid`,`patient_id`,`patient_name`,`age`,`place`,`phone_no`,`email`,`cid`) values 
(3,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',NULL),
(1,12,'jan','44','wedef','231423547','jan@gmail.com',NULL),
(2,13,'fas','56','nb ','756545466','fas@gmail.com',NULL);

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `hospital_id` int(11) NOT NULL,
  `review` varchar(50) DEFAULT NULL,
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`lid`,`user_id`,`hospital_id`,`review`) values 
(1,0,0,'\"++\"');

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_lid` int(11) DEFAULT NULL,
  `time_from` varchar(11) DEFAULT NULL,
  `time_to` varchar(11) DEFAULT NULL,
  `date` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

insert  into `schedule`(`schedule_id`,`doc_lid`,`time_from`,`time_to`,`date`) values 
(1,0,'','',''),
(2,10,'17:11','21:11','2023-03-16'),
(5,11,'18:25','15:28','2023-03-10'),
(6,10,'14:11','18:10','2023-03-27');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `login_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `phone_no` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `Photo` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `login_id` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`login_id`,`user_id`,`user_name`,`phone_no`,`email`,`place`,`Photo`) values 
(2,1,'sinu','9876543210','sin@gamil.com','cheliya',NULL),
(12,2,'ss@gmil.com','1234567890','ss@gmail.com','dsf',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
