def check_right_triangle():
    print("--- Right-Angled Triangle Calculator ---")
    print("Enter any two interior angles of the triangle in degrees.\n")
    
    try:
        angle1 = float(input("Enter the first angle: "))
        angle2 = float(input("Enter the second angle: "))
        
        # Validate that inputs form a valid pair of angles in a triangle
        if angle1 <= 0 or angle2 <= 0:
            print("Error: Angles must be positive numbers greater than 0.")
            return
        
        if angle1 + angle2 >= 180:
            print("Error: The sum of two angles in a triangle must be less than 180 degrees.")
            return
        
        # Calculate the third angle (sum of angles in a triangle = 180°)
        angle3 = 180.0 - (angle1 + angle2)
        
        print(f"\nCalculated Third Angle: {angle3:.2f}°")
        
        # Check if any of the three angles equals 90 degrees
        # (using standard tolerance for potential floating-point inputs)
        if abs(angle1 - 90) < 1e-6 or abs(angle2 - 90) < 1e-6 or abs(angle3 - 90) < 1e-6:
            print("Result: Yes, this IS a right-angled triangle! 📐")
        else:
            print("Result: No, this is NOT a right-angled triangle.")
            
    except ValueError:
        print("Error: Please enter valid numerical values.")

# Run the calculator
check_right_triangle()