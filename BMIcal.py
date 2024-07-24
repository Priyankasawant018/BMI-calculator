def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms (kg)
    and height in meters (m).
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value and provide a corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    print("-----------------------------")

    # Input weight in kilograms
    weight = float(input("Enter your weight in kilograms (kg): "))

    # Input height in meters
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    bmi_category = interpret_bmi(bmi)

    # Print results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"This means you are: {bmi_category}")

if __name__ == "__main__":
    main()
