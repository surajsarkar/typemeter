import math
from tkinter import *
import tkinter.font

DEMO_STORY = 'Nash grows older and approaches his old\nfriend and intellectual rival Martin\nHansen, now head of the Princeton\nmathematics department, who grants him\npermission to work out of the library\nand audit classes, though the university\nwill not provide him with his own\n'


class Ui( Tk ):
    def __init__(self, teacher) :
        super().__init__()
        # evaluator instence
        self.teacher = teacher
        # window configs(first)
        self.minsize( 1080, 450 )
        self.title( "Typemeter" )
        self.config( padx=10, pady=10 )

        # components variables
        self.current_user = 'anonymous'
        self.f_s_button: Button
        self.f_s_entry: Entry
        self.f_s_yur_name_label: Label
        self.timer = None
        self.count_down_label: Label
        self.text_box: Text
        self.text_showcase_canvas: Canvas
        self.text_showcase_label: Label

        # extra configuration
        self.button_font_config = tkinter.font.Font( size=24, weight='bold' )

        # screen components rendering func
        self.start_screen_components()

    def start_screen_components(self) :
        self.config( bg='#9d84b7' )
        # button_img = PhotoImage(file="needed_images/button.png")
        self.f_s_button = Button( self, width=15, command=self.on_f_s_click, text='Start Test', cursor='hand2', bd=0,
                                  bg='#091353', fg='#B2F9FC', padx=10, font=self.button_font_config )
        self.f_s_button.grid( column=1, row=3, columnspan=2 )

        self.f_s_entry = Entry( self, bg='#D5D5D5', width=20, bd=1, justify='center', textvariable=self.current_user,
                                font=self.button_font_config, )
        self.f_s_entry.grid( column=1, row=1, columnspan=2 )

        self.f_s_yur_name_label = Label( self, text='Your name', font=self.button_font_config, justify='center',
                                         anchor='center', bg='#9D84B7' )
        self.f_s_yur_name_label.grid( column=1, row=0, columnspan=2 )

    def on_f_s_click(self) :
        if self.f_s_entry.get() != '':
            self.current_user = self.f_s_entry.get()
        self.f_s_entry.destroy()
        self.f_s_yur_name_label.destroy()
        self.f_s_button.destroy()

        self.second_screen_components(DEMO_STORY)

    def second_screen_components(self, fetched_text) :
        self.config( bg='#091353' )

        # font
        text_showcase_font = tkinter.font.Font( size=18, weight='bold' )

        # canvas for showing some text
        self.text_showcase_canvas = Canvas( self, width=800, height=250 )
        self.text_showcase_canvas.pack()

        # label containg text inside canvas
        self.text_showcase_label = Label( self.text_showcase_canvas, width=40, pady=10, padx=10, font=text_showcase_font, text=fetched_text )
        self.text_showcase_label.pack()

        # count down label
        print( 'label' )
        self.count_down_label = Label( self, text=3, font=text_showcase_font, bg='#091353', fg='#FFFFFF' )
        self.count_down_label.pack()

        # typing box
        print( 'text box' )
        self.text_box = Text( self, width=70, height=5, padx=20, pady=20, state='disabled' )
        self.text_box.pack()

        self.count_down( time_interval=3, after_timer_function=self.after_time_over )

    def after_time_over(self):
        self.text_box.config( state='normal')
        self.text_box.focus_set()
        self.count_down( time_interval=30, after_timer_function=self.evaluate )

    def count_down(self, time_interval, after_timer_function):
        if time_interval != 0:
            self.count_down_label.config(text=f'{time_interval}')
            self.timer = self.after( 1000, self.count_down, time_interval-1, after_timer_function )
        else:
            self.count_down_label.config(text='0')
            self.after_cancel(self.timer)
            after_timer_function()

    def evaluate(self):
        user_typed = self.text_box.get( 1.0, 'end-1c' )

        # destroying second screen
        self.text_box.config(state='disabled')
        self.text_box.destroy()
        self.text_showcase_canvas.destroy()
        self.count_down_label.destroy()

        # call third screen
        correct, wrong, wpm = self.teacher(DEMO_STORY, user_typed)
        self.third_screen( number_of_correct=correct, mistaken_letter=wrong, speed=wpm )

    def third_screen(self, number_of_correct, mistaken_letter,  speed):
        self.config(bg='#E5E5E5')

        comment = f'''
        {self.current_user}
        
        Your score is
        {math.ceil(speed)}
        wpm
        
        You should pay attention to {mistaken_letter} letters.
        Keep practicing ☺☺
        '''

        score_board_font = tkinter.font.Font(size='30', weight='bold')
        # score_board_bg = PhotoImage(file='needed_images/Rectangle 5scoreboard.png')
        score_board = Canvas(self, width=400, height=200, bg='#091353', )
        score_board.pack()

        result_label = Label(score_board, font=score_board_font, fg='#9D84B7', text=comment)
        result_label.pack()
