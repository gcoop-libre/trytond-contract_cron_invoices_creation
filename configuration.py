# This file is part of the contract_cron_invoices_creation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']

class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'contract.configuration'
    contract_use_cron = fields.Boolean('Use Cron to create invoices')
