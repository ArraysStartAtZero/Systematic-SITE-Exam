from time import sleep
import sys
import time
import os
import csv
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Here line below we define our system and it starts from that point.
def Site():
    os.system("cls" if os.name == "nt" else "clear")
    # In line below that function sprints is a small aniamtion for printed text we use across our porgram.
    def sprints(str):
        for c in str + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)

    # Thats the first thing user sees in program with sprint and than printing a big text to make menu look more like interface.
    sprints("Starting Up ......")

    print(
        """

   _____              _                           _    _                       __ _____
  / ____|            | |                         | |  (_)           /\        / // ____|
 | (___   _   _  ___ | |_  ___  _ __ ___    __ _ | |_  _   ___     /  \      / /| (___
  \___ \ | | | |/ __|| __|/ _ \| '_ ` _ \  / _` || __|| | / __|   / /\ \    / /  \___ |
  ____) || |_| |\__ \| |_|  __/| | | | | || (_| || |_ | || (__   / ____ \  / /   ____) |
 |_____/  \__, ||___/ \__|\___||_| |_| |_| \__,_| \__||_| \___| /_/    \_\/_/   |_____/
           __/ |
   _____  |___/  _______  _____
  / ____||_   _||__   __||  ____|
 | (___    | |     | |   | |__
  \___ \   | |     | |   |  __|
  ____) | _| |_    | |   | |____
 |_____/ |_____|   |_|   |______|         _    _                 __  __             _         _
 |  ____|                                | |  (_)               |  \/  |           | |       | |
 | |__  ___   _ __  ___   ___  __ _  ___ | |_  _  _ __    __ _  | \  / |  ___    __| | _   _ | |  ___
 |  __|/ _ \ | '__|/ _ \ / __|/ _` |/ __|| __|| || '_ \  / _` | | |\/| | / _ \  / _` || | | || | / _ |
 | |  | (_) || |  |  __/| (__| (_| |\__ \| |_ | || | | || (_| | | |  | || (_) || (_| || |_| || ||  __/
 |_|   \___/ |_|   \___| \___|\__,_||___/ \__||_||_| |_| \__, | |_|  |_| \___/  \__,_| \__,_||_| \___|
                                                          __/ |
                                                         |___/

                                                                                                  """
    )

    time.sleep(2.5)
    # function loading is just to print please wait in other function.
    def loading():
        print("Please wait")
        sprint(
            """

  _____   _         _    _    _
 |  __ \ | |       | |  | |  (_)
 | |__) || |  ___  | |_ | |_  _  _ __    __ _
 |  ___/ | | / _ \ | __|| __|| || '_ \  / _` |
 | |     | | |(_)| | |_ | |_ | || | | | |(_| |
 |_|     |_| \___/  \__| \__||_||_| |_| \__, |
                                         __/ |
                                        |___/


      """
        )

    # function below is first function to count the data entries in the document
    def function1():

        with open("WindData.csv", "r") as read_obj:
            x = 0
            csv_reader = reader(read_obj)
            for row in csv_reader:
                x = x + 1
            print(x)

    # In this function we made it so user can input date and than get the highest wind speed for that day.
    def function2():

        y = input(
            "Enter Date between 16.11.2021 - 17.10.2021 [dd/mm/yyyy] :"
        )  # y is users input of date that we later use to search in document
        df = pd.read_csv("WindData1.csv", sep=";", usecols=["Date", "WindSpeed"])
        idx = df[
            df["Date"] == y
        ]  # if the date and the y is the same its gonna be found in dataframe and printed.
        column = idx["WindSpeed"]
        max_value = column.max()
        print("The maximum wind speed of the " + y + " is : " + max_value)

    # function below is made for filtering data we use it aswell in other fucntions before making graphs.
    def function3():
        # We definded the vaiable options for wind speed that are acceptable and if the reading is eaither to low or high it gets igonred since only values that equal to options gonna be in dataframe.
        df = pd.read_csv("WindData.csv", sep=";")
        options = ["2,5","2,6","2,7","2,8","2,9","3","3,1","3,2","3,3","3,4","3,5","3,6","3,7","3,8","3,9","4","4,1","4,2","4,3","4,4","4,5","4,6","4,7","4,8","4,9","5","5,1","5,2","5,3","5,4","5,5","5,6","5,7","5,8","5,9","6","6,1","6,2","6,3","6,4","6,5","6,6","6,7","6,8","6,9","7","7,1","7,2","7,3","7,4","7,5","7,6","7,7",
        ]

        rslt_df = df[
            df["WindSpeed"].isin(options)
        ]  # making a resoulting dataframe with the resoults and printing it.
        print("\nResult dataframe :\n", rslt_df)

    # thats the function for a bar graph and mean wind values for directions.
    def function4():

        df = pd.read_csv("WindData.csv", sep=";")
        options = ["2,5","2,6","2,7","2,8","2,9","3","3,1","3,2","3,3","3,4","3,5","3,6","3,7","3,8","3,9","4","4,1","4,2","4,3","4,4","4,5","4,6","4,7","4,8","4,9","5","5,1","5,2","5,3","5,4","5,5","5,6","5,7","5,8","5,9","6","6,1","6,2","6,3","6,4","6,5","6,6","6,7","6,8","6,9","7","7,1","7,2","7,3","7,4","7,5","7,6","7,7",
        ]
        rslt_df = df[df["WindSpeed"].isin(options)]

        df = rslt_df
        # here i define each direction with the correspondend values like with options just doing it for each direction, since thaat is an integer not string i tired using an alternative method with >< or "inrage" but thats the only solution that worked.
        east = [45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,
        ]
        # under there i make dataframe with resoults and i do it for each direction.
        rslt_dfeast = df[df["WindDirection"].isin(east)]

        south = [136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,
        ]

        rslt_dfsouth = df[df["WindDirection"].isin(south)]

        west = [225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,
        ]

        rslt_dfwest = df[df["WindDirection"].isin(west)]

        north = [315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,
        ]

        rslt_dfnorth = df[df["WindDirection"].isin(north)]
        # here i make a new dataframe with mean "avarage" value of each wind direction
        df_meannorth = rslt_dfnorth["WindDirection"].mean()
        df_meansouth = rslt_dfsouth["WindDirection"].mean()
        df_meaneast = rslt_dfeast["WindDirection"].mean()
        df_meanwest = rslt_dfwest["WindDirection"].mean()

        total_rowsnorth = rslt_dfnorth.count
        print(total_rowsnorth)
        total_rowssouth = rslt_dfsouth.count
        print(total_rowssouth)
        total_rowseast = rslt_dfeast.count
        print(total_rowseast)
        total_rowswest = rslt_dfwest.count
        print(total_rowswest)
        # here we make a bargraph using plt.
        plotvalue = [df_meannorth, df_meansouth, df_meaneast, df_meanwest]
        names = ["north", "south", "east", "west"]
        plt.bar(names, plotvalue)
        plt.show()
        # here after the user closes graph they can input the dircetion and find specific mean value for that direction.
        def more2():
            again = input("Enter Wind Direction :")
            if again == "east":
                print(df_meaneast)
            if again == "south":
                print(df_meansouth)
            if again == "west":
                print(df_meanwest)
            if again == "north":
                print(df_meannorth)

        more2()

    # here we filter data like earlier and make a scatter plot.
    def function5():
        df = pd.read_csv("WindData.csv", sep=";")
        options = ["2,5","2,6","2,7","2,8","2,9","3","3,1","3,2","3,3","3,4","3,5","3,6","3,7","3,8","3,9","4","4,1","4,2","4,3","4,4","4,5","4,6","4,7","4,8","4,9","5","5,1","5,2","5,3","5,4","5,5","5,6","5,7","5,8","5,9","6","6,1","6,2","6,3","6,4","6,5","6,6","6,7","6,8","6,9","7","7,1","7,2","7,3","7,4","7,5","7,6","7,7",
        ]

        rslt_df = df[df["WindSpeed"].isin(options)]
        data = rslt_df
        plt.scatter(data["Timestamp"], data["WindDirection"])
        plt.xlabel("Timestamp")
        plt.ylabel("WindDirection")
        plt.show()

    # below is another animation tool just with different values.
    def sprint(str):
        for c in str + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.0 / 40)

    # after each option of menu was fulfilled we display that so user can choose to either go back to menu or just shutthe program down
    def more():
        again = input("Back to menu? yes/no  >")
        if again == "yes":
            Site()

        else:
            sprints("Shutting Down!")
            time.sleep(3)
            quit()

    sprint("What would you like to do?.  .  .")
    # here i define the menu and all the options for menupoints
    def menu():
        print("[1] Count the number of Data Points")
        print("[2] Max wind speed for selected date")
        print("[3] Filter Data")
        print("[4] Plot bar graph of mean wind speed for each wind direction")
        print("[5] Plot scatter diagram")

    # if imput of pption equals functions number its gonna run that function.
    menu()
    option = int(input("Enter your option :"))
    while option != 0:
        if option == 1:

            print("Counting Data Entries")
            loading()
            function1()
            more()

        if option == 2:

            loading()
            function2()
            more()

        if option == 3:

            print("Filtering data below 2.5 m/s and above 25m/s")
            loading()
            function3()
            more()

        if option == 4:

            print("Plotting avarage wind speed for each wind direction")
            loading()
            function4()
            more()

        if option == 5:

            print("Plotting Scatter Diagram")
            loading()
            function5()
            more()
        else:
            print("invalid")
            sprints("Returning to start.")
            Site()

    print()


Site()
