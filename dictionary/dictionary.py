class Node():
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.meaning = kwargs.get('meaning')
        self.left = kwargs.get('left')
        self.right = kwargs.get('right')

    def set_left(self, node):
        if isinstance(node) == Node:
            self.left = node 

    def set_right(self, node):
        if isinstance(node) == Node:
            self.right = node 

class Dictionary():

    def __init__(self):
        self.head = None 

    def load_data(self):
        with open('C:\workspaces\coding_practice\dictionary\words_meanings.txt', 'r') as fp: 
            for line in fp:
                self.insert_node(line)

    def insert_node(self, line):
        word, meaning = line.split("=")
        node = Node(name=word, meaning=meaning)
        if not self.head:
            self.head = node
        else:
            prev = None
            current = self.head 
            child_type = None
            while current:
                prev = current
                if current.name > word:
                    current = current.left
                    child_type = 'left'
                else:
                    current = current.right
                    child_type = 'right'
            if child_type == 'left':
                prev.left = node 
            else:
                prev.right = node

    def delete_node(self, word):
        prev = None
        current = self.head 
        child_type = None
        while current and current.name != word:
            prev = current
            if current.name > word:
                current = current.left
            else:
                current = current.right

    def get_meaning(self, word):
        if not self.head:
            print(f"Tree is not prepared yet")
        else:
            current = self.head 
            while current:
                if current.name == word:
                    return current.meaning
                elif current.name < word:
                    current = current.right 
                else:
                    current = current.left 

    def print_node_lexical(self, node):
        if not node:
            return
        if node.left:
            self.print_node_lexical(node.left)
        print(f"{node.name} --> {node.meaning}")
        if node.right:
            self.print_node_lexical(node.right)

    def print_lexical_order(self):
        self.print_node_lexical(self.head)

    def print_node_reverse(self, node):
        if not node:
            return
        if node.right:
            self.print_node_reverse(node.right)
        print(f"{node.name} --> {node.meaning}")
        if node.left:
            self.print_node_reverse(node.left)

    def print_reverse_order(self):
        self.print_node_reverse(self.head)


if __name__ == "__main__":
    d = Dictionary()
    d.load_data()
    print(f"Meaning of ebullient --> {d.get_meaning('ebullient')}")
    print('-'*20)
    print("Dictionary in Ascending order: ")
    d.print_lexical_order()
    print('-'*20)
    print("Dictionary in Descending order: ")
    d.print_reverse_order()