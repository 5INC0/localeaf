from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from .models import User, Order, SupplierStock, BuyerStock, OrderHistory
from django.utils.timezone import now 

# Create your views here.

def home(request):
    return render(request, 'lapp/login.html')

def supplier(request):
    stocks= SupplierStock.objects.all().order_by('-stock_added_on')
    total_quantity = SupplierStock.objects.values('item').annotate(total_quantity=Sum('quantity'))
    try:
        total_revenue = f"{OrderHistory.objects.filter(status='Order Fulfilled').aggregate(Sum('total_price'))['total_price__sum']:,.2f}"
    except:
        total_revenue = 0
    orders = Order.objects.all()

    if (request.method=="POST"):
        name = request.POST.get('name')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        SupplierStock.objects.create(name=name, item=item, quantity=quantity)

    return render(request, 'lapp/supplier.html', {'stocks':stocks, 'total_quantity': total_quantity, 'orders':orders, 'total_revenue':total_revenue})

def s_inventory(request):
    stocks= SupplierStock.objects.all().order_by('-stock_added_on')
    total_quantity = SupplierStock.objects.values('item').annotate(total_quantity=Sum('quantity'))
    orders = OrderHistory.objects.all()
    allorders= OrderHistory.objects.all().order_by('-date')

    if (request.method=="POST"):
        name = request.POST.get('name')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        SupplierStock.objects.create(name=name, item=item, quantity=quantity)

    return render(request, 'lapp/inventory.html', {'stocks':stocks, 'total_quantity': total_quantity, 'orders':orders, 'allorders':allorders})

def buyer(request):
    stocks= SupplierStock.objects.all()
    orders = Order.objects.all()
    total_quantity = BuyerStock.objects.values('item').annotate(total_quantity=Sum('quantity'))
    return render(request, 'lapp/buyer.html', {'stocks':stocks, 'orders':orders, 'total_quantity':total_quantity})

def buying(request):
    orders = Order.objects.all()
    computation = {'Bok Choy':100, 'Trimmed Brocolli':200, 'Green Lettuce':200}
    total_price = 0

    if (request.method=="POST"):
        placed_by = request.POST.get('placed_by')
        supplier = request.POST.get('supplier')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        location = request.POST.get('location')

        total_price = int(computation[item])*int(quantity)
        
        Order.objects.create(total_price=total_price, placed_by=placed_by, supplier=supplier, item=item, quantity=quantity, location=location)
    return render(request, 'lapp/buying.html', {'orders':orders})

def b_orderhistory(request):
    stocks= BuyerStock.objects.all().order_by('-stock_added_on')
    total_quantity = BuyerStock.objects.values('item').annotate(total_quantity=Sum('quantity'))
    allorders= OrderHistory.objects.all().order_by('-date')

    if (request.method=="POST"):
        name = request.POST.get('name')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        BuyerStock.objects.create(name=name, item=item, quantity=quantity)

    return render(request, 'lapp/b_orderhistory.html', {'stocks':stocks, 'total_quantity': total_quantity, 'allorders':allorders})

# Buyer Options

def receive_order(request, pk):
    Order.objects.filter(pk=pk).update(status='Order Fulfilled')
    order = get_object_or_404(Order, pk=pk)
    BuyerStock.objects.create(
        supplier=order.supplier,
        item=order.item,
        quantity=order.quantity
    )
    OrderHistory.objects.create(
        buyer=order.placed_by,
        supplier=order.supplier,
        item=order.item,
        total_price=order.total_price,
        quantity=order.quantity,
        status=order.status
    )
    SupplierStock.objects.create(
        item=order.item, quantity=(order.quantity*-1)
    )

    Order.objects.filter(pk=pk).delete()
    return redirect('buyer')

def delete_order(request, pk):
    Order.objects.filter(pk=pk).delete()
    return redirect('buyer')

def return_order(request, pk):
    Order.objects.filter(pk=pk).update(status='Order Returned')
    return redirect('buyer')

def pay_order(request, pk):
    Order.objects.filter(pk=pk).update(status='Payment Sent')
    return redirect('buyer')

# Supplier Options

def accept_order(request, pk):
    Order.objects.filter(pk=pk).update(status='Order Accepted')
    return redirect('supplier')

def sent_order(request, pk):
    Order.objects.filter(pk=pk).update(status='Order Sent')
    return redirect('supplier')

def decline_order(request, pk):
    Order.objects.filter(pk=pk).update(status='Order Declined')
    order = get_object_or_404(Order, pk=pk)
    OrderHistory.objects.create(
        buyer=order.placed_by,
        supplier=order.supplier,
        total_price=order.total_price,
        item=order.item,
        quantity=order.quantity,
        status=order.status,
    )
    Order.objects.filter(pk=pk).delete()
    return redirect('supplier')

def receive_payment(request, pk):
    Order.objects.filter(pk=pk).update(status='Payment Received')
    return redirect('supplier')