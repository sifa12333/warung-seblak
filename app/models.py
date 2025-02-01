class MenuItem:
    def __init__(self, id, name, description, price, image):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image

menu_items = [
    MenuItem(1, 'Seblak Original', 'Lorem, deren, trataro, filede, nerada', 5.95, 'assets/img/menu/menu-item-1.png'),
    MenuItem(2, 'Seblak Telur', 'Lorem, deren, trataro, filede, nerada', 14.95, 'assets/img/menu/menu-item-2.png'),
]
