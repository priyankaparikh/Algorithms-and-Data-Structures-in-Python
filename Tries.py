class LetterStack(object):
    def __init__(self, initial=""):
        # my version of a stack is a python list
        self._stack = list(initial)

    def push(self,letter):
        # inserting items into self.stack
        self._stack.append(letter)

    def pop(self):
        # first item in last out
        return self._stack.pop()

    def peek(self):
        # return most recent pushed letter
        return self._stack[-1]

    def is_empty(self):
        # return true or false if list is isEmpty
        return not self._stack

    def as_word(self):
        # return the contents of the stack as a whole as_word
        return "".join(self._stack)

class TrieNode(object):

    # creating a marker
    COMPLETE_WORD = object()

    def __init__(self, letter, children=None):
        self.letter = letter
        self.children = children or []

    def find_child_words(node, words, word):

        if node is TrieNode.COMPLETE_WORD:
            words.append(word.as_word())
            return

        word.push(node.data)

        for n in node.children:
            _find_child_words(n, words, word)

            if not word.is_empty():
                word.pop()

        found_words = []

        for start_n in self.children:
            _find_child_words(start_n, found_words, LetterStack())

        return found_words
