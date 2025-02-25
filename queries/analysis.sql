-- count number of recipes
SELECT COUNT(*) AS recipe_count FROM Recipes;

-- Find Duplicate Recipes
SELECT name, url, time, rating, image_url, overview, COUNT(*) AS duplicate_count
FROM Recipes
GROUP BY name, url,
HAVING COUNT(*) > 1;

-- Remove Duplicate Recipes
DELETE r1 
FROM Recipes r1
JOIN Recipes r2 
ON r1.name = r2.name 
AND r1.url = r2.url
AND r1.time = r2.time
AND r1.rating = r2.rating
AND r1.image_url = r2.image_url
AND r1.overview = r2.overview
AND r1.id > r2.id;  -- Ensures we keep the recipe with the lowest ID

-- show complete recipe details
SELECT 
    r.id AS Recipe_ID,
    r.name AS Recipe_Name, 
    r.url AS Recipe_URL,
    r.time AS Cooking_Time, 
    r.rating AS Rating,
    r.image_url AS Image_URL,
    r.overview AS Overview,
    GROUP_CONCAT(DISTINCT i.ingredient ORDER BY i.ingredient ASC SEPARATOR ', ') AS Ingredients,
    GROUP_CONCAT(DISTINCT CONCAT(instr.step_order, '. ', instr.instruction) ORDER BY instr.step_order ASC SEPARATOR '\n') AS Instructions
FROM Recipes r
LEFT JOIN Ingredients i ON r.id = i.recipe_id
LEFT JOIN Instructions instr ON r.id = instr.recipe_id
WHERE r.name LIKE '%Boilermaker Tailgate Chili%'  -- Replace with actual recipe name or partial match
GROUP BY r.id, r.name, r.url, r.time, r.rating, r.image_url, r.overview;


-- Top 10 recipes by rating
SELECT name, rating 
FROM Recipes 
ORDER BY rating DESC 
LIMIT 10;

-- Top 10 recipes by cooking time and ratings (prefer faster recipes)
SELECT name, rating, time
FROM Recipes
WHERE time REGEXP '^[0-9]+ mins$'  -- Ensures we only extract numerical time values
ORDER BY CAST(REPLACE(time, ' mins', '') AS UNSIGNED) ASC
LIMIT 10;


-- Most Common Ingredients
SELECT ingredient, COUNT(*) AS usage_count 
FROM Ingredients 
GROUP BY ingredient 
ORDER BY usage_count DESC 
LIMIT 10;

-- Recipes with the Most Ingredients
SELECT r.name, COUNT(i.id) AS ingredient_count
FROM Recipes r
JOIN Ingredients i ON r.id = i.recipe_id
GROUP BY r.name
ORDER BY ingredient_count DESC
LIMIT 10;

-- Fastest Cooking Recipes
SELECT name, time
FROM Recipes

-- Most Complex Recipes
SELECT r.name, COUNT(i.id) AS step_count
FROM Recipes r
JOIN Instructions i ON r.id = i.recipe_id
GROUP BY r.name
ORDER BY step_count DESC
LIMIT 10;

-- Distribution of Ratings
SELECT 
    FLOOR(rating) AS rating_range, 
    COUNT(*) AS recipe_count
FROM Recipes
GROUP BY rating_range
ORDER BY rating_range DESC;

