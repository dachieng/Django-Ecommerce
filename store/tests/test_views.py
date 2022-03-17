from urllib import request
from django.http import HttpResponse
from django.test import Client, RequestFactory
from django.test import TestCase
from django.urls import reverse
from store.models import Category,Product
from django.contrib.auth.models import User
from unittest import skip
from store.views import products

#@skip("Skipping test for product")
class TestSkip(TestCase):
    def setUp(self):
        # client allows you test your views, acts as a dummy browser
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username="dorcas")  
        Category.objects.create(name="love",slug="love")
        Product.objects.create(category_id=1,user_id=1,title="life",
            slug="life",image="product_image",price=20.00)
    
    
    # test for for allowe urls
    def test_home_page(self):
        # test for the home page
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    # test fo detail page
    def test_detail_page(self):
        response = self.c.get(reverse("store:detail",args=['life']))
        self.assertEqual(response.status_code,200)

    # test for categories page
    def test_category_page(self):
        response = self.c.get(reverse("store:categories-list",args=['love']))
        self.assertEqual(response.status_code, 200)

    def test_home_page_html(self):
        request = HttpResponse()
        response = products(request)
        html = response.content.decode('utf8')
        print(html)
        # test fot the page title
        self.assertIn("<title>Home</title>",html)

    #estFactory
    def test_view_function(self):
        request = self.factory.get("/")
        response = products(request)
        html = response.content.decode('utf8')
        print(html)
        # test fot the page title
        self.assertIn("<title>Home</title>",html)



