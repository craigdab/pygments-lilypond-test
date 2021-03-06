# pygments-LilyPond-lexer

A LilyPond lexer for Pygments to highlight LilyPond code snippets.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## To test the lexer:

1. Clone the pygments repo: [https://github.com/pygments/pygments]

2. Copy the `lilypond.py` and the `_lilypond_builtins.py` files to the `pygments/pygments/lexer` folder.

3. Add any LilyPond file you like to the `pygments/tests/examplefiles` folder. Call the file `example.ily`. Make sure it has an `.ily` suffix. If you want you can add a second file, `example.ly`, with a `.ly` suffix. Just change the file extension to `.ly` in step 5.

4. Change to the `pygments` folder: `cd pygments` folder

5. Run ```make mapfiles```

6. Run the lexer to convert the LilyPond file to html: ```
python -m pygments -O full -f html -o /tmp/example.html tests/examplefiles/example.ily```

7. Open the `html` file: `/tmp/example.html`


## Contribute

- Issue Tracker: github.com/craigdab/pygments-lilypond-test/issues
- Source Code: github.com/craigdab/pygments-lilypond-test

## Support

If you are having issues, please let me know at: craig.dabelstein@gmail.com

## License

The project is licensed under the GNU General Public License.
