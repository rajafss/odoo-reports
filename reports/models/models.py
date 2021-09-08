# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Reports(models.Model):
    _name = 'reports.page'
#     _description = 'reports.reports'


    الإسم = fields.Text()
    description = fields.Text()

    def action_print(self):
        return self.env.ref('reports.report_page_class').report_action(self)


#الإسم
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
