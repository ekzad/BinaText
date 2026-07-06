import pyfiglet
import time
import os
import sys
import keyboard
ascii_binary_map = {
    # Lowercase letters
    'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100',
    'e': '01100101', 'f': '01100110', 'g': '01100111', 'h': '01101000',
    'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100',
    'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000',
    'q': '01110001', 'r': '01110010', 's': '01110011', 't': '01110100',
    'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000',
    'y': '01111001', 'z': '01111010',

    # Uppercase letters
    'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100',
    'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000',
    'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100',
    'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000',
    'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100',
    'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000',
    'Y': '01011001', 'Z': '01011010',

    # Digits
    '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011',
    '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111',
    '8': '00111000', '9': '00111001',
    ' ': ' '
}
class terminal:
    def __init__(self):
        self.user_text()

    def user_text(self):
        while True:
            print(pyfiglet.figlet_format("BinaText"))
            self.type("A simple but fun binary translator that will turn your text into binary using standard 8 bit ASCII")
            self.type("=========================")
            self.Text = input("Enter your plain text>> ")
            if 'exit' in self.Text.lower() or 'quit' in self.Text.lower():
                self.type("Do you want to exit? Y/N ")
                In = input(">> ")
                if In.lower() == 'y':
                    break
                elif In.lower()== 'n':
                    self.Binary = self.convert(str(self.Text))
                    self.type(self.Binary)
                    input("Press enter to continue...")
                    os.system('cls')
            elif 'clear' in self.Text.lower():
                os.system('cls')
            else:
              self.Binary = self.convert(str(self.Text))
              self.type(self.Binary)
              input("Press enter to continue... ")
              os.system('cls')
    def convert(self, text):
        self.type("Processing...")
        time.sleep(0.5)
        words = text
        letters = []
        for letter in words:
            self.type(letter)
            letters.append(letter)
        binary = []
        for letter in letters:
            binary.append(ascii_binary_map[letter])
            self.type(ascii_binary_map[letter])
        self.type(binary)
        result = ''.join(binary)
        os.system('cls')
        self.keyboard_output(result)
        return result
    def keyboard_output(self,binary):
        self.type("Do you want me to type this for you? If so, press Alt on your keyboard whenever you're ready. If not, press Esc")
        self.type("Note: If you press esc, I will only display the result.")
        key = keyboard.read_key()
        time.sleep(3)
        self.type(f"You pressed {key}")
        time.sleep(3)
        if key == 'esc':
            print("I will only show the result")
            pass
        elif key == 'alt':
            keyboard.write(binary, delay=0.05)
        else:
            self.type("Invalid Key")
            self.type("Showing result...")
    def on_key(self, event):
        return event.name
    def type(self, text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

if __name__ == '__main__':
    terminal()