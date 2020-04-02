from linked_binary_tree import LinkedBinaryTree
import pickle , sys
from array_stack import ArrayStack

class NotValidExpression(Exception):
    pass

"""For code, I would reference Chapter 8 from the book : Data Structures and Algorithms in Python by Goodrich, Tamassia and Goldwasser"""
class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.
        In a single parameter form, token should be a leaf value (e.g., '42'),
        and the expression tree will have that value at an isolated node.
        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator.
        """
        super().__init__()  # LinkedBinaryTree initialization
        self._add_root(token)  # use inherited, nonpublic method
        if left is not None:  # presumably three-parameter form
            self._attach(self.root(), left, right)  # use inherited, nonpublic method

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []  # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))  # leaf value as a string
        else:
            result.append('(')  # opening parenthesis
            self._parenthesize_recur(self.left(p), result)  # left subtree
            result.append(p.element())  # operator
            self._parenthesize_recur(self.right(p), result)  # right subtree
            result.append(')')  # closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())  # we assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:  # treat 'x' or '*' as multiplication
                return left_val * right_val
    def visualise_binary_tree(self):
        """Prints the expected output tree from the input"""
        tree_elements = [i for i in self.breadthfirst()] # saves the nodes of the tree in an array after the breadthfirst transversal is executed
        height = self.height(self.root())
        n = sum([2 ** i for i in range(0, height + 1)]) # total number of possible nodes of a tree
        array_tree = n * [" "] # array-based representation of a binary tree implemented by using level-numbering of positions(chapter 8.3.2 of Goodrich book)
        array_tree[0] = tree_elements[0] # assigning the root
        for i in range(0, len(tree_elements)):
            index1 = i
            if tree_elements[i] in array_tree:
                index1 = array_tree.index(tree_elements[i])
            for j in range(i, len(tree_elements)):
                if tree_elements[j] == self.left(tree_elements[i]):
                    array_tree[2 * index1 + 1] = tree_elements[j]
                if tree_elements[j] == self.right(tree_elements[i]):
                    array_tree[2 * index1 + 2] = tree_elements[j]
                    break
        for i in range(0, len(array_tree)):
            if array_tree[i] != " ": # the empty nodes are represented by " "
                array_tree[i] = array_tree[i].element() # changing the array from nodes to elements of the nodes
        height1 = height
        spaces = 2 ** (height + 1) - 2 # initialises the number of spaces that have to be added when displaying the nodes
        height -= 1
        pos = 0 # index of the node that is displayed
        print(spaces * " " + array_tree[pos])
        for i in range(0, height1 + 1): #iterates through all the levels of the binary tree
            spaces = 2 ** (height + 1) - 2
            level = spaces * " " # initialises each level of the binary tree with the appropiate number of spaces
            height += 1
            spaces = 2 ** (height + 1) - 1
            if 2 * pos + 3 > len(array_tree): # exit the loop if the tree was traversed
                break
            for j in range(0, 2 ** i):
                level += array_tree[2 * pos + 1] + " " * spaces + array_tree[2 * pos + 2] + " " * spaces # adds the nodes from that level
                pos += 1
            height -= 2
            print(level)
    def save_binary_tree(self): # saves the tree in a file
        file = open("backup","wb")
        pickle.dump(self,file)
        file.close()

    @staticmethod
    def load_binary_tree(): #loads the tree that has been saved
        file = open("backup","rb")
        other = pickle.load(file)
        file.close()
        return other

def match_paranthesis(expression):
    """Checks if the parantheses from the expression match up correctly"""
    stack=ArrayStack()
    for s in expression:
        if s == '(':
            stack.push(s)
        if s == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()

def no_operators(expression):
    """Checks if the expression contains any operators"""
    OPERATORS = set('+-*/')
    for i in expression:
        if i in OPERATORS:
            return True
    raise NotValidExpression('Not a valid expression, no operators')

def no_paranthesis(expression):
    """Checks if the expression contains any parantheses"""
    for i in expression:
        if i in '()':
            return True
    raise NotValidExpression('Not a valid expression, no paranthesis')

def no_numbers(expression):
    """Checks if the expression contains any numbers"""
    NUMBERS = '0123456789'
    for i in expression:
        if i in NUMBERS:
            return True
    raise NotValidExpression('Not a valid expression, no numbers')

def invalid_characters(expression):
    """Checks if the expression contains any invalid characters, others than numbers, parantheses or operators"""
    CHARACTERS = '0123456789()+-/*'
    for i in expression:
        if i not in CHARACTERS:
            raise NotValidExpression('Not a valid expression, invalid characters inserted')
    return True

def valid_expression(expression):
    """Verifies whether an expression is valid or not and displays appropiate messages"""
    OPERATORS= '+*/-'
    if no_operators(expression) != True:
        return no_operators(expression)
    if no_paranthesis(expression) != True:
        return no_paranthesis(expression)
    if no_numbers(expression) != True:
        return no_numbers(expression)
    if invalid_characters(expression) != True:
        return invalid_characters(expression)
    if match_paranthesis(expression) == False:
        raise NotValidExpression('Not a valid expression, brackets mismatched.')
    number_operators = 0
    number_paranthesis = 0
    for i in expression:
        if i in OPERATORS:
            number_operators += 1
        elif i == '(' or i == ')':
            number_paranthesis +=1
    expression1 = expression[1:(len(expression) - 1)] # checks if the expression without the first and last character is valid
    if match_paranthesis(expression1) == False and ('(' in expression1 or ')' in expression1):
        raise NotValidExpression('Not a valid expression, brackets mismatched.') # if it is not, raises an appropiate error
    for i in range(0, len(expression) - 1):
        #Checks if an operator is missing,if there exists a number followed by ( or if there is a )before the number
        if expression[i] not in OPERATORS and expression[i] not in '()':
            if expression[i + 1] == '(':
                raise NotValidExpression('Not a valid expression, operator missing.')
        elif expression[i] in OPERATORS and expression[i + 1] in OPERATORS + ')' :
            raise NotValidExpression('Not a valid expression, wrong placement of operators')
        #Checks if an operator is placed wrongly , before ) or next to another operator
        if expression[i+1] not in OPERATORS and expression[i + 1] not in '()':
            if expression[i] == ')':
                raise NotValidExpression('Not a valid expression, operator missing.')
        elif expression[i+1] in OPERATORS and expression[i] in OPERATORS + '(':
            raise NotValidExpression('Not a valid expression, wrong placement of operators')
    if 2*number_operators != number_paranthesis: # an expression is valid only if the number of paranthesis is equal to the double of the number of operators
        raise NotValidExpression('Not a valid expression, wrong number of operands.')
    return True

def tokenize(raw):
    """Produces list of tokens indicated by a raw expression string.
    For example the string '(43-(3*10))' results in the list
    ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    if valid_expression(raw) != True:
        return valid_expression(raw)

    SYMBOLS = set('+-*/() ')

    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j])  # complete preceding token
            if raw[j] != ' ':
                tokens.append(raw[j])  # include this token
            mark = j + 1  # update mark to being at next index
    if mark != n:
        tokens.append(raw[mark:n])  # complete preceding token
    return tokens


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression.
    tokens must be an iterable of strings representing a fully parenthesized
    binary expression, such as ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    S = []  # we use Python list as stack
    for t in tokens:
        if t in '+-*/':  # t is an operator symbol
            S.append(t)  # push the operator symbol
        elif t not in '()':  # consider t to be a literal
            S.append(ExpressionTree(t))  # push trivial tree storing value
        elif t == ')':  # compose a new tree from three constituent parts
            right = S.pop()  # right subtree as per LIFO
            op = S.pop()  # operator symbol
            left = S.pop()  # left subtree
            S.append(ExpressionTree(op, left, right))  # repush tree
        # we ignore a left parenthesis
    return S.pop()


if __name__ == '__main__':
    ch = input("Press L for loading the tree or any other key for continue ")
    if ch == 'L':
        big = ExpressionTree.load_binary_tree()
        big.visualise_binary_tree()
    ch1 = input("Enter an expression: ")
    big = build_expression_tree(tokenize(ch1))
    print(big, '=', big.evaluate())
    ch1 = input("Press V for visualising the tree or any key to continue ")
    if ch1 == "V":
        big.visualise_binary_tree()
    ch2 = input("Press S for saving the tree or any key for ending the program ")
    if ch2 == "S":
        big.save_binary_tree()
    else:
        sys.exit()
