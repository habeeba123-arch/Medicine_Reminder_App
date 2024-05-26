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

/*Table structure for table `care_taker` */

DROP TABLE IF EXISTS `care_taker`;

CREATE TABLE `care_taker` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `caretaker_id` int(11) NOT NULL,
  `caretaker_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`caretaker_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `care_taker` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `replay` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

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
  PRIMARY KEY (`doc_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`doc_id`,`lid`,`doc_name`,`photo`,`department`,`experience`,`qualification`,`gender`,`DOB`,`place`,`pin`,`phno`,`email`) values 
(8,4,'','','','','','','','','',NULL,NULL),
(11,3,'nana',NULL,'ENT','3year','md','female','23/3/1986','hhhaa','234245',NULL,NULL),
(12,0,'','','','','','','','','',0,''),
(13,0,'','','','','','','','','',0,''),
(14,10,'nana','/static/doctor_img/20230316165102.jpg','swass','edr','fgyh','Male','23/8/2000','jn','455566',456576,'nn@gamil.com'),
(15,11,'hana','/static/doctor_img/20230316161521.jpg','dwqwe','fvf','decd','Female','23/8/2000','dref','3214',21333,'abc@gmail.com');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'','',''),
(3,'','',''),
(4,'hg','ui','doctor'),
(5,'u','i','doctor'),
(10,'nn@gmail.com','1234','doctor'),
(11,'abc@gmail.com','321','doctor');

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
  PRIMARY KEY (`patient_id`),
  KEY `lid` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `hospital_id` int(11) NOT NULL,
  `review` varchar(50) DEFAULT NULL,
  KEY `lid` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `review` */

/*Table structure for table `schedule` */

DROP TABLE IF EXISTS `schedule`;

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_lid` int(11) DEFAULT NULL,
  `time_from` varchar(11) DEFAULT NULL,
  `time_to` varchar(11) DEFAULT NULL,
  `date` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `schedule` */

insert  into `schedule`(`schedule_id`,`doc_lid`,`time_from`,`time_to`,`date`) values 
(1,0,'','',''),
(2,10,'17:11','21:11','2023-03-16');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`login_id`,`user_id`,`user_name`,`phone_no`,`email`,`place`,`Photo`) values 
(2,1,'sinu','9876543210','sin@gamil.com','cheliya',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
