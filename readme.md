Just like my IBM glossary scraper, this one scrapes all glossary entries from `https://www.novell.com/documentation/glossary/?page=/documentation/glossary/glossenu/data/gl24.html`. However, since I couldn't work using lxml or beautifulsoup because of the way the page was designed, I had to use pyautogui to do "semiauto" work, making my computer automatically move the mouse, copy stuff and paste in a text editor. 

This means that the way it is now, it will only work on my computer, it was designed specifically for my screen resolution, my browser window position/size and the browser customizations I have that might change the width/height of the internal parts of the browser.

You can edit the code to fit your needs though.