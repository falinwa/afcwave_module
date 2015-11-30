# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp

class fal_portal_sale_order_wizard(models.TransientModel):
    _name = "fal.portal.sale.order.wizard"

    partner_id = fields.Many2one('res.partner', 'Customer', readonly=True)
    date_order = fields.Datetime('Date')
    order_line = fields.One2many('fal.portal.sale.order.line.wizard', 'order_wizard_id', 'Order Lines')
    """
    amount_untaxed = fields.Function(_amount_all_wrapper, digits_compute=dp.get_precision('Account'), string='Untaxed Amount',
            store={
                'sale.order': (lambda self, cr, uid, ids, c={}: ids, ['order_line'], 10),
                'sale.order.line': (_get_order, ['price_unit', 'tax_id', 'discount', 'product_uom_qty'], 10),
            },
            multi='sums', help="The amount without tax.", track_visibility='always'),
    amount_tax = fields.function(_amount_all_wrapper, digits_compute=dp.get_precision('Account'), string='Taxes',
            store={
                'sale.order': (lambda self, cr, uid, ids, c={}: ids, ['order_line'], 10),
                'sale.order.line': (_get_order, ['price_unit', 'tax_id', 'discount', 'product_uom_qty'], 10),
            },
            multi='sums', help="The tax amount."),
    amount_total = fields.function(_amount_all_wrapper, digits_compute=dp.get_precision('Account'), string='Total',
            store={
                'sale.order': (lambda self, cr, uid, ids, c={}: ids, ['order_line'], 10),
                'sale.order.line': (_get_order, ['price_unit', 'tax_id', 'discount', 'product_uom_qty'], 10),
            },
            multi='sums', help="The total amount."),
    """
#end of fal_portal_sale_order_wizard

        

class fal_portal_sale_order_line_wizard(models.TransientModel):
    _name = "fal.portal.sale.order.line.wizard"

    order_wizard_id = fields.Many2one('fal.portal.sale.order.wizard', 'Order Reference')
    name = fields.Text('Description', required=True)
    price_unit = fields.Float('Unit Price', required=True, digits_compute= dp.get_precision('Product Price'))
    #price_subtotal = fields.function(_amount_line, string='Subtotal', digits_compute= dp.get_precision('Account'))
    product_uom_qty = fields.Float('Quantity', digits_compute= dp.get_precision('Product UoS'), required=True)
    product_id = fields.Many2one('product.product', 'Product', domain=[('sale_ok', '=', True)], required=True)
    tax_id = fields.Many2many('account.tax', 'sale_order_line_wizard_tax', 'order_line_wizard_id', 'tax_id', 'Taxes')

#end of fal_portal_sale_order_line_wizard