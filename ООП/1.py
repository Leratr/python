class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print("Поприветсвуйте героя ->", self.name)
        print("Уровень здоровья:", self.health)
        print("Класс брони:", self.armor)
        print("Сила удара:", self.power)
        print("Оружие:", self.weapon)

    def strike(self, enemy):
        print("-> УДАР! " + self.name + " атакует " + enemy.name + " с силой " + str(self.power) + ", используя " + self.weapon + "\n")
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + " покачнулся(-ась).\nКласс брони упал до " + str(enemy.armor) + ", а уровень здоровья до " + str(enemy.health) + "\n")

knight = Hero("Ричард", 50, 25, 20, "меч")
knight.print_info()
rasca1 = Hero("Хелен", 20, 5, 5, "лук")
rasca1.print_info()
knight.strike(rasca1)
