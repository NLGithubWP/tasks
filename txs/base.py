
from . import *
from .params import *
from abc import abstractmethod


class Transactions(object):

    def __init__(self, update_batch_size: int, select_batch_size:int):
        self.update_batch_size = update_batch_size
        self.select_batch_size = select_batch_size

    @abstractmethod
    def new_order_transaction(self, m_conn, m_params: NewOrderTxParams) -> float:
        raise NotImplementedError

    @abstractmethod
    def payment_transaction(self, m_conn, m_params: PaymentTxName) -> float:
        raise NotImplementedError

    @abstractmethod
    def delivery_transaction(self, m_conn, m_params: DeliveryTxParams) -> float:
        raise NotImplementedError

    @abstractmethod
    def order_status_transaction(self, m_conn, m_params: OrderStatusTxParams) -> float:
        raise NotImplementedError

    @abstractmethod
    def stock_level_transaction(self, m_conn, m_params: StockLevelTxParams) -> float:
        raise NotImplementedError

    @abstractmethod
    def popular_item_transaction(self, m_conn, m_params: PopItemTxParams) -> float:
        raise NotImplementedError

    @abstractmethod
    def top_balance_transaction(self, m_conn) -> float:
        raise NotImplementedError

    @abstractmethod
    def related_customer_transaction(self, m_conn, m_params: RelCustomerTxParams) -> float:
        raise NotImplementedError

    def test_transaction(self, m_conn):

        k = 110102

        while True:
            with m_conn.cursor() as cur:
                query = "insert INTO cs5424db.workloadA.item (I_ID,I_NAME,I_PRICE,I_IM_ID,I_DATA) " \
                        "values ({}, 'noawtpfynitqxadf' ,330, 108, 'ugmvxubikoestjagbcxiytwclqdosiswxbf')".format(k)

                cur.execute(query)
                # print(cur.fetchone())
                m_conn.commit()
                k += 1

    def delivery_read_transaction(self, l_conn, m_params):
        pass

    def delivery_update_transaction1(self, l_conn, w_id, carrier_id, id_tuples):
        pass

    def delivery_update_transaction2(self, l_conn, c_id, ele, sum_value):
        pass

    def delivery_transaction_one_did(self, l_conn, m_params, d_id):
        pass

    def delivery_update_transaction3(self, l_conn, w_id, carrier_id, id_tuples, sum_map):
        pass

    def delivery_update_transaction4(self, l_conn, cid_map, sum_map):
        pass

