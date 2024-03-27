from django.contrib import admin
from . models import donate_table,cloth_table,bed_table,med_table,food_table,kitchen_table,communication_table,cart_item

admin.site.register(donate_table)
admin.site.register(cloth_table)
admin.site.register(bed_table)
admin.site.register(med_table)
admin.site.register(food_table)
admin.site.register(kitchen_table)
admin.site.register(communication_table)
admin.site.register(cart_item)
# Register your models here.
