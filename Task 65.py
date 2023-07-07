class GameCharacter:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def damage(self, summ):
        self.health -= summ
        if self.health < 0:
            self.health = 0

    def increase_level(self):
        self.level += 1
        self.attack *= 1.1
        self.health *= 1.1


batman = GameCharacter('Batman', 29, 890, 99, 60)
joker = GameCharacter('Joker', 25, 760, 106, 30)

for round_num in range(1, 4):
    print(f"Бой {round_num}")
    damage1 = batman.attack - joker.defense
    if damage1 < 0:
        damage1 = 0
    joker.damage(damage1)
    print(f"{batman.name} нападает на {joker.name} и наносит {damage1} единиц урона")
    damage2 = joker.attack - batman.defense
    if damage2 < 0:
        damage2 = 0
    batman.damage(damage2)
    print(f"{joker.name} внезапно наносит удар {batman.name} силой в {damage2} единиц урона")

if batman.health > joker.health:
    print(f"Победил: {batman.name}")
    print(f"Проиграл: {joker.name}")
elif joker.health > batman.health:
    print(f"Победил: {joker.name}")
    print(f"Проиграл: {batman.name}")
else:
    print("Бой закончился ничьей")