minimum = None

maximum = None
while True:     ## infinite loop so use "break" to exit
        number = input('Please enter a number, or "stop" to stop: ' )
        if number in ["STOP", "stop"]:
            print ("breaking while loop")
            break
        try:
            num = float(number)
            if (minimum) is None or (num < minimum):
                minimum = num
            if (maximum) is None or (num > maximum):
                maximum = num
            print ("Maximum: ", maximum)
            print ("Minimum: ", minimum)

        except ValueError:
            print("Non numeric data was entered.")
        except:
            print("Error with input...")

print ("Final Maximum: ", maximum)
print ("Final Minimum: ", minimum)