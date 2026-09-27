print("Приветствую воин, как тебя зовут?")
username = input().title()
import time
import random
print("Приятно познакомиться",username)
time.sleep(2)
print("Давай начнём наше приключение")
import time
time.sleep(2)
print("Выбери класс своего героя: Лучник, Варвар, Маг.")
class_hero = input().title()
if class_hero == 'Лучник':
    intellect = 6
    power = 4
    dexterity = 12
    level = 1
elif class_hero == 'Варвар':
    intellect = 3
    power = 12
    dexterity = 6
    level = 1
elif class_hero == 'Маг':
    intellect = 12
    power = 6
    dexterity = 2
    level = 1
print("Ты выбрал класс", class_hero, "хороший выбор!")
time.sleep(2)
print("Ты появился в рыбацкой деревне, пора порубить парочку троллей!")
time.sleep(2)
print("Ты отправился к заброшенному колодцу неподалёку от деревни")
time.sleep(2)
print("Перед тобой появился противник - злой тролль 1-го уровня")
time.sleep(2)
print("Сразишься с ним? Да/Нет")
decision = input().title()
throll_1_intellect = random.randint(1,2)
throll_1_power = random.randint(4,8)
throll_1_dexterity = random.randint(1,4)
if decision == 'Да':
    print("Началось сражение!")
    time.sleep(2)
    if power > throll_1_power:
        print("Ты победил и получаешь +1 к своим статистикам и новый уровень!")
        intellect = intellect + 1
        power = power + 1
        dexterity = dexterity + 1
        level = level + 1
        print(f"Твои новые показатели: \nИнтеллект {intellect} \nСила {power}\nЛовкость {dexterity} \nУровень {level}")
    else:
        print("Ты проиграл, тебе надо улучшить свои навыки!")
if level == 2:
    time.sleep(2)
    print("Ты продолжаешь свой поход против нечисти!")
    time.sleep(2)
    print("Ты дошёл до колодца, который охраняет Гидра!")
    time.sleep(2)
print("Дашь ли ты бой? Да/Нет")
hydra_1_intellect = random.randint(1,4)
hydra_1_power = random.randint(6,12)
hydra_1_dexterity = random.randint(4,7)
answer1 = input().title()
if answer1 == 'Да':
    print("Ты вступаешь в бой с Гидрой!")
    time.sleep(2)
    if power > hydra_1_power:
        print("Ты победил и получаешь +1 к своим статистикам и новый уровень!")
        intellect = intellect + 1
        power = power + 1
        dexterity = dexterity + 1
        level = level + 1
        print(f"Твои новые показатели: \nИнтеллект {intellect} \nСила {power}\nЛовкость {dexterity} \nУровень {level}")
    else:
        print("Ты проиграл, тебе надо улучшить свои навыки!")

    