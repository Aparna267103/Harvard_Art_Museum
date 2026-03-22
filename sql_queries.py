queries = {
"1. List all artifacts from the 11th century belonging to Byzantine culture":
"""
SELECT *
FROM artifact_metadata
WHERE century = '11th century'
AND culture='Byzantine'
""",

"2. What are the unique cultures represented in the artifacts":
"""
SELECT DISTINCT culture
FROM artifact_metadata
""",

"3. List all artifacts from the Archaic Period":
"""
SELECT *
FROM artifact_metadata
WHERE LOWER(period) LIKE '%%archaic%%'
""",

"4. List artifact titles ordered by accession year in descending order":
"""
SELECT title, accessionyear
FROM artifact_metadata
ORDER BY accessionyear DESC
""",

"5. How many artifacts are there per department":
"""
SELECT department, COUNT(*) AS total
FROM artifact_metadata
GROUP BY department
""",

"6. Which artifacts have more than 1 image":
"""
SELECT id, title,
       CASE WHEN description LIKE '%%image%%' OR description LIKE '%%images%%' 
            THEN 'Has images' 
            ELSE 'Unknown image count' END as image_status
FROM artifact_metadata
WHERE description LIKE '%%image%%' OR description LIKE '%%images%%'
LIMIT 20;
""",

"7. What is the average artifact_rank of all artifacts":
"""
SELECT AVG(artifact_rank) AS avg_rank
FROM artifact_media
""",

"8. Which artifacts have a higher colorcount than mediacount":
"""
SELECT objectid, colorcount, mediacount
FROM artifact_media
WHERE colorcount > mediacount
""",

"9. List all artifacts created between 1500 and 1600":
"""
SELECT id, title, accessionyear, century
FROM artifact_metadata
WHERE accessionyear BETWEEN 1500 AND 1600
   OR century LIKE '%%16th%%'
LIMIT 20
""",

"10. How many artifacts have no media files":
"""
SELECT COUNT(*) AS artifacts_without_media
FROM artifact_metadata
""",

"11. What are all the distinct hues used in the dataset":
"""
SELECT DISTINCT hue
FROM artifact_colors
ORDER BY hue
""",

"12. What are the top 5 most used colors by frequency":
"""
SELECT color, COUNT(*) AS freq
FROM artifact_colors
GROUP BY color
ORDER BY freq DESC
LIMIT 5
""",

"13. What is the average coverage percentage for each hue":
"""
SELECT hue, AVG(percent) AS avg_percent
FROM artifact_colors
GROUP BY hue
ORDER BY hue
""",

"14. List all colors used for a given artifact ID":
"""
SELECT objectid, color, hue, percent
FROM artifact_colors
WHERE objectid = objectid
ORDER BY percent DESC
""",

"15. What is the total number of color entries in the dataset":
"""
SELECT COUNT(*) AS total_color_entries
FROM artifact_colors
""",

"16. List artifact titles and hues for all artifacts belonging to Byzantine culture":
"""
SELECT m.title, c.hue
FROM artifact_metadata m
JOIN artifact_colors c ON m.id = c.objectid
WHERE m.culture ='Byzantine'
LIMIT 20
""",

"17. List each artifact title with its associated hues":
"""
SELECT m.title, c.hue
FROM artifact_metadata m
JOIN artifact_colors c ON m.id = c.objectid
LIMIT 20
""",

"18. Get artifact titles, cultures, and media ranks where the period is not null":
"""
SELECT m.title, m.culture, media.artifact_rank
FROM artifact_metadata m
JOIN artifact_media media ON m.id = media.objectid
WHERE m.period IS NOT NULL
LIMIT 20
""",

"19. Find artifact titles ranked in the top 10 that include the color hue Grey":
"""
SELECT m.title, media.artifact_rank
FROM artifact_metadata m
JOIN artifact_media media ON m.id=media.objectid
JOIN artifact_colors c ON m.id=c.objectid
WHERE c.hue='Grey'
ORDER BY media.artifact_rank
LIMIT 10
""",

"20. How many artifacts exist per classification, and the average media count":
"""
SELECT m.classification,
COUNT(*) AS total_artifacts,
AVG(media.mediacount) AS avg_media
FROM artifact_metadata m
JOIN artifact_media media ON m.id = media.objectid
GROUP BY m.classification
ORDER BY total_artifacts DESC
"""
}
