-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: escola
-- ------------------------------------------------------
-- Server version	8.0.38

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aluno`
--

DROP TABLE IF EXISTS `aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno` (
  `matriculaAluno` int NOT NULL AUTO_INCREMENT,
  `cpfAluno` char(11) NOT NULL,
  `nomeAluno` varchar(255) NOT NULL,
  `enderecoAluno` varchar(255) DEFAULT 'Sem Endereço',
  `telefoneAluno` char(11) DEFAULT '0000000000',
  `anoNascAluno` year NOT NULL,
  `nacionalidadealuno` varchar(45) DEFAULT 'Brasileiro',
  PRIMARY KEY (`matriculaAluno`),
  UNIQUE KEY `cpfAluno_UNIQUE` (`cpfAluno`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aluno`
--

LOCK TABLES `aluno` WRITE;
/*!40000 ALTER TABLE `aluno` DISABLE KEYS */;
INSERT INTO `aluno` VALUES (1,'1234567','Maria','Rua A','1234123',2000,'Brasileiro'),(3,'124544','Jorge','Rua C','1342345',2010,'Béligoc'),(7,'123456789','Marquinhos','Rua D','4321231',2005,'Béligoc'),(8,'1','Marcos','Endereço Não Cadastrado','0000000000',1995,'Béligoc'),(9,'2','Josefina','Endereço Não Cadastrado','0000000000',0000,'Brasileiro'),(10,'3','Manoel','Rua E','0000000000',2010,'Brasileiro'),(12,'5','Beltrano','Endereço Não Cadastrado','0000000000',1999,'Béligoc'),(13,'6','Ciclano','Endereço Não Cadastrado','0000000000',2007,'Béligoc'),(14,'11122233344','João Silva','Rua das Flores, 123','11987654321',2002,'Béligoc'),(15,'22233344455','Maria Santos','Av. Principal, 456','21999998888',2003,'Béligoc'),(16,'33344455566','Pedro Oliveira','Travessa dos Sonhos, 789','31777776666',2002,'Béligoc'),(17,'44455566677','Ana Souza','Alameda das Águias, 321','41555554444',2005,'Brasileiro'),(18,'55566677788','Carlos Lima','Rua dos Pássaros, 987','51333332222',2002,'Béligoc'),(19,'66677788899','Mariana Costa','Av. das Estrelas, 654','62111110000',2003,'Béligoc'),(20,'77788899900','Lucas Pereira','Praça das Árvores, 234','71888889999',2002,'Béligoc'),(21,'88899900011','Juliana Oliveira','Rua dos Girassóis, 876','81222223333',2001,'Béligoc'),(22,'99900011122','Fernando Martins','Av. das Rosas, 567','91444445555',2003,'Béligoc'),(23,'00011122233','Vanessa Silva','Alameda dos Ipês, 345','99666667777',2002,'Béligoc'),(24,'056984515','João Silva','Rua Triangulo','44028922',2009,'Brasileiro'),(25,'987894568','Marquinho Meire','Endereço Não Cadastrado','0000000000',2015,'Brasileiro');
/*!40000 ALTER TABLE `aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina` (
  `codDIsciplina` int NOT NULL AUTO_INCREMENT,
  `nomeDisciplina` varchar(255) NOT NULL,
  `codCurso` int NOT NULL,
  PRIMARY KEY (`codDIsciplina`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina`
--

LOCK TABLES `disciplina` WRITE;
/*!40000 ALTER TABLE `disciplina` DISABLE KEYS */;
/*!40000 ALTER TABLE `disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matricula`
--

DROP TABLE IF EXISTS `matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matricula` (
  `registroMatricula` int NOT NULL AUTO_INCREMENT,
  `matriculaAluno` int NOT NULL,
  `codDisciplina` int NOT NULL,
  `semestreMatricula` int NOT NULL,
  `anoMatricula` year NOT NULL,
  `notaMatricula` decimal(4,2) DEFAULT '0.00',
  `faltasMatricula` int DEFAULT '0',
  PRIMARY KEY (`registroMatricula`),
  KEY `fk_aluno_idx` (`matriculaAluno`),
  CONSTRAINT `fk_aluno` FOREIGN KEY (`matriculaAluno`) REFERENCES `aluno` (`matriculaAluno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matricula`
--

LOCK TABLES `matricula` WRITE;
/*!40000 ALTER TABLE `matricula` DISABLE KEYS */;
/*!40000 ALTER TABLE `matricula` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-02 10:53:31
