# Character-Generator
This project is a Python script that generates HTML pages with descriptions of random characters for a fantasy role-playing game. It uses `faker`, `jinja2`, `unicodedata`, `os`, `shutil` libraries to create and style the content.
## How to install
To work with this project, you will need the following libraries:
* [Jinja2](https://jinja.palletsprojects.com/): For creating HTML templates and rendering.
* [Unicodedata](https://docs.python.org/3/library/unicodedata.html): For handling Unicode characters.
* [shutil](https://docs.python.org/3/library/shutil.html): For file and directory operations.
You can install required dependencies with `pip`:
```
pip install -r requirements.txt
```
## How to use
1. **Install dependencies:**
Make sure all required libraries are installed with `pip`.
2. **Run the script:**
```
python template.py
```
The script will ask you how many characters to create. After entering the number and pressing Enter, the script will create the specified number of HTML files with character descriptions in the `characters` folder.
## Example
After running the script and entering a number, for example, 3, three HTML files will be created:
* `characters/character_1.html`
* `characters/character_2.html`
* `characters/character_3.html`

Each file will contain an HTML page with a description of one generated character. When these files are opened in the browser, information about the character (name, race, class, stats, skills) will be displayed with a corresponding image.
