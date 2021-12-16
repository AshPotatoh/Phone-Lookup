import pandas as pd
import twilio
from twilio.rest import Client
import csv
import openpyxl
import os

    

#place your Twilio API Key here.
client = Client()


def lookup():



    column_names = ["Phone"]

    df = pd.read_excel("PhoneNumbers.xlsx", sheet_name=0)
    numbers = df['Phone'].tolist()

    #Creates json file to store get requests, then loops through the list of phone numbers.
    with open('carrier.json', 'a') as f:

        bad_numbers = ['999-999-9999']
        writer = csv.writer(f)
        for num in numbers:
            if num in bad_numbers:

                print("Error Found" + num)
                f.write("{'name': 'Error Not Found'}")
                continue

            phone_number = client.lookups \
                            .phone_numbers(num) \
                            .fetch(type=['carrier'])


            carrier = phone_number.carrier
        

            print(num + "found!")
            f.write(str(carrier))
            f.write("\n")


lookup()