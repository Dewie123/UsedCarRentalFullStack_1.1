from flask import Flask, request, redirect, url_for, session, render_template , flash ,jsonify
import app  # Import the controller functions

app_boundary = Flask(__name__)
app_boundary.secret_key = '1234'  # Set up secret key for session management

@app_boundary.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
       
        # Call the login function in the controller
        user = app.login_user(username, password, user_type)
        
        if user:
            session['username'] = user['username']
            session['user_type'] = user['user_type']
            session['user_id'] = user['id']
            if user['user_type'] == 4:
                return redirect(url_for('render_admin_logged_in_page'))
            else:
                return redirect(url_for('index_logged_in'))
        else:
            flash("Invalid Credentials","error")
            return render_template('log_in.html', error="Invalid credentials")
    return render_template('log_in.html')

@app_boundary.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app_boundary.route('/')
def index():
    normal_listings, premium_listings = app.render_index()
    return render_template('index.html', normal_listings=normal_listings, premium_listings=premium_listings)

@app_boundary.route('/index_logged_in')
def index_logged_in():
    normal_listings, premium_listings = app.render_index()
    dealership_info = app.get_dealerships()

    print("dealership_info",dealership_info)
    return render_template('index_logged_in.html', normal_listings=normal_listings, premium_listings=premium_listings , dealership_info = dealership_info)

@app_boundary.route('/loan_calculator_page')
def loan_calculator_page():
    
    return render_template('loan_calculator_page.html')

@app_boundary.route('/create_listing', methods=['GET', 'POST'])
def create_listing():
    listing = app.get_all_submitted_dealership()
    if request.method == 'POST':
        form_data = request.form.to_dict()
        image_paths = request.files.getlist('images')
        user_id = session.get('user_id')
        dealer_name = session.get('username')
        
        app.create_listing(form_data, image_paths , user_id , dealer_name)
        return redirect(url_for('index_logged_in'))
    
    return render_template('create_listing_seller.html', listing=listing)

@app_boundary.route('/submit_dealership', methods=['GET', 'POST'])
def submit_dealership():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        image_paths = request.files.getlist('images')
        
        seller_name = session.get('username')
        
        app.submit_dealership(form_data, image_paths  , seller_name)
        flash("Listing submitted.")
        return redirect(url_for('index_logged_in'))
    
    return render_template('submit_to_dealership.html')

@app_boundary.route('/view_listing/<int:listing_id>')
def view_listing(listing_id):
    listing = app.view_listing(listing_id) 
    
    if listing:
        return render_template('view_listing_page.html', listing=listing)
    else:
        return render_template('404.html'), 404

@app_boundary.route('/shortlist_listing', methods=['POST'])
def shortlist_listing():
    if 'user_id' in session and session['user_type'] == 1:
        listing_id = request.form.get('listing_id')
        user_id = session['user_id']
        listing = app.view_listing(listing_id) 
        app.shortlist_listing(user_id,listing_id)
        
        flash("Listing saved to shortlist")
        

    else: 
        flash("You must be logged in as buyer to save listings")
        
    
    return render_template('view_listing_page.html', listing=listing)
       

@app_boundary.route('/get_shortlisted_listings')
def get_shortlisted_listings():

        user_id = session['user_id']
        listings = app.get_shortlisted_listings(user_id) 
        print('hi') # Assuming this function fetches the saved listings
        return jsonify(listings)
   


from dataclasses import dataclass

@dataclass
class SearchFilters:
    car_model: str = ""
    min_price: float = 0.0
    max_price: float = 0.0
    depreciation: float = 0.0
    reg_date: str = ""
   
@app_boundary.route('/search', methods=['POST'])
def search():
    # Capture form data
    filters = SearchFilters(
        car_model=request.form.get('car_model', ''),
        min_price=float(request.form.get('min_price', 0)),
        max_price=float(request.form.get('max_price', 0)),
        depreciation=float(request.form.get('depreciation', 0)),
        reg_date=request.form.get('reg_date', '')
    )
    
    # Retrieve filtered listings
    normal_listings = app.get_filtered_listings(filters)
    # Get latest and premium listings for display in the same page
    latest_listings = app.get_normal_listings()
    premium_listings = app.get_premium_listings()
    
    # Render searched_listing.html with the retrieved listings
    return render_template('searched_listing.html', 
                           normal_listings=normal_listings, 
                           latest_listings=latest_listings, 
                           premium_listings=premium_listings)


