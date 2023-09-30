from trie import Trie
from converter import Converter

class Main:
    """Pyörittää sovellusta.
    """
    def __init__(self):
        """Konstruktori.
        """
        self.actions = {'0': 'ukkonooatesti.txt'}
        self.converter = Converter()
        self.error = 'Syöttämäsi teksti ei kelpaa. Tarkista syöte ja yritä uudestaan.'

    def start(self):
        """Aloittaa sovelluksen toiminnan.
        """
        print('MUSIIKKIGENERAATTORI')

        while True:
            action = input('\nAloita generointi [0] tai sulje sovellus [1]: ')
            if action == '1':
                break

            elif action in self.actions:
                print('\n(generointi)')
                print('(ukko nooa sävelkorkeudet):')
                print(self.converter.read_song_file(f'src/{self.actions[action]}'))

            else:
                print(self.error)
                continue

            action = input('\nGeneroi uudestaan? [k/e]: ' )
            if action in ['k', 'K']:
                self.converter.converted = []
            elif action in ['e', 'E']:
                break
            else:
                print(self.error)

        print('\nHei hei :(')



if __name__ == "__main__":
    main = Main()
    main.start()
