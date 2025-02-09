import requests

# URLs de los microservicios
AUTH_USERS_URL = "http://18.205.183.111:3001/users"
RESERVATIONS_URL = "http://52.3.161.90:3101/reservations"
RESTAURANTS_URL = "http://44.198.236.2:5002/restaurants"

def user_exists(user_id):
    """ Verifica si el usuario existe en el microservicio de autenticación """
    try:
        response = requests.get(f"{AUTH_USERS_URL}/{user_id}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error verificando usuario: {e}")
        return False

def reservation_exists(reservation_id):
    """ Verifica si la reserva existe en el microservicio de reservas """
    try:
        response = requests.get(f"{RESERVATIONS_URL}/{reservation_id}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error verificando reserva: {e}")
        return False  

def restaurant_exists(restaurant_id):
    """ Verifica si el restaurante existe en el microservicio de restaurantes """
    try:
        response = requests.get(f"{RESTAURANTS_URL}/{restaurant_id}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error verificando restaurante: {e}")
        return False
