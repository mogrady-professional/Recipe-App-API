from django.test import TestCase, Client 
from django.contrib.auth import get_user_model
from django.urls import reverse 

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='te3st@gmail.com',
            password= 'test123'
        )
        self.client.force_login(self.admin_user) 
        self.user = get_user_model().objects.create_user(
            email='tes2t@gmail.com',
            password= 'test123',
            name='Test user full name'
        )
    
    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist') # Generate url for user list page
        res = self.client.get(url) # Get response from url

        self.assertContains(res, self.user.name) # Check if user name is in response
        self.assertContains(res, self.user.email) # Check if user email is in response

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        res = self.client.get(url) # HTTP:Get  on url -> response from url

        self.assertEqual(res.status_code, 200) # Check if response is 200

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200) # Check if response is 200