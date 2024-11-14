import models
from flask import Flask, render_template, request, redirect, url_for, session
from models import get_listing_by_id


# Handle user login
def login_user(username, password, user_type):
    user = models.validate_user(username, password, user_type)
    return user

# Handle user logout
#def logout_user():
#    session.clear()

# Render the index page with listings

def get_shortlisted_listings(user_id):
    listings = models.get_shortlisted_listings(user_id)
    return listings

def get_all_submitted_dealership():
    listings = models.get_all_submitted_dealership()
    return listings

def render_index():
    normal_listings = models.get_normal_listings()
    premium_listings = models.get_premium_listings()
    return normal_listings, premium_listings

def view_listing(listing_id):
    listing = models.get_listing_by_id(listing_id)  
    return listing  

def shortlist_listing(user_id,listing_id):
    return models.save_listing_for_user(user_id,listing_id)

# Create a new car listing
def create_listing(form_data, image_files,user_id , dealer_name):
    
    listing_type = form_data.get('listing_type')
    seller_name = form_data.get('sellerName')
    car_name = form_data.get('carName')
    price = form_data.get('price')
    depreciation = form_data.get('depreciation')
    mileage = form_data.get('mileage')
    road_tax = form_data.get('roadTax')
    dereg_value = form_data.get('deregValue')
    coe = form_data.get('coe')
    engine_cap = form_data.get('engineCap')
    curb_weight = form_data.get('curbWeight')
    vehicle_type = form_data.get('vehicleType')
    reg_date = form_data.get('regDate')
    manufactured = form_data.get('manufactured')
    transmission = form_data.get('transmission')
    omv = form_data.get('omv')
    arf = form_data.get('arf')
    power = form_data.get('power')
    num_owners = form_data.get('numOwners')
    user_id = user_id
    dealer_name = dealer_name

    # Convert images to paths
    image_paths = []
    for image in image_files:
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        image_paths.append(image_path)

    # Call the model function to insert the listing
    return models.insert_car_listing(listing_type, seller_name ,car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                              engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                              power, num_owners, image_paths, user_id , dealer_name)


def update_listing(listing_id,form_data, image_files,user_id , dealer_name):
    
    listing_type = form_data.get('listing_type')
    seller_name = form_data.get('sellerName')
    car_name = form_data.get('carName')
    price = form_data.get('price')
    depreciation = form_data.get('depreciation')
    mileage = form_data.get('mileage')
    road_tax = form_data.get('roadTax')
    dereg_value = form_data.get('deregValue')
    coe = form_data.get('coe')
    engine_cap = form_data.get('engineCap')
    curb_weight = form_data.get('curbWeight')
    vehicle_type = form_data.get('vehicleType')
    reg_date = form_data.get('regDate')
    manufactured = form_data.get('manufactured')
    transmission = form_data.get('transmission')
    omv = form_data.get('omv')
    arf = form_data.get('arf')
    power = form_data.get('power')
    num_owners = form_data.get('numOwners')
    user_id = user_id
    dealer_name = dealer_name
    listing_id = listing_id
    

    # Convert images to paths
    image_paths = []
    for image in image_files:
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        image_paths.append(image_path)

    print("a.py",user_id)
    print("a.py",dealer_name)
    # Call the model function to insert the listing
    return models.update_car_listing(listing_id,listing_type, seller_name ,car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                              engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                              power, num_owners, image_paths, user_id , dealer_name)

def delete_listing(listing_id):
    return models.delete_listing(listing_id)

