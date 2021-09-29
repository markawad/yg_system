from django.shortcuts import render, redirect
from bank.selectors import CardSelector
from django.core.exceptions import ObjectDoesNotExist


def scan_card(request):

    if not request.user.is_authenticated:
        return redirect('config:login')

    if 'card_number' not in request.GET:
        return render(request, 'bank/user_profile.html')
    try:
        card = CardSelector().get_card_by_number(request.GET['card_number'])
    except ObjectDoesNotExist:
        err = 'Card does not exist.'
        context = {
            'err': err,
            'num': request.GET['card_number']
        }
        return render(request, 'bank/user_profile.html', context)
    except ValueError:
        err = 'Please enter a valid number.'
        context = {
            'err': err,
            'num': request.GET['card_number']
        }
        return render(request, 'bank/user_profile.html', context)
    return redirect(card)
