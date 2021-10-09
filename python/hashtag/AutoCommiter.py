import pyautogui
import pyperclip

pyautogui.PAUSE = 1
#1 abrir o github

commitName = input("Whats the commit name?")

pyautogui.press("win")
pyautogui.write("GitHub Desktop")
pyautogui.press("enter")

#1.5 descrever comit

pyautogui.hotkey("win", "up")
pyautogui.click(x=134, y=908)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.write(commitName)


#2 Clicar em commit


pyautogui.click(x=158, y=1053)
pyautogui.hotkey("ctrl", "p")

#3 sair do github

pyautogui.hotkey("win", "down")
pyautogui.hotkey("alt", "tab")