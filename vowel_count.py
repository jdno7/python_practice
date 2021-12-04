def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    result = {}
    for char in phrase:
        # print (char.lower())
        
        if char.lower() in vowels:
            result[char.lower()] = phrase.count(char.lower())+phrase.count(char.upper())
    return result
