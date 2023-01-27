-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 27 jan. 2023 à 10:41
-- Version du serveur :  10.4.18-MariaDB
-- Version de PHP : 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pokemonapi`
--

-- --------------------------------------------------------

--
-- Structure de la table `competence`
--

CREATE TABLE `competence` (
  `id_competence` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `puissance` int(11) NOT NULL,
  `precisions` int(11) NOT NULL,
  `pp_max` int(11) NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `competence`
--

INSERT INTO `competence` (`id_competence`, `nom`, `description`, `puissance`, `precisions`, `pp_max`, `type_id`) VALUES
(1, 'Abime', 'lanceur fait tomber la cible', 12, 34, 78, 1),
(2, 'Acide', 'lanceur attaque la cible avec un jet d\'acide', 234, 456, 543, 2),
(3, 'Abri', 'lanceur se protege des attaque', 12, 53, 90, 3),
(4, 'Air d eau', 'une masse d eau s abat sur la cible', 43, 98, 100, 4),
(5, 'Aire de Feu', 'une masse de feu s abat sur la cible', 12, 53, 89, 5),
(6, 'Anti-air', 'lanceur jette un projectile sur la cible', 12, 23, 34, 6);

-- --------------------------------------------------------

--
-- Structure de la table `pokemon`
--

CREATE TABLE `pokemon` (
  `id_pokemon` int(11) NOT NULL,
  `numero_du_pokedex` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `taille` float NOT NULL,
  `poids` float NOT NULL,
  `statistiques_de_base` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `type_id` int(11) NOT NULL,
  `competence_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `pokemon`
--

INSERT INTO `pokemon` (`id_pokemon`, `numero_du_pokedex`, `nom`, `taille`, `poids`, `statistiques_de_base`, `image`, `type_id`, `competence_id`) VALUES
(401, 1, 'Bulbizarre', 0.7, 6.9, 118, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 1, 1),
(402, 2, 'Salameche', 0.6, 8.5, 116, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png', 2, 2),
(403, 3, 'Venusaur-mega', 2.4, 155.5, 200, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10033.png', 3, 3),
(404, 4, 'Charmander', 0.6, 8.5, 100, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png', 4, 4),
(405, 5, 'Flame Pokemon', 1.1, 19, 120, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png', 5, 5),
(406, 6, 'Charizard', 1.7, 90.5, 130, 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png', 6, 6);

-- --------------------------------------------------------

--
-- Structure de la table `type`
--

CREATE TABLE `type` (
  `id_type` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `typeForts` varchar(50) NOT NULL,
  `typeFaibles` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `type`
--

INSERT INTO `type` (`id_type`, `nom`, `typeForts`, `typeFaibles`) VALUES
(1, 'Acier', 'Roche', 'Feu'),
(2, 'Eau', 'Sol', 'Plante'),
(3, 'Vol', 'Combat ', 'Elektrik '),
(4, 'Feu', 'Vol', 'Eau'),
(5, 'Dragon', 'Dragon', 'Glace'),
(6, 'Glace', 'Sol', 'Acier');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `competence`
--
ALTER TABLE `competence`
  ADD PRIMARY KEY (`id_competence`),
  ADD KEY `type_id` (`type_id`);

--
-- Index pour la table `pokemon`
--
ALTER TABLE `pokemon`
  ADD PRIMARY KEY (`id_pokemon`),
  ADD KEY `type_id` (`type_id`),
  ADD KEY `competence_id` (`competence_id`);

--
-- Index pour la table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`id_type`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `pokemon`
--
ALTER TABLE `pokemon`
  MODIFY `id_pokemon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=407;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `competence`
--
ALTER TABLE `competence`
  ADD CONSTRAINT `competence_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `type` (`id_type`);

--
-- Contraintes pour la table `pokemon`
--
ALTER TABLE `pokemon`
  ADD CONSTRAINT `pokemon_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `type` (`id_type`),
  ADD CONSTRAINT `pokemon_ibfk_2` FOREIGN KEY (`competence_id`) REFERENCES `competence` (`id_competence`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
