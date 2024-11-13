import PySimpleGUI as sg

sg.theme('Green')

def main(player1_name="Player 1", player2_name="Player 2"):
    round_counter = 1

    layout = [
        [sg.Text("Tournament Scoring System")],
        [sg.Text(player1_name, key="player1_name")],
        [sg.Input(key="player1"), sg.Text("Score", key="score1")],
        [sg.Text(player2_name, key="player2_name")],
        [sg.Input(key="player2"), sg.Text("Score", key="score2")],
        [sg.Text("Round Counter", key="round_counter_label"),
         sg.Input(round_counter, key="round_counter", size=(2, 1), readonly=True),
         sg.Button("Next Round")],
        [sg.Button("Calculate Scores"), sg.Button("Reset"), sg.Button("Exit")],
        [sg.Text("Total Scores", font=("Calibri", 15))],
        [sg.Text(player1_name, key="player1_name")],
        [sg.Text("", key="total_score1", font=("Calibri", 12))],
        [sg.Text(player2_name, key="player2_name")],
        [sg.Text("", key="total_score2", font=("Calibri", 12))]
    ]

    window = sg.Window("Tournament Scoring System", layout)

    while True:
        event, values = window.read()

        if event == "Next Round":
            try:
                score1 = int(values["player1"])
                score2 = int(values["player2"])

                window["score1"].update(score1)
                window["score2"].update(score2)

                total_score1 = int(window["total_score1"].get()) + score1 if window["total_score1"].get() else score1
                total_score2 = int(window["total_score2"].get()) + score2 if window["total_score2"].get() else score2

                window["total_score1"].update(total_score1)
                window["total_score2"].update(total_score2)

                round_counter += 1
                if round_counter > 5:
                    if total_score1 > total_score2:
                        sg.popup("Round Limit Reached", "Winner: " + player1_name, "Loser: " + player2_name)
                    elif total_score1 < total_score2:
                        sg.popup("Round Limit Reached", "Winner: " + player2_name, "Loser: " + player1_name)
                    else:
                        sg.popup("Round Limit Reached", "It's a tie!", player1_name + ": " + str(total_score1), player2_name + ": " + str(total_score2))
                    round_counter = 1
                    window["player1"].update("")
                    window["player2"].update("")
                    window["score1"].update("Score")
                    window["score2"].update("Score")
                    window["total_score1"].update("")
                    window["total_score2"].update("")
                window["round_counter"].update(round_counter)

            except ValueError:
                sg.popup("Please enter valid numbers for the scores.")

        elif event == "Calculate Scores":
            try:
                score1 = int(values["player1"])
                score2 = int(values["player2"])

                window["score1"].update(score1)
                window["score2"].update(score2)

                total_score1 = int(window["total_score1"].get()) + score1 if window["total_score1"].get() else score1
                total_score2 = int(window["total_score2"].get()) + score2 if window["total_score2"].get() else score2

                window["total_score1"].update(total_score1)
                window["total_score2"].update(total_score2)

            except ValueError:
                sg.popup("Please enter valid numbers for the scores.")

        elif event == "Reset":
            window["player1"].update("")
            window["player2"].update("")
            window["score1"].update("Score")
            window["score2"].update("Score")
            window["total_score1"].update("")
            window["total_score2"].update("")
            round_counter = 1
            window["round_counter"].update(round_counter)

        elif event == "Exit":
            break

        elif event == sg.WIN_CLOSED:
            break

    window.close()

def enter_names():
    layout = [
        [sg.Text("Enter Player Names")],
        [sg.Text("Player 1"), sg.Input(key="player1_name")],
        [sg.Text("Player 2"), sg.Input(key="player2_name")],
        [sg.Button("Submit"), sg.Button("Cancel")]
    ]

    window = sg.Window("Enter Player Names", layout)

    while True:
        event, values = window.read()

        if event == "Submit":

            player1_name = values["player1_name"]
            player2_name = values["player2_name"]

            if player1_name and player2_name:
                window.close()
                main(player1_name, player2_name)
                break
            else:
                sg.popup("Please enter both player names.")

        elif event == "Cancel":
            break

        elif event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    enter_names()