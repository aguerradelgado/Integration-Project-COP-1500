# Alessandra Guerra Delgado
# Integration Project Interactive Map of Peru!
# Learn more than just the Geography! Culture, History, Cuisine, and Customs


def main_menu():
    """
This is the main function for the program. It takes the user on an 
educational journey through Peru. 
    """
    print("Welcome to the best Interactive Map of all Time!")
    print("Today, we will be traveling to the mystic country of Peru!")
    print("Peru is a beautiful country with a history rich in ancient "
          "civilization, amazing cuisine, and spectacular landscape")
    print("On this interactive map journey, you will learn all about the "
          "history, people, and customs of each region in Peru.")
    continue_program = True  # Boolean
    while continue_program:  # While Loop
        print("Main Menu: ")
        print("You may chose to go in order or jump around. Have fun!")
        print("1. Calculate Ticket Price")
        print("2. The Regions of Peru")
        print("3. Fun Facts! ")
        print("4. Write in Travel Journal")
        print("5. Built in Python Function Demo")
        print("6. Quit")
        user_choice = int(input("Enter number to make selection: "))
        if user_choice == 1:
            airport_selection()
        elif user_choice == 2:
            print("Welcome to Peru!")
            print("We are extremely excited to have you here")
            print("Peru is separated into 24 different regions."
                  "Similar to Provinces and "
                  "States.")
            peru_regions()
        elif user_choice == 3:
            print("Here you can find out the coolest facts about Peru.")
            ready_for_facts = input("Are you ready to get a super cool list "
                                    "of facts?: ")
            if ready_for_facts == "yes":
                fun_facts()
            elif ready_for_facts == "no":
                print("No, worries! Take your time in deciding, super cool "
                      "facts can be intimidating. You can always come back "
                      "to this option in the Main Menu.")
            else:
                print("Invalid input. Please type 'yes' or 'no'")

        elif user_choice == 4:
            travel_journal_log()

        elif user_choice == 5:
            built_in_function_demo()
        elif user_choice == 6:
            print("You are now leaving the Interactive Map.")
            continue_program = False

        else:
            print("Invalid selection. Enter numbers 1-4 to make selection.")


def calculate_ticket(start_location):
    """This program calculates how much your ticket will cost, when the
    start location is input
    :rtype: ticket price"""

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

    print("Let's fly over! Buckle up!")


