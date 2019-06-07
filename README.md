# Sentiment-Analysis-Using-Facebook-FastText
Sentiment analysis of Amazon Reviews for any particular product using Facebook FastText. I cann't attach the data we have, but below is the table schema you can consider in your project.


# Products Table:
CREATE TABLE `products` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`model` VARCHAR(250) NOT NULL,
	`asin_code` VARCHAR(250) NULL DEFAULT NULL,
	`product_title` VARCHAR(250) NULL DEFAULT NULL,
	`category` VARCHAR(250) NULL DEFAULT NULL,
	`subcategory` VARCHAR(250) NULL DEFAULT NULL,
	`dimensions` TEXT NULL,
	`product_uri` TEXT NOT NULL,
	`msrp` FLOAT NULL DEFAULT '0',
	`manufacturer` VARCHAR(50) NULL DEFAULT NULL,
	`description` TEXT NULL,
	`file_name` VARCHAR(250) NULL DEFAULT NULL,
	`is_processed` TINYINT(4) NOT NULL DEFAULT '0',
	`feat_tag` TINYINT(4) NOT NULL DEFAULT '0',
	`es_flag` TINYINT(4) NOT NULL DEFAULT '0',
	`summary_tag` TINYINT(4) NOT NULL DEFAULT '0',
	`date_added` DATE NULL DEFAULT NULL,
	`search_tag` VARCHAR(250) NULL DEFAULT NULL,
	`no_of_reviews` FLOAT(30,0) NULL DEFAULT '0',
	`review_url` TEXT NULL,
	`image_url` TEXT NULL,
	`s3_image_url` TEXT NULL,
	`youtube_url` TEXT NULL,
	`fourm_problem1` LONGTEXT NULL,
	`fourm_problem2` LONGTEXT NULL,
	`feature1` TEXT NULL,
	`feature2` TEXT NULL,
	`feature3` TEXT NULL,
	`feature4` TEXT NULL,
	`feature5` TEXT NULL,
	`feature6` TEXT NULL,
	`s3_input_url` TEXT NULL,
	`s3_output_url` TEXT NULL,
	`summary_url` TEXT NULL,
	`buy_url` TEXT NULL,
	`image_snippet` TEXT NULL,
	`wp_post_id` BIGINT(20) NOT NULL DEFAULT '0',
	`s3_input_flag` TINYINT(4) NULL DEFAULT '0',
	`rt_is_processed` TINYINT(4) NULL DEFAULT '0',
	`wc_is_processed` TINYINT(4) NULL DEFAULT '0',
	`image_processed` TINYINT(4) NULL DEFAULT '0',
	`full_name` VARCHAR(500) NOT NULL DEFAULT 'None',
	`product_feature` VARCHAR(500) NULL DEFAULT NULL,
	`es_id` VARCHAR(500) NULL DEFAULT NULL,
	`word_freq` TEXT NULL,
	`feature_confidence` VARCHAR(500) NULL DEFAULT NULL,
	`review_process_flag` VARCHAR(50) NOT NULL DEFAULT 'Pending',
	`word_freq_flag` TINYINT(4) NOT NULL DEFAULT '0',
	`full_name_flag` TINYINT(4) NULL DEFAULT '0',
	`post_update_flag` TINYINT(4) NOT NULL DEFAULT '0',
	`catg_is_processed` TINYINT(4) NOT NULL DEFAULT '0',
	`es_upload` TINYINT(4) NOT NULL DEFAULT '0',
	`overall_score` FLOAT(255,0) NULL DEFAULT NULL,
	`subcategory_processed` TINYINT(4) NULL DEFAULT '0',
	`rank` TINYINT(4) NULL DEFAULT NULL,
	`delete_flag` TINYINT(4) NULL DEFAULT '0',
	`score_out_of_10` FLOAT NULL DEFAULT NULL,
	`updated_on` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`affiliate_processed` INT(11) NULL DEFAULT NULL,
	`flag_done` TINYINT(4) NULL DEFAULT '0',
	`prdct_read` TINYINT(4) NULL DEFAULT '0',
	PRIMARY KEY (`id`, `wp_post_id`) USING BTREE,
	INDEX `id` (`id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;

# Product Reviews
CREATE TABLE `product_reviews` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`product_id` BIGINT(20) NULL DEFAULT NULL,
	`review_text` TEXT NOT NULL,
	`review_title` TEXT NULL,
	`review_date` DATE NOT NULL DEFAULT '0000-00-00',
	`date_of_review` VARCHAR(50) NOT NULL DEFAULT '0' COLLATE 'utf8_unicode_ci',
	`reviewer` VARCHAR(50) NULL DEFAULT '0',
	`rating` FLOAT NOT NULL DEFAULT '0',
	`helpfulness` VARCHAR(50) NULL DEFAULT '0',
	`full_review_text` TEXT NULL,
	`update_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_processed` TINYINT(4) NOT NULL DEFAULT '0',
	`feat_flag` TINYINT(4) NOT NULL DEFAULT '0',
	`sentence_tokenize_flag` TINYINT(4) NULL DEFAULT '0',
	`manual_taging` TINYINT(4) NULL DEFAULT '0',
	`weightage_duration` FLOAT NOT NULL DEFAULT '0',
	`manual_in_progress` TINYINT(4) NULL DEFAULT '0',
	`taxonomy_flag` TINYINT(4) NULL DEFAULT '0',
	`sentence_tokenize_flagCopy` TINYINT(4) NULL DEFAULT '0',
	`pretrained_sentiment_flag` TINYINT(4) NULL DEFAULT '0',
	PRIMARY KEY (`id`),
	INDEX `review_index` (`id`, `product_id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;

# Product Review Sentiment
CREATE TABLE `product_reviews_sentiments` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`date_created` DATE NOT NULL DEFAULT '0000-00-00',
	`review_id` BIGINT(20) NOT NULL,
	`positive` FLOAT NOT NULL,
	`negative` FLOAT NOT NULL,
	`mixed` FLOAT NOT NULL,
	`neutral` FLOAT NOT NULL,
	`nss` FLOAT NOT NULL,
	`weighted_positive` FLOAT NOT NULL,
	`weighted_negative` FLOAT NOT NULL,
	`final_score` INT(11) NOT NULL,
	`confidence_level` DECIMAL(10,4) NOT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;
