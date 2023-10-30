import pyautogui
import time
import keyboard


def cautare_google():
    if pyautogui.locateOnScreen(r"c:\Python_ex\search_bar.png", confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r"c:\Python_ex\search_bar.png", confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(2)
        pyautogui.write("zona it youtube")
        pyautogui.press("enter")
        time.sleep(3)


def gasire_canal():
    pyautogui.click(288, 484)
    time.sleep(4)


def subscribe_canal():
    pyautogui.click(700, 531)


response = pyautogui.confirm("Doriti sa incepeti rularea programului?", "Confirmare")
if (response == "OK"):
    cautare_google()
    gasire_canal()
    subscribe_canal()
else:
    pyautogui.alert("Ati ales anulare", "Anulare")
