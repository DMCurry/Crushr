-- MySQL dump 10.13  Distrib 9.0.1, for macos14.7 (arm64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('62aad929d98a');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analytics`
--

DROP TABLE IF EXISTS `analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `performance_test_id` int NOT NULL,
  `performance_test_result` float NOT NULL,
  `test_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `performance_test_id` (`performance_test_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `analytics_ibfk_1` FOREIGN KEY (`performance_test_id`) REFERENCES `performance_test` (`id`),
  CONSTRAINT `analytics_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analytics`
--

LOCK TABLES `analytics` WRITE;
/*!40000 ALTER TABLE `analytics` DISABLE KEYS */;
INSERT INTO `analytics` VALUES (1,1001,1,3.3,'2025-01-01'),(2,1001,1,10.21,'2025-01-23'),(3,1001,2,9,'2025-01-15');
/*!40000 ALTER TABLE `analytics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercise`
--

DROP TABLE IF EXISTS `exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercise` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exercise_name` varchar(30) NOT NULL,
  `description` text,
  `reps` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `exercise_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercise`
--

LOCK TABLES `exercise` WRITE;
/*!40000 ALTER TABLE `exercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `performance_test`
--

DROP TABLE IF EXISTS `performance_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `performance_test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `test_name` varchar(30) NOT NULL,
  `performance_value` float NOT NULL,
  `description` text,
  `training_plan_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `training_plan_id` (`training_plan_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `performance_test_ibfk_1` FOREIGN KEY (`training_plan_id`) REFERENCES `training_plan` (`id`),
  CONSTRAINT `performance_test_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `performance_test`
--

LOCK TABLES `performance_test` WRITE;
/*!40000 ALTER TABLE `performance_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `performance_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `training_exercise`
--

DROP TABLE IF EXISTS `training_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training_exercise` (
  `training_plan_id` int NOT NULL,
  `exercise_id` int NOT NULL,
  PRIMARY KEY (`training_plan_id`,`exercise_id`),
  KEY `exercise_id` (`exercise_id`),
  CONSTRAINT `training_exercise_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`),
  CONSTRAINT `training_exercise_ibfk_2` FOREIGN KEY (`training_plan_id`) REFERENCES `training_plan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training_exercise`
--

LOCK TABLES `training_exercise` WRITE;
/*!40000 ALTER TABLE `training_exercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `training_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `training_plan`
--

DROP TABLE IF EXISTS `training_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training_plan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plan_name` varchar(30) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `training_plan_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training_plan`
--

LOCK TABLES `training_plan` WRITE;
/*!40000 ALTER TABLE `training_plan` DISABLE KEYS */;
/*!40000 ALTER TABLE `training_plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `hashed_password` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weekly_schedule`
--

DROP TABLE IF EXISTS `weekly_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weekly_schedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `day` enum('MON','TUE','WED','THU','FRI','SAT','SUN') NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `weekly_schedule_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weekly_schedule`
--

LOCK TABLES `weekly_schedule` WRITE;
/*!40000 ALTER TABLE `weekly_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `weekly_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weekly_schedule_exercise`
--

DROP TABLE IF EXISTS `weekly_schedule_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weekly_schedule_exercise` (
  `weekly_schedule_id` int DEFAULT NULL,
  `exercise_id` int DEFAULT NULL,
  KEY `exercise_id` (`exercise_id`),
  KEY `weekly_schedule_id` (`weekly_schedule_id`),
  CONSTRAINT `weekly_schedule_exercise_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`),
  CONSTRAINT `weekly_schedule_exercise_ibfk_2` FOREIGN KEY (`weekly_schedule_id`) REFERENCES `weekly_schedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weekly_schedule_exercise`
--

LOCK TABLES `weekly_schedule_exercise` WRITE;
/*!40000 ALTER TABLE `weekly_schedule_exercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `weekly_schedule_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weekly_schedule_performance_test`
--

DROP TABLE IF EXISTS `weekly_schedule_performance_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weekly_schedule_performance_test` (
  `weekly_schedule_id` int DEFAULT NULL,
  `performance_test_id` int DEFAULT NULL,
  KEY `performance_test_id` (`performance_test_id`),
  KEY `weekly_schedule_id` (`weekly_schedule_id`),
  CONSTRAINT `weekly_schedule_performance_test_ibfk_1` FOREIGN KEY (`performance_test_id`) REFERENCES `performance_test` (`id`),
  CONSTRAINT `weekly_schedule_performance_test_ibfk_2` FOREIGN KEY (`weekly_schedule_id`) REFERENCES `weekly_schedule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weekly_schedule_performance_test`
--

LOCK TABLES `weekly_schedule_performance_test` WRITE;
/*!40000 ALTER TABLE `weekly_schedule_performance_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `weekly_schedule_performance_test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-01 15:54:35
