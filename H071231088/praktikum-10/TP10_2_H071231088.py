from abc import ABC, abstractmethod

# Abstract class dengan konsep encapsulation
class Hero(ABC):
    def __init__(self, nama, role, suara):
        self._nama = nama
        self._role = role
        self._suara = suara

    @property
    def nama(self):
        return self._nama

    @property
    def role(self):
        return self._role

    @property
    def suara(self):
        return self._suara

    @abstractmethod
    def skill_utama(self):
        pass

    def bersuara(self):
        return f"{self._nama} bersuara: {self._suara}"

# Kelas hero Marksman
class Marksman(Hero):
    def skill_utama(self):
        return f"{self._nama} memberikan: 'Kritikal damage!'"

# Kelas hero Mage
class Mage(Hero):
    def skill_utama(self):
        return f"{self._nama} memberikan: 'magic damage!'"

# Kelas hero Support
class Support(Hero):
    def skill_utama(self):
        return f"{self._nama} memberikan: 'Healing Wave!'"

# Kelas hero Fighter
class Fighter(Hero):
    def skill_utama(self):
        return f"{self._nama} memberikan: 'true damage!'"

# Kelas hero Tank
class Tank(Hero):
    def skill_utama(self):
        return f"{self._nama} memberikan : 'shield'"

# Kelas role Marksman
class MarksmanRole:
    heroes = [
        Marksman("Layla", "Marksman", "Meow!"),
        Marksman("Miya", "Marksman", "Arrow shot!"),
        Marksman("Clint", "Marksman", "Reload and fire!")
    ]

# Kelas role Mage
class MageRole:
    heroes = [
        Mage("Cyclops", "Mage", "Zap!"),
        Mage("Lylia", "Mage", "Dark Energy Burst!"),
        Mage("Kagura", "Mage", "Seimei Umbrella!")
    ]

# Kelas role Support
class SupportRole:
    heroes = [
        Support("Angela", "Support", "Love waves!"),
        Support("Estes", "Support", "Healing Light!"),
        Support("Diggie", "Support", "Time Journey!")
    ]

# Kelas role Fighter
class FighterRole:
    heroes = [
        Fighter("Aldous", "Fighter", "Unstoppable Force!"),
        Fighter("Leomord", "Fighter", "Phantom Steed!"),
        Fighter("Chou", "Fighter", "Jeet Kune Do!")
    ]

# Kelas role Tank
class TankRole:
    heroes = [
        Tank("Grock", "Tank", "Growl!"),
        Tank("Johnson", "Tank", "Full Throttle!"),
        Tank("Hylos", "Tank", "Ring of Punishment!")
    ]

# Pemilihan role
def pemilihan_role():
    print("Selamat datang di Mobile Legends! Silakan pilih role:")
    print("1. Marksman")
    print("2. Mage")
    print("3. Support")
    print("4. Fighter")
    print("5. Tank")

    pilihan_role = int(input("Masukkan nomor role yang ingin Anda pilih (1-5): "))

    roles = [MarksmanRole, MageRole, SupportRole, FighterRole, TankRole]
    if 1 <= pilihan_role <= len(roles):
        return roles[pilihan_role - 1]
    else:
        print("Pilihan tidak valid. Silakan pilih nomor role yang benar.")
        return None

# Pemilihan hero dengan konsep polymorphism
def pemilihan_hero(role):
    print(f"Silakan pilih hero dari role {role.__name__}:")
    
    for idx, hero in enumerate(role.heroes, start=1):
        print(f"{idx}. {hero.nama}")

    pilihan = int(input("Masukkan nomor hero yang ingin Anda pilih (1-3): "))

    if 1 <= pilihan <= 3:
        selected_hero = role.heroes[pilihan - 1]
        print(f"Anda memilih hero {selected_hero.nama} dengan role {selected_hero.role}")
        print(f"{selected_hero.skill_utama()}")
        print(selected_hero.bersuara())

    else:
        print("Pilihan tidak valid. Silakan pilih nomor hero yang benar.")


# Memanggil fungsi pemilihan_role untuk memilih role
selected_role = pemilihan_role()

# Jika role valid dipilih, lanjutkan dengan pemilihan hero
if selected_role:
    pemilihan_hero(selected_role)
