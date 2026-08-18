# SpotiPi
 
Displays currently playing Spotify album art on an RGB LED matrix panel, powered by a Raspberry Pi.
 
## How it works
 
- A Python process polls the Spotify API for the currently playing track
- A C++ component (using `rpi-rgb-led-matrix` and GraphicsMagick) renders the album art to the LED matrix
  
## Gallery
 
| | |
|---|---|
| ![Photo 1](SpotiPi/SpotiPi2.png) | ![Photo 2](Spotipi.jpg) |
 
