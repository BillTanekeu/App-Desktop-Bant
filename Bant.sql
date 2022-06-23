-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 09 juin 2022 à 10:19
-- Version du serveur : 10.4.19-MariaDB
-- Version de PHP : 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Bant`
--

-- --------------------------------------------------------

--
-- Structure de la table `amphi`
--

CREATE TABLE `amphi` (
  `id_amphi` int(8) NOT NULL,
  `nom_amphi` varchar(16) NOT NULL,
  `capacite_amphi` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `amphi`
--

INSERT INTO `amphi` (`id_amphi`, `nom_amphi`, `capacite_amphi`) VALUES
(1, 'A1001', 1500),
(2, 'A1002', 1500),
(3, 'A350', 350),
(4, 'A502', 500),
(5, 'A3', 250),
(6, 'A2', 150),
(7, 'A1', 100),
(8, 'R101', 100),
(9, 'R102', 100),
(10, 'R103', 100),
(11, 'R103', 100),
(12, 'R104', 100),
(13, 'R105', 100),
(14, 'R106', 100),
(15, 'R107', 100),
(16, 'R108', 100),
(17, 'R109', 100),
(18, 'R110', 100),
(19, 'A501', 500),
(20, 'S006', 100),
(21, 'S008', 200),
(22, 'A250', 250),
(23, 'A135', 135),
(24, 'S003', 100);

-- --------------------------------------------------------

--
-- Structure de la table `cellule`
--

CREATE TABLE `cellule` (
  `id_cellule` int(11) NOT NULL,
  `id_emploi` int(11) NOT NULL,
  `nom_matiere` varchar(20) NOT NULL,
  `nom_amphi` varchar(20) NOT NULL,
  `nom_enseignant` varchar(30) NOT NULL,
  `horaire` varchar(30) NOT NULL,
  `jour` varchar(15) NOT NULL,
  `cle` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `cellule`
--

INSERT INTO `cellule` (`id_cellule`, `id_emploi`, `nom_matiere`, `nom_amphi`, `nom_enseignant`, `horaire`, `jour`, `cle`) VALUES
(16, 1, 'INF 112', 'A502', 'TAPAMO', '07h05-9h15', 'Lundi', 11),
(17, 1, 'INF 122', 'A502', 'MELATAGIA', '10h05-12h55', 'Lundi', 21),
(18, 1, 'INF 142', 'A502', 'KOUOKAM', '07h05-9h15', 'Mardi', 12),
(19, 1, 'INF 152', 'A502', 'MESSI', '07h05-9h15', 'Mercredi', 13),
(22, 2, 'INF 3176', 'S006', 'JIOMEKONG', '07h05-9h15', 'Lundi', 11),
(23, 2, 'INF 3186', 'S006', 'MONTHE', '10h05-12h55', 'Lundi', 21),
(24, 2, 'INF 3276', 'S006', 'NDOUNDAM', '13h05-15h55', 'Lundi', 31),
(25, 2, 'INF 3266', 'S006', 'EKODECK', '16h05-18h55', 'Lundi', 41),
(26, 2, 'INF 3206', 'S006', 'HAMZA', '07h05-9h15', 'Mardi', 12),
(27, 2, 'INF 3216', 'S006', 'DOMGA', '10h05-12h55', 'Mardi', 22),
(28, 2, 'INF 3196', 'S006', 'ABESSOLO', '16h05-18h55', 'Mardi', 42),
(29, 2, 'INF 3256', 'S006', 'MESSI', '16h05-18h55', 'Mercredi', 43),
(30, 2, 'INF 3246', 'S006', 'TAPAMO', '07h05-9h15', 'Mercredi', 13),
(31, 2, 'INF 3046', 'A350', 'BAYEM', '07h05-9h15', 'Vendredi', 15),
(32, 2, 'INF 3236', 'S006', 'MELATAGIA', '10h05-12h55', 'Mercredi', 23),
(33, 2, 'INF 3226', 'S006', 'DOMGA', '13h05-15h55', 'Mercredi', 33),
(34, 2, 'INF 3036', 'A350', 'KOUOKAM', '13h05-15h55', 'Jeudi', 34),
(35, 2, 'INF 3286', 'S006', 'NKONDOCK', '13h05-15h55', 'Vendredi', 35),
(37, 3, 'MAT 112', 'A502', 'MBAKOP', '07h05-9h15', 'Vendredi', 15),
(40, 3, 'INF 142', 'A502', 'DOMGA', '13h05-15h55', 'Mardi', 32),
(41, 3, 'INF 122', 'A502', 'NZEKON', '16h05-18h55', 'Mardi', 42),
(42, 3, 'INF 142', 'A502', 'MELATAGIA', '16h05-18h55', 'Samedi', 46),
(43, 4, 'INF 2064', 'A250', 'MESSI', '13h05-15h55', 'Mercredi', 33),
(44, 4, 'MAT 2124', 'A3', 'FOKAM', '16h05-18h55', 'Jeudi', 44),
(45, 4, 'INF 2044', 'A3', 'MAKEMBE', '10h05-12h55', 'Vendredi', 25),
(46, 4, 'INF 2054', 'A250', 'JIOMEKONG', '13h05-15h55', 'Vendredi', 35),
(47, 5, 'INF 3176', 'S006', 'JIOMEKONG', '07h05-9h15', 'Lundi', 11),
(48, 5, 'INF 3186', 'S006', 'MONTHE', '10h05-12h55', 'Lundi', 21),
(49, 5, 'INF 3276', 'S006', 'NDOUNDAM', '13h05-15h55', 'Lundi', 31),
(50, 5, 'INF 3206', 'S006', 'HAMZA', '07h05-9h15', 'Mardi', 12),
(51, 5, 'INF 3216', 'S006', 'DOMGA', '10h05-12h55', 'Mardi', 22),
(52, 5, 'INF 3246', 'S006', 'TAPAMO', '07h05-9h15', 'Mercredi', 13),
(53, 5, 'INF 3236', 'S006', 'MELATAGIA', '10h05-12h55', 'Mercredi', 23),
(54, 5, 'INF 3226', 'S006', 'DOMGA', '13h05-15h55', 'Mercredi', 33),
(55, 5, 'INF 3036', 'A350', 'NZEKON', '13h05-15h55', 'Jeudi', 34),
(56, 5, 'INF 3046', 'A250', 'BAYEM', '07h05-9h15', 'Vendredi', 15),
(57, 5, 'INF 3286', 'S006', 'NKONDOCK', '13h05-15h55', 'Vendredi', 35),
(58, 5, 'INF 3196', 'S006', 'EKODECK', '16h05-18h55', 'Lundi', 41),
(59, 5, 'INF 3196', 'S006', 'ABESSOLO', '16h05-18h55', 'Mardi', 42),
(60, 5, 'INF 3256', 'S006', 'MESSI', '16h05-18h55', 'Mercredi', 43),
(61, 6, 'INF 4038', 'A135', 'TAPAMO', '07h05-9h15', 'Lundi', 11),
(62, 6, 'INF 4048', 'A135', 'KOUOKAM', '07h05-9h15', 'Mardi', 12),
(63, 6, 'INF 4288', 'S006', 'HAMZA', '13h05-15h55', 'Mardi', 32),
(64, 6, 'INF 4228', 'S003', 'AMINOU', '07h05-9h15', 'Mercredi', 13),
(65, 6, 'INF 4198', 'S003', 'JIOMEKONG', '10h05-12h55', 'Mercredi', 23),
(66, 6, 'INF 4288', 'S003', 'NDOUNDAM', '13h05-15h55', 'Mercredi', 33),
(67, 6, 'INF 4258', 'S003', 'NZEKON', '16h05-18h55', 'Mercredi', 43),
(68, 6, 'INF 4248', 'S006', 'MELATAGIA', '10h05-12h55', 'Vendredi', 25),
(69, 6, 'INF 4238', 'R103', 'TAPAMO', '13h05-15h55', 'Vendredi', 35),
(70, 6, 'INF 4188', 'S006', 'JIOMEKONG', '16h05-18h55', 'Samedi', 46),
(71, 7, 'PHY 112', 'A1001', 'BIYA MOTTO', '10h05-12h55', 'Mercredi', 23),
(72, 7, 'MAT 132', 'A1001', 'MBEHOU', '13h05-15h55', 'Mercredi', 33),
(73, 7, 'MAT 122', 'A1001', 'CHENDJOU', '13h05-15h55', 'Jeudi', 34),
(74, 7, 'PHY 112', 'A1002', 'ZEKENG', '07h05-9h15', 'Vendredi', 15),
(75, 7, 'MAT 142', 'A1002', 'NGUEFACKK', '10h05-12h55', 'Vendredi', 25),
(76, 8, 'MAT 2074', 'A350', 'LOUMGANG', '10h05-12h55', 'Lundi', 21),
(77, 8, 'MAT 2084', 'A350', 'MBAZOA', '13h05-15h55', 'Lundi', 31),
(78, 8, 'MAT 2094', 'A350', 'MBAZOA', '07h05-9h15', 'Jeudi', 14),
(79, 8, 'MAT 2104', 'A350', 'MBATAKOU', '10h05-12h55', 'Jeudi', 24),
(80, 8, 'MAT 2114', 'A350', 'CHENDJOU', '13h05-15h55', 'Mercredi', 33),
(81, 8, 'PHY 2054', 'A350', 'AYISSI EYEBE', '16h05-18h55', 'Jeudi', 44),
(82, 9, 'MAT 2074', 'A350', 'LOUMGANG', '10h05-12h55', 'Lundi', 21),
(83, 9, 'MAT 2084', 'A350', 'MBAZOA', '13h05-15h55', 'Lundi', 31),
(84, 9, 'MAT 2094', 'A350', 'MBAZOA', '07h05-9h15', 'Jeudi', 14),
(85, 9, 'MAT 2104', 'A350', 'MBATAKOU', '10h05-12h55', 'Jeudi', 24),
(86, 9, 'MAT 2114', 'A350', 'CHENDJOU', '13h05-15h55', 'Mercredi', 33),
(87, 9, 'PHY 2054', 'A350', 'AYISSI EYEBE', '16h05-18h55', 'Jeudi', 44),
(88, 10, 'MAT 3096', 'A3', 'FOKAM', '10h05-12h55', 'Lundi', 21),
(89, 10, 'MAT 3066', 'A250', 'LOUMGANG', '07h05-9h15', 'Jeudi', 14),
(90, 10, 'MAT 3086', 'A250', 'MBAKOP', '10h05-12h55', 'Jeudi', 24),
(91, 10, 'MAT 3116', 'A250', 'MBAKOP', '13h05-15h55', 'Jeudi', 34),
(92, 10, 'MAT 3076', 'A3', 'FOKAM', '13h05-15h55', 'Mercredi', 33),
(93, 10, 'MAT 3056', 'A350', 'CHENDJOU', '07h05-9h15', 'Vendredi', 15),
(94, 11, 'MAT 4228', 'R103', 'LOUMGANG', '13h05-15h55', 'Lundi', 31),
(95, 11, 'MAT 4128', 'R103', 'NIMPA', '07h05-9h15', 'Mardi', 12),
(96, 11, 'MAT 4118', 'A1', 'MBELE', '10h05-12h55', 'Mardi', 22),
(97, 11, 'MAT 4108', 'R103', 'FOKAM', '07h05-9h15', 'Mercredi', 13),
(98, 11, 'MAT 4218', 'R103', 'KUIMI', '10h05-12h55', 'Mercredi', 23),
(99, 11, 'MAT 4248', 'R103', 'NIMPA', '16h05-18h55', 'Mercredi', 43),
(100, 11, 'MAT 4178', 'R103', 'MBEHOU', '07h05-9h15', 'Jeudi', 14),
(101, 11, 'MAT 4308', 'R103', 'MBELE', '10h05-12h55', 'Jeudi', 24),
(102, 11, 'MAT 4268', 'R103', 'OGADOA', '16h05-18h55', 'Jeudi', 44),
(103, 11, 'MAT 4188', 'R104', 'MBATAKOU', '07h05-9h15', 'Vendredi', 15),
(104, 11, 'MAT 4168', 'R105', 'MBAZOA', '10h05-12h55', 'Vendredi', 25),
(105, 11, 'MAT 4138', 'R108', 'MBAKOP', '13h05-15h55', 'Vendredi', 35),
(106, 11, 'MAT 4208', 'R103', 'MBAKOP', '16h05-18h55', 'Vendredi', 45),
(107, 11, 'MAT 4298', 'R103', 'NGUEFACKK', '07h05-9h15', 'Samedi', 16),
(108, 12, 'MIB 3076', 'A502', 'MBANE', '07h05-9h15', 'Mercredi', 13),
(109, 12, 'MIB 3056', 'A502', 'BOYOMO', '10h05-12h55', 'Mercredi', 23),
(110, 12, 'MIB 3066', 'A502', 'RIWON', '07h05-9h15', 'Jeudi', 14),
(111, 12, 'MIB 3046', 'A502', 'NYEGUE', '10h05-12h55', 'Jeudi', 24),
(112, 13, 'MIB 4248', 'A2', 'RIWON', '07h05-9h15', 'Lundi', 11),
(113, 13, 'MIB 4148', 'R108', 'ASSAM', '13h05-15h55', 'Lundi', 31),
(114, 13, 'MIB 4038', 'A350', 'MBANE', '07h05-9h15', 'Mardi', 12),
(115, 13, 'MIB 4368', 'R108', 'ASSAM', '16h05-18h55', 'Lundi', 41),
(116, 13, 'MIB 4158', 'A135', 'ASSAM', '16h05-18h55', 'Mardi', 42),
(117, 13, 'MIB 4048', 'A350', 'BOYOMO', '07h05-9h15', 'Mercredi', 13),
(118, 13, 'MIB 4348', 'A3', 'BOYOMO', '07h05-9h15', 'Jeudi', 14),
(119, 13, 'MIB 4168', 'A3', 'ASSAM', '07h05-9h15', 'Vendredi', 15),
(120, 13, 'MIB 4258', 'A3', 'MBANE', '13h05-15h55', 'Vendredi', 35),
(121, 14, 'PHY 122', 'A1002', 'NDOP', '07h05-9h15', 'Mardi', 12),
(122, 14, 'PHY 112', 'A1001', 'EDONGUE', '10h05-12h55', 'Jeudi', 24),
(123, 14, 'MAT 162', 'A1002', 'SIEWE', '13h05-15h55', 'Jeudi', 34),
(124, 14, 'INF 132', 'A1001', 'EBELLE', '07h05-9h15', 'Samedi', 16),
(125, 15, 'PHY 2064', 'A1002', 'MELI\'I', '10h05-12h55', 'Mercredi', 23),
(126, 15, 'PHY 2044', 'A1001', 'NJANDJOCK', '07h05-9h15', 'Vendredi', 15),
(127, 15, 'PHY 2054', 'A1002', 'EKOBENA', '13h05-15h55', 'Samedi', 36),
(128, 15, 'MAT 2144', 'A1002', 'MBEHOU', '16h05-18h55', 'Samedi', 46),
(129, 16, 'PHY 3196', 'A3', 'MBONO SAMBA', '13h05-15h55', 'Lundi', 31),
(130, 16, 'PHY 3136', 'A1002', 'TCHAWOUA', '10h05-12h55', 'Mardi', 22),
(131, 16, 'PHY 3176', 'A3', 'ESSIMBI', '07h05-9h15', 'Mercredi', 13),
(132, 16, 'PHY 3166', 'A3', 'NDOP', '10h05-12h55', 'Jeudi', 24),
(133, 16, 'PHY 3186', 'A502', 'AYISSI EYEBE', '13h05-15h55', 'Jeudi', 34),
(134, 16, 'PHY 3146', 'A502', 'NDOP', '10h05-12h55', 'Vendredi', 25),
(135, 16, 'MAT 3136', 'A1001', 'OGADOA', '13h05-15h55', 'Samedi', 36),
(136, 16, 'PHY 3156', 'A502', 'TANESSONG', '07h05-9h15', 'Samedi', 16),
(137, 17, 'PHY 4378', 'A1', 'MVOGO', '07h05-9h15', 'Lundi', 11),
(138, 17, 'PHY 4458', 'R102', 'AYISSI EYEBE', '10h05-12h55', 'Lundi', 21),
(139, 17, 'PHY 4648', 'A250', 'SAIDOU', '13h05-15h55', 'Lundi', 31),
(140, 17, 'PHY 4638', 'A135', 'SIEWE', '16h05-18h55', 'Lundi', 41),
(141, 17, 'PHY 4368', 'R102', 'TEYOU', '07h05-9h15', 'Mardi', 12),
(142, 17, 'PHY 4358', 'R107', 'CHAMANI', '10h05-12h55', 'Mardi', 22),
(143, 17, 'PHY 4388', 'R102', 'NGO NYOBE', '13h05-15h55', 'Mardi', 32),
(144, 17, 'PHY 4528', 'A3', 'OBOUNOU', '16h05-18h55', 'Mardi', 42),
(145, 17, 'PHY 4568', 'A1', 'ESSIMBI', '10h05-12h55', 'Mercredi', 23),
(146, 17, 'PHY 4328', 'A135', 'TANESSONG', '13h05-15h55', 'Mercredi', 33),
(147, 17, 'PHY 4348', 'R108', 'NJANDJOCK', '16h05-18h55', 'Mercredi', 43),
(148, 17, 'PHY 4258', 'R109', 'CHAMANI', '07h05-9h15', 'Jeudi', 14),
(149, 17, 'PHY 4488', 'R102', 'SIEWE', '10h05-12h55', 'Jeudi', 24),
(150, 17, 'PHY 4398', 'R108', 'ABDOURAHIMI', '13h05-15h55', 'Jeudi', 34),
(151, 17, 'PHY 4298', 'R107', 'MELI\'I', '16h05-18h55', 'Jeudi', 44),
(152, 17, 'PHY 4278', 'R109', 'LAMARA', '07h05-9h15', 'Vendredi', 15),
(153, 17, 'PHY 4448', 'R107', 'ZEKENG', '10h05-12h55', 'Vendredi', 25),
(154, 17, 'PHY 4498', 'R104', 'NUMBEM', '13h05-15h55', 'Vendredi', 35),
(155, 17, 'PHY 4278', 'R101', 'MELI\'I', '16h05-18h55', 'Vendredi', 45),
(156, 17, 'PHY 4408', 'A3', 'SAIDOU', '07h05-9h15', 'Samedi', 16),
(157, 17, 'PHY 4318', 'A3', 'OBOUNOU', '10h05-12h55', 'Samedi', 26),
(158, 17, 'PHY 4468', 'R110', 'TCHAWOUA', '13h05-15h55', 'Samedi', 36),
(159, 17, 'PHY 4598', 'R103', 'EDONGUE', '16h05-18h55', 'Samedi', 46),
(160, 18, 'GEO 2074', 'A502', 'NTSAMA', '13h05-15h55', 'Lundi', 31),
(161, 18, 'GEO 2084', 'A502', 'NDAM', '16h05-18h55', 'Lundi', 41),
(162, 19, 'GEO 4098', 'A250', 'NGUEUTCHOUA', '07h05-9h15', 'Lundi', 11),
(163, 19, 'GEO 4188', 'A250', 'ABOSSOLO', '10h05-12h55', 'Lundi', 21),
(164, 19, 'GEO 4208', 'A501', 'ANABA', '13h05-15h55', 'Lundi', 31),
(165, 19, 'GEO 4128', 'A3', 'ATANGANA', '16h05-18h55', 'Lundi', 41),
(166, 19, 'GEO 4118', 'A250', 'TEMGA', '07h05-9h15', 'Mardi', 12),
(167, 19, 'GEO 4148', 'A3', 'NKOMBOU', '10h05-12h55', 'Mardi', 22),
(168, 19, 'GEO 4168', 'A250', 'NJILAH', '13h05-15h55', 'Mardi', 32),
(169, 19, 'GEO 4138', 'A3', 'KAMGANG', '10h05-12h55', 'Mercredi', 23),
(170, 19, 'GEO 4158', 'A350', 'EKOMANE', '16h05-18h55', 'Vendredi', 45),
(171, 19, 'GEO 4178', 'A250', 'TEMGA', '19h05-21h55', 'Vendredi', 55),
(172, 19, 'GEO 4198', 'A250', 'ANABA', '16h05-18h55', 'Jeudi', 44);

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

CREATE TABLE `departement` (
  `id_departement` int(8) NOT NULL,
  `nom_departement` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `departement`
--

INSERT INTO `departement` (`id_departement`, `nom_departement`) VALUES
(1, 'math'),
(2, 'info'),
(3, 'bios'),
(4, 'chimie'),
(5, 'physique'),
(6, 'bch'),
(7, 'mib'),
(8, 'geos'),
(9, 'langue'),
(10, 'ppe');

-- --------------------------------------------------------

--
-- Structure de la table `emploi_temps`
--

CREATE TABLE `emploi_temps` (
  `id_emploi` int(11) NOT NULL,
  `id_projet` int(8) NOT NULL,
  `nom_filiere` varchar(20) NOT NULL,
  `nom_niveau` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `emploi_temps`
--

INSERT INTO `emploi_temps` (`id_emploi`, `id_projet`, `nom_filiere`, `nom_niveau`) VALUES
(1, 13, 'informatique', 'LICENCE 1'),
(2, 14, 'informatique', 'LICENCE 3'),
(3, 15, 'informatique', 'LICENCE 1'),
(4, 15, 'informatique', 'LICENCE 2'),
(5, 15, 'informatique', 'LICENCE 3'),
(6, 15, 'informatique', 'MASTER 1'),
(7, 15, 'mathématiques ', 'LICENCE 1'),
(8, 15, 'mathématiques ', 'LICENCE 2'),
(9, 15, 'mathématiques ', 'LICENCE 2'),
(10, 15, 'mathématiques ', 'LICENCE 3'),
(11, 15, 'mathématiques ', 'MASTER 1'),
(12, 15, 'microbiologie', 'LICENCE 3'),
(13, 15, 'microbiologie', 'MASTER 1'),
(14, 15, 'physique ', 'LICENCE 1'),
(15, 15, 'physique ', 'LICENCE 2'),
(16, 15, 'physique ', 'LICENCE 3'),
(17, 15, 'physique ', 'MASTER 1'),
(18, 15, 'geosciences', 'LICENCE 2'),
(19, 15, 'geosciences', 'MASTER 1');

-- --------------------------------------------------------

--
-- Structure de la table `enseignant`
--

CREATE TABLE `enseignant` (
  `id_enseignant` int(8) NOT NULL,
  `id_departement` int(8) NOT NULL,
  `nom_enseignant` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `enseignant`
--

INSERT INTO `enseignant` (`id_enseignant`, `id_departement`, `nom_enseignant`) VALUES
(1, 3, 'AGHOUKENG'),
(2, 3, 'LOUMNGAM'),
(4, 3, 'BELL'),
(5, 3, 'NGALLE'),
(6, 1, 'OGADOA'),
(7, 3, 'LIKENG'),
(8, 3, 'DZEUFIET'),
(9, 3, 'TAN'),
(10, 3, 'DJOCGOUE'),
(11, 3, 'NGONKEU'),
(12, 3, 'TONFACK'),
(13, 3, 'BOUDJEKO'),
(14, 3, 'ACHU'),
(15, 3, 'BEBBE'),
(16, 4, 'NGO MBING'),
(17, 4, 'KOUAM'),
(18, 4, 'KENMOGNE'),
(19, 6, 'ATHOGO'),
(20, 6, 'DJUIDJE'),
(23, 6, 'FOKOU'),
(24, 6, 'EFFA'),
(25, 6, 'EWANE'),
(26, 6, 'DJAYOU'),
(27, 6, 'NDOYE'),
(28, 3, 'DJIETO'),
(29, 3, 'TADU'),
(30, 3, 'YEDE'),
(31, 3, 'NGOUNOUE'),
(32, 3, 'BILANDA'),
(33, 3, 'MONY'),
(35, 3, 'MVEYO'),
(36, 3, 'NGUEMBOCK'),
(37, 3, 'NGUEGUM'),
(38, 3, 'GOUNOUE'),
(39, 3, 'MEGNEKOU'),
(40, 3, 'NGOUATEU'),
(41, 3, 'NGUEGUIM'),
(42, 3, 'TOMBI'),
(43, 3, 'MBENOUM'),
(44, 3, 'NOAH'),
(47, 3, 'NOLA'),
(48, 3, 'MOUNGANG'),
(50, 3, 'LEKEUFACK'),
(51, 3, 'ATSAMO'),
(52, 3, 'KEKEUNOU'),
(53, 3, 'MAHOB'),
(54, 3, 'MEGAPTCHE'),
(55, 3, 'TAMSA'),
(60, 3, 'NDIOKOU'),
(61, 3, 'NWANE'),
(64, 3, 'MOSSEBO'),
(65, 3, 'ZAPFACK'),
(66, 3, 'GONMADJE'),
(67, 3, 'ONANA'),
(68, 3, 'MALA'),
(69, 3, 'MBOLO'),
(70, 3, 'AMBANG'),
(71, 3, 'MAHBOU'),
(72, 3, 'YOUMBI'),
(75, 3, 'BIYE'),
(76, 3, 'PIAL'),
(77, 6, 'FEKAM'),
(78, 3, 'KOTUE'),
(79, 6, 'MOUNDIPA'),
(80, 6, 'NJAYOU'),
(81, 6, 'TCHANA'),
(82, 6, 'OBEN'),
(83, 6, 'AKINDEH'),
(84, 6, 'NOUNGOUE'),
(85, 6, 'ATCHADE'),
(86, 6, 'NGUEFACK'),
(87, 6, 'DAKOLE'),
(88, 6, 'NGONDI'),
(93, 3, 'DJUIKWO'),
(94, 1, 'MBATAKOU'),
(95, 4, 'NJABON'),
(96, 4, 'BELIBI'),
(97, 4, 'DONGO'),
(98, 4, 'TAGATSING'),
(99, 4, 'DDJOUFACK'),
(100, 4, 'MBEY'),
(101, 4, 'NANSEU'),
(102, 4, 'KENNE'),
(103, 3, 'SADO'),
(104, 2, 'EBELLE'),
(105, 1, 'LOUMGANG'),
(106, 1, 'MBAZOA'),
(107, 4, 'NJOYA'),
(108, 4, 'KONG'),
(111, 4, 'NENWA'),
(112, 4, 'EMADAK'),
(113, 1, 'MBAKOP'),
(114, 2, 'TAPAMO'),
(115, 2, 'AMINOU'),
(116, 2, 'JIOMEKONG'),
(117, 2, 'KOUOKAM'),
(118, 2, 'NZEKON'),
(119, 2, 'MELATAGIA'),
(120, 2, 'HAMZA'),
(121, 2, 'DOMGA'),
(122, 2, 'TSOPZE'),
(123, 2, 'MESSI'),
(124, 1, 'FOKAM'),
(125, 2, 'MAKEMBE'),
(126, 2, 'MONTHE'),
(127, 2, 'NDOUNDAM'),
(128, 2, 'BAYEM'),
(129, 2, 'NKONDOCK'),
(130, 2, 'ABESSOLO'),
(131, 2, 'KIMBI'),
(132, 2, 'EKODECK'),
(133, 1, 'MBEHOU'),
(134, 1, 'CHENDJOU'),
(136, 1, 'NGUEFACKK'),
(176, 5, 'BIYA MOTTO'),
(177, 5, 'ZEKENG'),
(178, 5, 'HONA'),
(179, 5, 'NDOP'),
(180, 5, 'NJANDJOCK'),
(181, 5, 'AYISSI EYEBE'),
(182, 5, 'NUMBEM'),
(183, 5, 'CHAMANI'),
(184, 5, 'TCHAWOUA'),
(185, 5, 'NOUAYOU'),
(186, 5, 'SIEWE'),
(187, 5, 'TEYOU'),
(188, 5, 'NDJAKA'),
(189, 5, 'EYEBE FOUDA'),
(190, 7, 'MBANE'),
(191, 5, 'VONDOU'),
(192, 5, 'MBONO SAMBA'),
(193, 5, 'MVOGO'),
(194, 5, 'NGO NYOBE'),
(195, 5, 'EDONGUE'),
(196, 5, 'SAIDOU'),
(197, 5, 'EKOBENA'),
(198, 5, 'LAMARA'),
(199, 5, 'MELI\'I'),
(200, 5, 'OBOUNOU'),
(201, 5, 'TANESSONG'),
(202, 5, 'ABDOURAHIMI'),
(206, 8, 'NTSAMA'),
(207, 8, 'NDAM'),
(208, 8, 'ANABA'),
(209, 8, 'NGO BELNOUN'),
(210, 8, 'ETOUNA'),
(211, 8, 'NOMO'),
(212, 8, 'GANNO'),
(213, 8, 'MBIDA  YEM'),
(214, 8, 'NKOMBOU'),
(215, 8, 'NGUEUTCHOUA'),
(216, 8, 'ATANGANA'),
(217, 8, 'AKAMBA'),
(218, 8, 'ABOSSOLO'),
(219, 8, 'NYECK'),
(220, 8, 'NJILAH'),
(221, 8, 'KAMGANG'),
(222, 8, 'NZENTI'),
(223, 8, 'TEMGA'),
(224, 8, 'EKOMANE'),
(225, 5, 'ESSIMBI'),
(226, 1, 'NIMPA'),
(227, 1, 'KUIMI'),
(228, 1, 'MBELE'),
(229, 1, 'DOUALA'),
(230, 7, 'RIWON'),
(231, 7, 'BOYOMO'),
(232, 7, 'NYEGUE'),
(233, 7, 'ASSAM');

-- --------------------------------------------------------

--
-- Structure de la table `filiere`
--

CREATE TABLE `filiere` (
  `id_filiere` int(8) NOT NULL,
  `nom_filiere` varchar(30) NOT NULL,
  `id_departement` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `filiere`
--

INSERT INTO `filiere` (`id_filiere`, `nom_filiere`, `id_departement`) VALUES
(1, 'biochimie', 6),
(2, 'biosciences', 3),
(3, 'informatique', 2),
(4, 'chimie', 4),
(5, 'geosciences', 8),
(6, 'microbiologie', 7),
(7, 'mathématiques ', 1),
(8, 'physique ', 5);

-- --------------------------------------------------------

--
-- Structure de la table `groupe`
--

CREATE TABLE `groupe` (
  `id_groupe` int(8) NOT NULL,
  `id_specialite` int(8) NOT NULL,
  `id_niveau` int(8) NOT NULL,
  `nom_groupe` varchar(20) NOT NULL,
  `nb_etudiants` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `groupe`
--

INSERT INTO `groupe` (`id_groupe`, `id_specialite`, `id_niveau`, `nom_groupe`, `nb_etudiants`) VALUES
(1, 1, 3, 'BCH L3', 200),
(2, 1, 4, 'BCH M1', 100),
(3, 2, 2, 'BIOS 2', 250),
(4, 13, 3, 'MIB 3', 100),
(5, 13, 4, 'MIB 4', 100),
(7, 2, 3, 'BOA 3', 200),
(9, 3, 3, 'BOV 3 ', 200),
(11, 2, 4, 'BOA M1', 100),
(12, 3, 4, 'BOV M1', 100),
(15, 16, 3, 'CHIMIE 3', 250),
(16, 16, 4, 'CHIMIE  4', 200),
(17, 6, 3, 'GEOS 3', 300),
(18, 6, 4, 'STU', 200),
(19, 8, 3, 'DATA SCIENCE 3', 80),
(20, 8, 4, 'DATA SCIENCE 4', 70),
(21, 9, 3, 'GÉNIE LOGICIEL 3', 100),
(22, 9, 4, 'GÉNIE LOGICIEL 4', 100),
(23, 7, 3, 'SÉCURITÉ 3', 90),
(24, 7, 4, 'SÉCURITÉ 4', 70),
(25, 10, 3, 'RÉSEAU 3', 100),
(26, 10, 4, 'RÉSEAU 4', 70),
(27, 11, 3, 'ALGÈBRE 3', 70),
(28, 19, 4, 'MAT 4', 50),
(29, 19, 3, 'MAT 3', 80),
(34, 15, 1, 'BIOS 1 A', 1500),
(35, 16, 1, 'CHIMIE 1', 1000),
(36, 16, 2, 'CHIMIE 2', 1000),
(38, 6, 2, 'GEOS 2', 500),
(39, 18, 1, 'INFO 1', 500),
(40, 18, 2, 'INFO 2', 250),
(41, 19, 1, 'MATH 1', 1000),
(42, 19, 2, 'MATH 2', 300),
(43, 14, 1, 'PHY 1', 1000),
(44, 14, 2, 'PHY 2', 700),
(45, 14, 3, 'PHY 3', 250),
(48, 14, 4, 'PHY 4', 100),
(51, 19, 3, 'MAT 3', 180),
(52, 18, 3, 'INFO 3', 250),
(53, 18, 4, 'INFO 4', 100),
(54, 15, 1, 'BIOS 1 B', 1500),
(55, 15, 1, 'BIOS 1 C', 1500);

-- --------------------------------------------------------

--
-- Structure de la table `matiere`
--

CREATE TABLE `matiere` (
  `id_matiere` int(8) NOT NULL,
  `id_groupe` int(8) DEFAULT NULL,
  `id_departement` int(8) NOT NULL,
  `nom_matiere` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `matiere`
--

INSERT INTO `matiere` (`id_matiere`, `id_groupe`, `id_departement`, `nom_matiere`) VALUES
(1, 34, 1, 'MAT 152'),
(2, 34, 5, 'PHY 171'),
(3, 34, 3, 'BIO 112'),
(4, 3, 3, 'BIO 2054'),
(5, 3, 3, 'BIO 2064'),
(6, 3, 4, 'CHM 2083'),
(7, 3, 3, 'BIO 2074'),
(8, 1, 6, 'BCH 3056'),
(9, 1, 6, 'BCH 3076'),
(10, 1, 6, 'BCH   3066'),
(11, 1, 6, 'BCH 3106'),
(12, 1, 6, 'BCH 3096'),
(13, 1, 6, 'BCH 3116'),
(14, 7, 3, 'BIO 3076'),
(15, 7, 3, 'BIO 3066'),
(16, 7, 3, 'BIO 3096'),
(17, 7, 3, 'BIO 3056'),
(19, 11, 3, 'BOA 4098'),
(20, 11, 3, 'BOA 4068'),
(21, 11, 3, 'BOA 4108'),
(22, 11, 3, 'BOA 4158'),
(23, 11, 3, 'BOA 4168'),
(24, 11, 3, 'BOA 4218'),
(25, 11, 3, 'BOA 4138'),
(26, 11, 3, 'BOA 4078'),
(27, 11, 3, 'BOA 4238'),
(28, 11, 3, 'BOA  4088'),
(29, 11, 3, 'BOA 4288'),
(31, 9, 3, 'BOV 3096'),
(32, 9, 3, 'BOV 3066'),
(33, 9, 3, 'BOV 3076'),
(34, 9, 3, 'BOV 3086'),
(36, 12, 3, 'BOV 4068'),
(37, 12, 3, 'BOV 4168'),
(38, 12, 3, 'BOV 4178'),
(39, 12, 3, 'BOV 4078'),
(40, 12, 3, 'BOV 4088'),
(41, 12, 3, 'BOV 4158'),
(42, 12, 3, 'BOV 4148'),
(43, 12, 3, 'BOV 4098'),
(44, 2, 6, 'BCH 4128'),
(45, 2, 6, 'BCH 4138'),
(46, 2, 6, 'BCH 4088'),
(47, 2, 6, 'BCH 4098'),
(48, 2, 4, 'CHM 4168'),
(49, 2, 6, 'BCH 4108'),
(50, 2, 6, 'BCH 4118'),
(51, 35, 4, 'CHM 112'),
(52, 35, 4, 'CHM 122'),
(53, 35, 4, 'CHM 132'),
(55, 35, 3, 'BIO 152'),
(56, 36, 4, 'CHM 2054'),
(57, 36, 4, 'CHM 2064'),
(58, 36, 2, 'INF 2114'),
(59, 36, 4, 'CHM 2044'),
(60, 36, 3, 'BIO 2094'),
(61, 44, 1, 'MAT 2144'),
(63, 15, 4, 'CHM 3106'),
(64, 15, 4, 'CHM 3136'),
(65, 15, 4, 'CHM 3146'),
(66, 15, 4, 'CHM 3116'),
(67, 15, 4, 'CHM 3086'),
(68, 15, 6, 'BCH 3136'),
(69, 15, 4, 'CHM 3076'),
(70, 16, 4, 'CHM 4088'),
(71, 16, 4, 'CHM 4078'),
(72, 16, 4, 'CHM 4108'),
(73, 16, 4, 'CHM 4158'),
(74, 16, 4, 'CHM 4118'),
(76, 16, 4, 'CHM 4128'),
(77, 16, 4, 'CHM 4138'),
(78, 16, 6, 'BCH 4148'),
(80, 39, 1, 'MAT 112'),
(81, 39, 2, 'INF 122'),
(82, 39, 2, 'INF 142'),
(83, 39, 2, 'INF 152'),
(84, 43, 2, 'INF 132'),
(85, 40, 2, 'INF 2064'),
(86, 40, 2, 'INF 2044'),
(87, 40, 1, 'MAT 2124'),
(88, 40, 2, 'INF 2054'),
(89, 21, 2, 'INF 3176'),
(90, 21, 2, 'INF 3186'),
(91, 52, 2, 'INF 3036'),
(92, 52, 2, 'INF 3046'),
(93, 19, 2, 'INF 3246'),
(94, 19, 2, 'INF 3236'),
(95, 19, 2, 'INF 3256'),
(96, 21, 2, 'INF 3196'),
(97, 25, 2, 'INF 3206'),
(98, 25, 2, 'INF 3216'),
(99, 25, 2, 'INF 3226'),
(105, 23, 2, 'INF 3276'),
(106, 23, 2, 'INF 3286'),
(107, 23, 2, 'INF 3266'),
(108, 53, 2, 'INF 4038'),
(109, 53, 2, 'INF 4048'),
(110, 22, 2, 'INF 4188'),
(111, 22, 2, 'INF 4178'),
(112, 22, 2, 'INF 4198'),
(113, 26, 2, 'INF 4218'),
(114, 26, 2, 'INF 4228'),
(115, 26, 2, 'INF 4208'),
(116, 20, 2, 'INF 4238'),
(117, 20, 2, 'INF 4248'),
(118, 20, 2, 'INF 4258'),
(119, 24, 2, 'INF 4268'),
(120, 24, 2, 'INF 4278'),
(121, 24, 2, 'INF 4288'),
(122, 41, 1, 'MAT 132'),
(123, 41, 1, 'MAT 122'),
(124, 43, 5, 'PHY 112'),
(125, 41, 5, 'PHY 122'),
(126, 41, 1, 'MAT 142'),
(127, 42, 1, 'MAT 2074'),
(128, 42, 1, 'MAT 2084'),
(129, 36, 1, 'MAT 2114'),
(130, 42, 1, 'MAT 2094'),
(131, 42, 1, 'MAT 2104'),
(132, 42, 1, 'MAT 2134'),
(133, 42, 5, 'PHY 2044'),
(134, 42, 5, 'PHY 2054'),
(135, 51, 1, 'MAT 3096'),
(136, 51, 1, 'MAT 3106'),
(137, 51, 1, 'MAT 3076'),
(138, 51, 1, 'MAT 3066'),
(139, 51, 1, 'MAT 3086'),
(140, 51, 1, 'MAT 3116'),
(141, 51, 1, 'MAT 3126'),
(142, 51, 1, 'MAT 3056'),
(143, 28, 1, 'MAT 4228'),
(144, 28, 1, 'MAT 4198'),
(145, 28, 1, 'MAT 4128'),
(146, 28, 1, 'MAT 4118'),
(147, 28, 1, 'MAT 4108'),
(148, 28, 1, 'MAT 4218'),
(149, 28, 1, 'MAT 4158'),
(150, 28, 1, 'MAT 4248'),
(151, 28, 1, 'MAT 4298'),
(152, 28, 1, 'MAT 4178'),
(153, 28, 1, 'MAT 4308'),
(154, 28, 1, 'MAT 4268'),
(155, 28, 1, 'MAT 4188'),
(156, 28, 1, 'MAT 4168'),
(157, 28, 1, 'MAT 4148'),
(158, 28, 1, 'MAT 4138'),
(159, 28, 1, 'MAT 4208'),
(160, 28, 1, 'MAT 4298'),
(161, 4, 7, 'MIB 3076'),
(162, 4, 7, 'MIB 3056'),
(163, 4, 7, 'MIB 3066'),
(164, 4, 7, 'MIB 3046'),
(166, 5, 7, 'MIB 4148'),
(167, 5, 7, 'MIB 4368'),
(168, 5, 7, 'MIB 4038'),
(169, 5, 7, 'MIB 4158'),
(170, 5, 7, 'MIB 4348'),
(171, 5, 7, 'MIB 4048'),
(173, 5, 7, 'MIB 4248'),
(174, 5, 7, 'MIB 4168'),
(175, 5, 7, 'MIB 4258'),
(176, 43, 5, 'PHY 122'),
(177, 41, 5, 'PHY 112'),
(178, 35, 1, 'MAT 162'),
(180, 44, 5, 'PHY 2064'),
(181, 44, 5, 'PHY 2044'),
(182, 44, 5, 'PHY 2054'),
(185, 45, 5, 'PHY 3136'),
(186, 45, 5, 'PHY 3176'),
(187, 45, 5, 'PHY 3166'),
(188, 45, 5, 'PHY 3186'),
(189, 45, 5, 'PHY 3146'),
(190, 45, 5, 'PHY 3156'),
(191, 45, 1, 'MAT 3136'),
(192, 48, 5, 'PHY 4378'),
(193, 48, 5, 'PHY 4618'),
(194, 48, 5, 'PHY 4458'),
(195, 48, 5, 'PHY 4518'),
(196, 48, 5, 'PHY 4558'),
(197, 48, 5, 'PHY 4658'),
(198, 48, 5, 'PHY 4648'),
(199, 48, 5, 'PHY 4638'),
(200, 48, 5, 'PHY 4368'),
(201, 48, 5, 'PHY 4578'),
(202, 48, 5, 'PHY 4358'),
(203, 48, 5, 'PHY 4388'),
(204, 48, 5, 'PHY 4428'),
(205, 48, 5, 'PHY 4338'),
(206, 48, 5, 'PHY 4528'),
(207, 48, 5, 'PHY 4508'),
(208, 48, 5, 'PHY 4478'),
(209, 48, 5, 'PHY 4568'),
(210, 48, 5, 'PHY 4328'),
(211, 48, 5, 'PHY 4608'),
(212, 48, 5, 'PHY 4348'),
(213, 48, 5, 'PHY 4258'),
(214, 48, 5, 'PHY 4418'),
(215, 48, 5, 'PHY 4548'),
(216, 48, 5, 'PHY 4438'),
(217, 48, 5, 'PHY 4488'),
(218, 48, 5, 'PHY 4628'),
(219, 48, 5, 'PHY 4398'),
(220, 48, 5, 'PHY 4308'),
(221, 48, 5, 'PHY 4298'),
(222, 48, 5, 'PHY 4268'),
(223, 48, 5, 'PHY 4448'),
(224, 48, 5, 'PHY 4588'),
(225, 48, 5, 'PHY 4498'),
(226, 48, 5, 'PHY 4278'),
(227, 48, 5, 'PHY 4408'),
(228, 48, 5, 'PHY 4318'),
(229, 48, 5, 'PHY 4468'),
(230, 48, 5, 'PHY 4538'),
(231, 48, 5, 'PHY 4598'),
(232, 48, 5, 'PHY 4288'),
(233, 38, 8, 'GEO 2074'),
(234, 38, 8, 'GEO 2084'),
(235, 17, 8, 'GEO 3106'),
(236, 17, 8, 'GEO 3076'),
(237, 17, 8, 'GEO 3066'),
(238, 17, 8, 'GEO 3096'),
(239, 17, 8, 'GEO 3086'),
(240, 18, 8, 'GEO 4098'),
(241, 18, 8, 'GEO 4188'),
(242, 18, 8, 'GEO 4208'),
(243, 18, 8, 'GEO 4118'),
(244, 18, 8, 'GEO 4148'),
(245, 18, 8, 'GEO 4168'),
(246, 18, 8, 'GEO 4088'),
(247, 18, 8, 'GEO 4128'),
(248, 18, 8, 'GEO 4138'),
(249, 18, 8, 'GEO 4198'),
(250, 18, 8, 'GEO 4178'),
(251, 18, 8, 'GEO 4158'),
(252, 7, 3, 'BIO 3056'),
(253, 1, 6, 'BCH 3086'),
(254, 16, 4, 'CHM 4148'),
(255, 42, 1, 'MAT 2114'),
(256, 43, 5, 'MAT 162'),
(257, 45, 5, 'PHY 3196'),
(258, 54, 1, 'MAT 152'),
(259, 54, 5, 'PHY 171'),
(260, 54, 3, 'BIO 112'),
(261, 54, 9, 'ANG'),
(262, 34, 9, 'ANG'),
(263, 55, 9, 'ANG'),
(264, 55, 1, 'MAT 152'),
(265, 55, 5, 'PHY 171'),
(266, 55, 3, 'BIO 112'),
(267, 3, 10, 'PPE 2004'),
(268, 1, 10, 'PPE'),
(269, 7, 10, 'PPE 3006'),
(270, 9, 10, 'PPE 3006'),
(271, 35, 9, 'ANG'),
(272, 35, 10, 'PPE 1002'),
(273, 36, 10, 'PPE 2004'),
(274, 15, 10, 'PPE 3006'),
(275, 39, 9, 'ANG'),
(276, 39, 10, 'PPE 112'),
(277, 40, 9, 'ANG'),
(278, 40, 10, 'PPE 2004'),
(279, 52, 10, 'PPE'),
(280, 41, 9, 'ANG'),
(281, 41, 10, 'PPE'),
(282, 42, 10, 'PPE'),
(283, 51, 10, 'PPE'),
(284, 4, 10, 'PPE'),
(285, 43, 9, 'ANG'),
(286, 43, 10, 'PPE 112'),
(287, 44, 10, 'PPE'),
(288, 45, 10, 'PPE 3006'),
(289, 38, 9, 'ANG'),
(290, 38, 10, 'PPE'),
(291, 17, 10, 'PPE');

-- --------------------------------------------------------

--
-- Structure de la table `niveau`
--

CREATE TABLE `niveau` (
  `id_niveau` int(8) NOT NULL,
  `nom_niveau` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `niveau`
--

INSERT INTO `niveau` (`id_niveau`, `nom_niveau`) VALUES
(1, 'LICENCE 1'),
(2, 'LICENCE 2'),
(3, 'LICENCE 3'),
(4, 'MASTER 1');

-- --------------------------------------------------------

--
-- Structure de la table `projet`
--

CREATE TABLE `projet` (
  `id_projet` int(8) NOT NULL,
  `nom_projet` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `projet`
--

INSERT INTO `projet` (`id_projet`, `nom_projet`) VALUES
(13, 'Info L2'),
(14, 'Info L3'),
(15, 'FACS SEM2');

-- --------------------------------------------------------

--
-- Structure de la table `specialite`
--

CREATE TABLE `specialite` (
  `id_specialite` int(8) NOT NULL,
  `id_filiere` int(8) NOT NULL,
  `nom_specialite` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `specialite`
--

INSERT INTO `specialite` (`id_specialite`, `id_filiere`, `nom_specialite`) VALUES
(1, 1, 'BCH'),
(2, 2, 'BOA'),
(3, 2, 'BOV'),
(6, 5, 'GEOS'),
(7, 3, 'SÉCURITÉ '),
(8, 3, 'DATA SCIENCE'),
(9, 3, 'GÉNIE LOGICIEL '),
(10, 3, 'RÉSEAU '),
(11, 7, 'ALGÈBRE '),
(12, 7, 'ANALYSE'),
(13, 6, 'MICROBIOLOGIE '),
(14, 8, 'PHYSIQUE '),
(15, 2, 'BIOS'),
(16, 4, 'CHIMIE '),
(18, 3, 'INFO '),
(19, 7, 'MATH');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `amphi`
--
ALTER TABLE `amphi`
  ADD PRIMARY KEY (`id_amphi`);

--
-- Index pour la table `cellule`
--
ALTER TABLE `cellule`
  ADD PRIMARY KEY (`id_cellule`),
  ADD KEY `id_emploi` (`id_emploi`);

--
-- Index pour la table `departement`
--
ALTER TABLE `departement`
  ADD PRIMARY KEY (`id_departement`);

--
-- Index pour la table `emploi_temps`
--
ALTER TABLE `emploi_temps`
  ADD PRIMARY KEY (`id_emploi`),
  ADD KEY `id_projet` (`id_projet`);

--
-- Index pour la table `enseignant`
--
ALTER TABLE `enseignant`
  ADD PRIMARY KEY (`id_enseignant`),
  ADD UNIQUE KEY `nom_enseignant_2` (`nom_enseignant`),
  ADD UNIQUE KEY `nom_enseignant` (`nom_enseignant`) USING BTREE,
  ADD UNIQUE KEY `nom_enseignant_3` (`nom_enseignant`),
  ADD UNIQUE KEY `nom_enseignant_4` (`nom_enseignant`),
  ADD KEY `id_departement` (`id_departement`);

--
-- Index pour la table `filiere`
--
ALTER TABLE `filiere`
  ADD PRIMARY KEY (`id_filiere`),
  ADD KEY `id_departement` (`id_departement`);

--
-- Index pour la table `groupe`
--
ALTER TABLE `groupe`
  ADD PRIMARY KEY (`id_groupe`),
  ADD KEY `id_niveau` (`id_niveau`),
  ADD KEY `id_specialite` (`id_specialite`);

--
-- Index pour la table `matiere`
--
ALTER TABLE `matiere`
  ADD PRIMARY KEY (`id_matiere`),
  ADD KEY `id_departement` (`id_departement`),
  ADD KEY `id_groupe` (`id_groupe`);

--
-- Index pour la table `niveau`
--
ALTER TABLE `niveau`
  ADD PRIMARY KEY (`id_niveau`);

--
-- Index pour la table `projet`
--
ALTER TABLE `projet`
  ADD PRIMARY KEY (`id_projet`);

--
-- Index pour la table `specialite`
--
ALTER TABLE `specialite`
  ADD PRIMARY KEY (`id_specialite`),
  ADD KEY `id_filiere` (`id_filiere`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `amphi`
--
ALTER TABLE `amphi`
  MODIFY `id_amphi` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `cellule`
--
ALTER TABLE `cellule`
  MODIFY `id_cellule` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=173;

--
-- AUTO_INCREMENT pour la table `departement`
--
ALTER TABLE `departement`
  MODIFY `id_departement` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `emploi_temps`
--
ALTER TABLE `emploi_temps`
  MODIFY `id_emploi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT pour la table `enseignant`
