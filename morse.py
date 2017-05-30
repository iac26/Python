#morse

morse = ['.-','-...','-.-.','-..','.','..-.','--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',]
latin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']


def Decode(string):
    string = string.lower()
    words = string.split('//')
    message = ''
    for word in words:
        letters = word.split('/')
        mword = ''
        for letter in letters:
            try:
                pos = morse.index(letter)
                m = latin[pos]
            except:
                print 'ERROR'
            mword += m
        message += mword + ' '
    return message[:-1]

def Encode(string):
    string = string.lower()
    words = string.split(' ')
    message = ''
    for word in words:
        mword = ''
        for letter in word:
            try:
                pos = latin.index(letter)
                m = morse[pos]
            except:
                print 'ERROR'
            mword += m + '/'
        message += mword + '/'
    return message[:-2]
while True:
    choice = raw_input('Encode or Decode? ')
    choice = choice.lower()
    if choice.startswith('e'):
        message = raw_input('clear: ')
        print Encode(message)
    if choice.startswith('d'):
        message = raw_input('morse: ')
        print Decode(message)
    if choice == 'quit':
        break
