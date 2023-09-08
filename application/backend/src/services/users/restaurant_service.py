from ...schemas.users.restaurant_schema import RestaurantSchema

def add_restaurant(restaurant):
    new_restaurant = RestaurantSchema(**restaurant)
    return new_restaurant
