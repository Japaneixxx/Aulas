import pyautogui
import pyperclip

pyautogui.PAUSE = 1
#1 abrir o github

pyautogui.press("win")
pyautogui.write("Github Desktop")
pyautogui.press("enter")

#1.5 descrever comit

pyautogui.press("f11")
pyautogui.click(x=134, y=861)
pyautogui.hotkey("ctrl, a")
pyautogui.press("delete")
pyautogui.write("commit")


#2 Clicar em commit


pyautogui.click(x=116, y=1017)

#3 sair do github

pyautogui.press("f11")
pyautogui.hotkey("alt", "tab")