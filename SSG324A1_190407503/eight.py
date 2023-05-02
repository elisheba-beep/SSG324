birthdayDictionary = {"Melissa": "June 16", "Joseph": "September 2", "Emmanuella": "March 23"}
userName = input("What is your name?:")
userBirthday = birthdayDictionary.get(userName)
if userBirthday == None:
    print("I do not have birthday information for {}".format(userName))
else:
    print("{0} is the birthday of {1}".format(userBirthday, userName))