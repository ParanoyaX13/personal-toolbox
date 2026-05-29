from random import choice

def get_weather():
    """Simple weather simulator for different cities"""
    print("\n--- Weather Simulator ---")
    cities = ["Tehran", "Mashhad", "Isfahan", "Shiraz", "Tabriz", "New York", "London", "Tokyo"]
    
    city = input(f"Enter city name (or press Enter for random): ") or choice(cities)
    
    conditions = ["Sunny", "Cloudy", "Rainy", "Thunderstorm", "Snowy", "Windy", "Clear"]
    temperatures = range(-10, 45)
    
    temp = choice(list(temperatures))
    condition = choice(conditions)
    
    print(f"\n🌤️ Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {condition}")
    
    if temp > 30:
        print("🔥 It's very hot! Stay hydrated.")
    elif temp < 0:
        print("❄️ It's freezing! Wear warm clothes.")
    elif condition == "Rainy":
        print("☔ Don't forget your umbrella!")

if __name__ == "__main__":
    get_weather()
