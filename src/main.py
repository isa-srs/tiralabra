from trie import Trie
from converter import Converter

class Main:
    def __init__(self):
        self.guide = "Syötä haluamasi kappaleen numero, tai sulje sovellus:\n0 Ukko Nooa\n1 Sulje sovellus\n"
        self.actions = {'0': 'ukkonooatesti.txt'}
        self.converter = Converter()

    def start(self):
        print('MUSIIKKIGENERAATTORI')
        
        while True:
            action = input('\nAloita generointi [0] tai sulje sovellus [1]: ')
            if action == '1':
                break
            
            elif action in self.actions:
                print('\n(generointi)')
                print('(ukko nooa sävelkorkeudet):')
                print(self.converter.read_song_file(f'src/{self.actions[action]}'))

            action = input('\nGeneroi uudestaan? [k/e]: ' )
            if action in ['k', 'K']:
                self.converter.converted = []
                continue
            elif action in ['e', 'E']:
                break
        
        print('\nHei hei :(')



if __name__ == "__main__":
    main = Main()
    main.start()