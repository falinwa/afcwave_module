# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp

class PurchaseOrderLine(models.Model):
    _name = "purchase.order.line"
    _inherit = "purchase.order.line"

    fal_quantity_available = fields.Float('Available Quantity', related="product_id.qty_available")

#end of PurchaseOrderLine()