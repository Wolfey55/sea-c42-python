import math


donor_list = {
    'Bill Gates': [10000, 25000, 5000], 'Ed Sheeren': [3250]
}


mode = input("Welcome to Mailroom Madnes. \n"
"Choose from the following: \n"
"T - Send a (T)hank You \n"
"R - Create a (R)eport \n"
"quit - Quit the program")

# To send thank you email.
if mode == 'T' or 't':
    name = input("Please enter the donors name. ")
    amount = int(input("Please enter the donation amount."))
    for key in donor_list:
        if name == key:
            if amount != int:
                amount = int(input("Please enter the donation amount."))
            elif amount == int:
                donor_list[name].append(amount)
        elif name != key:
            # add new donor to list
            donor_list[name] = amount

    print("Dear %s, \n"
    " \n "
    "Thank you so much for your kind donation of $%s. We here at the Foundation \
for Homeless Whales greatly appreciate it. Your money will go towards \
creating new oceans on the moon for whales to live in. \n"
    " \n "
    "Thanks again, \n"
    "Jim Grant \n"
    "Director, F.H.W." % (name, amount))


"""class Donors(object):
    __init__ functions as the class constructor
    def __init__(self, name=None, orig_don=0, num_of_don=0, new_donation=0):
        self.name = name.lower()
        self.num_of_don = num_of_don
        self.new_donation = new_donation
        self.total_donations = self.orig_don + self.new_donation


mode = input("Send thank you or generate report?").lower()

if mode == "send thank you":
    name = input("Please enter the donors name. ").lower()
    amount = input("Please enter the donation amount.")
    for name in doner_list:
        if name == doner_list.name:
            if math.isnan(amount) = True:
                Re-prompt user for amount
            elif math.isnan(amount) = False:
                add donation to total donations

            print("email content with %s and %s added." % (name, amount))

         if name does not exist in database
            doner_list.append(Donors(name, 0, 0, amount))

if mode == "generate report":

    # membership: s = [1, 2, 3, 4, 5, 6]; 5 in s = True; 7 in s = False
    # s = "some string"; "some" in s = True

tuple('done'); (d, o, n, 'e')
nesting: l = [[1, 2, 3], [4, 5, 6]]; print(l[1])
a = [a, c, b]; a.sort(); a = [a, b, c]

animals = ["ant", "bat", "cat"]
print animals.index("bat")
animals.insert(1, "dog")
print animals


"""
