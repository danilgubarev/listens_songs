import customtkinter as ctk
import modules.main_screen as m_screen

class Create_Frame(ctk.CTkFrame):
    def __init__(self,master,width,height,corner_radius,border_width, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width)
        