import os
import random
import unicodedata
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape


def remove_diacritics(text):
    normalized_text = unicodedata.normalize('NFD', text)
    return ''.join(norm_text for norm_text in normalized_text if unicodedata.category(norm_text) != 'Mn')


def replace_letters(text, mapping):
    for letter, rune in mapping.items():
        text = text.replace(letter, rune)
    return text


def string_comparison(input_word, list_options, mapping):
    normalized_word = input_word.replace(' ', '').lower()

    for word in list_options:
        if word.replace(' ', '').lower() == normalized_word:
            print(word)
            runic_word = replace_letters(word, mapping)
            break
    else:
        print("Раса не найдена.") 

    return runic_word



def choose_character_option(list_options, character_input, letters, clases_base=None):
    while True:
        str_options = '\n'.join(f"{num + 1}. {option}" for num, option in enumerate(list_options))
        user_input = input(f"{character_input}\n{str_options}\nВведите номер или название: ")
        runic_option = None
        characteristics = None

        try:
            index = int(user_input) - 1
            if 0 <= index < len(list_options):
                chosen_option = list_options[index]
                runic_option = replace_letters(chosen_option, letters)
                if clases_base:
                    characteristics = clases_base.get(chosen_option, {})
                break
            else:
                print("Неверный номер. Попробуйте еще раз.")

        except ValueError:
            input_lower = user_input.replace(' ', '').lower()
            correspondence = False
            for option in list_options:
                if option.replace(' ', '').lower() == input_lower:
                    runic_option = replace_letters(option, letters)
                    if clases_base:
                        characteristics = clases_base.get(option, {})
                    correspondence = True
                    break
            if correspondence:
                break
            else:
                print("Расса или класс не найдена. Попробуйте еще раз.")
    return runic_option, characteristics


def main():
    characters_folder = 'characters'
    if os.path.exists(characters_folder):
        shutil.rmtree(characters_folder)
    os.makedirs(characters_folder)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    letters = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '
    }

    skills = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд",
    ]

    character_race = [
        'Лунные эльфы',
        'Огненные гномы',
        'Теневые вампиры',
        'Ледяные драконы',
        'Земные тролли',
        'Водяные нимфы',
        'Светлые ангелы',
        'Древесные духи',
        'Магические зверолюди',
        'Звёздные маги',
    ]

    character_classes = [
        'Маг',
        'Воин',
        'Охотник',
        'Ассасин',
        'Бард',
    ]

    clases_base = {
        'Маг': {
            'intelligence': 15,
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image_path': '../images/wizard.png',
        },
        'Воин': {
            'strength': 15,
            'intelligence': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image_path': '../images/warrior.png',
        },
        'Охотник': {
            'agility': 15,
            'strength': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image_path': '../images/archer.png',
        },
        'Ассасин': {
            'luck': 15,
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image_path': '../images/assasin.png',
        },
        'Бард': {
            'temper': 15,
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'image_path': '../images/bard.webp',
        },
    }

    count_heroes = int(input("Сколько персонажей нужно создать? (напишите цифрой): "))

    for number_heroes in range(count_heroes):
        hero_name = input("\nВведите имя персонажа: ")
        runic_name = replace_letters(hero_name, letters)

        runic_race, _ = choose_character_option(
            character_race,
            "Выберите расу персонажа из предложенных: ",
            letters
        )

        runic_class, class_characteristics = choose_character_option(
            character_classes,
            "Выберите класс персонажа из предложенных: ",
            letters,
            clases_base
        )

        selected_skills = random.sample(skills, 3)
        runic_skills = [replace_letters(skill, letters) for skill in selected_skills]

        dictionary = {
            "image_path": class_characteristics['image_path'],
            "name": runic_name.capitalize(),
            "character_race": runic_race,
            "character_class": runic_class,
            "strength": class_characteristics['strength'],
            "agility": class_characteristics['agility'],
            "intelligence": class_characteristics['intelligence'],
            "luck": class_characteristics['luck'],
            "temper": class_characteristics['temper'],
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2],
        }

        rendered_page = template.render(
            image=dictionary['image_path'],
            name=dictionary['name'],
            race=dictionary['character_race'],
            character_class=dictionary['character_class'],
            strength=dictionary['strength'],
            agility=dictionary['agility'],
            intelligence=dictionary['intelligence'],
            luck=dictionary['luck'],
            temper=dictionary['temper'],
            first_skill=dictionary['skill_1'],
            second_skill=dictionary['skill_2'],
            third_skill=dictionary['skill_3'],
        )

        filename = f"characters/character_{number_heroes+1}.html"
        with open(filename, 'w', encoding='utf8') as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()