doubanTop250
Crawling doubanTop250 movies

需要的第三方的库 pymysql
mysql的配置在/pipelines.py中
doubanMoives的表结构如下：
CREATE TABLE `doubanMoives` (
  `moive_guid` varchar(36) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `rate_number` varchar(20) DEFAULT NULL,
  `details` varchar(2000) DEFAULT NULL,
  `famous_words` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`moive_guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
