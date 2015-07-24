drop database if exists Restaurant;
create database Restaurant;
use Restaurant;



drop table if exists Restaurant_Entry;
create table Restaurant_Entry( RE_id int not null auto_increment,RE_name varchar(100) not null,RE_address varchar(100) not null,RE_phoneNumber varchar(100) not null,RE_rating int not null, RE_description varchar(500) default null,primary key(RE_id) );

drop table if exists Restaurant_Menu;
create table Restaurant_Menu(RM_id int not null auto_increment,RM_REid int not null,RM_dish varchar(100) not null,RM_price int not null,RM_description varchar(500) default null,primary key(RM_id),foreign key(RM_REid) references Restaurant_Entry(RE_id));
