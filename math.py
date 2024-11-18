import math


def math_questions():
    print("Math Quiz! Answer the following questions.")

    try:
        # Question 1: Area of a Circle
        print("\n1. What is the area of a circle with a radius of 5 meters? (Use π ≈ 3.14)")
        user_answer = float(input("Your answer (in m²): "))
        radius = 5
        correct_answer = math.pi * (radius ** 2)
        if math.isclose(user_answer, correct_answer, rel_tol=0.01):  # Allow small margin of error
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} m².")
            print("Working: Area = π * r² = 3.14 * 5² = 78.54 m².")

        # Question 2: Pythagoras Theorem
        print("\n2. If a triangle has sides 3 and 4, what is the hypotenuse?")
        user_answer = float(input("Your answer: "))
        side_a, side_b = 3, 4
        correct_answer = math.sqrt(side_a ** 2 + side_b ** 2)
        if math.isclose(user_answer, correct_answer, rel_tol=0.01):  # Allow small margin of error
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f}.")
            print("Working: Hypotenuse = √(a² + b²) = √(3² + 4²) = √(9 + 16) = 5.")

        # Question 3: Quadratic Equation
        print("\n3. Solve the quadratic equation: x² - 5x + 6 = 0. What are the roots?")
        user_answer = input("Your answer (in the form x1,x2): ")
        roots = [3, 2]  # Roots of the equation
        correct_answer = sorted(roots)
        user_roots = sorted([float(x.strip()) for x in user_answer.split(",")])
        if user_roots == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct roots are {correct_answer}.")
            print("Working: Solve x² - 5x + 6 = 0 using factorization: (x-3)(x-2) = 0, so roots are 3 and 2.")

        # Question 4: Simple Arithmetic
        print("\n4. What is the result of 15 + 25?")
        user_answer = float(input("Your answer: "))
        correct_answer = 15 + 25
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
            print("Working: 15 + 25 = 40.")

        # Question 5: Volume of a Cylinder
        print("\n5. What is the volume of a cylinder with a radius of 3 meters and height of 7 meters? (Use π ≈ 3.14)")
        user_answer = float(input("Your answer (in m³): "))
        radius = 3
        height = 7
        correct_answer = math.pi * (radius ** 2) * height
        if math.isclose(user_answer, correct_answer, rel_tol=0.01):  # Allow small margin of error
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer:.2f} m³.")
            print("Working: Volume = π * r² * h = 3.14 * 3² * 7 = 197.92 m³.")

    except ValueError:
        print("Invalid input. Please enter a numerical value.")


if __name__ == "__main__":
    math_questions()
