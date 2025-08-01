# --- Imports ---
import board
import busio  # Needed for the OLED display

# KMK Core
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner

# KMK Keys and Modules
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.layers import Layers
from kmk.modules.encoder import Encoder
from kmk.modules.media_keys import MediaKeys

# KMK Extensions (for extra hardware)
from kmk.extensions.rgb import RGB
from kmk.extensions.oled import OLED
from kmk.consts import KMK_RELEASE


# --- Basic Keyboard Setup ---
keyboard = KMKKeyboard()

# --- Module and Extension Setup ---
# Add layers and macros modules
keyboard.modules.append(Layers())
keyboard.modules.append(Macros())
keyboard.modules.append(MediaKeys())

# --- Pin Definitions (from your schematic) ---
# Your switches are in a 3x3 matrix.
# Columns are the pins that go directly to one side of the switch.
keyboard.col_pins = (
    board.GP1,  # Col 1: SW1, SW5, SW9
    board.GP0,  # Col 2: SW2, SW6, SW10
    board.GP29, # Col 3: SW3, SW7, SW11
)

# Rows are the pins connected to the other side of the switch through a diode.
# The row order depends on how you physically arrange them on the PCB.
# This assumes SW1-SW3 is the top row, SW5-SW7 is middle, SW9-SW11 is bottom.
keyboard.row_pins = (
    board.GP10, # Row 1: SW3, SW7, SW11 are connected here (check schematic)
    board.GP9,  # Row 2: SW2, SW6, SW10 are connected here
    board.GP8,  # Row 3: SW1, SW5, SW9 are connected here
)

# Use the MatrixScanner for your 3x3 grid
keyboard.matrix = MatrixScanner(
    cols=keyboard.col_pins,
    rows=keyboard.row_pins,
    diode_orientation='COL2ROW', # The current flows from column pin, through switch, through diode, to row pin.
)


# --- Rotary Encoder Setup ---
encoder = Encoder()
keyboard.modules.append(encoder)

# Define the encoder pins and what they do.
# The push button on your encoder is not wired, so we use 'None'.
# (Pin A, Pin B, Pin Push)
encoder.pins = ((board.GP27, board.GP26, None),)

# The actions for turning the encoder.
# (On clockwise turn, On counter-clockwise turn)
encoder.map = [
    (KC.VOLU, KC.VOLD),
]


# --- SK6812 LED (NeoPixel) Setup ---
# There are 16 LEDs in your 4x4 grid.
# The data pin is GP28.
rgb = RGB(
    pixel_pin=board.GP28,
    num_pixels=16,
    hue_default=100, # A nice starting color (green-ish blue)
    sat_default=255,
    val_default=150, # Brightness (0-255)
)
keyboard.extensions.append(rgb)

# --- OLED Display Setup (Bonus) ---
# This code will show the current layer on your OLED screen.
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)
oled = OLED(
    oled_bus=i2c,
    device_addr=0x3C, # Common address, may be 0x3D
    flip_vertically=True,
    flip_horizontally=False, # Change these to orient the display
    width=128,
    height=32, # For 0.91" OLEDs
)
keyboard.extensions.append(oled)

# --- Keymap and Macros ---
# Create aliases for layer switching keys to make the map cleaner
TO_BASE = KC.TO(0)
TO_MACRO = KC.TO(1)
TO_MEDIA = KC.TO(2)

# Define the physical layout of your keys in a 3x3 grid
# This should match the column/row pin definitions above.
# The order is [Row1_Keys, Row2_Keys, Row3_Keys]
keyboard.keymap = [
    # ---- LAYER 0: Base Layer (Navigation & Macros) ----
    [
        # Top Row (SW1, SW2, SW3) -> Mapped to Menu/Layer switching
        TO_MACRO,       KC.LCTL(KC.TAB),     TO_MEDIA,
        # Middle Row (SW5, SW6, SW7) -> Basic Macros
        KC.LCTL(KC.C),  KC.LCTL(KC.V),       KC.LCTL(KC.X),
        # Bottom Row (SW9, SW10, SW11) -> Advanced Macros
        KC.LCTL(KC.Z),  KC.LCTL(KC.S),       KC.MACRO("Hello from my Hackpad!")
    ],
    # ---- LAYER 1: Custom Macro Layer ----
    [
        # Top Row
        TO_BASE,        KC.TRNS,             KC.TRNS,
        # Middle Row -> Example: App specific shortcuts (e.g., for VSCode)
        KC.LCTL(KC.LSHIFT(KC.P)), # Command Palette
        KC.LCTL(KC.P),            # Go to File
        KC.LCTL(KC.BSLASH),       # Toggle Integrated Terminal
        # Bottom Row
        KC.F5,          KC.TRNS,             KC.TRNS,
    ],
    # ---- LAYER 2: Media Control Layer ----
    [
        # Top Row
        TO_BASE,        KC.TRNS,             KC.TRNS,
        # Middle Row
        KC.MPRV,        KC.MPLY,             KC.MNXT,
        # Bottom Row
        KC.MUTE,        KC.VOLD,             KC.VOLU,
    ],
]


# --- Main Loop ---
if __name__ == '__main__':
    keyboard.go()