# Submit to dealership
def submit_dealership(form_data, image_files , seller_name):
    
    listing_type = form_data.get('listing_type')
    dealer_name = form_data.get('dealerName')
    car_name = form_data.get('carName')
    price = form_data.get('price')
    depreciation = form_data.get('depreciation')
    mileage = form_data.get('mileage')
    road_tax = form_data.get('roadTax')
    dereg_value = form_data.get('deregValue')
    coe = form_data.get('coe')
    engine_cap = form_data.get('engineCap')
    curb_weight = form_data.get('curbWeight')
    vehicle_type = form_data.get('vehicleType')
    reg_date = form_data.get('regDate')
    manufactured = form_data.get('manufactured')
    transmission = form_data.get('transmission')
    omv = form_data.get('omv')
    arf = form_data.get('arf')
    power = form_data.get('power')
    num_owners = form_data.get('numOwners')
   
    seller_name = seller_name

    # Convert images to paths
    image_paths = []
    for image in image_files:
        image_path = f"static/seller_uploads/{image.filename}"
        image.save(image_path)
        image_paths.append(image_path)

    # Call the model function to insert the listing
    models.insert_seller_submission(listing_type, dealer_name ,car_name, price, depreciation, mileage, road_tax, dereg_value, coe, 
                              engine_cap, curb_weight, vehicle_type, reg_date, manufactured, transmission, omv, arf, 
                              power, num_owners, image_paths, seller_name)

def get_filtered_listings(filters):
    listings = models.get_filtered_listings(filters)
    return listings

def get_normal_listings():
    listings = models.get_normal_listings()
    return listings

def get_premium_listings():
    listings = models.get_premium_listings()
    return listings


def submit_registration(form_data, image_files):
    
    username = form_data.get('username')
    email = form_data.get('email')
    password = form_data.get('password')
    name = form_data.get('name')
    description = form_data.get('description')
    phone_number = form_data.get('phone_number')
    user_type = form_data.get('user_type')
    

    # Convert images to paths
    image_paths = []
    for image in image_files:
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        image_paths.append(image_path)

    # Call the model function to insert the listing
    models.submit_registration(username,email,password,name,description,phone_number,user_type, image_paths)

def get_seller_profile(user_id):
    return models.get_profile(user_id)

def save_review(user_id, dealer_id,listing_id, rating, review):
        return models.save_review(user_id,dealer_id,listing_id,rating,review)

def get_dealer_id(listing_id):
    dealer_id = models.get_dealer_id(listing_id)
    return dealer_id

def get_reviews_for_user(user_id):
    return models.get_reviews_for_user(user_id)

def get_dealerships():
    return models.get_dealerships()

def get_all_users():
    user_profiles = models.get_all_users()
    return user_profiles

def get_all_listings():
    listings = models.get_all_listings()
    return listings

def update_user_in_db(user_id, username,password, email, name, description, phone_number, user_type):
   return models.update_user_in_db(user_id, username,password, email, name, description, phone_number, user_type)

def deactivate_user_in_db(user_id):
    return models.deactivate_user_in_db(user_id)

def admin_register_user(form_data,image_files):
    username = form_data.get('username')
    email = form_data.get('email')
    password = form_data.get('password')
    name = form_data.get('name')
    description = form_data.get('description')
    phone_number = form_data.get('phone_number')
    user_type = form_data.get('user_type')
    

    # Convert images to paths
    image_paths = []
    for image in image_files:
        image_path = f"static/uploads/{image.filename}"
        image.save(image_path)
        image_paths.append(image_path)

    # Call the model function to insert the listing
    return models.admin_register_user(username,email,password,name,description,phone_number,user_type, image_paths)
   
def get_user_type_permissions():
    return models.get_user_type_permissions()


def add_user_type(user_type,user_type_name,create_listing,delete_listing,update_listing,view_listing):
    return models.add_user_type(user_type,user_type_name,create_listing,delete_listing,update_listing,view_listing)


def get_user_ids_by_type(user_type):
    return models.get_user_ids_by_type(user_type)

def update_user_type_permissions_in_db(
        id, user_type, create_listing, delete_listing, update_listing, view_listing, user_type_name
    ):
    return models.update_user_type_permissions_in_db(id, user_type, create_listing, delete_listing, update_listing, view_listing, user_type_name)