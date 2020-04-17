# Alessandra Guerra Delgado
# Integration Project Interactive Map of Peru!
# Learn more than just the Geography! Culture, History, Cuisine, and Customs

# Side-Note: might make this about the most popular regions of Peru rather
# than all regions

def main_menu():
    print("Welcome to the best Interactive Map of all Time!")
    print("Today, we will be traveling to the mystic country of Peru!")
    print("Peru is a beautiful country with a history rich in ancient "
          "civilization, amazing cuisine, and spectacular landscape")
    print("On this interactive map journey, you will learn all about the "
          "history, people, and customs of each region in Peru.")
    continue_program = True
    while continue_program:
        print("Here is going to be your Main Menu.")
        print("You may chose to go in order or jump around. Have fun!")
        print("1. Calculate Ticket Price")
        print("2. The Regions of Peru")
        print("3. Fun Facts! ")
        print("4. Quit")
        user_choice = int(input("Enter number to make selection: "))
        if user_choice == 1:
            ticket_main()
        elif user_choice == 2:
            print("Welcome to Peru!")
            print("We are extremely excited to have you here")
            print("Peru is separated into 24 different regions."
                  "Similar to Provinces and "
                  "States.")
            peru_regions()
        elif user_choice == 3:
            print("hi")
        elif user_choice == 4:
            continue_program = False
        else:
            print("Invalid selection. Try again.")


def calculate_ticket(start_location):
    """This program calculates how much your ticket will cost based on where
    you decide to fly out from"""

    if start_location == 1:
        economy_ticket_price = 400
    elif start_location == 2:
        economy_ticket_price = 500
    elif start_location == 3:
        economy_ticket_price = 350
    else:
        economy_ticket_price = 600

    print("The cost of your ticket is $",
          format(economy_ticket_price, '0.2f'),
          sep='')
    upgrade = input(
        "Would you like to upgrade your ticket to first class for an "
        "additional charge of $200.00?")
    if upgrade == 'yes':
        economy_ticket_price += 200
        print("AYE! Flying in STYLE! Your total ticket cost is now $",
              format(economy_ticket_price, '0.2f'), sep='')
    elif upgrade == 'no':
        print(
            "Way to save! First class is overrated. Your total ticket cost "
            "is $",
            format(economy_ticket_price, '0.2f'),
            sep='')

    print("Lets fly over!Buckle up!")


def ticket_main():
    print("Bellow are the airport locations with flights our to Peru.")
    print("1. Fort Myer's")
    print("2. Tampa")
    print("3. Miami")
    print("4. Orlando")
    start_location = int(input("Enter in the number of the airport you are "
                               "flying from:"))
    if start_location == 1:
        print("You are flying out of Fort Myer's.")
    elif start_location == 2:
        print("You are flying out of Tampa")
    elif start_location == 3:
        print("You are flying out of Miami.")
    elif start_location == 4:
        print("You are flying out of Orlando.")
    else:
        print("Invalid Input. Please enter a number 1-4.")

    calculate_ticket(start_location)


def peru_regions():
    for regions in range(1, 26):
        print("Please select which region you would like to visit.")
        print("1. Amazonas")
        print("2. Ancash")
        print("3. Apurimac")
        print("4. Arequipa")
        print("5. Ayacucho")
        print("6. Cajamarca")
        print("7. Callao")
        print("8. Cusco")
        print("9. Huancavelica")
        print("10. Huanuco")
        print("11. Ica")
        print("12. Janin")
        print("13. La Libertad")
        print("14. Cambayeque")
        print("15. Lima")
        print("16. Coneto")
        print("17. Madre de Dios")
        print("18. Pasco")
        print("19. Piura")
        print("20. Puno")
        print("21. San Martin")
        print("22. Tacna")
        print("23. Tumbles")
        print("24. Ucayali")
        print("25. Go back to Main Menu")
        print(
            "Please enter the number of the region you would like to travel "
            "to "
            "first:")

        user_choice = int(input())
        if user_choice == 1:
            print(
                "Great Selection! Las Amazonas, or the Amazon, is a great "
                "place to travel to. ")
            # Give a brief history about this region, average size and
            # population, known for Prompt to chose from more options,
            # Amazon tabe might be a bit different because there are not
            # really any in-habitats. Think more wild life and environment
            # Fun fact about Native people that are protected from modern
            # technology
        elif user_choice == 2:
            print(
                "Great Selection! Ancash is one of the best places to start "
                "our "
                "Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 3:
            print(
                "Great Selection! Apurimac is one of the best places to "
                "start our "
                "Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 4:
            print(
                "Great Selection! Arequipa is one of the best places to "
                "start our "
                "Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 5:
            print(
                "Great Selection! Ayacucho is one of the best places to "
                "start our "
                "Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 6:
            print(
                "Great Selection! Cajamarca is one of the best places to "
                "start our "
                "Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 7:
            print(
                "Great Selection! Callao is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 8:
            print(
                "Great Selection! Cusco is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 9:
            print(
                "Great Selection! Huancavelica is one of the best places to "
                "start our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 10:
            print(
                "Great Selection! Huanuco is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 11:
            print(
                "Great Selection! Ica is one of the best places to start our "
                "Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 12:
            print(
                "Great Selection! Junin is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 13:
            print(
                "Great Selection! La Libertad is one of the best places to "
                "start our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 14:
            print(
                "Great Selection! Lambayeque is one of the best places to "
                "start our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 15:
            print(
                "Great Selection! Lima is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 16:
            print(
                "Great Selection! Loneto is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 17:
            print(
                "Great Selection! Madre de Dios is one of the best places to "
                "start our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 18:
            print(
                "Great Selection! Pasco is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 19:
            print(
                "Great Selection! Piura is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 20:
            print(
                "Great Selection! Puno is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 21:
            print(
                "Great Selection! San Martin is one of the best places to "
                "start our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 22:
            print(
                "Great Selection! Tacna is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 23:
            print(
                "Great Selection! Tumbles is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 24:
            print(
                "Great Selection! Ucayali is one of the best places to start "
                "our Journey through Peru")
            # Give a brief history about this region, average size and
            # population, what it is known for best Prompt another menu of
            # choices: History, People, Food, Attractions, Geography,
            # What It's Like Today, and Fun-Facts
        elif user_choice == 25:
            main_menu()
        else:
            print("Invalid input. Please chose from options 1-24:")
            int(input("Enter region number:"))

main_menu()
