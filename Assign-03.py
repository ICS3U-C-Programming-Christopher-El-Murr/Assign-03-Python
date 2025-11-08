#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 11 08, 2025
# This program asks the user to input the air quality index
# Then procedes to git them the air quality


def main():
    try:
        # ask the user to input the air quality index
        user_input = int(input("Please enter the air quality index: "))
        # If the number is between 0 and 50 then display the air quality is good
        if user_input >= 0 and user_input <= 50:
            print(
                "The air quality is good. THis means that Polution poses little to no risk."
            )
        # If the number is between 51 and 100 then display the air quality index is moderate
        elif user_input >= 51 and user_input <= 100:
            print(
                "The air quality is moderate.  This means that there may be a health concern for people who are usually sensitive to air pollution."
            )
            # If the number is between 101 and 150, then display that the air quality is unhealthy for sensitive groups
        elif user_input >= 101 and user_input <= 150:
            print(
                "The air quality is unhealthy for sensitive groups.  This means that members of the general public are not likely to be affected, however sensitive groups may experience health effects"
            )
            # If the number is between 151 and 200, then display that the air quality is unhealthy
        elif user_input >= 151 and user_input <= 200:
            print(
                "The air quality is unhealthy.  This means that everyone may begin to experience serious health effects, and members of sensitive groups may experience more serious health effects."
            )
            # If the number is between 201 and 300, then display that the air quality is very unhealthy
        elif user_input >= 201 and user_input <= 300:
            print(
                "The air quality is very unhealthy.  This means that everyone may experience more serious health effects"
            )
            # If the number is between 301 and 500, then display that the air quality is Hazardous
        elif user_input >= 301 and user_input <= 500:
            print(
                "The air quality is Hazardous.  This means that the entire populations is more likely to be affected "
            )
    except ValueError:
        print("This is not a valid integer.")
        # display Stay safe
    finally:
        print("Stay safe!")


if __name__ == "__main__":
    main()
