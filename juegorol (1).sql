-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-08-2024 a las 21:18:11
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `juegorol`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipamientos`
--

CREATE TABLE `equipamientos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipamientos`
--

INSERT INTO `equipamientos` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Espada', 'Pieza de metal utilizada para cortar al enemigo'),
(2, 'Escudo', 'Pieza de hierro utilizado para proteger al portador de ataques enemigos'),
(3, 'Arco', 'Pieza de madera con un cordel tenso utilizado para derribar enemigos a la distancia'),
(4, 'Varita', 'Pieza de madera pequeña utilizada para facilitar el uso de la magia'),
(5, 'Armadura', 'Pieza de acero liviano utilizada para mitigar el daño entrante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE `estados` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`id`, `nombre`, `descripcion`) VALUES
(1, 'vivo', 'Personaje con puntos de vida existentes'),
(2, 'muerto', 'Personaje con los puntos de vida agotados'),
(3, 'Congelado', 'Personaje inmovilizado debido a reiterados ataques de hielo'),
(4, 'Relentizado', 'Velocidad de movimiento del personaje reducido debido a ataques de hielo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidades`
--

CREATE TABLE `habilidades` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `raza_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habilidades`
--

INSERT INTO `habilidades` (`id`, `nombre`, `descripcion`, `raza_id`) VALUES
(1, 'Correr', 'Permite al personaje moverse a mayor velocidad durante un periodo de tiempo', 2),
(2, 'Saltar', 'Permite al personaje alcanzar objetos altos y sobrepasar agujeros muy largos', 2),
(3, 'Caminar', 'Permite al personaje desplazarse de un lugar a otro', 2),
(4, 'Nadar', 'Permite al personaje no ahogarse si esté cae al agua', 2),
(5, 'Escalar', 'Permite al usuario subir montañas que no posean caminos', 2),
(6, 'Correr', 'Permite al personaje moverse a mayor velocidad durante un periodo de tiempo', 1),
(7, 'Saltar', 'Permite al personaje alcanzar objetos altos y sobrepasar agujeros muy largos', 1),
(8, 'Caminar', 'Permite al personaje desplazarse de un lugar a otro', 1),
(9, 'Trepar', 'Permite al personaje subirse a sitios altos como un árbol o una roca', 1),
(10, 'Deslizarse', 'Permite al usuario desplazarse a ras de suelo', 1),
(11, 'Correr', 'Permite al personaje moverse a mayor velocidad durante un periodo de tiempo', 3),
(12, 'Saltar', 'Permite al personaje alcanzar objetos altos y sobrepasar agujeros muy largos', 3),
(13, 'Caminar', 'Permite al personaje desplazarse de un lugar a otro', 3),
(14, 'Cavar', 'Permite al personaje hacer hoyos para la recolección de minerales o para esconderse', 3),
(15, 'Tenacidad', 'Permite al usuario resistir los controles de masa de manera más efectiva', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personaje`
--

CREATE TABLE `personaje` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `nivel` int(5) NOT NULL DEFAULT 1,
  `usuario_id` int(11) NOT NULL,
  `raza_id` int(11) NOT NULL,
  `habilidad_id` int(11) NOT NULL,
  `equipamiento_id` int(11) NOT NULL,
  `poderes_id` int(11) NOT NULL,
  `estado_id` int(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `poderes`
--

CREATE TABLE `poderes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `raza_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `poderes`
--

INSERT INTO `poderes` (`id`, `nombre`, `descripcion`, `raza_id`) VALUES
(1, 'Lanzar fuego', 'Proporciona un estado de quemadura si no se posee tenacidad y al mismo tiempo inflige daño', 2),
(2, 'Teletransportarse', 'Permite al usuario viajar de manera instantánea de un lugar a otro ', 2),
(3, 'Invisibilidad', 'Permite al personaje pasar desapercebido frente a otros personajes', 2),
(4, 'Controlar el hielo', 'Permite al personaje atacar con hielo causando daño y un efecto de ralentización', 1),
(5, 'descarga', '', 1),
(6, 'Curación', 'Permite al personaje recuperar vida de sí mismo o de otro personaje', 1),
(7, 'Invocar rocas', 'Permite al personaje atacar con rocas causando gran cantidad de daño', 3),
(8, 'Controlar tierra', 'Permite al usuario atacar utilizando la tierra alrededor causando daño mínimo', 3),
(9, 'Resistencia mágica', 'Otorga al personaje resistencia extra a lo demás poderes', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `raza`
--

CREATE TABLE `raza` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `raza`
--

INSERT INTO `raza` (`id`, `nombre`, `descripcion`) VALUES
(1, 'elfo', 'Raza mítica amante de la naturaleza especializada en la magia'),
(2, 'humano', 'Raza normal sin características especiales, posee las estadísticas bien balanceadas'),
(3, 'enano', 'Mítica raza de tamaño bajo pero que posee una mayor fuerza que la de los humanos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `enlinea` tinyint(1) NOT NULL DEFAULT 0,
  `tipo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `clave`, `enlinea`, `tipo`) VALUES
(18, 'andi', '827ccb0eea8a706c4c34a16891f84e7b', 1, 'master'),
(19, 'martin', '827ccb0eea8a706c4c34a16891f84e7b', 1, 'jugador');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipamientos`
--
ALTER TABLE `equipamientos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `habilidades`
--
ALTER TABLE `habilidades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_habraz` (`raza_id`);

--
-- Indices de la tabla `personaje`
--
ALTER TABLE `personaje`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_perUsu` (`usuario_id`),
  ADD KEY `fk_perRaz` (`raza_id`),
  ADD KEY `fk_perHab` (`habilidad_id`),
  ADD KEY `fk_perEqu` (`equipamiento_id`),
  ADD KEY `fk_perPod` (`poderes_id`),
  ADD KEY `fk_est_per` (`estado_id`);

--
-- Indices de la tabla `poderes`
--
ALTER TABLE `poderes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_podRaz` (`raza_id`);

--
-- Indices de la tabla `raza`
--
ALTER TABLE `raza`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipamientos`
--
ALTER TABLE `equipamientos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `estados`
--
ALTER TABLE `estados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `habilidades`
--
ALTER TABLE `habilidades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `personaje`
--
ALTER TABLE `personaje`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `poderes`
--
ALTER TABLE `poderes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `raza`
--
ALTER TABLE `raza`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `habilidades`
--
ALTER TABLE `habilidades`
  ADD CONSTRAINT `fk_habraz` FOREIGN KEY (`raza_id`) REFERENCES `raza` (`id`);

--
-- Filtros para la tabla `personaje`
--
ALTER TABLE `personaje`
  ADD CONSTRAINT `fk_est_per` FOREIGN KEY (`estado_id`) REFERENCES `estados` (`id`),
  ADD CONSTRAINT `fk_perEqu` FOREIGN KEY (`equipamiento_id`) REFERENCES `equipamientos` (`id`),
  ADD CONSTRAINT `fk_perHab` FOREIGN KEY (`habilidad_id`) REFERENCES `habilidades` (`id`),
  ADD CONSTRAINT `fk_perPod` FOREIGN KEY (`poderes_id`) REFERENCES `poderes` (`id`),
  ADD CONSTRAINT `fk_perRaz` FOREIGN KEY (`raza_id`) REFERENCES `raza` (`id`),
  ADD CONSTRAINT `fk_perUsu` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `poderes`
--
ALTER TABLE `poderes`
  ADD CONSTRAINT `fk_podRaz` FOREIGN KEY (`raza_id`) REFERENCES `raza` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
