

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";




--
-- Database: `pcbuilder`
--

-- --------------------------------------------------------

--
-- Table structure for table `links`
--

CREATE TABLE `links` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `search` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `links`
--

INSERT INTO `links` (`sno`, `name`, `search`) VALUES
(1, 'gtx 1650', 'https://mdcomputers.in/zotac-gtx-1650-oc-4gb-gddr5-zt-t16500f-10l.html'),
(2, 'gtx 1650 super', 'https://mdcomputers.in/zotac-gaming-gtx-1650-super-twin-fan-zt-t16510f-10l.html'),
(3, 'display', 'https://mdcomputers.in/index.php?category_id=0&search=display&submit_search=&route=product%2Fsearch');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `links`
--
ALTER TABLE `links`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `links`
--
ALTER TABLE `links`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

