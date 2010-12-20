from pcommerce.core.data import ShipmentData

def PickupShipmentData(as_customer=True, address=None):
    data = ShipmentData('pcommerce.shipment.pickup')
    return data
