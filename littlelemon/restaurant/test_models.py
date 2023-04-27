from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=4, title="Ice cream", price=5.00, inventory=5)
        self.assertEqual(item.title, "Ice cream")