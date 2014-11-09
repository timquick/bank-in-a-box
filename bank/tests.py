from django.test import TestCase

from bank.models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(
                legal_name = 'Bugs Bunny',
                tax_id = '123456789',
                street1 = 'address line 1',
                street2 = 'address line 2',
                city = 'Hollywood',
                state_province = 'CA',
                postal_code = '90210',
                email = 'bugsbunny@wb.com' )
                
    def test_create_customers(self):
        wileycoyote = Customer(legal_name = 'Wiley Coyote' )
        self.assertEqual(wileycoyote.legal_name, 'Wiley Coyote')
    def test_legal_name_assignment(self):
        bbunny = Customer.objects.get(pk=1)
        self.assertEqual(bbunny.__unicode__(), 'Bugs Bunny')
        
        
        

