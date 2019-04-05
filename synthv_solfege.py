#!/usr/bin/env python3

import json
import sys

lyric_from_midi_base = {
    0: "do",
    1: "di",
    2: "re",
    3: "ri",
    4: "mi",
    5: "fa",
    6: "fi",
    7: "so",
    8: "si",
    9: "la",
    10: "li",
    11: "ti"
}

def read_file(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data

def write_file(file_name, data):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file)

def get_midi_base_from_midi(midi):
    return midi % 12

def edit_lyrics(data):
    for track in data['tracks']:
        for note in track['notes']:
            midi = note['pitch']
            midi_base = get_midi_base_from_midi(midi)
            lyric = lyric_from_midi_base[midi_base]
            note['lyric'] = lyric
    return data

if __name__ == "__main__":
    if not (len(sys.argv) > 2):
        print("Usage:")
        print("    " + sys.argv[0] + " <infile> <outfile>")
        sys.exit(0)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    data = read_file(infile)
    dataa = edit_lyrics(data)
    write_file(outfile, dataa)