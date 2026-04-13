import requests

# Configuration de l'API OpenWeatherMap
API_KEY = "a5bf2e76ce5142d5330ae3791d91c299"   # clé API récupéré depuis le site openweather
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_meteo(ville):
    """
    Envoie une requête GET à l'API openweathermap
    et retourne les données météo de la ville demandée.
    """
    # Paramètres de la requête
    params = {
        "q": ville,          # Nom de la ville
        "appid": API_KEY,    # Clé d'authentification
        "units": "metric",   # Température en Celsius
        "lang": "fr"         # Descriptions en français
    }

    # Envoi de la requête HTTP GET
    response = requests.get(BASE_URL, params=params)

    # Vérification du code de statut HTTP
    if response.status_code == 200:
        # Succès : on retourne les données JSON
        return response.json()
    elif response.status_code == 404:
        print(f"Ville '{ville}' introuvable.")
        return None
    elif response.status_code == 401:
        print("Clé API invalide ou non activée.")
        return None
    else:
        print(f"Erreur HTTP {response.status_code}")
        return None


def afficher_meteo(data):
    """
    Affiche les informations météo de manière lisible
    à partir du JSON retourné par l'API.
    """
    ville       = data["name"]
    pays        = data["sys"]["country"]
    description = data["weather"][0]["description"]
    temp        = data["main"]["temp"]
    temp_min    = data["main"]["temp_min"]
    temp_max    = data["main"]["temp_max"]
    humidite    = data["main"]["humidity"]
    vent        = data["wind"]["speed"]

    print("\n" + "="*40)
    print(f"  Météo à {ville} ({pays})")
    print("="*40)
    print(f"  Description  : {description.capitalize()}")
    print(f"  Température  : {temp}°C")
    print(f"  Min / Max    : {temp_min}°C / {temp_max}°C")
    print(f"  Humidité     : {humidite}%")
    print(f"  Vent         : {vent} m/s")
    print("="*40 + "\n")



if __name__ == "__main__":
    print("=== Client Météo OpenWeatherMap ===")
    
    # L'utilisateur saisit le nom de la ville
    ville = input("Entrez le nom d'une ville : ").strip()
    
    if not ville:
        print("Veuillez entrer un nom de ville valide.")
    else:
        # Appel à l'API
        donnees = get_meteo(ville)
        
        # Affichage du résultat si la requête a réussi
        if donnees:
            afficher_meteo(donnees)