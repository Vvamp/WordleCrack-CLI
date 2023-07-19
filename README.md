<!-- Project Badges-->
![Contributors Badge](https://img.shields.io/github/contributors/Vvamp/WordleCrack-CLI.svg?)
![Forks Badge](https://img.shields.io/github/forks/Vvamp/WordleCrack-CLI.svg?)
![Stars Badge](https://img.shields.io/github/stars/Vvamp/WordleCrack-CLI.svg?)
![Issues Badge](https://img.shields.io/github/issues/Vvamp/WordleCrack-CLI.svg?)
![License Badge](https://img.shields.io/github/license/Vvamp/WordleCrack-CLI.svg?)
# WordleCrack-CLI

Hello there! Welcome to WordleCrack-CLI, a simple Python tool to assist in solving Wordle. 

WordleCrack-CLI helps you to whittle down the list of possible words in a Wordle game using simple syntax commands. The idea is to narrow down the potential words based on information from the game, like known letters and their positions.

## How to Use

**Prerequisites:**

This tool requires Python. No additional dependencies are needed.

**Steps:**

1. Download a dictionary text file from the internet. The text file should contain one word per line.

2. Clone this repository or download the source code.

3. Run `main.py` from your terminal or command line. You can do this by navigating to the directory where `main.py` is located and typing `python main.py`.

4. When prompted, provide the path to your dictionary text file and the length of the Wordle word.

## Command Syntax

This program uses a specific syntax to handle user input and process the Wordle clues. Here is an explanation of the command syntax:

- `+A` : Add `A` to the letter whitelist. The word has to contain this letter.
- `-A` : Add `A` to the letter blacklist. The word does not contain this letter.
- `1A` : Add `A` to the list of single occurrences. The letter `A` can occur only once in the word.
- `.+1A`: Add `A` to the position whitelist for position 1. The letter `A` has to be in that position.
- `.-1A`: Add `A` to the position blacklist for position 1. The letter `A` cannot be in that position.

**Notes:**

- The letter in your command should be alphabetic, non-alphabetic characters are already excluded.
- For positional rules, the position of the character starts from zero (0). So a word of 5 characters has the positions 0 to 4.
- Ensure the word length is set correctly at the start and make sure you are indexing from 0 (the first letter is position '0').

## Example

Let's assume that we know that the word has the letter 'A' in the second position, doesn't have the letter 'B', and 'C' occurs only once. Here are the commands we would use:

```
.+1A (The letter A has to be in the second position)
-B (Letter B doesn't occur)
+C (Letter C is in the word at an unknown location)
1C (Letter C occurs only once)
```

After entering these commands, you can append (or simply write) an asterisk `*` to get a list of the possible words based on your inputs.

## Dictionary
This project does not contain any dictionaries, you have to provide your own. There are endless of these files on the internet. 
Just make sure that for this project, the file is a simple text file with a single word per line.

For convenience, [here is a github project with English dictionaries](https://github.com/dwyl/english-words). I recommend using the 'words_alpha.txt'.

## Contribution

Feel free to contribute to this project by creating issues or pull requests. Any feedback is welcome.

## License

WordleCrack-CLI is [MIT licensed](./LICENSE).
