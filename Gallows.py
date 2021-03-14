import random

WORDS = [
    'cat',
    'dog',
    'macos',
    'charge',
    'september',
    'holiday',
    'tower',
    'cucumber',
    'vacation',
    'earl',
    'sweatshirt'
]  # TODO: add more words

MAX_ERRORS = 10


def return_random_word():
    return random.choice(WORDS)


def handle_user_input():
    user_input = input("Please, input letter: ")
    return user_input


def get_initial_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses


def is_game_finished(statuses, current_errors):
    if current_errors >= MAX_ERRORS:
        return True

    for status in statuses:
        if not status:
            return False

    return True


def perform_check_action(word, statuses, letter):
    if letter not in word:
        return False

    for index, l in enumerate(word):
        if letter == l:
            statuses[index] = True

    return True


def print_word(word, statuses):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()


def main():
    word = return_random_word()
    statuses = get_initial_statuses(word)
    current_errors = 0

    while not is_game_finished(statuses, current_errors):
        print_word(word, statuses)
        letter = handle_user_input()
        result = perform_check_action(word, statuses, letter)

        if not result:
            current_errors += 1


main()

while True:
    input("Game is finished! Press any button to exit:")
    break
