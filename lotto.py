import os
import json
import random



def main():
    print('\n')
    contest_rules = load_contest()
    play = input('Which game would you like to play? ').lower()

    if play == 'megaball':
        game = contest_rules['contests'][0]['name']
        ball_amount = int(contest_rules['contests'][0]['amount']) + 1
        special_ball = contest_rules['contests'][0]['extra']
        first_ball = contest_rules['contests'][0]['start']
        last_ball = contest_rules['contests'][0]['end']
        first_special = contest_rules['contests'][0]['extra_start']
        last_special = contest_rules['contests'][0]['extra_end']

    elif play == 'powerball':
        game = contest_rules['contests'][1]['name']
        ball_amount = int(contest_rules['contests'][1]['amount']) + 1
        special_ball = contest_rules['contests'][1]['extra']
        first_ball = contest_rules['contests'][1]['start']
        last_ball = contest_rules['contests'][1]['end']
        first_special = contest_rules['contests'][1]['extra_start']
        last_special = contest_rules['contests'][1]['extra_end']
    else:
        print('Pick a game.')


    print(f'Loading config... for {game}')
    print('Printing ticket.....\n')

    for ball in range(1, ball_amount):
        num = random.randint(first_ball, last_ball)
        print(f'Number {ball} is {num}')

    for special in range(special_ball):
        special_num = random.randint(first_special, last_special)
        print(f'{game}  is {special_num}')


def load_contest():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'contest_config.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)




if __name__ == '__main__':
    main()
