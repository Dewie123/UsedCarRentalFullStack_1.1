import unittest
from boundary import app_boundary as app  # Import your app from boundary.py

class AuthTestCase(unittest.TestCase):
    
    def setUp(self):
        # Create a test client and set up any other test configurations
        self.client = app.test_client()
        self.client.testing = True
    
    def tearDown(self):
        # Clean up after each test
        pass

    def test_login(self):
        login_data = {
        'username': 'admin1',
        'password': 'admin1pw',
        'user_type': '4'  # Update user_type as per your test case
        }

        # Make a POST request to the login route
        response = self.client.post('/login', data=login_data)
        
        # Check if login redirects to the expected page
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect
        self.assertIn('/admin_logged_in', response.location)  # Change to the expected redirect for 'buyer1' login

        # Check if the session contains the user data
        with self.client.session_transaction() as session:
            self.assertEqual(session.get('username'), 'admin1')
            self.assertEqual(str(session.get('user_type')), '4')


    def test_logout(self):
    # First, log in to create a session with `buyer1`
        login_data = {
            'username': 'admin1',
            'password': 'admin1pw',
            'user_type': '4'
        }
        self.client.post('/login', data=login_data)
        
        # Now, log out
        response = self.client.get('/logout', follow_redirects=True)
        
        # Check if logout redirects to the login page
        self.assertEqual(response.status_code, 200)
        
        # Check for a specific element that only appears on the login page (adjust based on your HTML)
        self.assertIn(b'<input type="text" id="username" name="username"', response.data)

        # Ensure session data is cleared after logout
        with self.client.session_transaction() as session:
            self.assertIsNone(session.get('username'))
            self.assertIsNone(session.get('user_type'))


if __name__ == '__main__':
    unittest.main()
