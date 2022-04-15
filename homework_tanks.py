import random

class Gun:
     
    def __init__(self, calibеr: int, barrel_lenght: int, dice: int) -> None:
        self.caliber = calibеr
        self.barrel_lenght = barrel_lenght

    
    def is_on_target(self, dice: int) -> bool:
        dice = random.randint(1, 6)
        return True if dice * self.barrel_lenght > 100 else False


class Ammo:
    
    def __init__(self, gun: Gun, type: str) -> None:
        self.gun = gun
        self.type = type

    def get_damage(self):
        damage = self.caliber * 3
        return damage
    

    def get_penetration(self):
        penetration = self.caliber
        return penetration


class HECartidge(Ammo):
    super().get_damage()


class HEATCartridge(Ammo):
    super().get_damage() * 0.6


class APCartridge(Ammo):
    super().get_damage() * 0.3


class Armour:
    def __init__(self, thickness: int, type: str) -> None:
        self.thickness = thickness
        self.type = type

    def is_penetrated(self, cartridge) -> bool:
        self.cartridge = cartridge
        return True if self.cartridge.get_damage() > self.thickness else False


class HArmour(Armour):
    def is_penetrated(self, cartridge) -> bool:
        if self.cartridge == 'HE':
            return True if self.cartridge.get_damage() > self.thickness * 1.2 else False
        elif self.cartridge == 'HEAT':
            return super().is_penetrated(cartridge)
        elif self.cartridge == 'AP':
            return True if self.cartridge.get_damage() > self.thickness * 0.7 else False