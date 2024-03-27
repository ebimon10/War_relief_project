from django.shortcuts import render,get_object_or_404,redirect
from . models import donate_table,cloth_table,bed_table,med_table,food_table,kitchen_table,communication_table,cart_item
import razorpay
from django.conf import settings
import json
from django.http import JsonResponse


def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact_us(request):
    return render(request,"contact_us.html")
def services(request):
    return render(request,"services.html")
def donate_details(request):
    if request.method=='POST':
       country_name = request.POST.get("country")
       pin_code = request.POST.get("pin")
       your_name = request.POST.get("yname")
       date_of_birth = request.POST.get("dtob")
       phone_number = request.POST.get("phone")
       email_id = request.POST.get("email")
    
       obj=donate_table.objects.create(country=country_name, pincode=pin_code, name=your_name, dob=date_of_birth, phone_number=phone_number, email=email_id)
       obj.save()
       if obj:
           return render(request,"products.html")
       else:
           msg="fill the form completely"
           return render(request,"donate_details.html",{'fail':msg})
    else:
        return render(request,"donate_details.html")

def products(request):
    return render(request,"products.html")

def clothing(request):
    product = cloth_table.objects.all()
    return render(request, 'clothing.html', {'products': product})

def bed(request):
    product= bed_table.objects.all()
    return render(request,"bed.html",{'products':product})

def food(request):
    product=food_table.objects.all()
    return render(request,"food.html",{'products':product})

def med(request):
    product= med_table.objects.all()
    return render(request,"med.html",{'products':product})

def kitchen(request):
    product=kitchen_table.objects.all()
    return render(request,"kitchen.html",{'products':product})

def communication(request):
    product=communication_table.objects.all()
    return render(request,"communication.html",{'products':product})

def go_cart(request, product_type, product_id):
    # Assuming 'product_type' can be 'cloth' or 'bed'
    if product_type == 'cloth':
        product_model = cloth_table
    elif product_type == 'bed':
        product_model = bed_table
    elif product_type == 'med':
        product_model = med_table
    elif product_type == 'communication':
        product_model = communication_table
    elif product_type == 'food':
        product_model = food_table
    elif product_type == 'kitchen':
        product_model = kitchen_table
    else:
        # Handle invalid product_type
        return redirect('products')  # Redirect to home or another appropriate view

    product = get_object_or_404(product_model, id=product_id)

    # Check if the item is already in the cart
    cart_items, created = cart_item.objects.get_or_create(
        product_type=product_type,
        product_id=product_id
    )

    # If the item is already in the cart, increase the quantity
    if not created:
        cart_items.quantity += 1
        cart_items.save()

    return redirect('view_cart')  # Redirect to the cart or another appropriate view

   
def view_cart(request):
    # Retrieve items in the cart
    cart_items = cart_item.objects.all()  # You might need to filter by user or session

    # Collect product information for items in the cart
    cart_products = []
    total_payment=0
    for item in cart_items:
        if item.product_type == 'cloth':
            product = get_object_or_404(cloth_table, id=item.product_id)
        elif item.product_type == 'bed':
            product = get_object_or_404(bed_table, id=item.product_id)
        elif item.product_type == 'med':
            product = get_object_or_404(med_table, id=item.product_id)
        elif item.product_type == 'communication':
            product = get_object_or_404(communication_table, id=item.product_id)
        elif item.product_type == 'kitchen':
            product = get_object_or_404(kitchen_table, id=item.product_id)
        elif item.product_type == 'food':
            product = get_object_or_404(food_table, id=item.product_id)

        total_payment += product.price    
        cart_products.append(product)
       

    return render(request, 'view_cart.html', {'cart_products': cart_products , 'total_payment': total_payment})

def delete_from_cart(request,item_id):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id is not None:
            # Retrieve the cart item if it exists
            cart_item_instance = get_object_or_404(cart_item, id=item_id)
            # Delete the cart item
            cart_item_instance.delete()
    return redirect('view_cart')

def delete_all(request):

    delete_items= cart_item.objects.all()
    delete_items.delete()

    return redirect(view_cart)



def succes(request):
    
    return render(request, 'succes.html')
