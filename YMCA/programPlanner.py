import PySimpleGUI as sg
import os.path
import random
from PySimpleGUI import Text
from tkinter import Tk, font

# sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '# A8FFF4',
#                                         'TEXT': '# 000000',
#                                         'INPUT': '# e4ccff',
#                                         'TEXT_INPUT': '# 000000',
#                                         'SCROLL': '# 99CC99',
#                                         'BUTTON': ('# 5AB1FF', '# 5AB1FF'),
#                                         'PROGRESS': ('# 5AB1FF', '# 5AB1FF'),
#                                         'BORDER': 1, 'SLIDER_DEPTH': 0, 
# 'PROGRESS_DEPTH': 0, }
  
# # Switch to use your newly created theme
# sg.theme('MyCreatedTheme')


sg.theme('LightGreen4')


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
#ADD GAMES HERE
games.append( game( "Rock, Paper, Scissors, Split",  "Explorers",  "All-Purpose" ))
games.append( game( "Name Blanket Drop",  "Explorers",  "Icebreakers" ))
games.append( game( "This or That",  "Explorers",  "All-Purpose" ))
games.append( game( "Boat/Outdoor Structure Building",  "Explorers",  "Creative Explorations" ))
games.append( game( "Telephone Charades",  "Explorers",  "Low Energy" ))
games.append( game( "Bunny-Bunny",  "Explorers",  "Low Energy" ))
games.append( game( "River Maker/Rythm Master",  "Explorers",  "Low Energy" ))
games.append( game( "In the Ponds, Out of the Ponds",  "Explorers",  "Low Energy" ))
games.append( game( "Ninja Sticks",  "Explorers",  "All-Purpose" ))
games.append( game( "Peter Paul",  "Explorers",  "Low Energy" ))
games.append( game( "Secret Society",  "Explorers",  "Low Energy" ))
games.append( game( "Create Your own Country",  "Explorers",  "Creative Explorations" ))
games.append( game( "I-Spy Bottle",  "Explorers",  "Creative Explorations" ))
games.append( game( "Optical Illusions",  "Explorers",  "Creative Explorations" ))
games.append( game( "Salt Paintings",  "Explorers",  "Creative Explorations" ))
games.append( game( "Land Art",  "Explorers",  "Creative Explorations" ))
games.append( game( "Sun, Moon, Earth",  "Explorers",  "High Energy" ))
games.append( game( "Speedway",  "Explorers",  "High Energy" ))
games.append( game( "Relay Race",  "Explorers",  "High Energy" ))
games.append( game( "Cardio Charades",  "Explorers",  "High Energy" ))
games.append( game( "Create your own Hopscotch",  "Explorers",  "High Energy" ))
games.append( game( "Switch, Change, Rotate",  "Explorers",  "All-Purpose" ))
games.append( game( "Sticks",  "Explorers",  "High Energy" ))
games.append( game( "Giants, Wizards, Elves",  "Explorers",  "High Energy" ))
games.append( game( "Captians Coming",  "Explorers",  "High Energy" ))
games.append( game( "Lion's Den",  "Explorers",  "All-Purpose" ))
games.append( game( "Electric Fence/Invisable Maze",  "Explorers",  "Low Energy" ))
games.append( game( "Insightful Questions Hike",  "Explorers",  "Icebreakers" ))
games.append( game( "Kick the Cans",  "Explorers",  "High Energy" ))
games.append( game( "Revenge Tag",  "Explorers",  "High Energy" ))
games.append( game( "Huckle Buckle",  "Explorers",  "High Energy" ))
games.append( game( "Rock, Stick & Grow",  "Explorers",  "Cool Down" ))
games.append( game( "Graditude Cards",  "Explorers",  "Cool Down" ))
games.append( game( "Postitive Affirmation Poster ",  "Explorers",  "Cool Down" ))
games.append( game( "4 x Directions",  "Explorers",  "Cool Down" ))
games.append( game( "Colour, Symbol, Image",  "Explorers",  "Cool Down" ))



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
    [sg.Push(), sg.Button('Submit', size=(15,2)), sg.Button('Exit', size=(15,2)), sg.Push()]
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

exportLayout = [
    [sg.Multiline(key="planText", size=(50, 20))]
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
        print(exportedGames[0][0])
        print(exportedGames[0][1])
        window = sg.Window('YMCA Games Generator - Export', exportLayout, element_padding=(1, 2), right_click_menu=sg.MENU_RIGHT_CLICK_EXIT,
                   keep_on_top=True, finalize=True)
        for i in exportedGames:
            for x in range(3):
                window['planText'].update(window['planText'].get() +'\n'+ i[x] + '\n')
        #         longString = longString + '\n' + str(i[x]) + '\n'
        # print(longString)
        
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
