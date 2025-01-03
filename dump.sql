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
  `training_plan_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `training_plan_id` (`training_plan_id`),
  CONSTRAINT `exercise_ibfk_1` FOREIGN KEY (`training_plan_id`) REFERENCES `training_plan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercise`
--

LOCK TABLES `exercise` WRITE;
/*!40000 ALTER TABLE `exercise` DISABLE KEYS */;
INSERT INTO `exercise` VALUES (1,'Push-Up','Push-up exercise for chest and triceps.',15,1),(2,'Sit-Up','Sit-ups for abdominal muscles.',20,2),(3,'Pull-Up','Pull-ups for back and biceps.',10,3),(4,'Squat','Squats for legs and glutes.',12,1),(5,'Lunge','Lunges for legs and balance.',10,NULL),(6,'Bicep Curl','Bicep curls for arm strength.',15,2),(7,'Tricep Dip','Tricep dips for arm toning.',12,3),(8,'Plank','Plank for core stability.',1,1),(9,'Mountain Climber','Mountain climbers for cardio.',20,2),(10,'Burpee','Burpees for full-body workout.',10,3),(11,'Deadlift','Deadlifts for back and leg strength.',8,NULL),(12,'Overhead Press','Overhead press for shoulders.',12,1),(13,'Crunch','Crunches for abs.',15,2),(14,'Step-Up','Step-ups for legs and cardio.',10,3),(15,'Russian Twist','Russian twists for obliques.',20,NULL),(16,'Calf Raise','Calf raises for lower legs.',15,1),(17,'Leg Raise','Leg raises for lower abs.',12,2),(18,'Bench Press','Bench press for chest.',10,3),(19,'Dumbbell Row','Dumbbell rows for back.',10,NULL),(20,'Jumping Jack','Jumping jacks for warm-up.',30,1);
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
  PRIMARY KEY (`id`),
  KEY `training_plan_id` (`training_plan_id`),
  CONSTRAINT `performance_test_ibfk_1` FOREIGN KEY (`training_plan_id`) REFERENCES `training_plan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `performance_test`
--

LOCK TABLES `performance_test` WRITE;
/*!40000 ALTER TABLE `performance_test` DISABLE KEYS */;
INSERT INTO `performance_test` VALUES (1,'Strength Test',75.5,'Measures overall strength using a combination of push-ups, squats, and deadlifts.',1),(2,'Cardio Endurance Test',85,'Evaluates stamina and cardiovascular efficiency through timed runs and cycling.',2),(3,'Full-Body Assessment',92.3,'Comprehensive test including flexibility, strength, and endurance metrics.',3);
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
  CONSTRAINT `training_exercise_ibfk_1` FOREIGN KEY (`training_plan_id`) REFERENCES `training_plan` (`id`),
  CONSTRAINT `training_exercise_ibfk_2` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`)
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training_plan`
--

LOCK TABLES `training_plan` WRITE;
/*!40000 ALTER TABLE `training_plan` DISABLE KEYS */;
INSERT INTO `training_plan` VALUES (1,'Beginner Strength Training',1001),(2,'Intermediate Cardio',1002),(3,'Advanced Full-Body Workout',1003);
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
  `hashed_password` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1004 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1001,'beginner_user','5f4dcc3b5aa765d61d8327deb882cf99'),(1002,'intermediate_user','e99a18c428cb38d5f260853678922e03'),(1003,'advanced_user','098f6bcd4621d373cade4e832627b4f6');
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
  `day` enum('MON','TUE','WED','THU','FRI') NOT NULL,
  `exercise_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exercise_id` (`exercise_id`),
  CONSTRAINT `weekly_schedule_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weekly_schedule`
--

LOCK TABLES `weekly_schedule` WRITE;
/*!40000 ALTER TABLE `weekly_schedule` DISABLE KEYS */;
INSERT INTO `weekly_schedule` VALUES (1,'MON',2),(2,'TUE',5),(3,'WED',3);
/*!40000 ALTER TABLE `weekly_schedule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-02 18:14:01
