-- Q1: What is the best carpark for The Helix?

	SELECT `Name` FROM `TABLE 2` WHERE `Nearby facilities` LIKE '%Helix%'

-- Q2: How many disabled carpark spaces are there on each campus?

	SELECT `Campus`, SUM(`Number of disabled spaces`) AS `Number of Disabled Spaces` FROM `TABLE 2` GROUP BY `Campus` ORDER BY `Number of disabled spaces` DESC;	

-- Q3: Historically, how occupied is St. Pats carpark in week 6 between 10am and 11am?

	SELECT `10` FROM `TABLE 1` WHERE `Car Park Name` LIKE '%Pats%' AND `Week of Yr`=6;

-- Q4: Where can a member of the general public park after 5pm on 18th of September? Answer should provide _both_ campus name and car park name.

	SELECT `Name`, `Campus` FROM `TABLE 2` WHERE `Available for` LIKE '%public%' AND CAST(SUBSTRING(`Opening hours`, 9, 2) AS SIGNED)>17;

-- Q5: When is the best time to arrive at DCU Glasnevin to be able to park near Invent?

SELECT `Car Park Name`, LEAST (8am, 9am, 10am, 11am, 12pm, 1pm, 2pm, 3pm, 4pm, 5pm, 6pm, 7pm, 8pm, 9pm) AS 9am FROM (SELECT `Car Park Name`, AVG(`8`) AS 8am, AVG(`9`) AS 9am, AVG(`10`) AS 10am, AVG(`11`) AS 11am, AVG(`12`) AS 12pm, AVG(`13`) AS 1pm, AVG(`14`) AS 2pm, AVG(`15`) AS 3pm, AVG(`16`) AS 4pm, AVG(`17`) AS 5pm, AVG(`18`) AS 6pm, AVG(`19`) AS 7pm, AVG(`20`) AS 8pm, AVG(`21`) AS 9pm FROM `TABLE 1` WHERE `Car Park Name` LIKE '%Invent%' GROUP BY 'Car Park Name') AS subquery 	
	
