from .display_abstract import DisplayAbstract
from errors.custom_errors import CloseChatError
import PySimpleGUI as sg
from . import data
from PIL import Image


class ChatMessagesDisplay(DisplayAbstract):
    def __main__(self) -> None:
        super().__init__()

    #   Shows available options
    def init_components(self, messages: []) -> None:
        lst = sg.Listbox(
            messages,
            size=(20, 4),
            font=("Arial Bold", 14),
            auto_size_text=True,
            enable_events=True,
            expand_x=True,
            expand_y=True,
            select_mode=sg.LISTBOX_SELECT_MODE_BROWSE,
            key="-LIST-",
        )
        layout = [
            [
                sg.Text(
                    "Chat Screen",
                    size=(50, 1),
                    justification="center",
                    font=data.FONT_TITLE,
                    relief=sg.RELIEF_RIDGE,
                    auto_size_text=True,
                )
            ],
            [lst],
            [
                sg.Radio(
                    "Send Message",
                    "RADIO1",
                    default=True,
                    size=(12, 1),
                    font=data.FONT,
                    key="-TXTMSG-",
                )
            ],
            [
                sg.Radio(
                    "Send Image",
                    "RADIO1",
                    default=True,
                    size=(10, 1),
                    font=data.FONT,
                    key="-IMGMSG-",
                )
            ],
            [
                sg.Radio(
                    "Remove User",
                    "RADIO1",
                    default=True,
                    size=(11, 1),
                    font=data.FONT,
                    key="-RMUSER-",
                )
            ],
            [
                sg.Button("Select", size=(10, 1), font=data.FONT),
                sg.Button("View", size=(10, 1), font=data.FONT),
                sg.Button("Close", size=(10, 1), font=data.FONT),
            ],
        ]
        self.__window = sg.Window(
            "Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True
        )

    def show_options(self, messages: list[str], paths: list[str]) -> str:
        self.init_components(messages)
        while True:
            event, values = self.__window.read()
            if event == "Select":
                if values["-TXTMSG-"]:
                    retval = "textmessage"
                elif values["-IMGMSG-"]:
                    retval = "imagemessage"
                elif values["-RMUSER-"]:
                    retval = "removeuser"
                else:
                    continue
                break
            elif event == "Select":
                retval = "openmessage"
            elif event == "View":
                if values["-LIST-"] == []:
                    super().show_message("No message was selected")
                    continue
                msg = values["-LIST-"][-1]
                image = msg.split(" ")
                for path in paths:
                    filename = path.split("/")
                    if image[-1] == filename[-1]:
                        Image.open(path).show()
                        break
                else:
                    super().show_message(values["-LIST-"])
            elif event == "Close":
                retval = "close"
                break
            elif event == sg.WIN_CLOSED:
                raise CloseChatError()
        self.__window.close()
        # self.close()  # isn't working
        return retval

    #   Get the text content to send
    def get_input_text(self) -> str:
        message = sg.popup_get_text(
            "Enter the message", title="Message Input", font=data.FONT
        )
        message = message.strip()
        self.__window.close()
        return message

    # Get the media's name that the user wants to send
    def get_input_image(self) -> str | None:
        layout = [
            [sg.Text("Enter a filename:")],
            [sg.Input(sg.user_settings_get_entry("-filename-", ""), key="-IN-")],
            [
                sg.FileBrowse(file_types=(("PNG Files", "*.png"),)),
                sg.B("Save"),
                sg.B("Exit Without Saving", key="Exit"),
            ],
        ]
        self.__window = sg.Window(
            "Users Menu",
            layout,
            size=(data.HEIGHT, data.WIDTH),
            font=data.FONT,
            finalize=True,
        )
        event, values = self.__window.read()
        while True:
            event, values = self.__window.read()
            if event == "Save":
                retval = str(values["-IN-"])
                break
            elif event == "Exit":
                retval = None
                break
            elif event == sg.WIN_CLOSED:
                raise CloseChatError()
        self.__window.close()
        return retval
