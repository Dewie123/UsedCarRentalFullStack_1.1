import mysql.connector

# Establish a connection to your database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="project_db",
    port=3305
)

def validate_user(username, password, user_type):
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password = %s AND user_type = %s"
    cursor.execute(query, (username, password, user_type))
    user = cursor.fetchone()
    cursor.close()
    return user

def insert_seller_submission(listing_type,dealer_name ,car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                       engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                       power, num_owners, images, seller_name):
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO SubmitDealership (listing_type,carName, price, depreciation, mileage, roadTax, deregValue, coe, 
                                      engineCap, curbWeight, vehicleType, regDate, manufactured, transmission, omv, arf, 
                                      power, numOwners,sellerName,dealerName) 
            VALUES (%s,%s ,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (listing_type, car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                               engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                               power, num_owners,seller_name,dealer_name))
        listing_id = cursor.lastrowid

        if images:
            for img_path in images:
                cursor.execute("""
                INSERT INTO seller_listing_images (listing_id, image_path)
                VALUES (%s, %s)""", (listing_id, img_path))
        
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()


def insert_car_listing(listing_type,seller_name ,car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                       engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                       power, num_owners, images, user_id, dealer_name):
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO CarListings (listing_type,carName, price, depreciation, mileage, roadTax, deregValue, coe, 
                                      engineCap, curbWeight, vehicleType, regDate, manufactured, transmission, omv, arf, 
                                      power, numOwners, user_id,sellerName,dealerName) 
            VALUES (%s,%s ,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (listing_type, car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                               engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                               power, num_owners, user_id,seller_name,dealer_name))
        listing_id = cursor.lastrowid

        if images:
            for img_path in images:
                cursor.execute("""
                INSERT INTO listing_images (listing_id, image_path)
                VALUES (%s, %s)""", (listing_id, img_path))
        
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()


def insert_car_listing(listing_type,seller_name ,car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                       engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                       power, num_owners, images, user_id, dealer_name):
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO CarListings (listing_type,carName, price, depreciation, mileage, roadTax, deregValue, coe, 
                                      engineCap, curbWeight, vehicleType, regDate, manufactured, transmission, omv, arf, 
                                      power, numOwners, user_id,sellerName,dealerName) 
            VALUES (%s,%s ,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (listing_type, car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                               engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                               power, num_owners, user_id,seller_name,dealer_name))
        listing_id = cursor.lastrowid

        if images:
            for img_path in images:
                cursor.execute("""
                INSERT INTO listing_images (listing_id, image_path)
                VALUES (%s, %s)""", (listing_id, img_path))
        
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        return True


def update_car_listing(listing_id, listing_type, seller_name, car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                       engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                       power, num_owners, images, user_id, dealer_name):
    
    print("m.py",user_id)
    print("m.py",dealer_name)
    try:
        cursor = conn.cursor()
        # Update the CarListings table
        query = """
            UPDATE CarListings 
            SET listing_type = %s, carName = %s, price = %s, depreciation = %s, mileage = %s, roadTax = %s, deregValue = %s, coe = %s, 
                engineCap = %s, curbWeight = %s, vehicleType = %s, regDate = %s, manufactured = %s, transmission = %s, omv = %s, arf = %s, 
                power = %s, numOwners = %s, sellerName = %s, dealerName = %s, user_id = %s
            WHERE id = %s
        """
        cursor.execute(query, (listing_type, car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                               engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                               power, num_owners, seller_name, dealer_name, user_id, listing_id))
        
        # Delete existing images related to this listing
        cursor.execute("DELETE FROM listing_images WHERE listing_id = %s", (listing_id,))
        
        # Insert new images if any
        if images:
            for img_path in images:
                cursor.execute(""" 
                INSERT INTO listing_images (listing_id, image_path)
                VALUES (%s, %s)""", (listing_id, img_path))
        
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        return True

def delete_listing(listing_id):
    try:
        cursor = conn.cursor()

        # Delete the images associated with this listing
        cursor.execute("DELETE FROM listing_images WHERE listing_id = %s", (listing_id,))

        # Delete the listing from the CarListings table
        cursor.execute("DELETE FROM CarListings WHERE id = %s", (listing_id,))
            
        conn.commit()
        return True
        
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        return True