--
ALTER TABLE `enseignant`
  MODIFY `id_enseignant` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=234;

--
-- AUTO_INCREMENT pour la table `filiere`
--
ALTER TABLE `filiere`
  MODIFY `id_filiere` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `groupe`
--
ALTER TABLE `groupe`
  MODIFY `id_groupe` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT pour la table `matiere`
--
ALTER TABLE `matiere`
  MODIFY `id_matiere` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=293;

--
-- AUTO_INCREMENT pour la table `niveau`
--
ALTER TABLE `niveau`
  MODIFY `id_niveau` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `projet`
--
ALTER TABLE `projet`
  MODIFY `id_projet` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `specialite`
--
ALTER TABLE `specialite`
  MODIFY `id_specialite` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `emploi_temps`
--
ALTER TABLE `emploi_temps`
  ADD CONSTRAINT `emploi_temps_ibfk_1` FOREIGN KEY (`id_projet`) REFERENCES `projet` (`id_projet`);

--
-- Contraintes pour la table `enseignant`
--
ALTER TABLE `enseignant`
  ADD CONSTRAINT `Enseignant_ibfk_1` FOREIGN KEY (`id_departement`) REFERENCES `departement` (`id_departement`);

--
-- Contraintes pour la table `filiere`
--
ALTER TABLE `filiere`
  ADD CONSTRAINT `Filiere_ibfk_1` FOREIGN KEY (`id_departement`) REFERENCES `departement` (`id_departement`);

--
-- Contraintes pour la table `groupe`
--
ALTER TABLE `groupe`
  ADD CONSTRAINT `Groupe_ibfk_2` FOREIGN KEY (`id_niveau`) REFERENCES `niveau` (`id_niveau`),
  ADD CONSTRAINT `Groupe_ibfk_3` FOREIGN KEY (`id_specialite`) REFERENCES `specialite` (`id_specialite`);

--
-- Contraintes pour la table `matiere`
--
ALTER TABLE `matiere`
  ADD CONSTRAINT `Matiere_ibfk_2` FOREIGN KEY (`id_departement`) REFERENCES `departement` (`id_departement`),
  ADD CONSTRAINT `Matiere_ibfk_5` FOREIGN KEY (`id_groupe`) REFERENCES `groupe` (`id_groupe`);

--
-- Contraintes pour la table `specialite`
--
ALTER TABLE `specialite`
  ADD CONSTRAINT `Specialite_ibfk_1` FOREIGN KEY (`id_filiere`) REFERENCES `filiere` (`id_filiere`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
