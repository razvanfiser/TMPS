# singleton class
# allows the existence of only one unique object of this class
class CarShop:
    def __new__(shop):
        if not hasattr(shop, 'instance'):
            shop.instance = super(CarShop, shop).__new__(shop)
        return shop.instance