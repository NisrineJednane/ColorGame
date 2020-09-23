# import modules

# list of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0

# time left
time_left = 30


# func start game
def startGame(event):
    if time_left == 30:
        countdown()

    nextColor()


# display next color function
def nextColor():
    global score
    global time_left
# if game currently on, make entry box active
    if time_left > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0, tkinter.END)

        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]))

        scoreLabel.config(text="Score: "+ str(score))


# countdown function
def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1

        timeLabel.config(text="Time Left: "+str(time_left))

        timeLabel.after(1000, countdown)


root = tkinter.Tk()
root.title('ColorGame')
root.geometry("375x200")

instructions = tkinter.Label(root, text='Type the colors of the words and not the word text', font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text='Press Enter to start', font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text='Time left: '+ str(time_left), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()