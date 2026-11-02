def verify_card_number(card_number):
    card_number = card_number.replace('-', '').replace(' ', '')
    reversed_card = card_number[::-1]

    total = 0
    for i, char in enumerate(reversed_card):
        digit = int(char)
        if i % 2 == 1:
            digit *=2
            if digit > 9:
                digit -= 9
        total += digit
    if total % 10 == 0:
        return 'VALID!'
    else:
        return "INVALID!"
