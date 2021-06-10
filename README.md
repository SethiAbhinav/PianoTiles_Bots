# PianoTiles_Bots (Image Recognition)
>Bots that work on different variants of the famous game "Piano Tiles". A bot that plays the game.

Firstly, find the location of the target. In my case, it was a black pixel. Open command prompt or terminal, and go ahead and type:

```python
>>>import pyautogui
>>>pyautogui.displayMousePosition()
```
Now go to the website of the game you want to play. Then find the X,Y coordinates and RGB value using the above lines of code. Hover over the black tile to find the rgb value of the black colour used by the game.
![image](https://user-images.githubusercontent.com/84278440/121556559-9c55a980-ca31-11eb-866f-2a5936d29f49.png)

*Note: Your X,Y coordinates may be different from mine.*

**Procedure:**

Take a note of the X, Y coordinates of a pixel from each of the 4 sections where the tiles appear in the game.( 4 sections indicated in the image at the bottom of the readme ) 

This was the basic procedure before getting into the code for both piano tiles games.

**The code simplified:**
1. Found the X,Y coordinates for 4 pixel locations (one for each section where the tiles can appear). 
2. Check if the pixel's rgb value is `(0,0,0)` (corresponding to black in my case).
3. If it is black, then click on the screen using `win32api` and `win32con`  .(First `LBUTTONDOWN`, then a delay of `0.01 seconds` and finally `LBUTTONUP`)
4. Else do nothing.
5. Press 'q' to stop program execution.


**Note:**
You have to ensure your IDE does not cover the game screen when you execute the code.
![image](https://user-images.githubusercontent.com/84278440/121559450-30c10b80-ca34-11eb-9ae4-b70d4a6e2ee5.png)

As can be seen my IDE is outside the game screen(yellow border).
