import customtkinter as ctk
import modules.main_screen as m_screen

sender_font = ctk.CTkFont(family= 'Calibri', size= 15, weight= 'bold')
sender_text_font = ctk.CTkFont(family= 'Calibri', size= 15, weight= 'normal')

class MessageFrame(ctk.CTkFrame):
    def __init__(self, name_song, minutes, width, height, master, border_width, fg_color, bg_color, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, fg_color= fg_color, bg_color= bg_color, **kwargs)
        
        # self.IMAGE_FRAME = self.create_image(image= m_img_frame.image_message)
        
        self.NAME_SONG = self.message_name_label(text= name_song, text_color= 'black', fg_color= 'transparent')
        self.MINUTES = self.message_text_label(text= minutes, text_color= 'black', fg_color= 'transparent')
        self.slider = ctk.CTkSlider(master=self, from_=0, to=200,number_of_steps = 100)
        self.slider.place(x = 237, y = 50, anchor = ctk.CENTER)
        #
        # self.IMAGE_FRAME.place(x=0, y=0)
        
        self.NAME_SONG.place(x= 40, y= 7)
        self.MINUTES.place(x= 430, y= 7)
        
    def message_name_label(self, text, text_color, fg_color):
        return ctk.CTkLabel(
            master= self,
            text= text,
            font= sender_font,
            text_color= text_color,
            fg_color= fg_color,
            bg_color= 'transparent',
            # image= m_img_frame.image_message
            )
    
    def message_text_label(self, text, text_color, fg_color):
       return ctk.CTkLabel(
           master= self,
           text= text,
           font= sender_text_font,
           text_color= text_color, 
           fg_color= fg_color,
           bg_color= 'transparent'
       )
           
song_line = MessageFrame(name_song='METAMORPHOSIS', width=466,height=42,master=m_screen.main_app.FRAME1,minutes='',border_width=0,fg_color='grey',bg_color='transparent')
song_line.place(x=250,y=60, anchor=ctk.CENTER)

listen_frame = MessageFrame(name_song='METAMORPHOSIS',width=475,height=85,master=m_screen.main_app.FRAME1,minutes='2:23',border_width=0,fg_color='grey',bg_color='transparent')
listen_frame.place(x = 253,y = 645, anchor = ctk.CENTER)