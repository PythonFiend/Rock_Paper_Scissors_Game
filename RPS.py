import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence, ImageGrab
from random import randint

#***************** IMAGE LINKS *****************
gif_rock = 'rock.gif'
gif_paper = 'paper.gif'
gif_scissors = 'scissors.gif'
gif_letsplay = 'letsplay.gif'
#***********************************************

#*************** OPENING SCREEN ***************
overture = [[sg.Image(key='-IMAGE-')],
            [sg.Button("GO")]]
overture_window = sg.Window("Let's PLay!", overture, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

letsplay_sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gif_letsplay))] 
interframe_duration = Image.open(gif_letsplay).info['duration']

while True:
    for frame in letsplay_sequence:
        event, values = overture_window.read(timeout=interframe_duration)
        overture_window['-IMAGE-'].update(data=frame)
        if event == sg.WIN_CLOSED:
            exit()
# ***************** END OF OPENING SCREEN ***************

# ***************** START MAIN SCREEN GUI ***********************        
        elif event == "GO":

            sg.theme('Reddit')
            col1 = [[sg.Text("Choose Your Weapons!", pad=(50,0), justification='c',font=("Arial", 16,"bold"))],
                    [sg.Button("ROCK", size=(9,1), pad=(100,20), font=("Arial", 18, "bold"))],
                    [sg.Button("PAPER", size=(9,1), pad=(100,20), font=("Arial", 18, "bold"))],
                    [sg.Button("SCISSORS", size=(9,1), pad=(100,20), font=("Arial", 18, "bold"))]]
                
            layout = [[sg.Text("Rock Paper Scissors Game", pad=(50,10), justification='c',  size=(72,1), font=("Arial", 18,"bold"))],
                    [sg.Column(col1), sg.VerticalSeparator(), sg.Image(key='-PLAYER_IMAGE-'), sg.Image(key='-COMPUTER_IMAGE-')],
                    [sg.Text("SCORE", font=("Arial", 14,"bold"), pad=(140,0))],
                    [sg.Text("Player", size=(5,1), pad=(40,0), font=("Arial", 14,"bold")), sg.Text("0", key='P_SCORE', font="Arial 14"), sg.Text("Computer", size=(8,1), pad=(20,0), font=("Arial", 14,"bold")), sg.Text("0", key='CP_SCORE', font="Arial 14"), sg.Text("PLAYER", text_color='white', background_color="#0079d3", pad=(200,0), font=("Arial", 14,"bold")), sg.Text("COMPUTER", text_color='white', pad=(30,0), background_color="#0079d3", font=("Arial", 14,"bold"))],
                    [sg.Text(size=(145,1), pad=(0,10))]]        
            window = sg.Window("Rock Paper Scissors Game", layout, finalize=True) 

            #ROCK
            rock_sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gif_rock))] 
            interframe_duration = Image.open(gif_rock).info['duration']
            #PAPER
            paper_sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gif_paper))] 
            interframe_duration = Image.open(gif_paper).info['duration']
            #SCISSORS
            scissors_sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gif_scissors))] 
            interframe_duration = Image.open(gif_scissors).info['duration']
    # ******************** END MAIN SCREEN GUI ****************

            # ****** variables used in score count ********
            i = 1
            player_score = 0
            computer_score = 0

            #************** START CODE *****************
            while True:
                i += 1
                event, values = window.read()
                if event == "Exit" or event == sg.WIN_CLOSED:
                    exit()

                if event == "ROCK":
                    for frame in rock_sequence:
                        event, values = window.read(timeout=interframe_duration)
                        window['-PLAYER_IMAGE-'].update(data=frame)
                                
                    choices = ['[0] = rock','[1]= paper','[2] = scissors']
                    for x in choices:
                        c = [0,1,2]
                        machine = c[randint(0,2)]
                    #print(machine)

                    if machine == 0:
                        for frame in rock_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)

                    if machine == 1:
                        computer_score += 1
                        for frame in paper_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)
                            if computer_score > player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='green')
                                window['P_SCORE'].update(value=(player_score), text_color='red')
                            elif computer_score < player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='red')
                                window['P_SCORE'].update(value=(player_score), text_color='green')
                            elif computer_score == player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='black')
                                window['P_SCORE'].update(value=(player_score), text_color='black')

                            
                    if machine == 2:
                        player_score += 1
                        for frame in scissors_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)
                            if player_score > computer_score:
                                window['P_SCORE'].update(value=(player_score), text_color='green')
                                window['CP_SCORE'].update(value=(computer_score), text_color='red')
                            elif player_score < computer_score:
                                window['P_SCORE'].update(value=(player_score), text_color='red')
                                window['CP_SCORE'].update(value=(computer_score), text_color='green')
                            elif computer_score == player_score:
                                window['P_SCORE'].update(value=(player_score), text_color='black')
                                window['CP_SCORE'].update(value=(computer_score), text_color='black')
                

                if event == "PAPER":

                    for frame in paper_sequence:
                        event, values = window.read(timeout=interframe_duration)
                        window['-PLAYER_IMAGE-'].update(data=frame)
                                
                    choices = ['[0] = rock','[1]= paper','[2] = scissors']
                    for x in choices:
                        c = [0,1,2]
                        machine = c[randint(0,2)]
                    print(machine)

                    if machine == 0:
                        player_score += 1
                        for frame in rock_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)
                            if player_score > computer_score:
                                window['P_SCORE'].update(value=(player_score), text_color='green')
                                window['CP_SCORE'].update(value=(computer_score), text_color='red')
                            elif player_score < computer_score:
                                window['P_SCORE'].update(value=(player_score), text_color='red')
                                window['CP_SCORE'].update(value=(computer_score), text_color='green')
                            elif computer_score == player_score:
                                window['P_SCORE'].update(value=(player_score), text_color='black')
                                window['CP_SCORE'].update(value=(computer_score), text_color='black')

                    if machine == 1:
                        for frame in paper_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)

                    if machine == 2:
                        computer_score += 1
                        for frame in scissors_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)
                            if computer_score > player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='green')
                                window['P_SCORE'].update(value=(player_score), text_color='red')
                            elif computer_score < player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='red')
                                window['P_SCORE'].update(value=(player_score), text_color='green')
                            elif computer_score == player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='black')
                                window['P_SCORE'].update(value=(player_score), text_color='black')
                        

                if event == "SCISSORS":

                    for frame in scissors_sequence:
                        event, values = window.read(timeout=interframe_duration)
                        window['-PLAYER_IMAGE-'].update(data=frame)
                                
                    choices = ['[0] = rock','[1]= paper','[2] = scissors']
                    for x in choices:
                        c = [0,1,2]
                        machine = c[randint(0,2)]
                    print(machine)

                    if machine == 0:
                        computer_score += 1
                        for frame in rock_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)
                            if computer_score > player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='green')
                                window['P_SCORE'].update(value=(player_score), text_color='red')
                            elif computer_score < player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='red')
                                window['P_SCORE'].update(value=(player_score), text_color='green')
                            elif computer_score == player_score:
                                window['CP_SCORE'].update(value=(computer_score), text_color='black')
                                window['P_SCORE'].update(value=(player_score), text_color='black')

                    if machine == 1:
                        player_score += 1
                        for frame in paper_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)
                            if player_score > computer_score:
                                window['P_SCORE'].update(value=(player_score), text_color='green')
                                window['CP_SCORE'].update(value=(computer_score), text_color='red')
                            elif player_score < computer_score:
                                window['P_SCORE'].update(value=(player_score), text_color='red')
                                window['CP_SCORE'].update(value=(computer_score), text_color='green')
                            elif computer_score == player_score:
                                window['P_SCORE'].update(value=(player_score), text_color='black')
                                window['CP_SCORE'].update(value=(computer_score), text_color='black')

                    if machine == 2:
                        for frame in scissors_sequence:
                            event, values = window.read(timeout=interframe_duration)
                            window['-COMPUTER_IMAGE-'].update(data=frame)


                    # **************** END CODE *******************
            window.close()
overture_window.close()