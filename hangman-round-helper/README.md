# Hangman Round Helper

Build a few small functions that power a Hangman-style game.

**Complete these functions in `main.py`:**

- `choose_secret_word(words, seed)`
- `build_masked_word(secret_word, guessed_letters)`
- `is_round_won(secret_word, guessed_letters)`

## Requirements

### `choose_secret_word(words, seed)`

Pick and return one word from the `words` list.

- Use Python's [`random`](https://docs.python.org/3/library/random.html) module
- Use the given `seed` so the result is predictable for testing
- If `words` is empty, return `""`

> `random.seed(seed)` resets the random generator so the same seed gives the same result.

### `build_masked_word(secret_word, guessed_letters)`

Return the current visible version of the word.

Rules:

- Show guessed letters
- Show `_` for letters that have not been guessed yet
- Separate each character with a single space
- Reveal every copy of a guessed letter

Example:

```py
secret_word = "banana"
guessed_letters = ["a", "n"]

print(build_masked_word(secret_word, guessed_letters))
# _ a n a n a
```

### `is_round_won(secret_word, guessed_letters)`

Return `True` if every letter in `secret_word` has been guessed. Otherwise return `False`.

- Repeated letters only need to be guessed once
- If the word is empty, return `True`

## Notes

- Use functions, loops, and lists
- Do not print anything from `main.py`
- `main.py` should only define functions and values