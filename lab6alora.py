def encode(password):
    encoded = ''
    for i in password:
        num = int(i)
        num += 3
        encoded += str(num)
    return encoded

def decoded(password):
    decoded_password = ''
    for i in password:
        integer_num = int(i)
        integer_num -= 3
        decoded_password += str(integer_num)
    return decoded_password

if __name__ == "__main__":
    repeat_menu = True
    while repeat_menu:
        print("Menu")
        print("---------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print('')
        # begin if statements here.
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            user_pass = str(input("Please enter your password: "))
            user_pass = encode(user_pass)
            print("Your password has been encoded and stored!\n")
            print()
        elif menu_choice == 2:
            decoded_password = decoded(user_pass)
            print(f'The encoded password is {user_pass}, and the original password is {decoded_password}')
            print('') # enter decode program here
        elif menu_choice == 3:
            repeat_menu = False


