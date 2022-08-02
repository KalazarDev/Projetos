from tkinter import Button
from pytube import YouTube 
from http.client import IncompleteRead
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.cols = 2  
        self.add_widget(Label(text="Link: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name) 
        



class main(App):
    def build(self):
        return MyGrid()


main().run()

if __name__ == "__main__":
            
    SAVE_PATH = "C:/TEMP" 
    lista = list()
    link="https://www.youtube.com/watch?v=4yWw1D71Ry4"
    yt = YouTube(link)
    qualidade = yt.fmt_streams
    try: 

        yt = YouTube(link)
        
    except Exception as error: 
        print("Erro: ", error) 

    mp4files = yt.streams.filter(file_extension='mp4',progressive=True)
    file = yt.streams.get_by_itag(22)
    # 18 360 / 22 720p / 243 / 137 / 135 /'content-length' 160

    for c in range(1):
        
        try: 
            print('Efetuando o Download aguarde!')
            file.download(SAVE_PATH,max_retries=3) 
            
            
        except IncompleteRead:
            continue
            
        except Exception as Error: 
            print("Erro ao fazer Download", Error) 
            
        print('Concluido') 