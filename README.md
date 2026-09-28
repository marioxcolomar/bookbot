# BookBot

BookBot is a simple way of counting character in text files. Store the text files in the books directory and use the path when running the program.

## Quick start
For future testing or adding more functionality you can add the text files in the `/books` directory. For now you can use the following command for getting your first text file:
`mkdir -p books && curl -L "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt" -o books/frankenstein.txt`

For running the program simple use python run time:
`python3 main.py books/frankenstein.txt`
