from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from api.api_connections import payment_request_create
from tpaga_project_1.forms import ItemForm
from tpaga_project_1.models import PurchaseOrder, Item, CREATED, PurchaseItem


class ItemListView(ListView):
    template_name = 'item_list.html'

    def get_queryset(self):
        return Item.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['items_list'] = Item.objects.all()
        context['form'] = ItemForm
        return context

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            order_description = form.cleaned_data['order_description']
            if items:
                cost = sum([item.value for item in items])
                # Create order
                order = PurchaseOrder.objects.create(
                    purchase_description=order_description,
                    cost=cost,
                    status=CREATED
                )

                for item in items:
                    # Create purchase items
                    purchase_item = PurchaseItem.objects.create(
                        order=order,
                        item=item
                    )
                    # Add items to order
                    order.items.add(purchase_item)

                print(order)
                # Get data from API mobile
                get_data_payement = payment_request_create(order)
                if isinstance(get_data_payement, dict):
                    tpaga_payment_url = get_data_payement['tpaga_payment_url']
                    # Save tpaga_payment_url
                    order.tpaga_payment_url= tpaga_payment_url
                    order.save()
        return redirect(reverse('order-detail', args={order.pk}))


class PurchaseOrderListView(ListView):
    #model = PurchaseOrder
    template_name = 'purchaseorder_list.html'

    def get_queryset(self):
        return PurchaseOrder.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['orders_list'] = PurchaseOrder.objects.all()
        return context


class OrderDetailView(DetailView):
    template_name = 'purchaseorder_detail.html'
    model = PurchaseOrder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context