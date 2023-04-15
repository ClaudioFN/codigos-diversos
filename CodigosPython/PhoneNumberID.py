"""
Created Date: 11/04/2023
Last Update: 11/04/2023
Description: Identify the carrier and region of a phone number 
Observation: Code created to be used for brazilian content. Change the 'pt-br' to other countries.
"""
# Install the package phonenumbers
import phonenumbers
from phonenumbers import geocoder, carrier
import re 

phone_number_validator = "^\\+?[1-9][0-9]{7,14}$"

class PhoneData:
    # Initiate the program
    def __init__(self):
        PhoneData.type_the_number()
    
    # Validate the phone number typed
    def phone_validator(pPhoneTyped):
        result_validator = re.match(phone_number_validator, pPhoneTyped)

        if result_validator == None:
            print("Phone typed is invalid! Please try again!")
            return False 
        else:
            return True

    # Get the number from the user or finish the program if it is typed 'exit'
    def type_the_number():
        # Type your number with the code from your country and DDD
        phone_typed = input("\nType your phone number in the format\n +(international prefix)CC(coutry code)AA(area code)NNNNNNNN(nine digits number) or\n 'exit' to finish the program: ")
        # Finish the execution
        if phone_typed == 'exit':
            exit()

        validated = PhoneData.phone_validator(phone_typed)
        if validated:
            PhoneData.get_data(phonenumbers.parse(phone_typed))
            PhoneData.type_the_number()
        else:
            PhoneData.type_the_number()

    # Show the data about the phone number typed
    def get_data(phone_number):
        # Carrier
        origin_carrier = carrier.name_for_number(phone_number, 'pt-br')

        # Region
        region = geocoder.description_for_number(phone_number, 'pt-br')

        # Result
        print("Carrier: " + origin_carrier)
        print("Region: " + region)
        
# Call class
if __name__ == '__main__':
    PhoneData()
