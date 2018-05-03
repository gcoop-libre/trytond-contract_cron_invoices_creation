# This file is part of the contract_vdb module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import PoolMeta, Pool
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
import logging
logger = logging.getLogger(__name__)

__all__ = ['CreateInvoices', 'CreateInvoicesCron']


class CreateInvoices:
    __metaclass__ = PoolMeta
    __name__ = 'contract.create_invoices'

    def do_create_invoices(self, action):
        pool = Pool()
        Configuration = pool.get('Configuration')
        config = Configuration(1)
        if config.contract_use_cron:
            CreateInvoicesCron = pool.get('contract.create_invoices_cron')
            create_invoices_cron_data = CreateInvoicesCron()
            create_invoices_cron_data.date = self.start.date
            create_invoices_cron_data.save()
        else:
            super(CreateInvoices, self).do_create_invoices(action)




class CreateInvoicesCron(ModelSingleton, ModelSQL, ModelView):
    'Create Invoices Cron'
    __name__ = 'contract.create_invoices_cron'

    date = fields.Date('Date')

    @classmethod
    def create_invoices_cron(cls, args=None):
        '''
        Cron create invoices.
        '''
        logger.info('Start Scheduler - create invoices.')
        pool = Pool()
        create_invoices_cron_data = cls.get_singleton()
        consumptions = []
        invoices = []
        if create_invoices_cron_data.date:
            Consumptions = pool.get('contract.consumption')
            consumptions = Consumptions.search([('invoice_date', '<=', create_invoices_cron_data.date)])
            logger.info('Create invoices - ' + str(len(consumptions)) + ' consumptions to invoice')
            logger.info('Create invoices - Start invoices creation')
            invoices = Consumptions._invoice(consumptions)
            logger.info('Create invoices - ' + str(len(invoices)) + ' invoices created')
        logger.info('End Scheduler - create invoices')
