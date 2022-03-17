from django.test import TestCase
from django.urls import reverse
from store.models import Product,Category
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):
    # create the object
    def setUp(self):
        self.category = Category.objects.create(name="hello",slug="hello")
        
    # test the model
    def test_create_category(self):
        data = self.category
        self.assertIsInstance(data,Category)
        self.assertEqual(data.name,'hello')
        self.assertEqual(data.slug,'hello')

    # test fo the get_absolute_url()
    def test_get_absolute_url(self):
        data = self.category
        self.assertEqual(data.get_absolute_url(), reverse('store:categories-list', args=[data.slug]))

       
    # checks for return __str__(self)
    def test_return_type(self):
        data = self.category
        # must match name 'hello'
        self.assertEqual(str(data),'hello')

class TestUserModel(TestCase):
    # create the object
    def setUp(self):
        Category.objects.create(name="love",slug="love")
        User.objects.create(username="dorcas")
        self.product = Product.objects.create(category_id=1,user_id=1,title="life",
            slug="life",image="product_image",price=20.00)
    
    # test the model
    def test_create_product(self):
        product = self.product
        self.assertIsInstance(product,Product)
    
    # check the return type __str(self)__ method
    def test_product_return_type(self):
        product = self.product
        self.assertEqual(str(product),'life')
    
    # test fo the get_absolute_url()
    def test_get_absolute_url(self):
        data = self.product
        self.assertEqual(data.get_absolute_url(), reverse('store:detail', args=[data.slug]))






    



       
   