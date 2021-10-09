import PySimpleGUI as sg

sg.theme("Dark Purple")

layout = [
    [sg.Text("text")],
    [sg.Text("Console:"), sg.InputText( key="Input"),],
    [sg.Button("Ok"), sg.Button("Cancel")]
]


window = sg.Window("titulo", layout)

event, values = window.read()
console = values["Input"]
status = event

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel" or event == "Ok":
        break
window.close()

if event == "Ok":
    print(console)
