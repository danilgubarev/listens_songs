import customtkinter as ctk
import modules.create_frame as m_frame

app_width = 507
app_height = 698


class Create_App(ctk.CTk):
    def __init__(self, app_width, app_height, **kwargs):
        super().__init__(**kwargs)
        self.WIDTH = app_width
        self.HEIGHT = app_height
        # self.SCREEN_WIDTH = self.winfo_screenwidth
        # self.SCREEN_HEIGHT = self.winfo_screenheight
        self.geometry("507x698")
        self.resizable(False,False)
        self.FRAME1 = m_frame.Create_Frame(master = self, width=507,height=698,corner_radius=3,border_width=5)
        self.FRAME1.place(x = 0,y = 0)

        
main_app = Create_App(app_width,app_height)