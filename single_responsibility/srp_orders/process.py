import sys, os; sys.path.append(os.path.dirname(__file__))

from customer_order_data import CustomerOrderData
from invoice_calculator import InvoiceCalculator
from invoice_printer import InvoicePrinter
from logging import log_order


class CustomerOrderFacade:
    def __init__(self, order):
        self.order = order

    def log(self):
        return log_order(self.order)
    
    def print_invoice(self, card_type):
        calculator = InvoiceCalculator(self.order.amount, card_type)
        printer = InvoicePrinter(self.order, calculator)
        printer.print()


def process_order(order_id, item, amount, card_type):
    data = CustomerOrderData(order_id, item, amount)
    order = CustomerOrderFacade(data)
    order.log()
    order.print_invoice(card_type)


if __name__ == '__main__':
    process_order('abc_defghi_jkl', "Lunch", 38.20, 'amex')
    process_order('mno_pqrstu_vwx', "Dinner", 24.99, 'visa')
