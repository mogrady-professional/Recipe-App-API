from django.test import TestCase # Import the TestCase class
from django.contrib.auth import get_user_model # Import the get_user_model function

class ModelTests(TestCase): # Create a test class that inherits from TestCase
    def test_create_user_with_email_successful(self): # Create a test method
        """Test creating a new user with an email is successful"""
        email = 'test@email.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        ) # Create a new user with the email and password

        self.assertEqual(user.email, email) # Assert that the email is equal to the email we created
        self.assertTrue(user.check_password(password)) 
        # Assert that the password is equal to the password we created
        
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
        # Assert that the email is normalized to lowercase

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
            # Assert that the ValueError is raised when the email is not provided

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        # Assert that the user is a superuser and a staff member