from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        #check user email id is valid or not
        email="rohitofficial95@outlook.com"
        password="1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
         """Test the email for a new user is normalized"""

         email= 'test@GMAIL.com'
         user= get_user_model().objects.create_user(email,'test123')

         self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
         """Test user with no email gets error"""
         with self.assertRaises(ValueError):
             get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        """ Test Creating new super user""" 
        user= get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)




