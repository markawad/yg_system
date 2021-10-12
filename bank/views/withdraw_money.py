from django.shortcuts import render, redirect
from bank.services import CardService
from bank.selectors import CardSelector
from bank.selectors import TransactionSelector
from django.core.exceptions import ValidationError


def withdraw_money(request, card_number):

    if not request.user.is_authenticated:
        return redirect('config:login')

    # If no card is inserted
    if 'amount' not in request.POST:
        card = CardSelector().get_card_by_number(card_number)
        return redirect(card)

    err = None
    success = None
    card = None

    try:
        card = CardSelector().get_card_by_number(card_number)
        CardService().withdraw_money(card=card, amount=int(request.POST['amount']))
    # Incorrect amount / negative values
    except ValueError as e:
        ex = ''.join(list(e))
        err = f'Error: {ex}'
    # If amount exceeds max
    except ValidationError as e:
        ex = ''.join(list(e))
        err = f'Error: {ex}'
    if not err:
        success = f'{request.POST["amount"]} removed from the card successfully.'

    transactions = TransactionSelector().get_all_transactions_by_card(card_number)
    context = {
        'err': err,
        'success': success,
        'student': card.holder,
        'transactions': transactions
    }
    return render(request, 'bank/user_profile.html', context)
