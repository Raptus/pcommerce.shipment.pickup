from zope.interface import implements

from Products.Five.browser import BrowserView

from pcommerce.core.interfaces import IShipmentView, IOrder, IShoppingCart

from pcommerce.shipment.pickup.data import PickupShipmentData

class PickupBase(BrowserView):
    implements(IShipmentView)
    
    errors = {}
    
    def __init__(self, shipment, request):
        self.shipment = shipment
        self.context = shipment.context
        self.request = request
        self.cart = IShoppingCart(self.context)
        self.order = IOrder(self.context)
        self.data = self.order.shipmentdata.get('pcommerce.shipment.pickup', PickupShipmentData())
    
    def __call__(self):
        return self.template()
    
    def validate(self):
        return True
    
    def renders(self):
        return True
        
    def process(self):
        return
