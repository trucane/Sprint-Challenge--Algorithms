'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "ruTh"
def count_th(word):
    #base case
    if len(word) <= 1:
        return 0

    #account for string case
    #if word[:2].lower() == 'th':
    #thought I needed to until I ran test
    
    if word[:2] == 'th':
        return count_th(word[1:]) + 1

    
    return count_th(word[1:])
    


print(count_th(word))
    
