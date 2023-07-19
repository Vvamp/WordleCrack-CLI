POSITION_WHITELIST = {}
POSITION_BLACKLIST = {}
LETTER_BLACKLIST =  []
LETTER_WHITELIST = []
SINGLE_OCCURENCES = []


### Check if which words match the current rules
def check_matches(wordlist, wordlength : int):
    matches = []
    for word in wordlist:
        word = word.strip()
        if len(word) != wordlength:
            continue
        if word.isalpha() == False:
            continue

        isNoMatch = False
        for whitelist_key in POSITION_WHITELIST.keys():
            if word[whitelist_key].lower() != POSITION_WHITELIST[whitelist_key].lower():
                isNoMatch=True
                break 
        
        if isNoMatch==False:
            for blacklist_key in POSITION_BLACKLIST.keys():
                blacklisted_letter = blacklist_key.lower()
                blacklisted_indices = POSITION_BLACKLIST[blacklist_key]
                for blacklisted_index in blacklisted_indices:
                    if word[blacklisted_index].lower() == blacklisted_letter.lower():
                        isNoMatch=True
                        break
                if isNoMatch:
                    break 

        if isNoMatch==False:
            for single_occurences in SINGLE_OCCURENCES:
                character_count = word.lower().count(single_occurences.lower())
                if(character_count > 1):
                    isNoMatch=True
                    break

        if isNoMatch==False:
            for letter in word:
                if letter.upper() in LETTER_BLACKLIST:
                    isNoMatch = True
                    break

        if isNoMatch==False:
            for letter in LETTER_WHITELIST:
                if letter.lower() not in word.lower():
                    isNoMatch=True
                    break

        if isNoMatch:
            continue 
        matches.append(word)

    return matches

### Ask the user for path to wordlist and load it in
def request_wordlist():
    wordlist = []
    while wordlist == []:
        wordlist_path = input("Enter path to a wordlist (Ensure a simple text file, one word per line): ")
        try:
            wordlist_file = open(wordlist_path, "r")
            wordlist = wordlist_file.readlines()
        except:
            print("Failed to open wordlist '{}'. Please ensure the file at the given path exists and the proper permissions are set".format(wordlist_path))
        finally:
            wordlist_file.close()
    return wordlist

### Ask the user for the length of the word
def request_wordlength():
    wordlength = 5
    while True:
        wordlength_input = input("Please enter a desired word length, or enter for default (Default: 5): ")
        if(wordlength_input == ""):
            break 
        if(wordlength_input.isnumeric() == False):
            print("'{}' is not a number. Please enter a numeric value, i.e. 5")
            continue 
        wordlength = int(wordlength_input)
        break
    return wordlength

### Process and act based on user input
def process_input(userInput : str, wordlength : int):
    if userInput[0] == "+":
        if(userInput[1].isalpha() == False):
            print("The word can only contain alphabetic characters")
            return
        LETTER_WHITELIST.append(userInput[1].upper())
        print("+ Added '{}' to letter whitelist. Word has to contain this letter.".format(userInput[1].upper()))
    if userInput[0] == "-":
        if(userInput[1].isalpha() == False):
            print("Non-alphabetic characters are already excluded")
            return
        LETTER_BLACKLIST.append(userInput[1].upper())
        print("- Added '{}' to letter blacklist. Word does not contain this letter.".format(userInput[1].upper()))
    if userInput[0] == "1":
        if(userInput[1].isalpha() == False):
            print("The word can only contain alphabetic characters")
            return 
        SINGLE_OCCURENCES.append(userInput[1].upper())
        print("(1) Added '{}' to single occurences. Letter can occur only once.".format(userInput[1].upper()))
    if userInput[0] == ".":
        # Position: .
        # Blacklist/Whitelist: -/+
        # Position(0-4)
        # Letter

        if len(userInput) != 4 or userInput[1] not in ["+", "-"] or userInput[2].isnumeric() == False or userInput[3].isalpha() == False:
            print("Please enter a positional rule in the following format\n1. A dot (.) to indicate that you want to define a positional rule\n2. A plus (+) to indicate a whitelist character(indicate that the letter has to be in that position) or a minus (-) to indicate a blacklist character(indicate that a letter can not be in a specific position)\n3. The position of the character starting from zero (0). So a word of 5 characters has the positions 0 to 4.\n4. The letter to add to the whitelist or blacklist.")
            return
            
        isWhitelist = userInput[1] == "+"
        pos = int(userInput[2])
        letter = userInput[3].upper()
        if(pos >= wordlength or pos < 0):
            print("The position is out of bounds for the given word length. Please ensure the wordlength is set correctly at the start and make sure you are indexing from 0(the first letter is position '0').")
            return 

        if isWhitelist:
            POSITION_WHITELIST[pos] = letter 
            print(".+ Added '{}' to position whitelist for position {}. Letter has to be in that position.".format(letter, pos))
        else:
            if letter.upper() not in POSITION_BLACKLIST.keys():
                POSITION_BLACKLIST[letter.upper()] = []
            POSITION_BLACKLIST[letter.upper()].append(pos)
            print(".- Added '{}' to position blacklist for position {}. Letter can not be in that position.".format(letter, pos))

### Filter unusable words from wordlist
def sanitize_wordlist(wordlist, wordlength):
    final_wordlist = []
    for word in wordlist:
        word = word.strip()
        if len(word) == wordlength and word.isalpha():
            final_wordlist.append(word)
    return final_wordlist

def main():
    current_wordlist = request_wordlist()
    current_wordlength = request_wordlength()
    current_wordlist = sanitize_wordlist(current_wordlist, current_wordlength)

    print("Starting game with {} possible words and a word length of {}".format(len(current_wordlist), current_wordlength))
    while True:
        if len(current_wordlist) == 0:
            print("No possible matches left in current wordlist")
            return 
        if len(current_wordlist) == 1:
            print("Only a single possible match left: {}".format(current_wordlist[0]))
            return

        # Add new rule
        userInput = input("Enter a new rule. Append '*' to show matches: ")
        userInput = userInput.lower()

        # Process new rule
        process_input(userInput, current_wordlength)

        # Update and optionally show matches
        showMatches = userInput[-1] == "*"
        current_wordlist = check_matches(current_wordlist, current_wordlength)
        print("Matching Words ({})".format(len(current_wordlist)))
        if showMatches:
            for match in current_wordlist:
                print("-", match.lower())

if __name__ == "__main__":
    main()
        

