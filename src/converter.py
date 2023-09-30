
class Converter:
    def __init__(self):
        self.conversion = {
            'C': 1, 'C#': 2, 'D': 3, 'D#': 4, 'E': 5, 'F': 6, 'F#': 7, 'G': 8, 'G#': 9, 'A': 10,
            'A#': 11, 'B': 12, 'c': 13
        }
        self.converted = []

    def read_song_file(self, song):
        with open(song) as song:
            melody = song.read()
            for note in melody:
                self.converted.append(self.conversion[note])
        return self.converted


    

        
if __name__ == "__main__":
    file2 = 'src/ukkonooatesti.txt'
    print(Converter().read_song_file(file2))