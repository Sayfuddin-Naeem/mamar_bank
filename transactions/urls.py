from django.urls import path
from .views import TransactionReportView, DepositMoneyView, WithdrawaMoneyView, LoanRequestView, PayLoanView, LoanListView

urlpatterns = [
    path('report/', TransactionReportView.as_view(), name='transaction_report'),
    path('deposit/', DepositMoneyView.as_view(), name='deposit_money'),
    path('withdraw/', WithdrawaMoneyView.as_view(), name='withdraw_money'),
    path('loan/request/', LoanRequestView.as_view(), name='loan_request'),
    path('loan/list/', LoanListView.as_view(), name='loan_list'),
    path('loan/pay/<int:loan_id>', PayLoanView.as_view(), name='loan_pay'),
]
