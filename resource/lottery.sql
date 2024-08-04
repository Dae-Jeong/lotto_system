create database lottery;

use lottery;

drop table if exists lottery;
create table lottery (
    round_number int primary key,
    draw_date date not null,
    winning_numbers varchar(36) not null,
    bonus_number int not null,
    created_dt timestamp default current_timestamp
);

drop table if exists purchased_lottery;
create table purchased_lottery (
    purchased_lottery_id varchar(100) primary key,
    round_number int not null ,
    winning_numbers varchar(100) not null,
    bonus_number int not null,
    created_dt timestamp default current_timestamp
);