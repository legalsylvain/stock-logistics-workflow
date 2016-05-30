# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import fields, models, api


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    is_expense_transfer = fields.Boolean(
        string='Is Expense Transfer', compute="_compute_is_expense_transfer",
        store=True)

    expense_transfer_account_id = fields.Many2one(
        string='Expense Transfer Account', comodel_name='account.account',
        help="Set an Expense Account if you want to allow accountant to"
        " generate Expense Transfer Accounting Entries."
        " Then generated entry will belong the following lines :\n"
        " * Debit : This expense account\n"
        " * Credit : The default expense account of the product\n"
        " (The value used will be the 'Cost' field of the product)")

    expense_transfer_journal_id = fields.Many2one(
        string='Expense Transfer Journal', comodel_name='account.journal',
        help="Set a Journal that will be used to write expense Transfer"
        " Accounting Entries.")

    @api.multi
    @api.depends('expense_transfer_account_id')
    def _compute_is_expense_transfer(self):
        for picking_type in self:
            picking_type.is_expense_transfer =\
                picking_type.expense_transfer_account_id is not False
