from odoo import models, fields


class DiscountLimit(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_limit = fields.Boolean(string='DiscountLimit',
                                    config_parameter="True")
    limit = fields.Float(string='Limit',
                         config_parameter="discount_limit.limit")