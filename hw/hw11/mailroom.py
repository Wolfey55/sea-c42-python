donor_list = {
    'Bill Gates': [10000, 25000, 5000, 17500],
    'Ed Sheeren': [3250, 500],
    'Eddie Murphy': [5000, 1750, 3200],
    'Tom Cruise': [20000, 15000],
    'Stephan Bosch': [2500, 3250, 1000]
}


def create_report():
    print("Name\t\t|\tTotal\t|\t#\t|\tAverage\n" + ('_' * 50))
    sorted_list = sorted(donor_list, key=lambda donor: sum(donor_list[donor]), reverse=True)
    #import pdb; pdb.set_trace()
    for key in sorted_list:
        donor_name = key
        total = sum(donor_list[key])
        number = len(donor_list[key])
        average = total / number
        print('%s\t|\t$%d\t|\t%d\t|\t$%d' % (donor_name, total, number, average))


def donor_names():
    for key in donor_list:
        print(key)


def append_donation(donor, dollars):
    # append donation to existing donor's record
    donor_list[donor].append(dollars)


def add_donor(donor, dollars):
    donor_list[donor] = dollars


def send_thanks(donor, dollars):

    letter = ("Dear %s, \n" "\n" "Thank you so much for your kind donation of\
$%s. We here at the Foundation for Homeless Whales greatly appreciate \
it. Your money will go towards creating new oceans on the moon for\
whales to live in. \n" "\n" "Thanks again, \n" "Stephan Bosch \n"
"Director, F.H.W." % (donor, dollars))

    with open(donor + '.txt', 'w') as f:
        f.write(letter)

    print(letter)


if __name__ == "__main__":

    while True:
        mode = input("Welcome to Mailroom Madness.\n "
        "Choose from the following:\n "
        "T - Send a (T)hank You\n "
        "R - Create a (R)eport\n "
        "quit - Quit the program\n ")


        while True:
            if mode == 'T' or mode == 't':

                while True:
                    name = input("Please enter a name, or choose from the following:\n "
                    "list - Print a list of previous donors\n "
                    "quit - Return to main menu\n ")

                    if name == 'quit':
                        break

                    elif name == 'list':
                        donor_names()

                    else:
                        while True:
                            try:
                                amount = int(input("Please enter the donation amount.\n "))
                            except ValueError:
                                print("Invalid input, please enter a number.")
                                continue
                            else:
                                break

                        check_list = False
                        for key in donor_list:
                            if name == key:
                                check_list = True
                                break
                            else:
                                check_list = False

                        if check_list == True:
                            append_donation(name, amount)
                        else:
                            # add new donor to list
                            add_donor(name, amount)

                        send_thanks(name, amount)

                        break

                break

            if mode == 'R' or mode == 'r':
                create_report()

                break

            if mode == 'quit':
                exit()

                break

            else:
                mode = input("Invalid input. Please enter 'R', 'T' or 'quit'")
