def solution(src):
    """One of your new coworkers has submitted code with variable names in snake case, where multiword names are separated by underscores (such as my_counter). Your company's convention is to use only lower camel case, where multiword variable names are concatenated, capitalizing the first letter of every word except the first (e.g. myCounter).

    Your team is tasked with taking the source code src from your coworker, and returning code with the all the names in snake case converted into lower camel case. More specifically:

    Variable names may start with one or more underscores, and these should be preserved. For example _the_variable should become _theVariable
    
    Variable names may end with trailing underscores, and these should be preserved. For example, the_variable__ should become theVariable__.

    To keep the problem simple, you are not restricted to variable names, but instead should replace all instances of snake case.

    Example
    For src = "This is the doc_string for __secret_fun", the output should be
    solution(src) = "This is the docString for __secretFun".

    Args:
        src (string): a string of characters with underscores

    Returns:
        str: a camel case string format of the input
    """
    
    
    words = src.split()
    modified_words = []
    
    for word in words:
        if '_' in word:
            parts = word.split('_')
            
            leading = ''
            trailing = ''
            
            while parts[0] == '':
                leading += '_'
                parts.pop(0)
            
            while parts[-1] == '':
                trailing += '_'
                parts.pop()
                
            if word.istitle():
                camel_case = parts[0].capitalize() + ''.join(part.capitalize() for part in parts[1:])
            else:
                camel_case = parts[0].lower() + ''.join(part.capitalize() for part in parts[1:])
            
            modified_word = leading + camel_case + trailing
        
        else:
            modified_word = word
        
        modified_words.append(modified_word)
    
    return ' '.join(modified_words)


# Example usage
src = "This is the doc_string for __secret_fun"
print(solution(src))  # Output: "This is the docString for __secretFun"