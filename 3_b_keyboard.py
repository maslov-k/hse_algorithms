class Keyboard:
    def __init__(self, buttons_life):
        self.buttons_life = buttons_life

    def tap(self, button_index):
        self.buttons_life[button_index] -= 1

    def print_buttons_status(self):
        for i in self.buttons_life:
            print('no' if i >= 0 else 'yes')


if __name__ == '__main__':
    _n = int(input())
    _buttons_life = list(map(int, input().split()))

    keyboard = Keyboard(_buttons_life)

    _k = int(input())
    _taps = list(map(int, input().split()))

    for tap in _taps:
        keyboard.tap(tap - 1)

    keyboard.print_buttons_status()
