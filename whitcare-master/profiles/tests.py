from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from .models import Profile
from .views import search_results

import factory

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
    
    first_name = 'John'
    last_name = 'Smith'
    available_weekends = True
    available_weeknights = False 
    rate = 13.35

class SearchResultsTest(TestCase):

    def test_returns_correct_page(self):
        request = HttpRequest()
        response = search_results(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Search Results", html)
    
    def test_first_name_one_result(self):
        profile = ProfileFactory.create(first_name='Test', last_name='Tester')
        response = self.client.get(reverse('search-results'), {'first_name': 'Test'})
        self.assertIn('Test Tester', response.content.decode())
    
    def test_first_name_two_results(self):
        profile1 = ProfileFactory.create(first_name='Test', last_name='Tester')
        profile2 = ProfileFactory.create(first_name='Test', last_name='Tennant')
        response = self.client.get(reverse('search-results'), {'first_name': 'Test'})
        self.assertIn('Test Tester', response.content.decode())
        self.assertIn('Test Tennant', response.content.decode())
        
    def test_last_name_results(self):
        profile1 = ProfileFactory.create(first_name='Test', last_name='Tester')
        response = self.client.get(reverse('search-results'), {'last_name': 'Tester'})
        self.assertIn('Test Tester', response.content.decode())

    def test_first_and_last_name_results(self):
        profile1 = ProfileFactory.create(first_name='Test', last_name='Tester')
        profile2 = ProfileFactory.create(first_name='Test', last_name='Testing')
        response = self.client.get(reverse('search-results'), {'first_name': 'Test', 'last_name': 'Tester'})
        self.assertIn('Test Tester', response.content.decode())
        self.assertNotIn('Test Testing', response.content.decode())

    def test_return_results_for_shortened_first_name(self):
        profile = ProfileFactory.create(first_name='Geoffrey', last_name='Tester')
        response = self.client.get(reverse('search-results'), {'first_name': 'Geoff'})
        self.assertIn('Geoffrey Tester', response.content.decode())

    def test_return_results_for_shortened_last_name(self):
        profile = ProfileFactory.create(first_name='Test', last_name='Tester')
        response = self.client.get(reverse('search-results'), {'last_name': 'Test'})
        self.assertIn('Test Tester', response.content.decode())

    def test_if_no_results_error_message_displayed(self):
        response = self.client.get(reverse('search-results'), {'first_name': 'DoesNotExist'})
        self.assertIn('No results found', response.content.decode())
    
    def test_if_no_params_error_message_displayed(self):
        profile = ProfileFactory.create(first_name='NotHere', last_name='NotHere-ington')
        response = self.client.get(reverse('search-results'))
        self.assertIn('No results found', response.content.decode())

    def test_results_are_case_insensitive(self):
        profile = ProfileFactory.create(first_name='Test', last_name='Tester')
        response = self.client.get(reverse('search-results'), {'first_name': 'test'})
        self.assertIn('Test Tester', response.content.decode())
    
    def test_results_have_link_to_profile(self):
        profile = ProfileFactory.create()
        response = self.client.get(reverse('search-results'), {'first_name': profile.first_name})
        profile_url = profile.get_absolute_url()
        self.assertIn(profile_url, response.content.decode())