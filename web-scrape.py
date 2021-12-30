import pyautogui
import os
import time


def find_and_click(url):
    done = 0
    r = None
    while done < 5 or r is None:
        r = pyautogui.locateCenterOnScreen(url, confidence=.9)
        done += 1
    select_x, select_y = r
    pyautogui.click(select_x, select_y)

def main():
    os.chdir('Factiva Search Results')
    [os.remove(os.path.join(os.curdir, f)) for f in os.listdir()]
    os.chdir('../Images')

    count = 0
    has_next = True
    while has_next:
        count += 1
        try:
            select_x, select_y = pyautogui.locateCenterOnScreen('selectall.png')
        except TypeError:
            select_x, select_y = pyautogui.locateCenterOnScreen('selectallprev.png')
        pyautogui.click(select_x, select_y)

        savedata_x, savedata_y = pyautogui.locateCenterOnScreen('savedataas.png')
        pyautogui.click(savedata_x, savedata_y)
        time.sleep(1)
        pyautogui.click(savedata_x, savedata_y + 50)
        time.sleep(4)
        pyautogui.rightClick()
        find_and_click('saveas.png')
        time.sleep(.5)
        find_and_click('factiva.png')
        pyautogui.write(str(count))
        pyautogui.press('enter')
        time.sleep(.1)
        find_and_click('exit.png')
        done = 0
        r = None
        while done < 5 or r is None:
            try:
                r = pyautogui.locateCenterOnScreen('selectallselected.png', confidence=.9)
            except TypeError:
                r = pyautogui.locateCenterOnScreen('selectallprevselected.png',confidence=.9)
            done += 1
        select_x, select_y = r
        pyautogui.click(select_x, select_y)

        find_and_click('next100.png')
        time.sleep(20)


if __name__ =='__main__':
    main()