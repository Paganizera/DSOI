from .display_abstract import DisplayAbstract
from errors.custom_errors import InvalidOptionError, ClosedProgramWindowError
from history.image_message import ImageMessage
from history.video_message import VideoMessage
from history.text_message import TextMessage
import PySimpleGUI as sg
from . import data

class ChatMessagesDisplay(DisplayAbstract):
    def __main__(self) -> None:
        super().__init__()


    #   Shows available options
    def init_components(self, messages: []) -> None:
        lst = sg.Listbox(messages, size=(20, 4), font=('Arial Bold', 14), auto_size_text=True, enable_events=True, expand_x=True, select_mode=sg.LISTBOX_SELECT_MODE_BROWSE ,key='-LIST-')
        layout = [
            [sg.Text("Chat Screen", size=(50, 1), justification="center", font=data.FONT_TITLE, relief=sg.RELIEF_RIDGE)],
            [lst],
            [sg.Radio("Send Message", "RADIO1", default=True, size=(12, 1), font=data.FONT, key="-TXTMSG-")],
            [sg.Radio("Send Image", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-IMGMSG-")],
            [sg.Radio("Send Video", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-VDOMSG-")],
            [sg.Radio("Remove User", "RADIO1", default=True, size=(11, 1), font=data.FONT, key="-RMUSER-")],
            [sg.Radio("Exit Chat", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-EXIT-")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)


    def show_options(self, messages: []) -> str:
        self.init_components(messages)
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                if values["-TXTMSG-"]:
                    retval = 'textmessage'
                elif values["-IMGMSG-"]:
                    retval = 'imagemessage'
                elif values["-VDOMSG-"]:
                    retval = 'videomessage'
                elif values["-RMUSER-"]:
                    retval = 'removeuser'
                elif values["-EXIT-"]:
                    retval = 'exit'
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

    #   Get the text content to send
    def get_input_text(self) -> str:
        message = sg.popup_get_text('Enter the message', title="Message Input")        
        message = message.strip()
        self.__window.close()
        return message

    # Get the media's name that the user wants to send
    def get_inputfile_name(self) -> str:
        layout = [
            [sg.Text('Enter a filename:')],
            [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse(file_types=(
                ("PNG Files", "*.png"),("JPG Files", "*.jpg"), ("GIF Files", "*.gif")
                ))],
            [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]
            ]
        self.__window = sg.Window("Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        event, values = self.__window.read()
        while True:
            event, values = self.__window.read()
            if event == "Save":
                retval = str(values["-IN-"])
                break
            elif event == "Exit Without Saving":
                retval = None
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        return retval
    