from zope.interface import implements, Interface
from zope.component import adapts

from pcommerce.core import PCommerceMessageFactory as _
from pcommerce.core.interfaces import IShipmentMethod
from pcommerce.shipment.pickup.interfaces import IPickupShipment

class PickupShipment(object):
    implements(IShipmentMethod, IPickupShipment)
    adapts(Interface)
    
    title = _('Pickup')
    description = _('Goods are picked up by the customer')
    icon = '++resource++pcommerce_shipment_pickup_icon.gif'
    logo = '++resource++pcommerce_shipment_pickup_logo.gif'
    
    def __init__(self, context):
        self.context = context
    
    def mailInfo(self, order, lang=None, customer=False):
        return _('Goods are picked up by the customer')
