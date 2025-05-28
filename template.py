import os
import random
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape


def choose_character_option(list_options, character_input, clases_base=None):
    while True:
        str_options = '\n'.join(f"{num + 1}. {option}" for num, option in enumerate(list_options))
        user_input = input(f"{character_input}\n{str_options}\nВведите номер или название: ")
        chosen_option = None
        characteristics = None

        try:
            index = int(user_input) - 1
            if 0 <= index < len(list_options):
                chosen_option = list_options[index]
                if clases_base:
                    characteristics = clases_base.get(chosen_option, {})
                break
            else:
                print("Неверный номер. Попробуйте еще раз.")

        except ValueError:
            input_lower = user_input.strip().lower()
            correspondence = False
            for option in list_options:
                if option.strip().lower() == input_lower:
                    chosen_option = option
                    if clases_base:
                        characteristics = clases_base.get(option, {})
                    correspondence = True
                    break
            if correspondence:
                break
            else:
                print("Расса или класс не найдена. Попробуйте еще раз.")
    return chosen_option, characteristics


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

        character_race, _ = choose_character_option(
            character_race,
            "Выберите расу персонажа из предложенных: ",
        )

        character_class, class_characteristics = choose_character_option(
            character_classes,
            "Выберите класс персонажа из предложенных: ",
            clases_base
        )

        selected_skills = random.sample(skills, 3)

        dictionary = {
            "image_path": class_characteristics['image_path'],
            "name": hero_name.capitalize(),
            "character_race": character_race,
            "character_class": character_class,
            "strength": class_characteristics['strength'],
            "agility": class_characteristics['agility'],
            "intelligence": class_characteristics['intelligence'],
            "luck": class_characteristics['luck'],
            "temper": class_characteristics['temper'],
            "skill_1": selected_skills[0],
            "skill_2": selected_skills[1],
            "skill_3": selected_skills[2],
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
