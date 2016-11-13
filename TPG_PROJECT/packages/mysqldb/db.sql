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
  `password` varchar(512) not null,
  `logged`  TINYINT not null,
  primary key(`id`, `username`),
  key (`id`)
  )ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

drop table if exists `subscriptions`;
create table `subscriptions`(
  `user_id` int(10) unsigned not null,
  `stop_id` varchar(4) not null,
  primary key(`user_id`, `stop_id`),
  foreign key(`user_id`) references `users` (`id`) on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;