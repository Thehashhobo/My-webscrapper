-- Create Database and Tables for RecipeDB
CREATE DATABASE Recipedb;
USE RecipeDB;

-- Main Recipes Table
CREATE TABLE Recipes (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(500),
    time VARCHAR(50),
    rating FLOAT,
    image_url VARCHAR(500),
    overview TEXT
);

-- Ingredients Table (One-to-Many Relationship)
CREATE TABLE Ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT,
    ingredient VARCHAR(255) NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id) ON DELETE CASCADE
);

-- Instructions Table (One-to-Many Relationship)
CREATE TABLE Instructions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT,
    step_order INT NOT NULL,
    instruction TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(id) ON DELETE CASCADE
);
-- Ensure Database supports Unicode format utf8mb4
ALTER DATABASE Recipedb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert Recipes table
ALTER TABLE Recipes CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE Recipes 
MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
MODIFY url VARCHAR(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
MODIFY time VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
MODIFY image_url VARCHAR(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
MODIFY overview TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- Convert Ingredients table
ALTER TABLE Ingredients CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE Ingredients 
MODIFY ingredient VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert Instructions table
ALTER TABLE Instructions CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE Instructions 
MODIFY instruction TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Increase group_concat_max_len to handle large concatenated strings from instructions
SET SESSION group_concat_max_len = 16384;