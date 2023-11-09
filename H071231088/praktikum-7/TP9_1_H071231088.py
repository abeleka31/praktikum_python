# kapala ini (nenek na)
class Human:
    def __init__(self, name):
        self.name = name
        self.__position = ""
        self.speed = ""

    def movement(self, arah):
        if arah == "L":
            self.__position = "Kiri"
        elif arah == "R":
            self.__position = "Kanan"

    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
    
    def setposition(self, position):
        self.__position = position
    def getposition(self):
        return self.__position
    
#hero mewarisi atribut dari human
# ini mamak na (ta gantung i ke nenek)

class Hero(Human):
    def __init__(self, name):
        super().__init__(name)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target.sethealth(target.gethealth()-self._power)
    
    def setpower(self, power):
        self._power = power
    def getpower(self):
        return self._power

    def sethealth(self, health):
        self._health = health
    def gethealth(self):
        return self._health
    
    def setarmor(self, armor):
        self._armor = armor
    def getarmor(self):
        return self._armor
    
    def setspeed(self, speed):
        self._speed = speed
    def getspeed(self):
        return self._speed

# ini anak pertamana

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._power = 32
        self._armor = 45
        target.sethealth(target.gethealth()-self._power)
    
    def setpower(self, power):
        return self.setpower(power)
    def getpower(self):
        return self.getpower()
    def setarmor(self, armor):
        return self.setarmor(armor)
    def getarmor(self):
        return self.getarmor()
    
    
# anak kedua 
class Asassin(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._power = 35
        self._speed = 4
    
    def special(self, target):
        self._power = 42
        self._speed = 7
        target.sethealth(target.gethealth() - self._power)
    def setpower(self, power):
        return super().setpower(power)
    def getpower(self):
        return super().getpower()
    def setspeed(self, speed):
        return super().setspeed(speed)
    def getspeed(self):
        return super().getspeed()

# anak ketiga
class Support(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target.sethealth(target.gethealth() + 150)
    def sethealth(self, health):
        return super().sethealth(health)
    def gethealth(self):
        return super().gethealth()
    def setarmor(self, armor):
        return super().setarmor(armor)
    def getarmor(self):
        return super().getarmor()
    def setspeed(self, speed):
        return super().setspeed(speed)
    def getspeed(self):
        return super().getspeed()
    


warrior = Warrior("Roby")
assassin = Asassin("Mufli")
support = Support("jar")


#sebelum
print("health (before):", warrior.gethealth())
assassin.attack(warrior)
#sesudah 
print("health (after):", warrior.gethealth())
print("-"*10)

#seblum 
print("warrior (health):", warrior.gethealth())
print("support (speed):", support.getspeed())

support.special(warrior)
print("warrior (health):", warrior.gethealth())
print("support (speed):", support.getspeed())


# Membuat objek Hero
hero = Hero("karina")

# Menggunakan metode movement pada objek Hero
hero.movement("L")  # Menggerakkan Hero ke kiri

# Mengakses posisi Hero
print("hero berpindah ke:", hero.getposition())  # Output: "Kiri"

# Menggunakan metode movement lagi untuk menggerakkan ke kanan
hero.movement("R")

# Mengakses posisi Hero setelah diubah
print("hero bergeser ke kanan", hero.getposition())  # Output: "Kanan"
