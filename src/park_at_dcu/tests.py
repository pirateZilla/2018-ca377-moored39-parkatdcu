# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class IndexTests(TestCase):
    def test_welcome(self):
        """
        An appropriate welcome message is displayed once the page is loaded.
        """
        response = self.client.get(reverse('park_at_dcu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Park@DCU!")
