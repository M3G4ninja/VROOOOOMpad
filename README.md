The VROOOOMpad
The VROOOOMpad is a high-performance, 9-key macropad designed to be the control panel for your digital workflow. With a tactile rotary encoder, a dashboard-like OLED display, and fully addressable RGB "underglow," this pad is built to accelerate your most common tasks and shortcuts.
This project serves as a reference for building a feature-rich macropad, combining a key matrix, per-key RGB, an encoder, and a display, all powered by the supercharged XIAO RP2040 and the easy-to-modify KMK firmware.
Features:
Custom-Tuned with KMK Firmware! No complex build environment needed. Just pop the hood and edit code.py to remap your engine.
A crisp 128x32 OLED Display acts as your digital dashboard, showing vital stats like your current 'gear' (layer).
A tactile EC11 Rotary Encoder for precision control—perfect for scrubbing timelines or fine-tuning volume.
A full 4x4 grid of SK6812 'Underglow' LEDs, providing per-key lighting that acts as a tachometer for your tasks.
Nine fully programmable keys in a high-response 3x3 matrix—your launch buttons for any command.
Chassis (CAD Model):
The PCB is the engine block of the VROOOOMpad, designed to be mounted securely into a custom chassis. The mounting holes are placed for M3 bolts, making it perfect for a custom 3D-printed enclosure or a stacked acrylic frame with a 5-degree 'racing' tilt.
The Control Board (PCB)
Here's the PCB! It was engineered in KiCad to be compact and powerful. The design is centered around the XIAO RP2040 microcontroller.
Schematic
[Link to your Schematic Image Here]
PCB Layout
[Link to your PCB Layout Image Here]
The board uses standard MX-style footprints for a responsive, mechanical feel. To keep the design efficient, a 3x3 key matrix with 1N4148 diodes is used, allowing 9 keys to be read with only 6 GPIO pins, freeing up the rest of the 'ECU' for other high-performance features.
Firmware: The Engine Control Unit (ECU)
The VROOOOMpad runs on KMK firmware, a CircuitPython-based firmware that's incredibly easy to customize.
The rotary encoder is your primary dial, mapped to control system volume.
The 9 keys are your command triggers, configured with multi-layer keymaps like a sequential gearbox. Shift up to a 'Track Mode' layer for gaming macros, or down to a 'Cruising' layer for media controls.
The OLED dashboard displays your current layer, so you never miss a shift.
The RGB 'Tach' LEDs provide instant visual feedback, confirming actions or highlighting your active toolset with a blast of color.
Build Sheet (BOM):
Here is the official parts list to build your own VROOOOMpad.
The Engine (ECU):
1x Seeed Studio XIAO RP2040
The Cockpit Controls:
9x Cherry MX style switches (Linear for speed, Tactile for precision!)
9x Keycaps (Your preferred profile)
1x EC11 Rotary Encoder
9x 1N4148 Diodes
Dashboard & Underglow:
1x 0.91" 128x32 I2C OLED Display (GND-VCC-SCL-SDA pinout)
16x SK6812 5050 RGB LEDs
Chassis & Fasteners:
1x Custom Case (3D Printed or Laser Cut)
M3 Bolts and Heat-set inserts as required by your case design
1x 4-pin connector for the OLED
Extra Stuff
Time to get off the starting line. Tune your VROOOOMpad to redline your productivity, streamline your creative process, or just get the jump on the competition. It's not just a macropad; it's a performance upgrade for your desk.
