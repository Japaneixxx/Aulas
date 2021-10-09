import pyautogui
import pyperclip
import PySimpleGUI as sg

pyautogui.PAUSE = 1

sg.theme("Dark Purple")

layout = [
    [sg.Text("Escreva aqui seu commit:"), sg.InputText( key="Commit")],
    [sg.Button("Ok"), sg.Button("Cancel")]
]


window = sg.Window("titulo", layout)

event, values = window.read()
Commit = values["Commit"]
status = event

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel" or event == "Ok":
        break
window.close()

if event == "Ok":


#1 abrir o github

#commitName = input("Whats the commit name?")

    pyautogui.press("win")
    pyautogui.write("GitHub Desktop")
    pyautogui.press("enter")

    #1.5 descrever comit

    pyautogui.hotkey("win", "up")
    pyautogui.click(x=134, y=908)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")
    pyautogui.write(Commit)


    #2 Clicar em commit


    pyautogui.click(x=158, y=1053)
    pyautogui.hotkey("ctrl", "p")

    #3 sair do github

    pyautogui.hotkey("win", "down")
    pyautogui.hotkey("alt", "tab")