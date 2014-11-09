from django.db import models
'''
Banking Data Model
  A reasonable question would be: "why not use one of the industry standard
  data models?"  To be honest, I tried to leverage at least part of what I
  learned in Len Silverston's 'Data Models' books, as well as studying the IFX
  messaging specifications.  Perhaps the data model we use here will evolve
  into one of those sophisticated models over time.  For this exercise, we
  decided to start small and solve banking issues one at a time.  This is 
  largely due to the fact that we know so little about the industry, and want
  to preserve as much as possible the simplicity we get when we're ignorant
  of the inherent complexities of the business.
  
'''
class Customer(models.Model):
    legal_name = models.CharField(max_length=70, blank=True)
    tax_id = models.CharField(max_length=9, blank=True)
    street1 = models.CharField(max_length=50, blank=True)
    street2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.legal_name
    
class Agreement(models.Model):
    account_type = models.CharField(max_length=3)
    description  = models.CharField(max_length=50)
    effective_date = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.account_type, self.description)
    
class BankAccount(models.Model):
    agreement_id = models.ForeignKey(Agreement)
    routing_number = models.IntegerField()
    account_number = models.IntegerField()
    account_title = models.CharField(max_length=60)
    available_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    posted_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    last_activity  = models.DateField(auto_now_add=True)
    cycle_day = models.IntegerField(default=1)
    stage = models.CharField(max_length=15,default='New')
    
    def __unicode__(self):
        return u'%d %d %s' % (self.routing_number, self.account_number, self.account_title)
    
    
class AccountRole(models.Model):
    '''
    Represents the relationship between a Customer and an account.
    Typical roles are:  Owner, Beneficiary, Custodian, Trustee
    In a pure sense, we make a leap when we refer to anyone with an account 
    relationship as a 'customer', since 'customer' represents the relationship
    between a person and our organization, and is normally dependent on having 
    an account relationship.  For now, we'll live with the underlying 
    assumption.
    
    '''
    customer_id = models.ForeignKey(Customer)
    account_id  = models.ForeignKey(BankAccount)
    role_code   = models.CharField(max_length=15)
    from_date   = models.DateField(auto_now_add=True)
    thru_date   = models.DateField(blank=True,null=True)
    allocation_pct = models.DecimalField(max_digits=3,decimal_places=2,default=1.00)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.customer_id, self.account_id, self.role_code)


    
    