def get_normal_listings():
    query = """
    SELECT cl.id,cl.carName, cl.price, 
           (SELECT li.image_path 
            FROM listing_images li 
            WHERE li.listing_id = cl.id 
            LIMIT 1) as image_path
    FROM CarListings cl
    WHERE cl.listing_type = 'normal'
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    listings = cursor.fetchall()
    for listing in listings:
        listing['image_path'] = listing['image_path'].replace('static/', '').replace('\\', '/')
        listing['image_path'] = listing['image_path'].split(',')[0]
    return listings

def get_premium_listings():
    query = """
    SELECT cl.id,cl.carName, cl.price, 
           (SELECT li.image_path 
            FROM listing_images li 
            WHERE li.listing_id = cl.id 
            LIMIT 1) as image_path
    FROM CarListings cl
    WHERE cl.listing_type = 'premium'
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    listings = cursor.fetchall()
    for listing in listings:
        listing['image_path'] = listing['image_path'].replace('static/', '').replace('\\', '/')
        listing['image_path'] = listing['image_path'].split(',')[0]
    return listings

def get_all_submitted_dealership():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM SubmitDealership")
    listing = cursor.fetchall()  
    cursor.close()
    print("DEBUG: Retrieved listing:", listing)
    return listing

def get_listing_by_id(listing_id):
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CarListings cl WHERE id = %s", (listing_id,))
    listing = cursor.fetchone()  
    cursor.execute("SELECT image_path FROM listing_images WHERE listing_id = %s", (listing_id,))
    images = cursor.fetchall()  
    cursor.execute("SELECT COUNT(listing_id) FROM SavedListings WHERE listing_id = %s",(listing_id,))
    shortlistCount = cursor.fetchone()
    image_paths = [img['image_path'].replace('static/', '').replace('\\', '/') for img in images]
    listing['image_paths'] = image_paths
    listing['shortlist_count'] = shortlistCount
    cursor.close()
    print("DEBUG: Retrieved listing:", listing)
    return listing


def save_listing_for_user(user_id, listing_id):
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO SavedListings (user_id, listing_id)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE listing_id = listing_id
        """
        cursor.execute(query, (user_id, listing_id))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while saving the listing: {e}")
        conn.rollback()
    finally:
        cursor.close()
        return True



def get_shortlisted_listings(user_id):
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT cl.id, cl.carName, cl.price, MIN(li.image_path) as image_path
        FROM CarListings cl
        JOIN SavedListings sl ON cl.id = sl.listing_id
        JOIN listing_images li ON li.listing_id = cl.id 
        WHERE sl.user_id = %s
        GROUP BY cl.id, cl.carName, cl.price
    """
    cursor.execute(query, (user_id,))
    listings = cursor.fetchall()
    cursor.close()
    return listings


def get_filtered_listings(filters):
    cursor = conn.cursor(dictionary=True)

    print("Filter Values:")
    print(f"Car Model: {filters.car_model}")
    print(f"Min Price: {filters.min_price}")
    print(f"Max Price: {filters.max_price}")
    print(f"Depreciation: {filters.depreciation}")
    print(f"Registration Date: {filters.reg_date}")

    
    
    if filters.reg_date:
        reg_date_query = "regDate <= %s"
        reg_date_param = (filters.reg_date,)
    else:
        reg_date_query = "1=1"  
        reg_date_param = ()

   
    query = """
        SELECT cl.id, cl.carName, cl.price, MIN(li.image_path) as image_path
        FROM CarListings cl
        JOIN listing_images li ON li.listing_id = cl.id
        WHERE (carName LIKE %s OR %s = '')
          AND (price >= %s)
          AND (price <= %s OR %s = 0)
          AND (depreciation <= %s)
          AND {}
        GROUP BY cl.id, cl.carName, cl.price
    """.format(reg_date_query)

    
    params = (
        f"%{filters.car_model}%", filters.car_model,
        filters.min_price,
        filters.max_price, filters.max_price,
        filters.depreciation,
        *reg_date_param,  
    )
    
    cursor.execute(query, params)
    listings = cursor.fetchall()
    cursor.close()
    return listings


