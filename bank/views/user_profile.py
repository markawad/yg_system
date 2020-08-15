from django.shortcuts import render
from bank.selectors.card import CardSelector
from bank.selectors.transaction import TransactionSelector
from django.core.exceptions import ObjectDoesNotExist


def user_profile(request, card_number):
    # Card does not exist
    try:
        student = CardSelector().get_student_by_card_number(card_number)
    except ObjectDoesNotExist:
        err = 'Card number invalid or does not exist.'
        context = {
            'err': err,
            'num': card_number
        }
        return render(request, 'bank/user_profile.html', context)
    # Card exists
    transactions = TransactionSelector().get_all_transactions_by_card(card_number)
    context = {
        'student': student,
        'transactions': transactions
    }
    return render(request, 'bank/user_profile.html', context)
