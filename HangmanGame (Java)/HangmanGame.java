import java.util.Scanner;

public class HangmanGame {

    public static void main(String[] args) {
        // List of words for the game
        String[] wordList = { "programming", "computer", "hangman", "technology", "java" };

        // Select a random word from the list
        int randomIndex = (int) (Math.random() * wordList.length);
        String selectedWord = wordList[randomIndex];

        // Initialize player progress
        StringBuilder playerProgress = new StringBuilder();
        for (int i = 0; i < selectedWord.length(); i++) {
            playerProgress.append("_ ");
        }

        int incorrectGuessesLeft = 6; // Number of incorrect guesses allowed

        Scanner scanner = new Scanner(System.in);

        // Game loop
        while (incorrectGuessesLeft > 0) {
            System.out.println("Welcome to Hangman!");
            System.out.println("Current word: " + playerProgress);
            System.out.println("Incorrect guesses left: " + incorrectGuessesLeft);

            System.out.print("Guess a letter: ");
            char guessedLetter = scanner.next().charAt(0);

            if (!Character.isLetter(guessedLetter)) {
                System.out.println("Invalid input. Please enter a letter.");
                continue; // Restart the loop
            }

            boolean letterFound = false;
            for (int i = 0; i < selectedWord.length(); i++) {
                if (selectedWord.charAt(i) == guessedLetter) {
                    letterFound = true;
                    playerProgress.setCharAt(i * 2, guessedLetter);
                }
            }

            if (!letterFound) {
                incorrectGuessesLeft--;
            }

            if (playerProgress.indexOf("_") == -1) {
                System.out.println("Congratulations! You guessed the word: " + selectedWord);
                break; // Exit the loop
            }

            if (incorrectGuessesLeft == 0) {
                System.out.println("Sorry, you ran out of guesses. The word was: " + selectedWord);
                break; // Exit the loop
            }
        }

        scanner.close();
    }
}
