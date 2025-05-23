# Character-Generator Etot proyekt predstavlyayet soboy skript na Python, kotoryy generiruyet HTML-stranitsy s opisaniyami sluchaynykh personazhey dlya fenteziynoy rolevoy igry. On ispol'zuyet biblioteki `faker`, `jinja2`, `unicodedata`, `os`, `shutil` dlya sozdaniya i stilizatsii kontenta. ## Kak ustanovit' Dlya raboty s etim proyektom potrebuyutsya sleduyushchiye biblioteki: * [Faker](https://faker.readthedocs.io/): Dlya generatsii sluchaynykh imen i drugikh dannykh. * [Jinja2](https://jinja.palletsprojects.com/): Dlya sozdaniya HTML-shablonov i renderinga. * [Unicodedata](https://docs.python.org/3/library/unicodedata.html): Dlya obrabotki Unicode simvolov. * [shutil](https://docs.python.org/3/library/shutil.html): Dlya operatsiy s faylami i direktoriyami. Vy mozhete ustanovit' neobkhodimyye zavisimosti s pomoshch'yu `pip`: ``` pip install -r requirements.txt ``` ## Kak ispol'zovat' 1. **Ustanovite zavisimosti:** Ubedites', chto vse neobkhodimyye biblioteki ustanovleny s pomoshch'yu `pip`. 2. **Zapustite skript:** ``` python main.py ``` Skript zaprosit u vas, skol'ko personazhey nuzhno sozdat'. Posle vvoda chisla i nazhatiya Enter, skript sozdast ukazannoye kolichestvo HTML-faylov s opisaniyami personazhey v papke `characters`. ## Primer Posle zapuska skripta i vvoda chisla, naprimer, 3, budut sozdany tri HTML-fayla: * `characters/character_1.html` * `characters/character_2.html` * `characters/character_3.html` Kazhdyy fayl budet soderzhat' HTML-stranitsu s opisaniyem odnogo sgenerirovannogo personazha. Pri otkrytii etikh faylov v brauzere budet otobrazhena informatsiya o personazhe (imya, rasa, klass, kharakteristiki, navyki) s sootvetstvuyushchim izobrazheniyem.
1 656 / 5 000
# Character-Generator
This project is a Python script that generates HTML pages with descriptions of random characters for a fantasy role-playing game. It uses `faker`, `jinja2`, `unicodedata`, `os`, `shutil` libraries for content creation and styling.
## How to install
To work with this project, you will need the following libraries:
* [Faker](https://faker.readthedocs.io/): For generating random names and other data.
* [Jinja2](https://jinja.palletsprojects.com/): For creating HTML templates and rendering.
* [Unicodedata](https://docs.python.org/3/library/unicodedata.html): For handling Unicode characters.
* [shutil](https://docs.python.org/3/library/shutil.html): For file and directory operations.
You can install the required dependencies with `pip`:
```
pip install -r requirements.txt
```
## How to use
1. **Install dependencies:**
Make sure all required libraries are installed with `pip`.
2. **Run the script:**
```
python main.py
```
The script will ask you how many characters to create. After entering the number and pressing Enter, the script will create the specified number of HTML files with character descriptions in the `characters` folder.
## Example
After running the script and entering a number, for example, 3, three HTML files will be created:
* `characters/character_1.html`
* `characters/character_2.html`
* `characters/character_3.html`
Each file will contain an HTML page with a description of one generated character. When you open these files in your browser, the character information (name, race, class, stats, skills) will be displayed with a corresponding image.
