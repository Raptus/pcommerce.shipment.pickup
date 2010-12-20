from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from pcommerce.shipment.pickup.browser.base import PickupBase

class PickupConfirmation(PickupBase):
    template = ViewPageTemplateFile('confirmation.pt')
