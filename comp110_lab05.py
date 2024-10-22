"""
comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

def max_wind_speed(hurricane_filename):
   a = open(hurricane_filename,'r')
   biggest = 0
   for line in a:

    vals = line.split(',')
    location = int(vals[4])
    if location > biggest:
        biggest = location
      
   return biggest
       


def contains_word(word, review):
    word = word.lower()
    review = review.lower()
    return word in review.split()



def test_max_wind_speed():
    """ Function that tests the max_wind_speed function. """
    mw = max_wind_speed('irma.csv')
    print("Starting test of max_wind_speed")
    if mw == 185:
        print("Wind speed passed")
    else: 
        print("FAILED: Not implemented yet.")

    mw1 = max_wind_speed('florence.csv')
    print("Starting test of max_wind_speed")
    if mw1 == 140:
        print("Wind speed passed")
    else: 
        print("FAILED: Not implemented yet.")

    mw2= max_wind_speed('dorian.csv')
    print("Starting test of max_wind_speed")
    if mw2 == 185:
        print("Wind speed passed")
    else: 
        print("FAILED: Not implemented yet.")
 


def test_contains_word():
    """ Function that tests the contains_word function. """

    print("\nStarting test of contains word")

    if contains_word('ok', 'ok') != True:
        print("FAILED: contains_word('ok', 'ok')")
    elif contains_word('ok', 'OK') != True:
        print("FAILED: contains_word('ok', 'OK')")
    elif contains_word('ok', 'bad') != False:
        print("FAILED: contains_word('ok', 'bad')")
    elif contains_word('ok', 'movie ok') != True:
        print("FAILED: contains_word('ok', 'movie ok')")

    elif contains_word('OK','Movie ok' ) != True:
        print("FAILED: contains_word('ok', 'movie ok')")
    elif contains_word('ok','Movie OK' ) != True:
        print("FAILED: contains_word('ok', 'movie ok')")
    elif contains_word('ok', 'stoke' ) != True:
        print("FAILED: contains_word('ok')")
    else:
        print("All contains_word test cases passed!")


    print("Done testing contains word")


def main():
    """ Calls the tester functions in the code. """
    test_max_wind_speed()
    test_contains_word()

if __name__ == "__main__":
    main()
