from datetime import date
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains("order_line")
    def sale_order(self):
        check_date = fields.datetime.today().month
        sale_order = self.search([]).filtered(lambda l: l.date_order.
                                              month == check_date)
        total_lines = sale_order.mapped("order_line")
        discount_limit = [rec.product_uom_qty *
                          rec.price_unit-rec.price_subtotal
                          for rec in total_lines]
        discount_limit_vals = float(self.env['ir.config_parameter'].
                                    sudo().get_param('discount_limit.limit'))
        if discount_limit_vals <= sum(discount_limit):
            raise ValidationError('Discount amount is exceed for this month')

