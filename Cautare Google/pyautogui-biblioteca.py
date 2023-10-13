import pyautogui
import time
import keyboard
def cautare_google():
    if pyautogui.locateOnScreen(r"c:\Python_ex\search_bar.png", confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r"c:\Python_ex\search_bar.png", confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(3)
        pyautogui.write("zona it")
        pyautogui.press("enter")
        time.sleep(2)


response = pyautogui.confirm("Doriti sa incepeti rularea programului?", "Confirmare")
if (response == "OK"):
    cautare_google()
else:
    pyautogui.alert("Ati ales anulare", "Anulare")
