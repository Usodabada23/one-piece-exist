import TypeDevilFruit
class DevilFruit:

    name: str
    typeFruit: TypeDevilFruit
    description: str
    ability: str
    rarity: str
    is_eaten: bool

    def __init__(self,name: str,typeFruit: TypeDevilFruit,description: str,ability: str,rarity: str,is_eaten: bool):
        self.name = name
        self.typeFruit = typeFruit
        self.description = description
        self.ability = ability
        self.rarity = rarity
        self.is_eaten = is_eaten
    