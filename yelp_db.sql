CREATE DATABASE yelp_db;

USE yelp_db;

CREATE TABLE `covid` (
  `covid_id` int(11) NOT NULL,
  `business_id` int(11) NOT NULL,
  `github_enabled` varchar(50) NOT NULL,
  `delivery_or_takeout` varchar(50) NOT NULL,
  `call_to_action_enabled` varchar(50) NOT NULL,
  `request_qoute_enabled` tinyint(1) NOT NULL,
  `covid_banner` varchar(100) NOT NULL,
  `temporary_closed_until` varchar(100) NOT NULL,
  `virtual_service_enabled` varchar(100) NOT NULL,
  `highlights` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `precipitation` (
  `date` date NOT NULL,
  `precipitation` int(11) NOT NULL,
  `precipitation_normal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `temperature` (
  `date` date NOT NULL,
  `temperature_min` int(11) NOT NULL,
  `temperature_max` int(11) NOT NULL,
  `normal_min` int(11) NOT NULL,
  `normal_max` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `yelp_business` (
  `business_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(500) NOT NULL,
  `attributes` varchar(100) NOT NULL,
  `categories` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(100) NOT NULL,
  `is_open` int(11) NOT NULL,
  `longitude` int(11) NOT NULL,
  `latitude` int(11) NOT NULL,
  `postal_code` int(11) NOT NULL,
  `review_count` int(11) NOT NULL,
  `hours` int(11) NOT NULL,
  `stars` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `yelp_review` (
  `business_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `review_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `cool` int(11) NOT NULL,
  `funny` int(11) NOT NULL,
  `stars` int(11) NOT NULL,
  `text` varchar(1000) NOT NULL,
  `useful` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `yelp_tip` (
  `tip_id` int(11) NOT NULL,
  `business_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `compliment_count` int(11) NOT NULL,
  `text` varchar(1000) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `yelp_user` (
  `user_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `average_stars` int(11) NOT NULL,
  `compliment_cool` int(11) NOT NULL,
  `compliment_cute` int(11) NOT NULL,
  `compliment_funny` int(11) NOT NULL,
  `compliment_hot` int(11) NOT NULL,
  `compliment_list` int(11) NOT NULL,
  `compliment_more` int(11) NOT NULL,
  `compliment_note` int(11) NOT NULL,
  `compliment_photo` int(11) NOT NULL,
  `compliment_plain` int(11) NOT NULL,
  `compliment_profile` int(11) NOT NULL,
  `compliment_writer` int(11) NOT NULL,
  `cool` int(11) NOT NULL,
  `elite` varchar(50) NOT NULL,
  `fans` int(11) NOT NULL,
  `friends` varchar(500) NOT NULL,
  `funny` int(11) NOT NULL,
  `review_count` int(11) NOT NULL,
  `useful` int(11) NOT NULL,
  `yelping_since` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE `covid`
  ADD PRIMARY KEY (`covid_id`),
  ADD KEY `covid_business_id_fk` (`business_id`);


ALTER TABLE `precipitation`
  ADD KEY `p_date_fk` (`date`);


ALTER TABLE `temperature`
  ADD KEY `t_date_fk` (`date`);


ALTER TABLE `yelp_business`
  ADD PRIMARY KEY (`business_id`);


ALTER TABLE `yelp_review`
  ADD PRIMARY KEY (`date`) USING BTREE,
  ADD KEY `review_business_id_fk` (`business_id`),
  ADD KEY `review_user_id_fk` (`user_id`);


ALTER TABLE `yelp_tip`
  ADD PRIMARY KEY (`tip_id`),
  ADD KEY `tip_business_id_fk` (`business_id`),
  ADD KEY `tip_user_id_fk` (`user_id`);


ALTER TABLE `yelp_user`
  ADD PRIMARY KEY (`user_id`);


ALTER TABLE `covid`
  ADD CONSTRAINT `covid_ibfk_1` FOREIGN KEY (`business_id`) REFERENCES `yelp_business` (`business_id`);


ALTER TABLE `precipitation`
  ADD CONSTRAINT `precipitation_ibfk_1` FOREIGN KEY (`date`) REFERENCES `yelp_review` (`date`);


ALTER TABLE `temperature`
  ADD CONSTRAINT `temperature_ibfk_1` FOREIGN KEY (`date`) REFERENCES `yelp_review` (`date`);


ALTER TABLE `yelp_review`
  ADD CONSTRAINT `yelp_review_ibfk_1` FOREIGN KEY (`business_id`) REFERENCES `yelp_business` (`business_id`),
  ADD CONSTRAINT `yelp_review_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `yelp_user` (`user_id`);


ALTER TABLE `yelp_tip`
  ADD CONSTRAINT `yelp_tip_ibfk_1` FOREIGN KEY (`business_id`) REFERENCES `yelp_business` (`business_id`),
  ADD CONSTRAINT `yelp_tip_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `yelp_user` (`user_id`);
COMMIT;