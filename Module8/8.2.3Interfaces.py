from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class PhonePay(Payment):
    def pay(self):
        return "Do payment via Phone pay method"


class Gpay(Payment):
    def pay(self):
        return "I want to pay via Gpay"


class UPIPay(Payment):

    def pay(self):
        return " Pay via UPI payment method"


class BhimPay(Payment):

    def bhim_pay(self):
        return "Pay via Bhim UPI payment"

    def pay(self):
        return "Pay via bhim pay if other payment methods not works"


gpy = Gpay()
print(gpy.pay())

b = BhimPay()
print(b.bhim_pay())


from abc import ABC, abstractmethod


class OnlinePayment(ABC):
    def online_pay(self):
        return "Online payment method"


class MyPayments(OnlinePayment, Payment):

    def online_pay(self):
        return "I want to Pay via netbanking on online mode"

    def pay(self):
        return "I want pay money via online method with credit card payment"

    def cash_payment(self):
        return "I want to pay cash amount to the user"


m = MyPayments()
net_payment = m.online_pay()
print(net_payment)

credit_pay = m.pay()
print(credit_pay)

cash_pay = m.cash_payment()
print(cash_pay)
