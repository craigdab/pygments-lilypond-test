# pygments-LilyPond-lexer

A LilyPond lexer for Pygments to highlight LilyPond code snippets.

## To test the lexer:

1. Clone the pygments repo: [https://github.com/pygments/pygments]

2. Copy the `lilypond.py` and the `_lilypond_builtins.py` files to the `pygments/pygments/lexer` folder.

3. Add any LilyPond file you like to the `pygments/tests/examplefiles` folder. Call the file `example.ily`. Make sure it has an `.ily` suffix. If you want you can add a second file, `example.ly`, with a `.ly` suffix. Just change the file extension to `.ly` in step 5.

4. Change to the `pygments` folder: `cd pygments` folder

5. Run the lexer to convert the LilyPond file to html: ```
python -m pygments -O full -f html -o /tmp/example.html tests/examplefiles/example.ily```

6. Open the `html` file: `/tmp/example.html`
