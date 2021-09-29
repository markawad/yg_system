from django.shortcuts import render, redirect
from bank.selectors import CardSelector


def total_money(request):

    if not request.user.is_authenticated:
        return redirect('config:login')

    money = CardSelector().get_total_money_in_bank()
    cards = CardSelector().get_all_cards()
    context = {
        'total_money': money,
        'cards': cards
    }
    return render(request, 'bank/home.html', context)
