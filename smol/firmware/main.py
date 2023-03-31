import time
start = time.monotonic()
import gc
start_ram = gc.mem_free()

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap


from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.tapdance import TapDance
import words

combos = Combos()

keyboard = KMKKeyboard()
tapdance = TapDance()
modtap = ModTap()
layers_ext = Layers()
keyboard.debug_enabled = False
tapdance.tap_time = 200

keyboard.modules = [layers_ext, modtap, combos, tapdance]
_______ = KC.TRNS
__NO___ = KC.NO
CTRLLOWER = KC.TD(KC.LCTL, KC.MO(2))
TOGNAV = KC.TO(3)
TOGDEFAULT = KC.TO(0)
LCTRLH = KC.MT(KC.H, KC.LCTL, tap_time=200)
LCTRLF = KC.MT(KC.F, KC.LCTL, tap_time=200)

LSFTS = KC.MT(KC.S, KC.LSFT, tap_time=200)
LSFTL = KC.MT(KC.L, KC.LSFT, tap_time=200)

LGUID = KC.MT(KC.D, KC.LGUI, tap_time=200)
NAV = KC.MO(3)
RAISE_ENT = KC.LT(1, KC.ENT, tap_time=100)
RAISE_BK = KC.LT(1, KC.BSPC, tap_time=100)
LOWER_SPC = KC.LT(2, KC.SPC, tap_time=100)
COPY = KC.LCTL(KC.C)
CUT = KC.LCTL(KC.X)
PST = KC.LCTL(KC.V)
ALL = KC.LCTL(KC.A)
UNDO = KC.LCTL(KC.Z)

LSFTZ = KC.MT(KC.Z, KC.LSFT, tap_time=200)
LSFTSL = KC.MT(KC.SLSH, KC.LSFT, tap_time=200)
LALTQ = KC.MT(KC.Q, KC.LALT, tap_time=200)
LALTP = KC.MT(KC.P, KC.LALT, tap_time=200)
LGUIA = KC.MT(KC.A, KC.LGUI, tap_time=200)
LGUISC = KC.MT(KC.SCLN, KC.LGUI, tap_time=100)
LOWER = KC.MO(2)
RAISE = KC.MO(1)
RAISE_ENT = KC.LT(1, KC.ENT, tap_time=70)
RAISE_BK = KC.LT(1, KC.BSPC, tap_time=100)


# NOQA
# flake8: noqa
# fmt: off
keyboard.keymap = [
      [  #QWERTY
        LALTQ,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   LALTP,\
        LGUIA,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, LGUISC,\
        LSFTZ,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, LSFTSL,\
           _______,    LOWER,   CTRLLOWER,  RAISE_ENT,     RAISE_BK,    LOWER_SPC,  KC.LEADER,
    ],
    [  #RAISE
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                        KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,\
        _______,  _______, _______, _______, _______,                      KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT, KC.QUOT,\
        _______, KC.GRV,  _______,_______, TOGNAV,                      KC.MINS,  KC.EQL, KC.LBRC, KC.RBRC, KC.BSLS,\
                                _______, _______, _______,      _______, _______, _______,_______,
    ],
    [  #LOWER
        KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,      KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,\
        _______,  _______, _______, _______, _______,      KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT, KC.DQT,\
        _______, KC.TILD, _______, _______, TOGNAV,     KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,\
                            _______, _______, _______,      KC.ENT,  _______, KC.DEL
    ],
      [  #NAV
        TOGDEFAULT,  _______, _______, _______, _______,      _______,  _______, _______, _______, _______,\
        _______,  _______, _______, _______, _______,      KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT, _______,\
       KC.LSFT,  _______, _______, _______, TOGDEFAULT,     _______,  _______, _______, _______, _______,\
                            _______, _______, _______,      _______, _______, _______,_______
    ]


    

] 

combos.combos = [
    Chord((KC.W, KC.E), KC.ESC),       
    Chord((KC.I, KC.U), KC.BSPC),                                                                                                                                                                                        
    Chord((KC.K, KC.J), KC.COLN),
    Chord((KC.COMM, KC.M), KC.N),
    Chord((KC.COMM, KC.DOT), KC.SLSH),
    Chord((KC.E, KC.R), KC.TAB),
    Sequence((KC.LEADER, KC.C, KC.N), words.const),
    Sequence((KC.LEADER,KC.C,KC.L),words.consolelog),
    Sequence((KC.LEADER,KC.M,KC.DOT),words.arrowfunc)
]


finish=time.monotonic()
finish_ram=gc.mem_free()
print("start:",start,"finish:",finish,finish-start)
print("RAM")
print("start:",start_ram,"finish:",finish_ram,start_ram-finish_ram)

if __name__ == '__main__':
   
    keyboard.go()
