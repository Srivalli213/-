# Task 4: Temperature Converter Program

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("🌡️  Temperature Converter 🌡️")
    print("1. Celsius ➡️ Fahrenheit")
    print("2. Fahrenheit ➡️ Celsius")
    
    choice = input("Choose conversion type (1 or 2): ")

    # Validate user choice
    if choice not in ['1', '2']:
        print("❌ Invalid choice. Please enter 1 or 2.")
        return

    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    if choice == '1':
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {converted:.2f}°F")
    else:
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {converted:.2f}°C")

if __name__ == "__main__":
    main()
