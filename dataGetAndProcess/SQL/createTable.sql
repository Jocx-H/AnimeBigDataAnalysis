/*
 Navicat Premium Data Transfer

 Source Server         : CentOS
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : bigdataproject

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 24/06/2022 10:38:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `uid` int(0) NOT NULL,
  `uname` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  INDEX `uid`(`uid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for anime
-- ----------------------------
DROP TABLE IF EXISTS `anime`;
CREATE TABLE `anime`  (
  `aid` int(0) NOT NULL,
  `title` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `index_show` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_finished` tinyint(1) NULL DEFAULT NULL,
  `video_link` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cover` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pub_real_time` bigint(0) NULL DEFAULT NULL,
  `renewal_time` bigint(0) NULL DEFAULT NULL,
  `favorites` int(0) NULL DEFAULT NULL,
  `coins` int(0) NULL DEFAULT NULL,
  `views` int(0) NULL DEFAULT NULL,
  `danmakus` int(0) NULL DEFAULT NULL,
  `depth` int(0) NULL DEFAULT NULL,
  `media_tags` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` float NULL DEFAULT NULL,
  `cm_count` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `introduce` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`aid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comic
-- ----------------------------
DROP TABLE IF EXISTS `comic`;
CREATE TABLE `comic`  (
  `cid` int(0) NOT NULL,
  `url` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cover` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `last_short_title` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `author` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `state` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for novel
-- ----------------------------

create table novel
(
    `nid`         int          not null
        primary key,
    `url`         varchar(256) null,
    `cover`       varchar(256) null,
    `title`       varchar(256)  null,
    `author`      varchar(32)  null,
    `score`       float        null,
    `type`        varchar(64)  null,
    `depth`       int          null,
    `state`       varchar(32)  null,
    `click_cnt`   int          null,
    `update_time` date         null,
    `introduce`   varchar(512) null
);


SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cosplay
-- ----------------------------
DROP TABLE IF EXISTS `cosplay`;
CREATE TABLE `cosplay`  (
  `cosid` int(0) NOT NULL,
  `url` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cover` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cosid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for useranimehistory
-- ----------------------------
DROP TABLE IF EXISTS `useranimehistory`;
CREATE TABLE `useranimehistory`  (
  `ahid` int(0) NOT NULL,
  `uid` int(0) NULL DEFAULT NULL,
  `aid` int(0) NULL DEFAULT NULL,
  `score` float NULL DEFAULT NULL,
  `ratio` float NULL DEFAULT NULL,
  `thumb` tinyint(1) NULL DEFAULT NULL,
  `collect` tinyint(1) NULL DEFAULT NULL,
  `time` bigint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ahid`) USING BTREE,
  INDEX `uid`(`uid`) USING BTREE,
  INDEX `aid`(`aid`) USING BTREE,
  CONSTRAINT `useranimehistory_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `useranimehistory_ibfk_2` FOREIGN KEY (`aid`) REFERENCES `anime` (`aid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for usercomichistory
-- ----------------------------
DROP TABLE IF EXISTS `usercomichistory`;
CREATE TABLE `usercomichistory`  (
  `chid` int(0) NOT NULL,
  `uid` int(0) NULL DEFAULT NULL,
  `cid` int(0) NULL DEFAULT NULL,
  `score` float NULL DEFAULT NULL,
  `ratio` float NULL DEFAULT NULL,
  `thumb` tinyint(1) NULL DEFAULT NULL,
  `collect` tinyint(1) NULL DEFAULT NULL,
  `time` bigint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`chid`) USING BTREE,
  INDEX `uid`(`uid`) USING BTREE,
  INDEX `cid`(`cid`) USING BTREE,
  CONSTRAINT `usercomichistory_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `usercomichistory_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `comic` (`cid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

create table UserCosplayHistory
(
    `coshid`    int        not null,
    `uid`       int        null,
    `cosid`     int        null,
    `score`     float      null,
    `ratio`     float      null,
    `thumb`    tinyint(1) null,
    `collect`   tinyint(1) null,
    `time` date       null,
    constraint UserCosplayHistory_pk
        primary key (coshid),
    constraint UserCosplayHistory___fk1
        foreign key (`uid`) references user (`uid`),
    constraint UserCosplayHistory___fk2
        foreign key (cosid) references cosplay (cosid)
);


create table UserNovelHistory
(
    `nhid`    int        not null,
    `uid`      int        null,
    `nid`     int        null,
    `score`     float      null,
    `ratio`     float      null,
    `thumb`    tinyint(1) null,
    `collect`   tinyint(1) null,
    `time` date       null,
    constraint UserNovelHistory_pk
        primary key (nhid),
    constraint UserNovelHistory___fk1
        foreign key (`uid`) references user (`uid`),
    constraint UserNovelHistory___fk2
        foreign key (nid) references novel (nid)
);
