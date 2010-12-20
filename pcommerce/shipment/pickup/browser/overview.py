from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.pickup.browser.base import PickupBase

class PickupOverview(PickupBase):
    template = ViewPageTemplateFile('overview.pt')
