from django.contrib import admin
from bank.models import Customer, Agreement, BankAccount, AccountRole


admin.site.register(Customer)
admin.site.register(Agreement)
admin.site.register(BankAccount)
admin.site.register(AccountRole)
