
from openerp.osv import fields, orm
from openerp.tools.translate import _


class crm_claim(orm.Model):
    _name = "crm.claim"
    _inherit = "crm.claim"
    _order = 'claim_number'

    def on_change_serial_id(self, cr, uid, id, serial_id=False, context=None):
        if context==None:
            context={}
        res = {'value':{
          'deliver_order': False,
          'sale_order': False,
          'date_order': False,
          'partner_id': False,
          'product_id': False,
          'carrier': False,
          'carrier_tracking_ref': False,
          'salesperson' : False,

        }}
        if serial_id:
            serial_number = self.pool.get('stock.production.lot').browse(cr, uid, serial_id)
            res['value']['product_id'] = serial_number.product_id.id
            for move in serial_number.move_ids:
                if move.picking_id.sale_id: 
                    res['value']['deliver_order'] = move.picking_id.id
                    res['value']['sale_order'] = move.picking_id.sale_id.id
                    res['value']['salesperson'] = move.picking_id.sale_id.user_id.id
                    res['value']['date_order'] = move.picking_id.sale_id.date_order
                    res['value']['partner_id'] = move.picking_id.sale_id.partner_id.id
                    if move.picking_id.carrier_id:

                        res['value']['carrier'] = move.picking_id.carrier_id.id
                        res['value']['carrier_tracking_ref'] = move.picking_id.carrier_tracking_ref
        return res

    def onchange_partner_id(self, cr, uid, ids, part, email=False):
        """This function returns value of partner address based on partner
           :param part: Partner's id
           :param email: ignored
        """
        if not part:
            return {'value': {'email_from': False,
                              'partner_phone': False,
                              'partner_mphone': False,
                            }
                   }
        address = self.pool.get('res.partner').browse(cr, uid, part)
        # return super(crm_claim, self).onchange_partner_id(self, cr, uid, ids, part, val)
        return {'value': {'email_from': address.email, 'partner_phone': address.phone, 'partner_mphone': address.mobile }} 

    _columns = {
        'serial_id' : fields.many2one('stock.production.lot', string=_("Serial Number")),
        'deliver_order' : fields.many2one('stock.picking.out', string=_("Deliver Order")),
        'sale_order' : fields.many2one('sale.order', string=_("Sale Order")),
        'date_order' : fields.date(string=_('Order Date')),
        'claim_number' : fields.char('Claim Number', size=64),
        'product_id' : fields.many2one('product.product', string=_("Product Name")),
        'carrier' : fields.many2one('delivery.carrier', string=_("Carrier")),
        'carrier_tracking_ref' : fields.char('Carrier Tracking Ref', size=32),
        'partner_mphone' : fields.char("Mobile Phone"),
        'salesperson' : fields.many2one('res.users', string='Sales Person')
    }

    def create(self, cr, uid, vals, context=None):
        vals['claim_number'] = self.pool.get('ir.sequence').get(cr, uid, 'claimorder.fwa') or '/'
        return super(crm_claim, self).create(cr, uid, vals, context=context)

#end of crm_claim()





