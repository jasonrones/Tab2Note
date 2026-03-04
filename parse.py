# Import Libraries
import sys
import configparser

# Import Configuration
config = configparser.ConfigParser()
config.read('config.ini')
instrument = config['DEFAULT']['Instrument']
stringCount = config['DEFAULT']['String_Count']
accidentals = config['Lilypond']['Accidentals']

## Initialize Variables
output = '' # Output string
Tunings = {}

# All notes in sharp keys
sharpKey = {
    1: "c,,",
    2: "cis,,",
    3: "d,,",
    4: "dis,,",
    5: "e,,",
    6: "f,,",
    7: "fis,,",
    8: "g,,",
    9: "gis,,",
    10: "a,,",
    11: "ais,,",
    12: "b,,",
    13: "c,",
    14: "cis,",
    15: "d,",
    16: "dis,",
    17: "e,",
    18: "f,",
    19: "fis,",
    20: "g,",
    21: "gis,",
    22: "a,",
    23: "ais,",
    24: "b,",
    25: "c",
    26: "cis",
    27: "d",
    28: "dis",
    29: "e",
    30: "f",
    31: "fis",
    32: "g",
    33: "gis",
    34: "a",
    35: "ais",
    36: "b",
    37: "c'",
    38: "cis'",
    39: "d'",
    40: "dis'",
    41: "e'",
    42: "f'",
    43: "fis'",
    44: "g'",
    45: "gis'",
    46: "a'",
    47: "ais'",
    48: "b'",
    49: "c''",
    50: "cis''",
    51: "d''",
    52: "dis''",
    53: "e''",
    54: "f''",
    55: "fis''",
    56: "g''",
    57: "gis''",
    58: "a''",
    59: "ais''",
    60: "b''",
}

# All notes in flat keys
flatKey = {
    1: "c,,",
    2: "des,,",
    3: "d,,",
    4: "ees,,",
    5: "e,,",
    6: "f,,",
    7: "ges,,",
    8: "g,,",
    9: "aes,,",
    10: "a,,",
    11: "bes,,",
    12: "b,,",
    13: "c,",
    14: "des,",
    15: "d,",
    16: "ees,",
    17: "e,",
    18: "f,",
    19: "ges,",
    20: "g,",
    21: "aes,",
    22: "a,",
    23: "bes,",
    24: "b,",
    25: "c",
    26: "des",
    27: "d",
    28: "ees",
    29: "e",
    30: "f",
    31: "ges",
    32: "g",
    33: "aes",
    34: "a",
    35: "bes",
    36: "b",
    37: "c'",
    38: "des'",
    39: "d'",
    40: "ees'",
    41: "e'",
    42: "f'",
    43: "ges'",
    44: "g'",
    45: "aes'",
    46: "a'",
    47: "bes'",
    48: "b'",
    49: "c''",
    50: "des''",
    51: "d''",
    52: "ees''",
    53: "e''",
    54: "f''",
    55: "ges''",
    56: "g''",
    57: "aes''",
    58: "a''",
    59: "bes''",
    60: "b''",
}

# String: NoteID
match instrument:
    case 'Bass':
        tuning = Tunings["bass"] = {
            "string1": 32,
            "string2": 27,
            "string3": 22,
            "string4": 17
        }
    case 'Guitar':
        tuning = Tunings["guitar"] = {
            "string1": 41,
            "string2": 36,
            "string3": 32,
            "string4": 27,
            "string5": 22,
            "string6": 17
        }

# Read .tab file
file = sys.argv[1]
tabFile = open(file, 'r')
tabLines = tabFile.read().split('\n')

# Use Sharps or Flats?
match accidentals:
    case 'Sharps':
        notes = sharpKey
    case 'Flats':
        notes = flatKey
    case _:
        notes = sharpKey # default to sharp key if not specified
        output = 'Add "flat" or "sharp" in the input filename' + '\n' + '\n'

# Parse Tablature
lineNumber = 0
for line in tabLines:
    lineNumber = lineNumber + 1
    tabNotes = line.split()
    for tab in tabNotes:
        if tab.count(".") > 2: # Check for missing spaces between tab notes
            output = 'Check the tab on line ' + str(lineNumber) + '\n' + '\n'
        tabParts = tab.split(".")
        string = "string" + str(tabParts[0])
        # print(string)
        fret = tabParts[1]
        # print(fret)
        duration = tabParts[2].replace('*', '.')
        # print(duration)
        if string == "string0": # Check if note is a rest
            output = output + 'r' + duration + ' '
        else:
            noteID = tuning[string] + int(fret)
            output = output + notes[noteID] + duration + ' '
    output = output + '\n'

print('Copy/Paste into your .ly file: ' + '\n')

print(output)

print('This output is also saved in notes.txt')

# Print notes to text file
with open('notes.txt', 'w') as f:
    f.write(output)

# Print notes to lilypond file
match instrument:
    case 'Bass':
        lilyHead = r"""\header {title = "Tab2Note Output"}
part = {
  \clef bass
  """
    case 'Guitar':
        lilyHead = r"""\header {title = "Tab2Note Output"}
part = {
"""

lilyFoot = r"""\bar "|."
}

\score {
    \new Staff \part 
    \layout { }
    \midi { }
}"""

with open('output.ly', 'w') as f:
    f.write(lilyHead)
    f.write(output)
    f.write(lilyFoot)