-- Adminer 4.8.1 MySQL 8.2.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `Adresse`;
CREATE TABLE `Adresse` (
  `id_N_Adresse` int NOT NULL AUTO_INCREMENT,
  `id_N_Batiment` int NOT NULL,
  `id_CP` int NOT NULL,
  `id_cmplt_rue` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_VIlle` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Nom_rue` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Utilisateur` int NOT NULL,
  PRIMARY KEY (`id_N_Adresse`),
  KEY `id_Utilisateur` (`id_Utilisateur`),
  CONSTRAINT `Adresse_ibfk_1` FOREIGN KEY (`id_Utilisateur`) REFERENCES `Compte` (`id_Utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Adresse` (`id_N_Adresse`, `id_N_Batiment`, `id_CP`, `id_cmplt_rue`, `id_VIlle`, `id_Nom_rue`, `id_Utilisateur`) VALUES
(3,	30,	35470,	'',	'Bain-de-bretagne',	'Rue des résistants',	4);

DROP TABLE IF EXISTS `Compte`;
CREATE TABLE `Compte` (
  `id_Utilisateur` int NOT NULL AUTO_INCREMENT,
  `id_Mail` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `Num_tel` int NOT NULL,
  `id_Nom` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Prenom` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_Nom_societee` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_Mdp` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id_Type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_Utilisateur`),
  UNIQUE KEY `id_Mail` (`id_Mail`),
  UNIQUE KEY `Num_tel` (`Num_tel`),
  KEY `id_Type` (`id_Type`),
  CONSTRAINT `Compte_ibfk_1` FOREIGN KEY (`id_Type`) REFERENCES `id_Roles` (`id_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Compte` (`id_Utilisateur`, `id_Mail`, `Num_tel`, `id_Nom`, `id_Prenom`, `id_Nom_societee`, `id_Mdp`, `id_Type`) VALUES
(4,	'PB.Importation@gmail.com',	664410748,	'Paimblanc',	'',	'',	'$2b$12$xRX3npaO.RMCW7bYtKA7derXhuYs1lb8rlc5oYHCfRu5n.nRbus8S',	'ADMIN'),
(5,	'paimblancleo@orange.fr',	664410749,	'Paimblanc',	'Léo',	'',	'$2b$12$/mst/TsSdhDvQ0EuI8CfEehtMKuhlvntGpH/P6dQnRkA31FecYuO.',	'EMPLOYE');

DROP TABLE IF EXISTS `Demande`;
CREATE TABLE `Demande` (
  `id_Demande` int NOT NULL AUTO_INCREMENT,
  `id_Marque` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Serie` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Moteur` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Boite` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id_Puissance` text COLLATE utf8mb4_general_ci,
  `id_KM_max` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `id_Budget` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `id_Annee` text COLLATE utf8mb4_general_ci,
  `id_Options` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_Description` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_Utilisateur` int NOT NULL,
  `id_Type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Etat` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_Demande`),
  KEY `id_Utilisateur` (`id_Utilisateur`),
  KEY `id_Type` (`id_Type`),
  KEY `id_Etat` (`id_Etat`),
  CONSTRAINT `Demande_ibfk_1` FOREIGN KEY (`id_Utilisateur`) REFERENCES `Compte` (`id_Utilisateur`),
  CONSTRAINT `Demande_ibfk_2` FOREIGN KEY (`id_Type`) REFERENCES `id_Prestation` (`id_Type`),
  CONSTRAINT `Demande_ibfk_3` FOREIGN KEY (`id_Etat`) REFERENCES `id_Status` (`id_Etat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Demande` (`id_Demande`, `id_Marque`, `id_Serie`, `id_Moteur`, `id_Boite`, `id_Puissance`, `id_KM_max`, `id_Budget`, `id_Annee`, `id_Options`, `id_Description`, `id_Utilisateur`, `id_Type`, `id_Etat`) VALUES
(7,	'BMW',	'SERIE 1',	'Hybride',	'Automatique',	NULL,	NULL,	NULL,	NULL,	NULL,	NULL,	4,	'Importation_complète',	'En_attente'),
(8,	'BMW',	'SERIE 1',	'Hybride',	'Manuel',	NULL,	NULL,	'20000€',	'2007-2012',	'TO',	'ROUGE',	4,	'Importation_complète',	'En_attente'),
(9,	'BMW',	'SERIE 1',	'Diesel',	'Automatique',	NULL,	NULL,	'20000€',	'2007-2012',	'TO',	'ROUGE',	4,	'Importation_complète',	'En_attente'),
(10,	'BMW',	'SERIE 1',	'Essence',	'Automatique',	'500',	NULL,	'',	'',	'',	'',	4,	'Importation_complète',	'En_attente'),
(11,	'audi',	'rs3',	'Essence',	'Automatique',	'850',	'206000',	'50 000€',	'2020',	'TO',	'gris nardo',	4,	'Importation_complète',	'En_attente'),
(12,	'Ferrari',	'348',	'Essence',	'Automatique',	'500',	'157000',	'70 000',	'1991',	'ts',	'ROUGE',	5,	'gestion_administrative',	'En_attente'),
(13,	'BMW',	'130i',	'Essence',	'Manuel',	'370',	'139000',	'20000€',	'2007-2012',	'TO',	'gris nardo',	5,	'WW_provisoire',	'En_attente'),
(14,	'BMW',	'SERIE 1',	'Essence',	'Automatique',	'290',	'180000',	'',	'',	'',	'',	4,	'WW_provisoire',	'En_attente');

DROP TABLE IF EXISTS `id_Prestation`;
CREATE TABLE `id_Prestation` (
  `id_Type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `id_Prestation` (`id_Type`) VALUES
('gestion_administrative'),
('Importation_complète'),
('WW_provisoire');

DROP TABLE IF EXISTS `id_Roles`;
CREATE TABLE `id_Roles` (
  `id_Type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `id_Roles` (`id_Type`) VALUES
('ADMIN'),
('EMPLOYE'),
('UTILISATEUR');

DROP TABLE IF EXISTS `id_Status`;
CREATE TABLE `id_Status` (
  `id_Etat` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_Etat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `id_Status` (`id_Etat`) VALUES
('En_attente'),
('En_cours'),
('Terminé');

DROP TABLE IF EXISTS `id_Vitrine`;
CREATE TABLE `id_Vitrine` (
  `id_N_Vitrine` int NOT NULL,
  `id_pourcentage_gagne` int NOT NULL,
  `id_Lien_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `id_Duree_import` int NOT NULL,
  `id_Demande` int NOT NULL,
  PRIMARY KEY (`id_N_Vitrine`),
  UNIQUE KEY `id_Demande` (`id_Demande`),
  UNIQUE KEY `id_Lien_image` (`id_Lien_image`),
  CONSTRAINT `id_Vitrine_ibfk_1` FOREIGN KEY (`id_Demande`) REFERENCES `Demande` (`id_Demande`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `id_fidelitee`;
CREATE TABLE `id_fidelitee` (
  `id_dossier_clot` int NOT NULL,
  `id_Utilisateur` int NOT NULL,
  PRIMARY KEY (`id_dossier_clot`),
  KEY `id_Utilisateur` (`id_Utilisateur`),
  CONSTRAINT `id_fidelitee_ibfk_1` FOREIGN KEY (`id_Utilisateur`) REFERENCES `Compte` (`id_Utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- 2025-05-18 09:16:48
