# This file is part of the contract_vdb module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import configuration
from . import invoice


def register():
    Pool.register(
        invoice.CreateInvoices,
        invoice.CreateInvoicesCron,
        configuration.Configuration,
        module='contract_cron_invoices_creation', type_='model')
    Pool.register(
        invoice.CreateInvoices,
        module="contract_cron_invoices_creation", type_="wizard")
