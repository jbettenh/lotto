import os
import json
import random
import email_ticket


def main():
    print('\n')

    play = input('Which game would you like to play? ').lower()
    amount_tickets = int(input('How many tickets would you like? '))
    email_receipt = input("Would you like to send an email of the tickets? (yes/no) ").lower()

    while amount_tickets != 0:
        picks = gen_lotto_numbers(play)
        ticket = print_ticket(picks)

        if email_receipt == 'yes':
            player = input("Enter your email address: ")
            html_tickets = f" <html> <body><p>Hi,<br>Your ticket is: <br>{ticket}</p></body></html>"
            email_ticket.send_email(player, "Your Python Generated Lotto Numbers", ticket, html_tickets)
        else:
            print(ticket)

        amount_tickets -= 1


def load_contest():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'config_contests.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def gen_lotto_numbers(choice):
    contest_rules = load_contest()
    lotto_numbers = []

    if choice == 'megaball':
        index = 0
    elif choice == 'powerball':
        index = 1
    elif choice == 'eurojackpot':
        index = 2
    else:
        print('Pick a game.')

    game = contest_rules['contests'][index]['name']
    ball_amount = contest_rules['contests'][index]['amount'] + 1
    special_ball = contest_rules['contests'][index]['extra']
    first_ball = contest_rules['contests'][index]['start']
    last_ball = contest_rules['contests'][index]['end']
    first_special = contest_rules['contests'][index]['extra_start']
    last_special = contest_rules['contests'][index]['extra_end']


    print(f'Loading config for {game}')
    print('Printing ticket.....\n')

    for ball in range(1, ball_amount):
        current_pick = random.randint(first_ball, last_ball)

        while current_pick in lotto_numbers:
            current_pick = random.randint(first_ball, last_ball)

        lotto_numbers.append(current_pick)

    for special in range(special_ball):
        lotto_numbers.append(random.randint(first_special, last_special))

    return lotto_numbers


def print_ticket(numbers):
    pretty_ticket = ""
    for idx, ball in enumerate(numbers):
        pretty_ticket += f'Number {idx + 1} is {ball},  \n'

    return pretty_ticket


if __name__ == '__main__':
    main()
