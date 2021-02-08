import requests
from tpaga_project_1.settings import URL_API_TPAGA


URL_API_TPAGA_PAYMENT_REQUESTS = URL_API_TPAGA + "payment_requests/"
URL_API_TPAGA_PAYMENT_CREATE = URL_API_TPAGA_PAYMENT_REQUESTS + "create/"
USER_CREDENTIALS = "Basic bWluaWFwcG1hLW1pbmltYWw6YWJjMTIz"
#URL_MERCADO_LIBRE_ITEMS = URL_API_MERCADO_LIBRE + "items/"


def payment_request_create(order):
    """
    Request information from Mercado Libre API Categories
    :param order:
    :return:
    """
    data ={
        "order_id": order.pk,
        "purchase_description": order.purchase_description,
        #"purchase_items":  [{"name": item.item.name, "value": str(item.item.value)} for item in order.items.all()],
        "cost": int(order.cost),
        "expires_at": "2021-11-05T20:10:57.549653+00:00",
        "idempotency_token": "errrea0c78c5-e85a-48c4-b7f9-24a9014a237823{}".format(order.pk),
        "purchase_details_url": "https://example.com/compra/{}".format(order.pk),
        "voucher_url": "https://example.com/comprobante/{}".format(order.pk),
        #"purchase_items": [],
        "terminal_id": "sede_45",
        "user_ip_address": "61.1.224.70",
    }
    response = requests.post(URL_API_TPAGA_PAYMENT_CREATE, data=data, headers={'Authorization': USER_CREDENTIALS})
    if response.status_code != 200 and response.status_code != 201:
        return "Bad request"
    return response.json()

