import PySimpleGUI as sg
import os.path
import random
from PySimpleGUI import Text
from tkinter import Tk, font
import gamesList

#('LightBrown13')
sg.theme('TealMono')


#-------------------------------
#Creating the class and array for all of the games
class game:
  def __init__(self, name, age, category):
    self.name = name
    self.age = age
    self.category = category
games = []
usedGames = []
exportedGames = []
longString = "test - \n\n"

#-------------------------------
games.append( game("4 Corners",  "Tenderfeet",  "High Energy"))
games.append( game("Obstacle Courses",  "Tenderfeet",  "High Energy"))
games.append( game("Line Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Ball Play",  "Tenderfeet",  "High Energy"))
games.append( game("Cat and mouse tag",  "Tenderfeet",  "High Energy"))
games.append( game("Shark Attack",  "Tenderfeet",  "High Energy"))
games.append( game("Screamer",  "Tenderfeet",  "High Energy"))
games.append( game("Red Light Green Light",  "Tenderfeet",  "High Energy"))
games.append( game("Camoflauge",  "Tenderfeet",  "High Energy"))
games.append( game("Octopus Tag",  "Tenderfeet",  "High Energy"))
games.append( game("British Bulldog",  "Tenderfeet",  "High Energy"))
games.append( game("Bandaid Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Flamingo Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Blob Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Statues",  "Tenderfeet",  "Low Energy"))
games.append( game("Alphabet Game",  "Tenderfeet",  "Low Energy"))
games.append( game("Superpowers",  "Tenderfeet",  "Low Energy"))
games.append( game("Action Dance",  "Tenderfeet",  "High Energy"))
games.append( game("Build a Pizza",  "Tenderfeet",  "High Energy"))
games.append( game("Wax Museum",  "Tenderfeet",  "Low Energy"))
games.append( game("Animal Kingdom",  "Tenderfeet",  "High Energy"))
games.append( game("Duck Duck Goose",  "Tenderfeet",  "High Energy"))
games.append( game("10 Questions",  "Tenderfeet",  "Icebreakers"))
games.append( game("Category is...",  "Tenderfeet",  "Icebreakers"))
games.append( game("Body Bingo",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Animal Relay",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Simon Says",  "Tenderfeet",  "Low Energy"))
games.append( game("Graveyard",  "Tenderfeet",  "Low Energy"))
games.append( game("Doggy Doggy",  "Tenderfeet",  "Low Energy"))
games.append( game("Stories",  "Tenderfeet",  "Low Energy"))
games.append( game("Musical Chairs",  "Tenderfeet",  "High Energy"))
games.append( game("Name Slap",  "Tenderfeet",  "Icebreakers"))
games.append( game("Rhythm Master",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Boardgames",  "Tenderfeet",  "Low Energy"))
games.append( game("Line Choice Game",  "Tenderfeet",  "Icebreakers"))
games.append( game("Ispy",  "Tenderfeet",  "Low Energy"))
games.append( game("Bubble Painting",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Human Knot",  "Tenderfeet",  "Icebreakers"))
games.append( game("Ninja",  "Tenderfeet",  "Low Energy"))
games.append( game("Rock Paper Scissors ev.",  "Tenderfeet",  "Low Energy"))
games.append( game("Splat",  "Tenderfeet",  "Low Energy"))
games.append( game("Catch it Drop it",  "Tenderfeet",  "Low Energy"))
games.append( game("One Minute Challenge",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Freeze Dance",  "Tenderfeet",  "High Energy"))
games.append( game("Mr. Wolf",  "Tenderfeet",  "High Energy"))
games.append( game("Fairy Gardens",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Micro Villages",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Blindfold Relay Race",  "Tenderfeet",  "Low Energy"))
games.append( game("Fruit Salad",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Giant Tic Tac Toe",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Elephant Soccer",  "Tenderfeet",  "Low Energy"))
games.append( game("Giants Wizards Elves",  "Tenderfeet",  "Low Energy"))
games.append( game("Chalk",  "Tenderfeet",  "Low Energy"))
games.append( game("This or That",  "Tenderfeet",  "High Energy"))
games.append( game("Volcanos",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Paper Bags",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Rain Cloud",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Firework Painting",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Pop Rocket",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Kite",  "Tenderfeet",  "Creative Explorations"))
games.append( game("Parachute (Small)",  "Tenderfeet",  "High Energy"))
games.append( game("Animal Charades",  "Tenderfeet",  "Low Energy"))
games.append( game("Freeze Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Colour Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Animal Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Zombie Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Captains Coming",  "Tenderfeet",  "High Energy"))
games.append( game("Black Magic",  "Tenderfeet",  "Cool Down"))
games.append( game("Four Corners",  "Tenderfeet",  "All-Purpose Games"))
games.append( game("Indy 500",  "Tenderfeet",  "High Energy"))
games.append( game("Mingle Mingle",  "Tenderfeet",  "Icebreakers"))
games.append( game("Sardines",  "Tenderfeet",  "High Energy"))
games.append( game("Toilet Tag",  "Tenderfeet",  "High Energy"))
games.append( game("Name and Motion",  "Discoverers",  "Icebreakers"))
games.append( game("Camping Trip",  "Discoverers",  "Icebreakers"))
games.append( game("One Word Story",  "Discoverers",  "Icebreakers"))
games.append( game("Identity Circle",  "Discoverers",  "Icebreakers"))
games.append( game("Dragon Lair",  "Discoverers",  "Low Energy"))
games.append( game("10's",  "Discoverers",  "Low Energy"))
games.append( game("Splat",  "Discoverers",  "Low Energy"))
games.append( game("Masterchef Junior",  "Discoverers",  "Low Energy"))
games.append( game("Frogger",  "Discoverers",  "Cool Down"))
games.append( game("7 Up",  "Discoverers",  "Cool Down"))
games.append( game("Cool Wind Blows",  "Discoverers",  "Cool Down"))
games.append( game("Airplanes",  "Discoverers",  "Creative Explorations"))
games.append( game("Rock Pets",  "Discoverers",  "Creative Explorations"))
games.append( game("Wands",  "Discoverers",  "Creative Explorations"))
games.append( game("Coffee Filter Butterfly",  "Discoverers",  "Creative Explorations"))
games.append( game("Chalk",  "Discoverers",  "Creative Explorations"))
games.append( game("ABC Yoga",  "Discoverers",  "Cool Down"))
games.append( game("Hit Record",  "Discoverers",  "All-Purpose Games"))
games.append( game("Fruit Salad",  "Discoverers",  "High Energy"))
games.append( game("Obstacle Course",  "Discoverers",  "High Energy"))
games.append( game("Mother May I",  "Discoverers",  "High Energy"))
games.append( game("Rock Paper Scissors Ev.",  "Discoverers",  "All-Purpose Games"))
games.append( game("Tic-Tac-Throw",  "Discoverers",  "High Energy"))
games.append( game("Musical Chairs",  "Discoverers",  "High Energy"))
games.append( game("Dot Race",  "Discoverers",  "High Energy"))
games.append( game("Musical Chairs",  "Discoverers",  "High Energy"))
games.append( game("Scavenger Hunt",  "Discoverers",  "High Energy"))
games.append( game("Noodle Tag",  "Discoverers",  "High Energy"))
games.append( game("Talent Show",  "Discoverers",  "Creative Explorations"))
games.append( game("I can Wheel",  "Discoverers",  "Creative Explorations"))
games.append( game("Happiness Poster",  "Discoverers",  "Cool Down"))
games.append( game("Gratitude Dice Game",  "Discoverers",  "Cool Down"))
games.append( game("Favourite Things - 5 Senses",  "Discoverers",  "Cool Down"))
games.append( game("Get to Know a Stick",  "Discoverers",  "Cool Down"))
games.append( game("Parachute",  "Discoverers",  "High Energy"))
games.append( game("Bandaid Tag",  "Discoverers",  "High Energy"))
games.append( game("Hot Dog Tag",  "Discoverers",  "High Energy"))
games.append( game("Link Tag",  "Discoverers",  "High Energy"))
games.append( game("Octopus Tag",  "Discoverers",  "High Energy"))
games.append( game("Freeze Tag",  "Discoverers",  "High Energy"))
games.append( game("Colour Tag",  "Discoverers",  "High Energy"))
games.append( game("Animal Tag",  "Discoverers",  "High Energy"))
games.append( game("Zombie Tag",  "Discoverers",  "High Energy"))
games.append( game("Blob Tag",  "Discoverers",  "High Energy"))
games.append( game("Captains Coming",  "Discoverers",  "High Energy"))
games.append( game("Flamingo Tag",  "Discoverers",  "High Energy"))
games.append( game("Shrinking Island ",  "Discoverers",  "High Energy"))
games.append( game("Graveyard",  "Discoverers",  "Cool Down"))
games.append( game("Black Magic",  "Discoverers",  "Cool Down"))
games.append( game("Going on a Trip",  "Discoverers",  "Cool Down"))
games.append( game("Screamer",  "Discoverers",  "High Energy"))
games.append( game("British Bulldog",  "Discoverers",  "High Energy"))
games.append( game("Catch it/ Drop it",  "Discoverers",  "Low Energy"))
games.append( game("Stella Ella Ola",  "Discoverers",  "Low Energy"))
games.append( game("Rhythm Master",  "Discoverers",  "All-Purpose Games"))
games.append( game("Indy 500",  "Discoverers",  "High Energy"))
games.append( game("Mingle Mingle",  "Discoverers",  "Icebreakers"))
games.append( game("Shadow Tag",  "Discoverers",  "High Energy"))
games.append( game("Freeze Dance",  "Discoverers",  "High Energy"))
games.append( game("Four Corners",  "Discoverers",  "All-Purpose Games"))
games.append( game("Giants Wizards Elves",  "Discoverers",  "All-Purpose Games"))
games.append( game("Toilet Tag",  "Discoverers",  "High Energy"))
games.append( game("Name slap",  "Discoverers",  "Icebreakers"))
games.append( game("Ground is Lava",  "Discoverers",  "All-Purpose Games"))
games.append( game("Rock, Paper, Sicssers, Split",  "Explorers",  "All-Purpose Games"))
games.append( game("Name Blanket Drop",  "Explorers",  "Icebreakers"))
games.append( game("This or That",  "Explorers",  "All-Purpose Games"))
games.append( game("Boat/Outdoor Structure Building",  "Explorers",  "Creative Explorations"))
games.append( game("Telephone Charades",  "Explorers",  "Low Energy"))
games.append( game("Bunny-Bunny",  "Explorers",  "Low Energy"))
games.append( game("River Maker/Rythm Master",  "Explorers",  "Low Energy"))
games.append( game("In the Ponds, Out of the Ponds",  "Explorers",  "Low Energy"))
games.append( game("Ninja Sticks",  "Explorers",  "All-Purpose Games"))
games.append( game("Peter Paul",  "Explorers",  "Low Energy"))
games.append( game("Secret Society",  "Explorers",  "Low Energy"))
games.append( game("Create Your own Country",  "Explorers",  "Creative Explorations"))
games.append( game("I-Spy Bottle",  "Explorers",  "Creative Explorations"))
games.append( game("Optical Illusions",  "Explorers",  "Creative Explorations"))
games.append( game("Salt Paintings",  "Explorers",  "Creative Explorations"))
games.append( game("Land Art",  "Explorers",  "Creative Explorations"))
games.append( game("Sun, Moon, Earth",  "Explorers",  "High Energy"))
games.append( game("Speedway",  "Explorers",  "High Energy"))
games.append( game("Relay Race",  "Explorers",  "High Energy"))
games.append( game("Cardio Charades",  "Explorers",  "High Energy"))
games.append( game("Create your own Hopscotch",  "Explorers",  "High Energy"))
games.append( game("Switch, Change, Rotate",  "Explorers",  "All-Purpose Games"))
games.append( game("Sticks",  "Explorers",  "High Energy"))
games.append( game("Giants, Wizards, Elves",  "Explorers",  "High Energy"))
games.append( game("Captians Coming",  "Explorers",  "High Energy"))
games.append( game("Lion's Den",  "Explorers",  "All-Purpose Games"))
games.append( game("Electric Fence/Invisable Maze",  "Explorers",  "Low Energy"))
games.append( game("Insightful Questions Hike",  "Explorers",  "Icebreakers"))
games.append( game("Kick the Cans",  "Explorers",  "High Energy"))
games.append( game("Revenge Tag",  "Explorers",  "High Energy"))
games.append( game("Huckle Buckle",  "Explorers",  "High Energy"))
games.append( game("Rock, Stick & Grow",  "Explorers",  "Cool Down"))
games.append( game("Graditude Cards",  "Explorers",  "Cool Down"))
games.append( game("Postitive Affirmation Poster ",  "Explorers",  "Cool Down"))
games.append( game("4 x Directions",  "Explorers",  "Cool Down"))
games.append( game("Colour, Symbol, Image",  "Explorers",  "Cool Down"))
games.append( game("Parachute",  "Explorers",  "High Energy"))
games.append( game("Splat",  "Explorers",  "Low Energy"))
games.append( game("Bandaid Tag",  "Explorers",  "High Energy"))
games.append( game("Hot Dog Tag",  "Explorers",  "High Energy"))
games.append( game("Link Tag",  "Explorers",  "High Energy"))
games.append( game("Octopus Tag",  "Explorers",  "High Energy"))
games.append( game("Freeze Tag",  "Explorers",  "High Energy"))
games.append( game("Colour Tag",  "Explorers",  "High Energy"))
games.append( game("Animal Tag",  "Explorers",  "High Energy"))
games.append( game("Zombie Tag",  "Explorers",  "High Energy"))
games.append( game("Blob Tag",  "Explorers",  "High Energy"))
games.append( game("Flamingo Tag",  "Explorers",  "High Energy"))
games.append( game("Graveyard",  "Explorers",  "Cool Down"))
games.append( game("Going on a Trip",  "Explorers",  "Cool Down"))
games.append( game("British Bulldog",  "Explorers",  "High Energy"))
games.append( game("Catch it/ Drop it",  "Explorers",  "Low Energy"))
games.append( game("Elephant Soccer",  "Explorers",  "Low Energy"))
games.append( game("Human Knot",  "Explorers",  "Cool Down"))
games.append( game("Change Places",  "Explorers",  "Low Energy"))
games.append( game("Telephone",  "Explorers",  "Cool Down"))
games.append( game("2 truths and a lie",  "Explorers",  "Icebreaker"))
games.append( game("Honey if you love me",  "Explorers",  "Low Energy"))
games.append( game("Rhythm Master",  "Explorers",  "All-Purpose Games"))
games.append( game("Mingle Mingle",  "Explorers",  "Icebreakers"))
games.append( game("Flinch",  "Explorers",  "Low Energy"))
games.append( game("Werewolf (Mafia)",  "Explorers",  "Low Energy"))
games.append( game("Toilet Tag",  "Explorers",  "High Energy"))
games.append( game("Name slap",  "Explorers",  "Icebreakers"))
games.append( game("Do As I Say, Not As I Do",  "Adventurers",  "Low Energy"))
games.append( game("Never Have I Ever",  "Adventurers",  "Icebreakers"))
games.append( game("Smiles Laughing Game",  "Adventurers",  "Low Energy"))
games.append( game("Contact",  "Adventurers",  "Icebreakers"))
games.append( game("Around the World",  "Adventurers",  "All-Purpose"))
games.append( game("3 - 6 - 9 Clap Game",  "Adventurers",  "Low Energy"))
games.append( game("007 Bang ",  "Adventurers",  "All-Purpose"))
games.append( game("Psychiatrist",  "Adventurers",  "Low Energy"))
games.append( game("Jump-In Jump-Out",  "Adventurers",  "Low Energy"))
games.append( game("Mafia/Werewolf",  "Adventurers",  "Low Energy"))
games.append( game("Honey if you like me",  "Adventurers",  "Icebreakers"))
games.append( game("Around the World",  "Adventurers",  "Icebreakers"))
games.append( game("Do As I Say, Not As I Do",  "Adventurers",  "Icebreakers"))
games.append( game("Steal the Bacon",  "Adventurers",  "High Energy"))
games.append( game("Revenge Tag",  "Adventurers",  "High Energy"))
games.append( game("Capture the Flag",  "Adventurers",  "High Energy"))
games.append( game("Fly Back",  "Adventurers",  "High Energy"))
games.append( game("Keep the Balloon/Ball up",  "Adventurers",  "High Energy"))
games.append( game("Tic-tac-toe Relay",  "Adventurers",  "High Energy"))
games.append( game("Builders and Buldozers/ Lake and Mountains",  "Adventurers",  "High Energy"))
games.append( game("Line Math",  "Adventurers",  "High Energy"))
games.append( game("Bust a Rhyme",  "Adventurers",  "High Energy"))
games.append( game("Fitness Bingo",  "Adventurers",  "High Energy"))
games.append( game("Trap Zone",  "Adventurers",  "High Energy"))
games.append( game("Shoe Connect 4",  "Adventurers",  "High Energy"))
games.append( game("Tape Painting",  "Adventurers",  "High Energy"))
games.append( game("Paper Pinwheel",  "Adventurers",  "High Energy"))
games.append( game("Pocket Fan",  "Adventurers",  "High Energy"))
games.append( game("Mini Catapults",  "Adventurers",  "High Energy"))
games.append( game("Mini Books",  "Adventurers",  "High Energy"))
games.append( game("Outdoor Survival Skills 101",  "Adventurers",  "High Energy"))
games.append( game("Making Sundials",  "Adventurers",  "High Energy"))
games.append( game("Compass Points",  "Adventurers",  "High Energy"))
games.append( game("Event Mapping",  "Adventurers",  "High Energy"))
games.append( game("Gratitude Journal",  "Adventurers",  "High Energy"))
games.append( game("See, Think, Wonder & Feel",  "Adventurers",  "High Energy"))
games.append( game("Sound Waves",  "Adventurers",  "High Energy"))
games.append( game("Outdoor Bingo",  "Adventurers",  "High Energy"))
games.append( game("Rock Paper Scissors Rumble",  "Adventurers",  "All-Purpose Games"))
games.append( game("Ninja",  "Adventurers",  "Low Energy"))
games.append( game("Graveyard",  "Adventurers",  "Cool Down"))
games.append( game("Dodgeball",  "Adventurers",  "High Energy"))
games.append( game("Flinch",  "Adventurers",  "Low Energy"))
games.append( game("Elephant Soccer",  "Adventurers",  "Low Energy"))
games.append( game("Human Knot",  "Adventurers",  "Icebreakers"))
games.append( game("Change Places",  "Adventurers",  "Low Energy"))
games.append( game("Telephone",  "Adventurers",  "Cool Down"))
games.append( game("2 truths and a lie",  "Adventurers",  "Icebreakers"))
games.append( game("Kickball",  "Adventurers",  "High Energy"))
games.append( game("Bocce Ball",  "Adventurers",  "High Energy"))
#-------------------------------
def makeExportWindow():
    exportLayout = [
    [sg.Multiline(key="planText", size=(50, 20))],
    [sg.Button('Back', size=(15,2)), sg.Push()]
    ]


    window2 = sg.Window('YMCA Games Generator - Export', exportLayout, element_padding=(1, 2), right_click_menu=sg.MENU_RIGHT_CLICK_EXIT,
                   keep_on_top=True,no_titlebar=True, grab_anywhere=True,margins=(5, 4), finalize=True)
    return window2

#-------------------------------
#Function based on room, choose game
def getGames(category,age):
        #if the age is correct
        applicable0 = [x for x in games if x.age == age]
        #Finding category
        if(category != 'Creative Explorations (craft)'):
            applicable1 = [x for x in applicable0 if x.category == category or x.category == "All-Purpose"]
        else:
            applicable1 = [x for x in applicable0 if x.category == category]
        
#------------
        rand1 = int(random.randint(0,len(applicable1)-1))
        rand2 = int(random.randint(0,len(applicable1)-1))
        rand3 = int(random.randint(0,len(applicable1)-1))
        if((len(applicable1)-1) >= 3):
            while(rand2 == rand1):
                rand2 = int(random.randint(0,len(applicable1)-1))
            while(rand3 == rand1 or rand3 == rand2):
                rand3 = int(random.randint(0,len(applicable1)-1))

        
        return applicable1[rand1].name + "\n" + applicable1[rand2].name + "\n" + applicable1[rand3].name



#-------------------------------


col1 = [
    [sg.Text('Age group:', size=(15,1)),sg.Combo(['Tenderfeet','Discoverers','Explorers','Adventurers','Challengers'])],
    [sg.Text('Block 1', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Text('Block 2', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Text('Block 3', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Text('Block 4', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Text('Block 5', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Text('Block 6', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Text('Block 7', size=(15,3)),sg.Combo(['Icebreakers', 'Creative Explorations','High Energy', 'Low Energy', 'Cool Down', 'Creative Explorations (Craft)'])],
    [sg.Push(), sg.Button('Submit', size=(15,2)), sg.Push()]
]

col2 = [
    # [sg.Button('', image_data=red_x_base64,
    #       button_color=(sg.theme_background_color(),sg.theme_background_color()),
    #       border_width=0, key='Exit')]
    [sg.Text('Game ideas:')],
    [sg.Text('Block 1', size=(15,1)),sg.Text(size=(25,3), key = 't1a'), sg.Button('Roll 1')],
    [sg.Text('Block 2', size=(15,1)),sg.Text(size=(25,3), key = 't2a'), sg.Button('Roll 2')],
    [sg.Text('Block 3', size=(15,1)),sg.Text(size=(25,3), key = 't3a'), sg.Button('Roll 3')],
    [sg.Text('Block 4', size=(15,1)),sg.Text(size=(25,3), key = 't4a'), sg.Button('Roll 4')],
    [sg.Text('Block 5', size=(15,1)),sg.Text(size=(25,3), key = 't5a'), sg.Button('Roll 5')],
    [sg.Text('Block 6', size=(15,1)),sg.Text(size=(25,3), key = 't6a'), sg.Button('Roll 6')],
    [sg.Text('Block 7', size=(15,1)),sg.Text(size=(25,3), key = 't7a'), sg.Button('Roll 7')],
    [sg.Push(), sg.Button('Generate again', size=(15,2)), sg.Button('Export', size=(15,2)), sg.Push()]
]


layout = [
    [sg.Push(), sg.Text("YMCA Daycamp Program Planning Helper", font='_ 24', justification='c', expand_x=True),sg.Push()],
    [sg.Push(), sg.Text("Use this tool to help you program plan. Copy and paste the results from this \n into your actual plan and make sure to make changes! \n (if you do not input a category, they will be chosen from all-purpose)", font='_ 14', justification='c', expand_x=True),sg.Push()],
    [sg.Column(col1),
    sg.VSeperator(),
    sg.Column(col2)]
    ]




#no_titlebar=True, grab_anywhere=True,margins=(3, 4),
window = sg.Window('YMCA Games Generator', layout, element_padding=(1, 2), right_click_menu=sg.MENU_RIGHT_CLICK_EXIT,
                   keep_on_top=True, finalize=True)



event, values = window.read()
 


while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Submit' or event == 'Generate again': 
        window['t1a'].update(getGames(values[1],values[0]))
        window['t2a'].update(getGames(values[2],values[0]))
        window['t3a'].update(getGames(values[3],values[0]))
        window['t4a'].update(getGames(values[4],values[0]))
        window['t5a'].update(getGames(values[5],values[0]))
        window['t6a'].update(getGames(values[6],values[0]))
        window['t7a'].update(getGames(values[7],values[0]))
    if event == 'Export':
        exportedGames.append(((window['t1a'].get())).split('\n'))
        exportedGames.append(((window['t2a'].get())).split('\n'))
        exportedGames.append(((window['t3a'].get())).split('\n'))
        exportedGames.append(((window['t4a'].get())).split('\n'))
        exportedGames.append(((window['t5a'].get())).split('\n'))
        exportedGames.append(((window['t6a'].get())).split('\n'))
        exportedGames.append(((window['t7a'].get())).split('\n'))
        window2 = makeExportWindow()
        for i in exportedGames:
            for x in range(3):
                window2['planText'].update(window2['planText'].get() +'\n'+ i[x] + '\n')
        event, values = window2.read()   # Read the event that happened and the values dictionary
        if event == sg.WIN_CLOSED or event == 'Back':     # If user closed window with X or if user clicked "Back" button then exit
            exportedGames.clear()
            window2['planText'].update(" ")
            window2.close()

    if event == ('Roll 1'):
        window['t1a'].update(getGames(values[1],values[0]))
    if event == ('Roll 2'):
        window['t2a'].update(getGames(values[2],values[0]))
    if event == ('Roll 3'):
        window['t3a'].update(getGames(values[3],values[0]))
    if event == ('Roll 4'):
        window['t4a'].update(getGames(values[4],values[0]))
    if event == ('Roll 5'):
        window['t5a'].update(getGames(values[5],values[0]))
    if event == ('Roll 6'):
        window['t6a'].update(getGames(values[6],values[0]))
    if event == ('Roll 7'):
        window['t7a'].update(getGames(values[7],values[0]))


window.close()
