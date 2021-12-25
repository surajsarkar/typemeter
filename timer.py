#just for experiment

from tkinter import *

window = Tk()
timer = None



def countdown(stamp:int, message:str):
    global timer
    if stamp != 0:
        print(f'I got executed {stamp} {message}' )
        timer = window.after( 1000, countdown, stamp-1, 'passed' )
    else:
        print('destroying timer')
        window.after_cancel(timer)



countdown(10, 'passed')



window.mainloop()

