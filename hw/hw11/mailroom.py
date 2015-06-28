import sys

donor_list = {
    'Bill Gates': [10000, 25000, 5000, 17500],
    'Ed Sheeren': [3250, 500],
    'Eddie Murphy': [5000, 1750, 3200],
    'Tom Cruise': [20000, 15000]
}


def create_report():
    for key in donor_list:
        print("Name: ", key)
        print("Donations: ", donor_list.get(key))


def donor_names():
    for key in donor_list:
        print(key)


def add_donation(donor, dollars):
    for key in donor_list:
        if donor == key:
            if type(dollars) == int:
                # append donation to existing donor's record
                donor_list[donor].append(dollars)
            else:
                # Re-prompt user for donation amount
                dollars = int(input("Please enter the donation amount."))

        #else:
            # add new donor to list
            # donor_list[donor] = amount
            # print(donor_list)

def send_thanks(donor, dollars):
    print("Dear %s, \n" "\n" "Thank you so much for your kind donation of \
        $%s. We here at the Foundation for Homeless Whales greatly appreciate \
        it. Your money will go towards creating new oceans on the moon for \
        whales to live in. \n" "\n" "Thanks again, \n" "Jim Grant \n"
        "Director, F.H.W." % (donor, dollars))

if __name__ == "__main__":

    mode = input("Welcome to Mailroom Madness.\n "
    "Choose from the following:\n "
    "T - Send a (T)hank You\n "
    "R - Create a (R)eport\n "
    "quit - Quit the program\n ")

    if mode == 'T' or mode == 't':

        name = input("Please enter a name, or choose from the following:\n "
        "list - Print a list of previous donors\n "
        "quit - Return to main menu\n ")

        amount = int(input("Please enter the donation amount.\n "))

        if name == 'list':
            donor_names()

        elif name == 'quit':
            exit()

        else:
            add_donation(name, amount)
            print(donor_list)
            send_thanks(name, amount)

    if mode == 'R' or mode == 'r':
        create_report()
