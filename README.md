# Introduction
https://github.com/jasonrones/Tab2Note

[lilypond](http://lilypond.org) is a powerful system for typesetting beautiful music.

As a bass player I sometimes want to transcribe a piece into notation and/or tablature.  Not
being an expert at converting from string+fret positions on the bass into standard notation,
I wanted to be able to enter music by giving string+fret together with tuning information to lilypond.


## Simplified Tab Notation
This project uses simplified tab notation from [jeremy9959's BanjoTab project](https://github.com/jeremy9959/BanjoTab)

Each note is entered as (string).(fret).(duration) - So 2.0.4 means a quarter note on
the open second string.

* Rests should be notated as 0.0.(duration)
* Dotted notes are represented by appending * to the duration (1.1.4*)

## Configuration
You can edit the following settings in the config.ini file:
* Instrument = (Guitar/Bass)
* Accidentals = (Sharps/Flats)

### Notation Not Currently Supported
* Triplets
* Articulations
* Alternate Tunings
* Guitars with more than 6 strings
* Bass with more than 4 strings

## Running Script

```bash
$ python3 parse.py tab.txt
```

The output will be written to notes.txt and the contents can be copy/pasted into your .ly (LilyPond) file.
