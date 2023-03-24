import customtkinter as ctk
import modules.main_screen as m_screen
import modules.create_text_frame as m_text_frame

class Create_Button(ctk.CTkButton):
    def __init__(self, master,width,height, corner_radius, border_width,fg_color,text, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width,text='', fg_color='black')

play = Create_Button(master=m_text_frame.song_line, width=20,height=20,corner_radius=20,border_width=0, fg_color='black',text='<')
play.place(x = 18, y = 20, anchor=ctk.CENTER)

play_or_stop = Create_Button(master= m_text_frame.listen_frame,width=20,height=20,corner_radius=20,border_width=0,fg_color='black',text='>')
play_or_stop.place(x = 237, y = 20, anchor = ctk.CENTER)

