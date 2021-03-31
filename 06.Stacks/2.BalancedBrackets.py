def BalancedBrackets(string):
    openBraces="({["
    closeBraces=")}]"
    matchingTypes={ ")":"(", "}":"{", "]":"[" }
    stack=[]

    for ch in string:
        if ch in openBraces:
            stack.append(ch)
        elif ch in closeBraces:
            if len(stack)==0:
                return False
            elif stack[-1]==matchingTypes[ch]:
                stack.pop()
            else:
                return False
    return len(stack)==0


string='(([]()()){})'
print(BalancedBrackets(string))