@app_boundary.route('/register')
def register():
    return render_template('register.html')

@app_boundary.route('/submit_registration', methods=['POST'])
def submit_registration():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        image_paths = request.files.getlist('images')
        
        print(form_data)
        
        app.submit_registration(form_data, image_paths)
        return redirect(url_for('login'))
    
    return redirect(url_for('register'))

@app_boundary.route('/seller_profile')
def load_seller_profile():
    user_id = session.get('user_id')  # Assuming user_id is stored in session
    print ("user_id" , user_id)
    if not user_id:
        # Redirect to login or show an error if user is not logged in
        return redirect(url_for('login'))
    
    # Retrieve seller profile information
    profile_data = app.get_seller_profile(user_id)
    reviews = app.get_reviews_for_user(user_id)
    print("Reviews from backend",reviews)
    print("profile_data from backend",profile_data)
    print(type(profile_data))
    # Render the template with the profile data
    return render_template('seller_profile.html', profile_data=profile_data , reviews=reviews)

@app_boundary.route('/dealer_profile/<user_id>')
def load_dealer_profile(user_id):
      # Assuming user_id is stored in session
    print ("user_id" , user_id)
    
    # Retrieve seller profile information
    profile_data = app.get_seller_profile(user_id)
    reviews = app.get_reviews_for_user(user_id)
    print("Reviews from backend",reviews)
    print("profile_data from backend",profile_data)
    print("Image path for profile:" ,profile_data['image_path'])
    
    # Render the template with the profile data
    return render_template('seller_profile.html', profile_data=profile_data , reviews=reviews)


@app_boundary.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.get_json()
    rating = data.get('rating')
    review = data.get('review')
    

    # Assume user_id and listing_id are known; set them based on current session/user context
    user_id = session.get('user_id')  # Retrieve the current user ID from session
    # Or pass it explicitly when this button is pressed
    listing_id = data.get('listing_id')
    dealer_id = app.get_dealer_id(listing_id)

    print(type(user_id))
    print(type(dealer_id))
    print(type(listing_id))
    print(type(rating))
    print(type(review))
    

    print (user_id,dealer_id,listing_id,rating,review)
    # Save the review in the database
    if app.save_review(user_id,dealer_id, listing_id, rating, review):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 500

@app_boundary.route('/modify_listing/<int:listing_id>', methods=['GET', 'POST'])
def modify_listing(listing_id):
    # Check if the user is authorized
    

    if request.method == 'POST':
        # Handle form submission
        form_data = request.form.to_dict()
        image_paths = request.files.getlist('images')
        user_id = session.get('user_id')
        dealer_name = session.get('username')
        print("b.py",form_data)
        print("b.py",image_paths)
        print("bLid.py",listing_id)
        print("b.py",user_id)
        print("b.py",dealer_name)

        # Update listing in the database
        update_successful = app.update_listing(listing_id,form_data, image_paths, user_id, dealer_name)

        if update_successful:
            return redirect(url_for('load_seller_profile'))
        else:
            flash("An error occurred while updating the listing.")
            return redirect(url_for('modify_listing', listing_id=listing_id))

    # Fetch existing listing data for the form
    listing_data = app.get_listing_by_id(listing_id)
    return render_template('modify_listing.html', listing=listing_data)


@app_boundary.route('/delete_listing/<int:listing_id>', methods=['POST'])
def delete_listing(listing_id):
    # Check if the user is authorized (optional, if needed)
     # Get the logged-in user's ID
    
    
        # Delete the listing from the database
    delete_successful = app.delete_listing(listing_id)
        
    if delete_successful:
        flash("Listing deleted successfully.")
        return redirect(url_for('load_seller_profile'))  # Redirect to the profile or listings page
    else:
        flash("An error occurred while deleting the listing.")
        return redirect(url_for('load_seller_profile'))  # Optionally, stay on the profile page
 

