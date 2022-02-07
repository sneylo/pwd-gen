import random


def random_number():
    return random.randint(0, 9)


def random_upper_char():
    return chr(random.randint(65, 90))


def random_lower_char():
    return chr(random.randint(97, 122))


def main():
    pwd = []
    pwd_length = (input("Length of the password?\n"))
    while pwd_length == "":
        pwd_length = input("Length of the password?\n")
    choices = input("Do you want numbers or characters? (Default is combination of both)\n")
    choices_char = ""
    if choices in ["characters", "char", "chr", "2"]:
        choices_char = input("Do you prefer lower, upper or random? (default is upper) \n")
    for i in range(abs(int(pwd_length))):
        if choices in ["numbers", "num", "1"]:
            pwd.append(random_number())
        elif choices_char in ["lower", "upper", "random", "1", "2", "3"]:
            if choices_char in ["lower", "1"]:
                pwd.append(random_lower_char())
            elif choices_char in ["upper", "2"]:
                pwd.append(random_upper_char())
            elif choices_char in ["random", "3"]:
                pwd.append(random.choice([random_upper_char, random_lower_char])())
        else:
            pwd.append(random.choice([random_number, random_lower_char, random_upper_char])())
    print(*pwd, sep="")


if __name__ == '__main__':
    main()
    while input("do you want another password?\n") in ['Y', 'y', "yes", "YES", "1"]:
        main()
    else:
        print("Goodbye!")
