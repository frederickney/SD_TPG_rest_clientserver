/**
 *
 */
drop database if exists TPG;
create database TPG;
use TPG;
drop table if exists `users`;
create table `users`(
  `id` int(10) unsigned not null auto_increment,
  `username` varchar(32) not null,
  `password` varchar(256) not null,
  primary key(`id`, `username`),
  key (`id`)
  )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

drop table if exists `tpg_stops`;
create table `tpg_stops` (
  `id` int(10) unsigned not null auto_increment,
  `stop_name` varchar(64) not null,
  `line_numbers` set('1','2','3','4','5','6','7','8','9','10','11','12','14','15','18','19','21','22','23','25','28','31','32','33','34','35','36','41','42','43','44','45','46','47','51','53','54','57','61','A','B','C','D','Dn','E','F','G','K','L','M','O','S','T','U','V','W','X','Y','Z') not null,
  `location` POINT not null,
  `end_line` varchar(64) not null,
  `start_line` varchar(64) not null,
  primary key (`id`, `stop_name`, `location`, `direction`),
  key(`id`)
  )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
  
drop table if exists `handicaped_capabilities`;
create table `handicaped_capabilities`
(
    `line_number` varchar(2) primary key not null,
    `is_capable` tinyint default 0 not null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

drop table if exists `subscriptions`;
create table `subscriptions`(
  `user_id` int(10) unsigned not null,
  `stop_id` int(10) unsigned not null,
  primary key(`user_id`, `stop_id`),
  foreign key(`user_id`) references `users` (`id`) on update cascade,
  foreign key(`stop_id`) references `tpg_stops` (`id`) on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

drop table if exists `horaire`;
create table `horaire`(
  `stop_id` int(10) unsigned not null,
  `ligne_number` varchar(2) not null,
  `line_horaire` time not null,
  primary key(`ligne_number` , `line_horaire`),
  foreign key(`stop_id`) references `tpg_stops` (`id`) on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