def submit_registration(username, email, password, name, description, phone_number, user_type, image_paths):
    try:
        cursor = conn.cursor()
        
        # Insert into the users table
        user_query = """
            INSERT INTO users (username, password, user_type)
            VALUES (%s, %s, %s)
        """
        cursor.execute(user_query, (username, password, user_type))
        
        # Get the generated user_id
        user_id = cursor.lastrowid
        
        # Insert into the AccountDetails table
        details_query = """
            INSERT INTO AccountDetails (name, description, phone_number, email, user_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(details_query, (name, description, phone_number, email,user_id))
        
        # Insert each image path into the AccountImages table
        if image_paths:
            for img_path in image_paths:
                image_query = """
                    INSERT INTO AccountImages (user_id, image_path)
                    VALUES (%s, %s)
                """
                cursor.execute(image_query, (user_id, img_path))
        
        # Commit the transaction
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()


def admin_register_user(username, email, password, name, description, phone_number, user_type, image_paths):
    try:
        cursor = conn.cursor()
        
        # Insert into the users table
        user_query = """
            INSERT INTO users (username, password, user_type)
            VALUES (%s, %s, %s)
        """
        cursor.execute(user_query, (username, password, user_type))
        
        # Get the generated user_id
        user_id = cursor.lastrowid
        
        # Insert into the AccountDetails table
        details_query = """
            INSERT INTO AccountDetails (name, description, phone_number, email, user_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(details_query, (name, description, phone_number, email,user_id))
        
        # Insert each image path into the AccountImages table
        if image_paths:
            for img_path in image_paths:
                image_query = """
                    INSERT INTO AccountImages (user_id, image_path)
                    VALUES (%s, %s)
                """
                cursor.execute(image_query, (user_id, img_path))
        
        # Commit the transaction
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        return True

def get_profile(user_id):
    try:
        cursor = conn.cursor(dictionary=True)
        
        # Retrieve account details for the user
        cursor.execute("""
            SELECT a.name, a.description, a.phone_number, a.email, ai.image_path
            FROM AccountDetails a
            LEFT JOIN AccountImages ai ON a.user_id = ai.user_id
            WHERE a.user_id = %s
        """, (user_id,))
        
        profile_data = cursor.fetchone()
        
        # Retrieve car listings for the user (either as dealer or seller)
        cursor.execute("""
            SELECT cl.id, cl.carName, cl.mileage, cl.price, MIN(li.image_path) AS image_path
            FROM CarListings cl
            LEFT JOIN listing_images li ON cl.id = li.listing_id
            WHERE cl.user_id = %s OR cl.sellerName = (SELECT name FROM AccountDetails WHERE user_id = %s)
            GROUP BY cl.id
        """, (user_id, user_id))
        
        listings = cursor.fetchall()

        cursor.execute("""
            SELECT user_type
            FROM users
            
            WHERE id = %s
        """, (user_id,))

        profile_data['user_type'] = cursor.fetchone()

        cursor.execute("""
            SELECT COUNT(sl.listing_id) AS saved_count
            FROM CarListings cl
            LEFT JOIN SavedListings sl ON cl.id = sl.listing_id
            WHERE cl.sellerName = (
                SELECT u.username FROM users u WHERE u.id = %s
            )
            GROUP BY cl.id
        """, (user_id,))

        
        shortlistCount = cursor.fetchone()
        profile_data['shortlist_count'] = shortlistCount
        
        
        # If listings exist, include them in the profile data
        if listings:
            profile_data['listings'] = listings
        else:
            profile_data['listings'] = None  # No listings for this user
        
        return profile_data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        cursor.close()


def save_review(user_id, dealer_id, listing_id, rating, review):

    print (user_id,dealer_id,listing_id,rating,review)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Reviews (user_id, dealer_id, listing_id, rating, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (user_id, dealer_id, listing_id, rating, review))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        cursor.close()

def get_dealer_id(listing_id):
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM CarListings WHERE id = %s", (listing_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        cursor.close()


def get_reviews_for_user(user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT rating, description, created_at , user_id 
            FROM Reviews 
            WHERE dealer_id = %s
            ORDER BY created_at DESC
        """, (user_id,))
        reviews = cursor.fetchall()
        return reviews if reviews else []
    except Exception as e:
        print(f"An error occurred while fetching reviews: {e}")
        return []
    finally:
        cursor.close()


def get_dealerships():
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.name, a.description, a.phone_number, a.email, ai.image_path , a.user_id
            FROM AccountDetails a
            LEFT JOIN AccountImages ai ON a.user_id = ai.user_id
            LEFT JOIN users u ON a.user_id = u.id
            WHERE u.user_type = 3
        """)
        dealerships = cursor.fetchall()  # This will return a list of tuples
        return dealerships
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        cursor.close()


def get_all_users():
    try: 
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.id AS user_id, u.username,u.password ,u.user_type, 
            ad.name, ad.email, ad.phone_number, ad.description, 
            ai.image_path , u.status
            FROM users u
            JOIN AccountDetails ad ON u.id = ad.user_id
            LEFT JOIN AccountImages ai ON u.id = ai.user_id;   
                       """)
        user_profiles = cursor.fetchall()
        return user_profiles
    except Exception as e:
        print (f"An error occured: {e}")
        return []
    finally:
        cursor.close()

def get_all_listings():
    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT cl.id AS listing_id, cl.carName, cl.price, cl.mileage, cl.depreciation,
        cl.roadTax, cl.deregValue, cl.coe, cl.engineCap, cl.curbWeight, cl.vehicleType,
        cl.regDate, cl.manufactured, cl.transmission, cl.omv, cl.arf, cl.power, cl.numOwners,
        cl.dealerName, cl.sellerName,
        GROUP_CONCAT(li.image_path ORDER BY li.id ASC) AS image_paths
        FROM CarListings cl
        LEFT JOIN listing_images li ON cl.id = li.listing_id
        GROUP BY cl.id;
                       """)
        listings = cursor.fetchall()
        return listings
    except Exception as e:
        print (f"An error occured: {e}")
        return []
    finally:
        cursor.close()


