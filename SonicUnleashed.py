# Sonic Unleashed: Stage Objectives Program

class SonicUnleashedStageObjective:
    def __init__(self):
        self.countries = {
            "Apotos": "A lovely ocean backdrop marks this port town, the start of Sonic's adventure.\n",
            "Mazuri": "Exotic wild animals are a frequent sight near this village built on reddish-brown soil.\n",
            "Spagonia": "The world's art capital and home to a university that attracts those in search of knowledge.\n",
            "Holoska": "Covered in snow, this northern land is gripped by extreme cold and dotted with houses of ice.\n",
            "Chun-nan": "This small town in the mountains has passed down its meat bun recipe for generations.\n",
            "Empire City": "A melting pot of diverse folk and ideas. All who come here dream of making it big.\n",
            "Shamar": "A town of ruins and ancient customs, now celebrating the Feast of Sun and Moon.\n",
            "Adabat": "The village is an architectural marvel, built atop the water and ringed by ancient ruins.\n",
            "Eggmanland": "A maniacal metropolis of machinery built by Dr. Eggman and his mad ambitions.\n"
        }
        self.levels = {
            "Apotos": {
                "Windmill Isle Day": [
                    "Act 1: Head for the goal!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Head for the goal!",
                    "Time Trial Lv.3: Finish in 2:30!",
                    "Battle Trial Lv.3: Beat over 25 foes!",
                    "Ring Trial Lv.3: Grab 300 rings!",
                    "[DLC] Act 2-2: Head for the goal!",
                    "Act 3: Complete one full lap!",
                    "[DLC] Act 4: Head for the goal!"
                ],
                "Windmill Isle Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 10:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "The Elder's Doubt: Get the specs in 90 sec!",
                    "The Elder's Plans: Protect Gregorios!",
                    "The Elder's Book: Get the book!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "[DLC] Act 1-3: Head for the goal!",
                    "Act 2: Head for the goal!"
                ]
            },
            "Mazuri": {
                "Savannah Citadel Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 2:30!",
                    "Battle Trial Lv.3: Beat over 40 foes!",
                    "Ring Trial Lv.3: Grab 300 rings!",
                    "Before the Ritual: Find that plant!",
                    "Spooky Shadows: Beat the boss in 60 sec!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Get to the goal in time!",
                    "Act 3: Head for the goal!",
                    "[DLC] Act 3-2: Gather 300 rings in time!",
                    "[DLC] Act 4: Get to the goal in time!",
                    "[DLC] Act 5: Head for the goal!",
                    "Egg Beetle: Beat Eggman's Egg Beetle!"
                ],
                "Savannah Citadel Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 10:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "Run Yaya Run: Find Yaya in 120 sec!",
                    "Final Exam: Pass the chief's test!",
                    "Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!",
                    "[DLC] Act 4: Head for the goal!"
                ]
            },
            "Spagonia": {
                "Rooftop Run Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 4:30!",
                    "Battle Trial Lv.3: Beat over 80 foes!",
                    "Ring Trial Lv.3: Grab 800 rings!",
                    "Lunch Thief!: Find the thief!",
                    "A Miffed Mom: Gather 10 oranges!",
                    "Elio's Loss: Gather 100 rings!",
                    "Tower Terror: Tag the 2 ghosts!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Complete three full laps!",
                    "[DLC] Act 2-2: Head for the goal!",
                    "Act 3: Find the Chao!",
                    "[DLC] Act 4: Head for the goal!",
                    "[DLC] Act 5: Head for the goal!",
                    "Egg Devil Ray: Beat Eggman's Egg Devil Ray!",
                    "Tornado Defense: Act 1: Head for the goal!"
                ],
                "Rooftop Run Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 10:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "Elio's Nights: Find Elio!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "[DLC] Act 2: Head for the goal!"
                ]
            },
            "Holoska": {
                "Cool Edge Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 3:30!",
                    "Battle Trial Lv.3: Beat over 60 foes!",
                    "Ring Trial Lv.3: Grab 500 rings!",
                    "Love Is Jerky: Get the jerky in time!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Complete three full laps!",
                    "[DLC] Act 2-2: Complete three full laps!",
                    "[DLC] Act 3: Get to the goal in time!",
                    "[DLC] Act 4: Head for the goal!"
                ],
                "Cool Edge Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 10:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "A Promise Made: Protect Jari-Pekka!",
                    "[DLC] Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!",
                    "Dark Moray: Beat the Dark Moray!"
                ]
            },
            "Chun-nan": {
                "Dragon Road Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 4:00!",
                    "Battle Trial Lv.3: Beat over 30 foes!",
                    "Ring Trial Lv.3: Grab 500 rings!",
                    "Find A Cure: Gather the herbs!",
                    "Get Pumped: Don't get hit!",
                    "Kung Fu Flex: Beat the enemies!",
                    "Kung Fu Speed: Get to the goal in time!",
                    "Hide-and-Seek: Play hide-and-seek!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Complete three full laps!",
                    "[DLC] Act 2-2: Complete five full laps!",
                    "Act 3: Head for the goal!",
                    "[DLC] Act 4: Head for the goal!",
                    "[DLC] Act 5: Complete four full laps!"
                ],
                "Dragon Road Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 3:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "Checkup Time: Beat the enemies!",
                    "Chronic Ailment: Get the medicine!",
                    "Energy Boost: Get the snack in time!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!",
                    "Dark Gaia Phoenix: Beat the Dark Gaia Phoenix!"
                ]
            },
            "Empire City": {
                "Skyscraper Scamper Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 3:00!",
                    "Battle Trial Lv.3: Beat over 55 foes!",
                    "Ring Trial Lv.3: Grab 300 rings!",
                    "No Appointment: Meet with Def!",
                    "Passion Power: Beat the enemies!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!"
                ],
                "Skyscraper Scamper Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 10:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "A Rising Star: Find the producer!",
                    "Dead End: Deliver the demo tape!",
                    "Play It Cool: Get to the goal in time!",
                    "Sonic Presents: Deliver the gift in time!",
                    "[DLC] Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!"
                ]
            },
            "Shamar": {
                "Arid Sands Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 3:00!",
                    "Battle Trial Lv.3: Beat over 70 foes!",
                    "Ring Trial Lv.3: Grab 600 rings!",
                    "Committee Call: Break the crates!",
                    "Urgent Mission: Gather the oranges!",
                    "Missing Sister: Find Yasmine!",
                    "Shamaran Peace: Beat the enemies!",
                    "Ice Dream: Get the supplies!",
                    "[DLC] Act 1-2: Get to the goal in time!",
                    "Act 2: Head for the goal!",
                    "[DLC] Act 3: Find the Chao!"
                ],
                "Arid Sands Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 20:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "Missing Son: Find Labib's son!",
                    "[DLC] Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!",
                    "Dark Guardian: Beat the Dark Guardian!"
                ]
            },
            "Adabat": {
                "Jungle Joyride Day": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 6:00!",
                    "Battle Trial Lv.3: Beat over 70 foes!",
                    "Ring Trial Lv.3: Grab 400 rings!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Complete three full laps!",
                    "Act 3: Head for the goal!",
                    "[DLC] Act 4: Head for the goal!",
                    "[DLC] Act 5: Head for the goal!",
                    "Egg Lancer: Beat Eggman's Egg Lancer!"
                ],
                "Jungle Joyride Night": [
                    "Act 1: Head for the goal!",
                    "Time Trial Lv.3: Finish in 10:00!",
                    "Survival Lv.3: No healing! Guard well to stay alive!",
                    "Jungle Fright: Find the ghosts in time!",
                    "[DLC] Act 1-2: Head for the goal!",
                    "Act 2: Head for the goal!",
                    "[DLC] Act 3: Head for the goal!"
                ]
            },
            "Eggmanland": {
                "Eggmanland": [
                    "Eggmanland: Head for the goal!",
                    "Time Trial Lv.3: Finish in 45:00!",
                    "Egg Dragoon: Beat Eggman's Egg Dragoon!",
                    "Dark Gaia: Defeat Dark Gaia!",
                    "Tornado Defense: Act 2: Head for the goal!"
                ]
            }
        }

    def display_countries(self):
        print("\nChoose a country:")
        for idx, country in enumerate(self.countries.keys(), start=1):
            print(f"{idx}. {country}")
        print(f"{len(self.countries) + 1}. Quit")

    def display_levels(self, country):
        print(self.countries[country])
        print(f"Choose a day or night section:")
        for idx, level in enumerate(self.levels[country].keys(), start=1):
            print(f"{idx}. {level}")
        print(f"{len(self.levels[country]) + 1}. Go Back\n{len(self.levels[country]) + 2}. Quit")

    def display_objectives(self, country, level):
        print(self.countries[country])
        print(f"{level} Objectives:")
        for objective in self.levels[country][level]:
            print(objective)
        print(f"Total Stages: {len(self.levels[country][level])}\n")

        while True:
            print("Options:")
            print("1. Go Back")
            print("2. Quit")
            choice_option = input("Enter the number of the option you want to select: ")

            if choice_option.isdigit() and 1 <= int(choice_option) <= 2:
                if int(choice_option) == 1:
                    return  # Go back to level selection
                elif int(choice_option) == 2:
                    print("\nThe world adventure continues, Goodbye!\n")
                    exit()

            else:
                print("\nInvalid input. Please enter a valid number.\n")

    def run(self):
        print("\nWelcome to the Sonic Unleashed: Stage Objectives Program.")
        print("This program lets you select a fictional country from the 2008 video game, Sonic Unleashed, and see the objective for each day and night stage.")

        while True:
            self.display_countries()
            choice_country = input("\nEnter the number of the country you want to select: ")

            if choice_country.isdigit() and 1 <= int(choice_country) <= len(self.countries) + 1:
                if int(choice_country) == len(self.countries) + 1:
                    print("\nThe world adventure continues, Goodbye!\n")
                    break

                country_list = list(self.countries.keys())
                selected_country = country_list[int(choice_country) - 1]

                print(f"\nYou have selected {selected_country}.")
                self.display_levels(selected_country)

                while True:
                    choice_level = input("\nEnter the number you want to select: ")

                    if choice_level.isdigit() and 1 <= int(choice_level) <= len(self.levels[selected_country]) + 2:
                        if int(choice_level) == len(self.levels[selected_country]) + 1:
                            break  # Go back to country selection
                        elif int(choice_level) == len(self.levels[selected_country]) + 2:
                            print("\nThe world adventure continues, Goodbye!\n")
                            return

                        level_list = list(self.levels[selected_country].keys())
                        selected_level = level_list[int(choice_level) - 1]

                        self.display_objectives(selected_country, selected_level)

                    else:
                        print("\nInvalid input. Please enter a valid number.")


# Run the program
sonic_program = SonicUnleashedStageObjective()
sonic_program.run()