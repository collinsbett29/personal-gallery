from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        # create a new location and save
        self.new_location = Location(name='Nairobi')
        self.new_location.save()

        # create a new category and save
        self.new_category = Category(name='ocean')


