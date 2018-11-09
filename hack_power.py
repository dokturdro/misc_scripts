# Input the hack
hack = input("Enter the hack you wish to process:")

# Define the function
def hack_calculator(hack,letters,phrases):

    # Check if the hack consists only of hack letters
    for letter in hack:
        if letter not in letters.keys():

            # Inform that the hack has invalid letters
            # Ask if the user wishes to update the hack letters
            hack_query = input("Letter '" + hack[letter] + "' is not "
                               "defined.\nWould you like to add"
                               " a new hack?")
            if hack_query in ['yes', 'y', 'tak']:

                # Get new letter and hack power, store it in the dictionary
                new_hack = input("Enter a new single letter hack:")
                if len(new_hack) == 1:
                    new_value = input("Enter a value for this hack:")
                    letters[str(new_hack)] = int(new_value)

                    # Ask if the user wishes to update phrases too
                    phrase_query = input("Would you like to add"
                                         " a new multiletter phrase hack?")
                    if phrase_query in ['yes', 'y', 'tak']:
                        new_hack = input("Please enter a new phrase:")
                        if len(new_hack) > 1:
                            new_value = input("Enter a value for this hack:")
                            phrases[str(new_hack)] = int(new_value)
                            hack = input("Enter a new hack you wish to process:")
                        else:
                            hack = input("This is a single letter hack not"
                                         " a phrase!\mEnter a new hack you wish"
                                         " to process:")
                    else:
                        hack = input("Enter a new hack you wish to process:")
                else:
                    hack = input("This is a phrase, not a single letter hack!")
                    break
            else:
                break


    # Loop the hack input and count instances
    letter_power = 0
    for letter_key in letters.keys():
        letter_power += letters[letter_key] * sum(range(hack.count(letter_key)+1))

    # Sort the phrases by length and remove values from unwanted keys
    phrase_power = 0
    for phrase_key in sorted(phrases, key=len, reverse=True):
        phrase_power += phrases[phrase_key] * hack.count(phrase_key)
        hack = hack.replace(phrase_key,'')

    # Print the final hack power
    print("Hack power is: " + str((letter_power + phrase_power)))

hack_calculator(hack,
                letters={'a': 1, 'b': 2, 'c': 3},
                phrases={'ba': 10, 'baa': 20,})



