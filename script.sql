CREATE TABLE `aliment` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nom` varchar(100) NOT NULL,
  `marque` varchar(100) DEFAULT NULL,
  `sucre` float DEFAULT NULL,
  `calories` int NOT NULL,
  `graisses` float DEFAULT NULL,
  `proteines` float DEFAULT NULL
);

CREATE TABLE `langue` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nom` varchar(100) NOT NULL,
  `code` varchar(100) NOT NULL
);