def update_user_in_db(user_id, username, password, email, name, description, phone_number, user_type):
    """Update user information in the database"""
    
    cursor = conn.cursor()
    
    
    # Update users table (username, password, user_type)
    update_users_query = """
    UPDATE users
    SET username = %s, password = %s, user_type = %s
    WHERE id = %s
    """
    cursor.execute(update_users_query, (username, password, user_type, user_id))
    print("Executing query:", update_users_query)
    print("With parameters:", (username, password, user_type, user_id)) 
    
    # Update AccountDetails table (name, email, phone_number, description)
    update_account_details_query = """
    UPDATE AccountDetails
    SET name = %s, email = %s, phone_number = %s, description = %s
    WHERE user_id = %s
    """
    cursor.execute(update_account_details_query, (name, email, phone_number, description, user_id))
    print("Executing query:", update_account_details_query)
    print("With parameters:", (username, password, user_type, user_id))

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    
    # Return True if the update was successful (at least one row updated in both tables)
    return cursor.rowcount > 0

def deactivate_user_in_db(user_id):
    """Deactivate user by updating status in the database"""
    
    cursor = conn.cursor()

    # Update the status to 'inactive' in the users table
    update_status_query = """
    UPDATE users
    SET status = 'inactive'
    WHERE id = %s
    """
    cursor.execute(update_status_query, (user_id,))
    
    # Commit the changes and close the connection
    conn.commit()
    cursor.close()

    # Return True if the update was successful (at least one row updated)
    if cursor.rowcount > 0:
        return {"success": True, "message": "User deactivated successfully"}
    else:
        return {"success": False, "message": "Failed to deactivate user"}
    

def get_user_type_permissions():
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM user_type_permissions
                       """)
    
    user_type_permissions = cursor.fetchall()

    return user_type_permissions


def add_user_type(user_type,user_type_name,create_listing,delete_listing,update_listing,view_listing):

    cursor = conn.cursor()
    query = """
        INSERT INTO user_type_permissions (user_type, create_listing, delete_listing, update_listing, view_listing , user_type_name)
            VALUES (%s, %s, %s, %s, %s, %s)
                       """
    cursor.execute(query, (user_type, create_listing, delete_listing, update_listing, view_listing, user_type_name))
    conn.commit()
    cursor.close()
    return True

def get_user_ids_by_type(user_type):
    query = "SELECT id FROM users WHERE user_type = %s"
    cursor = conn.cursor()
    cursor.execute(query, (user_type,))
    result = cursor.fetchall()
    cursor.close()
    return [row[0] for row in result]



def update_user_type_permissions_in_db(id, user_type, create_listing, delete_listing, update_listing, view_listing, user_type_name):
    
    cursor = conn.cursor()

    query = """
        UPDATE user_type_permissions
        SET
            user_type = %s,
            create_listing = %s,
            delete_listing = %s,
            update_listing = %s,
            view_listing = %s,
            user_type_name = %s
        WHERE id = %s;
        """
    cursor.execute(query,(user_type,create_listing,delete_listing,update_listing,view_listing,user_type_name,id))

    conn.commit()
    cursor.close()
    return True
