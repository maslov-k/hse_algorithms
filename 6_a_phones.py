def clear_phone_number(phone_number):
    clean_number = 0

    base = 1

    for i in range(len(phone_number) - 1, -1, -1):
        c = phone_number[i]

        if c.isdigit():
            if base == 10000000000:
                clean_number += base * 7
            else:
                clean_number += base * int(c)
            base *= 10

    if base == 10000000:
        clean_number += 7495 * base

    return clean_number


def main():
    new_contact = input()

    clean_number = clear_phone_number(new_contact)

    for i in range(3):
        print('YES' if clean_number == clear_phone_number(input()) else 'NO')


if __name__ == '__main__':
    main()