@app_boundary.route('/admin_logged_in')
def render_admin_logged_in_page():
    user_profiles = app.get_all_users()
    user_type_permissions = app.get_user_type_permissions()
    print("userprofiles: ",user_profiles)
    print("usertypeperms: ",user_type_permissions)

    return render_template('admin_logged_in.html',user_profiles = user_profiles , user_type_permissions = user_type_permissions )

@app_boundary.route('/admin_logged_in_manage_listing')
def render_admin_logged_in_manage_listing_page():
    listings = app.get_all_listings()
   
    print("listings:  ",listings)
    return render_template('admin_logged_in_manage_listing.html' , listings = listings)


@app_boundary.route('/update_user', methods=['POST'])
def update_user():
    
    data = request.get_json()
    print("Received Data: ", data)
        # Extract user data from the request
    user_id = data.get('user_id')
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    description = data.get('description')
    phone_number = data.get('phone_number')
    user_type = data.get('user_type')

    # Call the function to update user info in the database
    updated = app.update_user_in_db(user_id, username,password, email, name, description, phone_number, user_type)
    
    if updated:
        return {"message": "User updated successfully"}
    else:
        return {"message": "Failed to update user"}
    
@app_boundary.route('/deactivate_user', methods=['POST'])
def deactivate_user():
    data = request.get_json()

    user_id = data.get('user_id')
    
    # Call the function to deactivate user
    success = app.deactivate_user_in_db(user_id)
    
    if success:
        return {"success": True, "message": "User deactivated successfully."}
    else:
        return {"success": False, "message": "Failed to deactivate user."}
    

@app_boundary.route('/admin_register_user', methods=['POST'])
def admin_register_user():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        image_paths = request.files.getlist('images')
        
        print(form_data)
        
        app.admin_register_user(form_data, image_paths)
        return redirect(url_for('render_admin_logged_in_page'))
    
    return redirect(url_for('admin_logged_in'))


@app_boundary.route('/admin_logged_in_create_user')
def render_admin_logged_in_create_user_page():
    
   
    
    return render_template('admin_logged_in_create_user.html')

@app_boundary.route('/add_user_type', methods=['POST'])
def add_user_type():
    data = request.json
    user_type = data['user_type']
    user_type_name = data['user_type_name']
    create_listing = data['create_listing']
    delete_listing = data['delete_listing']
    update_listing = data['update_listing']
    view_listing = data['view_listing']

    if (app.add_user_type(user_type,user_type_name,create_listing,delete_listing,update_listing,view_listing)) :
        return jsonify({"success": True})
    # Database connection (replace with your credentials and setup)
    
@app_boundary.route('/deactivate_users_by_type', methods=['POST'])
def deactivate_users_by_type():
    data = request.get_json()
    user_type = data.get('user_type')

    print("test:", user_type)
    
    # Fetch all users with the specified user_type from the database
    user_ids = app.get_user_ids_by_type(user_type)  # This function should return a list of user IDs with that type
    print("test2:", user_ids)
    if not user_ids:
        return {"success": False, "message": f"No users found with user type '{user_type}'."}
    
    # Deactivate each user
    for user_id in user_ids:
        app.deactivate_user_in_db(user_id)  # Reuse the same function to deactivate each user individually

    return {"success": True, "message": f"All users with user type '{user_type}' have been deactivated."}


@app_boundary.route('/update_user_type_permission', methods=['POST'])
def update_user_type_permission():
    data = request.get_json()
    id = data.get('id')
    user_type = data.get('user_type')
    create_listing = data.get('create_listing')
    delete_listing = data.get('delete_listing')
    update_listing = data.get('update_listing')
    view_listing = data.get('view_listing')
    user_type_name = data.get('user_type_name')

    # Call the function to update the permissions in the database
    success = app.update_user_type_permissions_in_db(
        id, user_type, create_listing, delete_listing, update_listing, view_listing, user_type_name
    )
    
    if success:
        return {"success": True, "message": "Permissions updated successfully."}
    else:
        return {"success": False, "message": "Failed to update permissions."}

if __name__ == '__main__':
    app_boundary.run(debug=True)