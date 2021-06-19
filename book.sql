-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2021 at 08:56 AM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `author` text NOT NULL,
  `language` text NOT NULL,
  `title` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `author`, `language`, `title`) VALUES
(1, '	Vita Sackville-West', 'English', 'All Passion Spent'),
(2, 'Madeleine L Engle', 'English', 'An Acceptable Time'),
(3, 'Robert Penn Warren', 'English', 'All the Kings Men'),
(4, 'William Faulkner', 'English', 'As I Lay Dying'),
(5, 'Michael Moorcock', 'English', 'Behold the Man'),
(6, 'James Ellroy', 'English', 'Blood a Rover'),
(7, 'Dharamvir Bharati', 'Hindi', 'Gunaho Ka Devta'),
(8, 'Kamleshwar', 'Hindi', 'Kitne Pakistan'),
(9, 'Kashinath Singh', 'Hindi', 'ashi Ka Assi'),
(10, 'Phanishwar Nath', 'Hindi', 'Maila Aanchal'),
(11, 'Mannu Bhandari', 'Hindi', 'Aapka Bunti'),
(12, 'Shrilal Shukla', 'Hindi', 'Rag Darbari');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
