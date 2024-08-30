-- CptS451_HW4_MarkShinozaki.sql
-- Mark Shinozaki
-- WSU ID: 11672355

-- Question 1: Find distinct courses that 'SYS' track students in 'CptS' major are enrolled in

SELECT DISTINCT C.courseno, C.credits
FROM Course C
JOIN Enroll E ON C.courseno = E.courseno
JOIN Student S ON E.sID = S.sID
WHERE S.major = 'CptS' AND S.trackcode = 'SYS'
ORDER BY C.courseno;


-- Question 2: Find students enrolled in more than 18 credits

SELECT S.sName, S.sID, S.major, S.trackcode, SUM(C.credits) as sum
FROM Student S
JOIN Enroll E ON S.sID = E.sID
JOIN Course C ON E.courseno = C.courseno
GROUP BY S.sName, S.sID, S.major, S.trackcode
HAVING SUM(C.credits) >= 19
ORDER BY S.sName;


-- Question 3: Find courses that only 'SE' track students in 'CptS' major have been enrolled in

SELECT DISTINCT C.courseno
FROM Course C
JOIN Enroll E ON C.courseno = E.courseno
JOIN Student S ON E.sID = S.sID
WHERE S.major = 'CptS' AND S.trackcode = 'SE'
  AND NOT EXISTS (
    SELECT 1
    FROM Enroll E2
    JOIN Student S2 ON E2.sID = S2.sID
    WHERE E2.courseno = C.courseno
      AND (S2.major != 'CptS' OR S2.trackcode != 'SE')
  );


-- Question 4: Find students enrolled in the same courses and grades as Diane

SELECT S.sName, S.sID, S.major, E.courseno, E.grade
FROM Enroll E
JOIN Student S ON E.sID = S.sID
WHERE (E.courseno, E.grade) IN (
    SELECT E2.courseno, E2.grade
    FROM Enroll E2
    JOIN Student S2 ON E2.sID = S2.sID
    WHERE S2.sName = 'Diane'
)
AND S.sName <> 'Diane'
ORDER BY S.sName, E.courseno;


-- Question 5: Find 'CptS' major students not enrolled in any classes using OUTER JOIN

SELECT S.sName, S.sID
FROM Student S
LEFT JOIN Enroll E ON S.sID = E.sID
WHERE S.major = 'CptS' AND E.sID IS NULL;


-- Question 6: Find courses in 'Sloan' building with enrollments exceeding limits
-- This was the harder question, I couldnt figure out why I couldnt query "Sloan" it was due to the names being like  'Sloan150', 'Sloan9', 'Sloan223', etc.
SELECT C.courseno, C.enroll_limit, COUNT(E.sID) as enrollnum
FROM Course C
JOIN Enroll E ON C.courseno = E.courseno
WHERE C.classroom LIKE 'Sloan%'
GROUP BY C.courseno, C.enroll_limit
HAVING COUNT(E.sID) > C.enroll_limit;


-- Question 7: Find 'CptS' major students who failed prereq for a course they are enrolled in

SELECT S.sName, S.sID, E.courseno
FROM Enroll E
JOIN Student S ON E.sID = S.sID
JOIN Prereq P ON E.courseno = P.courseNo
JOIN Enroll E2 ON S.sID = E2.sID AND E2.courseno = P.preCourseNo
WHERE S.major = 'CptS' AND E2.grade < 2;


-- Question 8: Find pass rates for each 'CptS' course

SELECT E.courseno, 
       ROUND(100.0 * SUM(CASE WHEN E.grade >= 2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS passrate
FROM Enroll E
JOIN Course C ON E.courseno = C.courseno
WHERE C.courseno LIKE 'CptS%'
GROUP BY E.courseno;


-- Question 9: Relational algebra expression explanation and equivalent SQL query

-- Explanation: The expression finds courses with at least 2 prerequisites.
-- Equivalent SQL query:
SELECT C.courseno, COUNT(P.preCourseNo) AS pcount
FROM Course C
JOIN Prereq P ON C.courseno = P.courseNo
GROUP BY C.courseno
HAVING COUNT(P.preCourseNo) >= 2;

