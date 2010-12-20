from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from pcommerce.shipment.pickup.browser.base import PickupBase
from pcommerce.shipment.pickup.data import PickupShipmentData

class PickupShipment(PickupBase):
    
    def renders(self):
        return False
    
    def process(self):
        self.data = PickupShipmentData()
        props = getToolByName(self.context, 'portal_properties').pcommerce_properties
        self.data.pretaxcharge = props.getProperty('pickup_pretaxcharge', 0.0)
        self.data.posttaxcharge = props.getProperty('pickup_posttaxcharge', 0.0)
        return self.data
