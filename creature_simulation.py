class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")

if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== SwimmingCreature Tests ===\n")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {serpent.depth}")

    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    print(f"Dummy HP should be 33 → Actual: {dummy.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    # ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    MIN_FIRE = 0
    MAX_FIRE = 100

    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = self._clamp_fire(fire_level)

    def _clamp_fire(self, level):
        # Keep fire_level inside 0-100
        return max(self.MIN_FIRE, min(self.MAX_FIRE, level))

    def emit_fire(self, new_fire_level):
        clamped = self._clamp_fire(new_fire_level)
        if clamped != new_fire_level:
            print(f"Fire level {new_fire_level} is out of range (0-100). Using {clamped}.")
        self.fire_level = clamped
        print(f"{self.name} emits fire! Fire level is now {self.fire_level}.")

    def fire_damage(self):
        # Every 10 points of fire_level adds 1 bonus damage (max +10)
        return self.fire_level // 10

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        bonus = self.fire_damage()
        total_damage = self.attack_power + bonus
        print(f"{self.name} breathes fire at level {self.fire_level}!")
        print(f"It burns {target.name} for {self.attack_power} + {bonus} fire = {total_damage} damage!")
        target.hp -= total_damage
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")

if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

   #test1
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)
    print()