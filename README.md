
### VROOOOMpad

VROOOOMpad is a 9-key macropad with a rotary encoder, an OLED Display. It also has 16 SK6812 LEDs, and uses KMK firmware.

It serves as a comprehensive example piece/reference for a feature-packed macropad, since it contains an implementation of every common part.

**Features:**

-   Designed for a custom 3D printed or laser-cut case.
    
-   128x32 OLED Display
    
-   EC11 Rotary encoder for whatever you want
    
-   16 SK6812 RGB LEDs for per-key lighting and effects.
    
-   9 Keys in a 3x3 matrix to save on controller pins.
    
-   KMK support! Edit your firmware with a simple text editor.
    

**CAD Model:**  
The PCB is designed to show off my first ever pcb build. This has been a long journey and I am quite proud of my pcb.

**PCB**  
Here's my PCB! It was made in KiCad.

**Schematic**  
![enter image description here](https://drive.google.com/file/d/18cYXN9dBHsvvs-i5QxGHF7S5kgjKLjsX/view?usp=sharing)
https://drive.google.com/file/d/18cYXN9dBHsvvs-i5QxGHF7S5kgjKLjsX/view?usp=sharing

**PCB Layout**  
![(Add your PCB layout image here)](https://drive.google.com/file/d/1or-7hfC62VdfGTGTljvyo4kLrXyLFp2b/view?usp=sharing)
https://drive.google.com/file/d/1or-7hfC62VdfGTGTljvyo4kLrXyLFp2b/view?usp=sharing

I used standard MX-style footprints for the keyswitches. A key design feature is the 3x3 key matrix using 1N4148 diodes, which allows 9 keys to be read using only 6 GPIO pins.

**Firmware Overview**  
This hackpad uses KMK firmware for everything.

-   The rotary encoder changes volume.
    
-   The 9 keys are set up with multiple layers for different shortcut menus and macros.
    
-   The OLED displays the currently active layer.
    

I might add more complex macros and lighting effects in the future! That's it for now.

**BOM:**  
Here should be everything you need to make this hackpad.

-   9x Cherry MX Switches (or clones)
    
-   9x Keycaps
        
-   9x 1N4148 DO-35 Diodes
    
-   16x SK6812 5050 LEDs
    
-   1x 0.91" 128x32 I2C OLED Display
    
-   1x EC11 Rotary Encoder
    
-   1x Seeed Studio XIAO RP2040
    
-   1x Case
    

**Extra stuff**  
Get through work as fast as 1..2..VROOOOOM. Just as fast as a Twin Turbo 1st Gen Audi R8 V10
Time to get off the starting line and tune your VROOOOMpad to redline your productivity.
