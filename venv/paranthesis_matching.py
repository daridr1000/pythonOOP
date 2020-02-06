from array_stack import ArrayStack

def match_paranthesis(paranthesis):
    left='{[(|'
    right='}])|'
    stack=ArrayStack()
    for s in paranthesis:
        if s in left and s not in right:
            stack.push(s)
        if s in right:
            if s not in left:
                if stack.is_empty():
                     return False
                else:
                    if right.index(s)==left.index(stack.top()):
                        stack.pop()
                    else:
                        return False
            else:
                if stack.is_empty():
                    stack.push(s)
                else:
                    if s!=stack.top():
                        stack.push(s)
                    else:
                        stack.pop()
    return stack.is_empty()
print(match_paranthesis('[||](|)|'))




