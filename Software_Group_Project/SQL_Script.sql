CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,  -- Storing hashed password
    user_type TINYINT NOT NULL,  -- 1: Buyer, 2: Individual Seller, 3: Dealership, 4: Admin
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO users (username, password, user_type)
VALUES 
('buyer1', 'buyer1pw', 1),  -- Buyer
('seller1', 'seller1pw', 2),  -- Individual Seller
('dealer1', 'dealer1pw', 3),  -- Dealership
('admin1', 'admin1pw', 4);   -- Admin

ALTER TABLE users
ADD status VARCHAR(255) DEFAULT 'active';

UPDATE users SET status = 'active' WHERE id = 5;


SELECT * FROM users;
SELECT * FROM AccountDetails;
SELECT * FROM AccountImages;
SELECT * FROM Reviews;
CREATE TABLE AccountDetails (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    phone_number INT,
    email VARCHAR(100),
    user_id INT, 
    FOREIGN KEY (user_id) REFERENCES Users(id) );
    
SELECT a.name, a.description, a.phone_number, a.email, ai.image_path
            FROM AccountDetails a
            LEFT JOIN AccountImages ai ON a.user_id = ai.user_id
            LEFT JOIN users u ON a.user_id = u.id
            WHERE u.user_type = 3;
    
    

CREATE TABLE AccountImages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    image_path VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES AccountDetails(user_id)
);


    
SELECT * FROM Reviews;

CREATE TABLE Reviews (
	id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    user_id INT, 
    FOREIGN KEY (user_id) REFERENCES Users(id) );
    
ALTER TABLE Reviews
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

DELETE FROM Reviews;

SELECT * FROM AccountDetails;
show databases;

DELETE FROM users;

SELECT * FROM USERS;

SET SQL_SAFE_UPDATES = 0;

ALTER TABLE users

DROP COLUMN created_at;

ALTER TABLE CarListings

DROP COLUMN images;

use project_db;
CREATE DATABASE project_db;


SHOW GRANTS FOR 'root'@'localhost';
GRANT ALL PRIVILEGES ON project_db.* TO 'root'@'localhost';

DELETE FROM CarListings;
SELECT * FROM CarListings;
SELECT user_id FROM CarListings WHERE id = 31;
CREATE TABLE CarListings (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each listing
    listing_type ENUM('normal', 'premium') NOT NULL,  -- Listing type (Normal or Premium)
    carName VARCHAR(255) NOT NULL,             -- Name of the vehicle
    price DECIMAL(10, 2) NOT NULL,             -- Price of the vehicle
    depreciation DECIMAL(10, 2) NOT NULL,      -- Depreciation value
    mileage INT NOT NULL,                       -- Mileage in km
    roadTax DECIMAL(10, 2) NOT NULL,           -- Road tax value
    deregValue DECIMAL(10, 2) NOT NULL,        -- Deregistration value
    coe DECIMAL(10, 2) NOT NULL,               -- Certificate of Entitlement value
    engineCap INT NOT NULL,                     -- Engine capacity in cc
    curbWeight INT NOT NULL,                    -- Curb weight in kg
    vehicleType VARCHAR(100) NOT NULL,         -- Type of vehicle
    regDate DATE NOT NULL,                      -- Registration date
    manufactured YEAR NOT NULL,                 -- Manufactured year
    transmission ENUM('auto', 'manual') NOT NULL,  -- Transmission type
    omv DECIMAL(10, 2) NOT NULL,               -- Open Market Value
    arf DECIMAL(10, 2) NOT NULL,                -- Additional Registration Fee
    power DECIMAL(10, 2) NOT NULL,             -- Power in kW
    numOwners INT NOT NULL          -- Number of owners
);
ALTER TABLE CarListings
ADD COLUMN dealerName VARCHAR(100);

ALTER TABLE CarListings
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(id);



CREATE TABLE SubmitDealership (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each listing
    listing_type ENUM('normal', 'premium') NOT NULL,  -- Listing type (Normal or Premium)
    carName VARCHAR(255) NOT NULL,             -- Name of the vehicle
    price DECIMAL(10, 2) NOT NULL,             -- Price of the vehicle
    depreciation DECIMAL(10, 2) NOT NULL,      -- Depreciation value
    mileage INT NOT NULL,                       -- Mileage in km
    roadTax DECIMAL(10, 2) NOT NULL,           -- Road tax value
    deregValue DECIMAL(10, 2) NOT NULL,        -- Deregistration value
    coe DECIMAL(10, 2) NOT NULL,               -- Certificate of Entitlement value
    engineCap INT NOT NULL,                     -- Engine capacity in cc
    curbWeight INT NOT NULL,                    -- Curb weight in kg
    vehicleType VARCHAR(100) NOT NULL,         -- Type of vehicle
    regDate DATE NOT NULL,                      -- Registration date
    manufactured YEAR NOT NULL,                 -- Manufactured year
    transmission ENUM('auto', 'manual') NOT NULL,  -- Transmission type
    omv DECIMAL(10, 2) NOT NULL,               -- Open Market Value
    arf DECIMAL(10, 2) NOT NULL,                -- Additional Registration Fee
    power DECIMAL(10, 2) NOT NULL,             -- Power in kW
    numOwners INT NOT NULL,          -- Number of owners
    sellerName VARCHAR(255) NOT NULL,
    dealerName VARCHAR(255) NOT NULL
);

SELECT * FROM SubmitDealership;
DELETE FROM SubmitDealership;


DELETE FROM listing_images;
select * from listing_images;
CREATE TABLE listing_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id INT,
    image_path VARCHAR(255),
    FOREIGN KEY (listing_id) REFERENCES CarListings(id)
);

DELETE FROM seller_listing_images;
select * from seller_listing_images;
CREATE TABLE seller_listing_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id INT,
    image_path VARCHAR(255),
    FOREIGN KEY (listing_id) REFERENCES SubmitDealership(id)
);

DELETE FROM listing_images;
ALTER TABLE listing_images
MODIFY image_path TEXT; 

DESCRIBE listing_images;
SELECT COUNT(listing_id) FROM SavedListings WHERE listing_id = 31;
SELECT * FROM SavedListings;
DELETE FROM SavedListings;
CREATE TABLE SavedListings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    listing_id INT NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (listing_id) REFERENCES CarListings(id) ON DELETE CASCADE,
    UNIQUE (user_id, listing_id)
);

SELECT cl.id AS listing_id, cl.carName, COUNT(sl.listing_id) AS saved_count
FROM CarListings cl
LEFT JOIN SavedListings sl ON cl.id = sl.listing_id
WHERE cl.sellerName = (
    SELECT u.username FROM users u WHERE u.id = 5
)
GROUP BY cl.id