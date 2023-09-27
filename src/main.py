from trie import Trie

class Main:
    def __init__(self):
        self.guide = "Syötä haluamasi kappaleen numero, tai sulje sovellus:\n0 Ukko Nooa\n1 Sulje sovellus\n"
        self.actions = {'0': 'ukkonooatesti.txt'}

    def start(self):
        while True:
            print('\nMUSIIKKIGENERAATTORI')
            print('\n0 Aloita generointi')
            print('1 Sulje sovellus')
            action = input('\nSyötä haluamasi toiminnon numero: ')
            if action == '1':
                print('\nHei hei :(')
                break
        


if __name__ == "__main__":
    main = Main()
    main.start()