def airport_selection():
    """
This program allows the user to select which location they wish to fly out
from. Calls to calculate_ticket function
    """
    print("Bellow are the airport locations with flights to Peru.")
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
    """
Allows user to select which region of Peru they would like to explore and
learn about
    """
    continue_regions = True  # Boolean Expression
    while continue_regions:  # All Information bellow is from Peru Wikipedia
        print("Please select which region you would like to visit.")
        print("1. Amazonas")
        print("2. Ancash")
        print("3. Apurimac")
        print("4. Arequipa")
        print("5. Ayacucho")
        print("6. Cajamarca")
        print("7. Moquegua")
        print("8. Cuzco")
        print("9. Huancavelica")
        print("10. Huanuco")
        print("11. Ica")
        print("12. Janin")
        print("13. La Libertad")
        print("14. Lambayeque")
        print("15. Lima")
        print("16. Loreto")
        print("17. Madre de Dios")
        print("18. Pasco")
        print("19. Piura")
        print("20. Puno")
        print("21. San Martin")
        print("22. Tacna")
        print("23. Tumbes")
        print("24. Ucayali")
        print("25. Go back to Main Menu")

        regions_choice = int(input("Please enter the number of the region "
                                   "you would like to travel to first: "))
        if regions_choice == 1:
            print(
                "Great Selection! Las Amazonas, or the Amazon, is a great "
                "place to learn about!. ")
            print("Las Amazonas is a region of northern Peru bordered by "
                  "Ecuador on the north and west, Carjamarca on the west, "
                  "La Libertad on the south, and Loreto and San Martín on "
                  "the east. Its capital is the city of Chachapoyas. With a "
                  "landscape of steep river gorges and mountains, Amazonas "
                  "is the location of Kuelap, a huge stone fortress "
                  "enclosing more than 400 stone structures; it was built on "
                  "a mountain about 3,000 meters high, starting about 500 AD "
                  "and was occupied to the mid-16th century. It is one of "
                  "Peru's major archeological sites.")
            # Amazon tab might be a bit different because there are not
            # really any in-habitats. Think more wild life and environment
        elif regions_choice == 2:
            print(
                "Great Selection! Ancash is a great place to learn about!")
            print("Ancash is a region of northern Peru. It is bordered by "
                  "the regions of La Libertad on the north, Huánuco and Pasco "
                  "on the east, Lima on the south, and the Pacific Ocean on "
                  "the west. Its capital is the city of Huaraz, and its "
                  "largest city and port is Chimbote. The name of the region "
                  "originates from the Quechua word anqash (light, of little "
                  "weight), from anqas (blue) or from anka (eagle)")
            # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 3:
            print(
                "Great Selection! Apurimac is a great place to learn about!")
            print("Aurimac is a region in southern-central Peru. It is "
                  "bordered on the east by the Cusco Region, on the west by "
                  "the Ayacucho Region, and on the south by the Arequipa and "
                  "Ayacucho regions. The region's name originates from the "
                  "Quechua language and means 'where the gods speak'' in "
                  "reference to the many mountains of the region (gods in "
                  "the andean religion) that seem to be talking to each "
                  "other.")
            # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 4:
            print(
                "Great Selection! Arequipa is a great place to learn about!")
            print("Arequipa is a region in southwestern Peru. It is bordered "
                  "by the departments of Ica, Ayacucho, Apurímac and Cusco "
                  "in the north, the Department of Puno in the east, "
                  "the Department of Moquegua in the south, and the Pacific "
                  "Ocean in the west. Its capital, also called Arequipa, "
                  "is Peru's second-largest city.")
            # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 5:
            print(
                "Great Selection! Ayacucho is a great place to learn about!")
            print("Ayacucho is a region of Peru, located in the "
                  "south-central Andes of the country. Its capital is the "
                  "city of Ayacucho. The region was one of the hardest hit "
                  "by terrorism in the 1980s during the guerrilla war waged "
                  "by Shining Path known as the internal conflict in Peru.")
            # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 6:
            print(
                "Great Selection! Cajamarca is a great place to learn about!")
            print("Cajamarca is a department in Peru. The capital is the "
                  "city of Cajamarca. It is located in the north part of the "
                  "country and shares a border with Ecuador. It is located "
                  "at heights reaching 2,700 metres (8,900 ft) above sea "
                  "level in the Andes Mountain Range, the longest mountain "
                  "range in the world. Part of its territory includes the "
                  "Amazon Rainforest, in total the largest in the world.")
            # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 7:
            print(
                "Great Selection! Moquegua is a great place to learn about!")
            print("Moquegua is a department in southern Peru that extends "
                  "from the coast to the highlands. Its capital is the city "
                  "of Moquegua, which is among the main Peruvian cities for "
                  "its high rates of GDP and national education.")
            # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 8:
            print(
                "Great Selection! Cuzco is a great place to learn about!")
            print("Cuzco is a department in Peru. It is bordered by the "
                  "departments of Ucayali on the north; Madre de Dios and "
                  "Puno on the east; Arequipa on the south; and Apurímac, "
                  "Ayacucho and Junín on the west. Its capital is Cusco, "
                  "the historical capital of the Inca Empire.")
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 9:
            print(
                "Great Selection! Huancavelica is a great place to learn "
                "about!")
            print("Huancavelica is a department in Peru with an area of 22,"
                  "131.47 km2 (8,545.01 sq mi) and a population of 347,"
                  "639 (2017 census). The capital is the city Huancavelica. "
                  "The region is bordered by the departments of Lima and Ica "
                  "in the west, Junín in the north, and Ayacucho in the "
                  "east.")
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 10:
            print(
                "Great Selection! Huanuco is a great place to learn about!")
            print("Huanuco is a department in central Peru.[1] It is "
                  "bordered by the La Libertad, San Martín, Loreto and "
                  "Ucayali regions in the north, the Ucayali Region in the "
                  "east, the Pasco Region in the south and the Lima and "
                  "Ancash regions in the west. Its capital is the city "
                  "Huánuco.")
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 11:
            print(
                "Great Selection! Ica is a great place to learn about!")
            print("Ica is a department in Peru. It borders the Pacific Ocean "
                  "on the west; the Lima Region on the north; the "
                  "Huancavelica and Ayacucho regions on the east; and the "
                  "Arequipa Region on the south. Its capital is the city of "
                  "Ica.")
        # Give a brief history about this region, average size and
        # population, what it is known for best Prompt another menu of
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 12:
            print(
                "Great Selection! Junin is a great place to learn about!")
            print("Junin is a region in the central highlands and "
                  "westernmost Peruvian Amazon. Its capital is Huancayo.")
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 13:
            print("Great Selection! La Libertad is a great place to learn "
                  "about!")
            print("La Libertad is a region in northwestern Peru. Formerly it "
                  "was known as the Department of La Libertad (Departamento "
                  "de La Libertad). It is bordered by the Lambayeque, "
                  "Cajamarca and Amazonas regions on the north, the San "
                  "Martín Region on the east, the Ancash and Huánuco regions "
                  "on the south and the Pacific Ocean on the west. Its "
                  "capital is Trujillo, which is the nation's third biggest "
                  "city. The region's main port is Salaverry, one of Peru's "
                  "largest ports. The name of the region is Spanish for "
                  "'freedom' or 'liberty'; it was named in honor of the "
                  "Intendencia of Trujillo's proclaiming independence from "
                  "Spain in 1820 and fighting for that.")
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 14:
            print(
                "Great Selection! Lambayeque is a great place to learn about!")
            print("Lambayeque is a department in northwestern Peru known for "
                  "its rich Moche and Chimú historical past. The region's "
                  "name originates from the ancient pre-Inca civilization of "
                  "the Lambayeque.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 15:
            print(
                "Great Selection! Lima is a great place to learn about!")
            print("Lima region contains the city of Lima, the country's "
                  "capital, is located west of the Department of Lima; this "
                  "province is autonomous and not under the jurisdiction of "
                  "the Regional Government.")
        # choices: History, People, Food, Attractions, Geography,
        elif regions_choice == 16:
            print(
                "Great Selection! Loreto is a great place to learn about!")
            print("Loreto is Peru's northernmost department. Covering almost "
                  "one-third of Peru's territory, Loreto is by far the "
                  "nation's largest department; it is also one of the most "
                  "sparsely populated regions due to its remote location in "
                  "the Amazon Rainforest. Its capital is Iquitos.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 17:
            print(
                "Great Selection! Madre de Dios is a great place to learn "
                "about!")
            print("Madre de Dios is a department in southeastern Peru, "
                  "bordering Brazil, Bolivia and the Peruvian departments of "
                  "Puno, Cusco and Ucayali, in the Amazon Basin. Its capital "
                  "is the city of Puerto Maldonado.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 18:
            print(
                "Great Selection! Pasco is a great place to learn about!")
            print("Pasco is a region in central Peru. Its capital is Cerro "
                  "de Pasco.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 19:
            print(
                "Great Selection! Piura is a great place to learn about!")
            print("Piura is a coastal region in northwestern Peru. The "
                  "region's capital is Piura and its largest port cities, "
                  "Paita and Talara, are also among the most important in "
                  "Peru. The area is known for its tropical and dry beaches.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 20:
            print(
                "Great Selection! Puno is a great place to learn about!")
            print("Puno is a department in southeastern Peru. It is bordered "
                  "by Bolivia on the east, the departments of Madre de Dios "
                  "on the north, Cusco and Arequipa on the west, Moquegua on "
                  "the southwest, and Tacna on the south. Its capital is the "
                  "city of Puno, which is located on Lake Titicaca in the "
                  "geographical region known as the Altiplano or high "
                  "sierra.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 21:
            print(
                "Great Selection! San Martin is a great place to learn about!")
            print("San Martin is a department in northern Peru. Most of the "
                  "department is located in the upper part of the Peruvian "
                  "Amazon rainforest. Its capital is Moyobamba and the "
                  "largest city in the department is Tarapoto.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 22:
            print(
                "Great Selection! Tacna is a great place to learn about!")
            print("Tacna is a city in the southernmost department in Peru. "
                  "The Chilean Army occupied the present-day Tacna "
                  "Department during the War of the Pacific from 1885 to "
                  "1929 when it was reincorporated into Peruvian soil.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 23:
            print(
                "Great Selection! Tumbes is a great place to learn about!")
            print("Tumbes is a coastal region in northwestern Peru and "
                  "southwestern Ecuador. Due to the region's location near "
                  "the Equator it has a warm climate, with beaches that are "
                  "considered among the finest in Peru.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 24:
            print(
                "Great Selection! Ucayali is a great place to learn about!")
            print("Ucayali is an inland department of Peru. Located in the "
                  "Amazon rainforest, its name is derived from the Ucayali "
                  "River. Its capital is the city of Pucallpa.")
        # choices: History, People, Food, Attractions, Geography
        elif regions_choice == 25:
            continue_regions = False
        else:
            print("Invalid input. Please chose from options 1-24:")


def fun_facts():
    """
This function prints and numbers the first fifteen lines from the file
peru_fact_list.txt
    """
    print("Here are some of the top 15 facts about Peru: ")
    fact_list = open('peru_fact_list.txt')  # All facts are from my personal
    # knowledge, I am peruvian, or from Peru wikipedia page
    for index in range(1, 16):
        facts = fact_list.readline()
        print(str(index) + ". ", facts.strip())
    fact_list.close()


def travel_journal_log():
    """
    This function lets user save a journal entry to a file

    """
    print("Here is where you can write about what you loved in each region. ")
    date_visited = input("Enter date: ")
    region_traveled = input("Enter the region you are writing about: ")
    journal_entry = input("Write about your experience in that region:  ")

    in_file = open("peru_travel_journal.txt", 'a')
    # The 'a' open the file for appending, creating one if it does not exist
    # The 'w' open the file for writing, creates if does not exist
    in_file.write("\nDate: " + date_visited)
    in_file.write("\nRegion: " + region_traveled)
    in_file.write("\nExperience: " + journal_entry)
    in_file.close()
    print("Done! Entry is saved in file: peru_travel_journal.txt")


def built_in_function_demo():
    continue_demo = True
    print("This is the demonstrative section of the Integration "
          "Project\n" "This is going to teach you how to apply and use "
          "Predefined and Built-in Functions within Python.")
    print("In python, there are predefined segments of code that already "
          "have certain functions")
    while continue_demo:
        print("Today we will be using the predefined functions:")
        print("1. abs()")
        print("2. pow()")
        print("3. round()")
        print("4. import")
        print("5. Close ")
        function_selection = int(input("Enter the number of the function you "
                                       "would "
                                       "like to learn about first: "))
        if function_selection == 1:
            print("You selected abs().")
            print("This function finds the absolute value of two numbers.")
            print("For example, if we execute the following program: ")
            print("print(abs(-4.67))")
            print("Your output would be: ", abs(-4.67))  # absolute value

        elif function_selection == 2:
            print("You selected pow().")
            print("This function works in the same way as '**' in Python.")
            print("If you were to execute the following program: ")
            print("print(pow(5, 3))")
            print("Your output would be:", pow(5, 3), "Which is 5 to the 3rd "
                                                      "power")
        elif function_selection == 3:
            print("You selected round().")
            print("This function will round a number up to the nearest whole "
                  "number.")
            print("If you were to execute the following program: ")
            print("print(round(6.9))")
            print("Your output would be: ", round(6.9))
            learn_more = input("Would you like to learn more about how to "
                               "round a number up or down in Python? ")
            if learn_more == "yes":
                import math
                print("There are a few ways to round a value up or down in "
                      "python")
                print("If you import math, which we learned about in the "
                      "'import' section, you can use math.ceil() and "
                      "math.floor() to round up or down")
                print("Assign values to a few variables: \n", "x = 4.7\n",
                      "y = 5.3\n", "z = -4.8")
                print("To round up, enter the variables as arguments to "
                      "math.ceil()")
                print("To round down, enter the variables as arguments to "
                      "math.floor()")
                print("If we use x: ")
                print("print(math.ceil(x))")
                print("print(math.floor(x))")
                x = 4.7
                print("Output would be:", math.ceil(x), "Which is rounded "
                                                        "up.")
                print("Output would be:", math.floor(x), "Which is rounded "
                                                         "down.")
            elif learn_more == "no":
                print("Cool man!")
            else:
                print("Invalid. Please enter: 'yes' or 'no' ")

        elif function_selection == 4:
            print("You selected to import random.")
            print("Now this option is different than the others.")
            print("In Python there are some predefined modules, as well as "
                  "functions.")
            print(
                "So to search and bind a module, we need to use 'import'. \n",
                "It does both.")
            print("If you were to execute the following program: ")
            print("import random\n", "print(random.randint(1, 100))")
            print(
                "The 'import random' would let us be able to get a random set "
                "of numbers to use in the print statement. ")
            import random  # gets a random number
            print("Which would make the output: ", random.randint(1, 100),
                  "Which is a random number between 1 and 100")

        elif function_selection == 5:
            continue_demo = False
        else:
            print("Invalid input. Chose a number 1-4")


main_menu()
