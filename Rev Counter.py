chips_are_good = True
while chips_are_good:

    # lines 4 - 16 is what lets the user input the TLE as two lines (one paste function). User MUST press Enter, Ctrl-Z, and then Enter again

    print("Please enter TLE. After it's pasted, press 'Enter', then 'Ctrl-Z, and 'Enter' again:")
    contents = []
    while True:
        try:
            tle = input()
        except EOFError:
            break
        contents.append(tle)

    temp_list = (contents[0] + " ") + contents[1]   # this addes a space to the end of the first index. If not, it will combine the '2' from the second line
                                                    # to the end of the first line

    tle_list = temp_list.split()

    # define TLE elements

    epoch_date = tle_list[3]   #didn't make this a float cause it doesn't include the 0 in two digit year. Ex. (08)
    epoch_day = float(epoch_date[2:])
    epoch_day_decimal = float(epoch_date[5:])
    mean_motion = float(tle_list[16][0:11])
    current_rev = int(tle_list[16][11:16])

    # determine how long in epoch time it takes to complete one rev

    def rev_time_epoch_time():
        rev_per_hour = 24 / mean_motion
        one_rev_in_epoch = rev_per_hour / 24 
        return one_rev_in_epoch

    # convert the current zulu time to a decimal so we can do calculations

    def current_time_to_epoch():  
        while True:
            current_time = input("What time is it in zulu time? Please use format hhmm: ")
            if len(str(current_time)) != 4:
                current_time
            elif current_time.isdigit() == False:
                current_time
            else:
                break            
        hours = int(current_time[0:2])
        minutes = int(current_time[2:]) / 60
        time = hours + minutes
        epoch_time = time / 24 
        return epoch_time

    # take the time delta and divide by the amount of time it takes to complete one rev in epoch time

    def rev_number_since_tle():
        global number_of_revs
        epoch_time_delta = current_time_to_epoch() - epoch_day_decimal
        number_of_revs = epoch_time_delta / rev_time_epoch_time()
        return number_of_revs


    # add the number of revs that passed to the total revs, and that is the rev number based on the zulu time inputed by user

    print(f"Your current rev number based off of the TLE is {current_rev}.")
    print(f"Your new rev number is based off of the time inputted is: " + str(current_rev + rev_number_since_tle()))
    

    # if (current_rev + number_of_revs) < current_rev:
    #     print("Something went wrong. Ensure the time you entered and the TLE Julian Day is the same and you entered a time after the TLE")
    
    while True:
        another_input = input("Would you like to get another rev time? Please enter 'y' or 'n': ").lower()
        another_input

        if another_input == 'y':
            break
        elif another_input == 'n':
            chips_are_good = False
            break
        else:
            print("Please enter y or n: ")