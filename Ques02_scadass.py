
def calculate_bmi(weight, height_cm):
    """
    Calculates Body Mass Index (BMI) using weight (kg) and height (cm).
    Returns the BMI rounded to 2 decimal places.
    """
    height_m = height_cm / 100  
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def suggest_plan(bmi):
    if bmi < 18.5:
        return ("Workout: Light walking or yoga (20 mins)", "Diet: Eat more — rice, nuts, milk")
    elif 18.5 <= bmi < 24.9:
        return ("Workout: Brisk walk or cycling (30 mins)", "Diet: Balanced meals — fruits, veggies, meat")
    elif 25 <= bmi < 29.9:
        return ("Workout: Fast walking or jogging (45 mins)", "Diet: Eat less sugar, more fiber")
    else:
        return ("Workout: Intense workout or gym (60 mins)", "Diet: Low-fat food, avoid junk")
    
def test_calculate_bmi_normal_case():
    assert calculate_bmi(70, 175) == 22.86

def test_calculate_bmi_underweight():
    assert calculate_bmi(45, 160) == 17.58

def test_calculate_bmi_overweight():
    assert calculate_bmi(75, 165) == 27.55

def test_calculate_bmi_obese():
    assert calculate_bmi(95, 160) == 37.11

def test_suggest_plan_underweight():
    workout, diet = suggest_plan(17.0)
    assert "Light" in workout
    assert "Eat more" in diet

def test_suggest_plan_normal():
    workout, diet = suggest_plan(22.0)
    assert "Brisk" in workout
    assert "Balanced" in diet

def test_suggest_plan_overweight():
    workout, diet = suggest_plan(27.0)
    assert "Fast" in workout
    assert "fiber" in diet

def test_suggest_plan_obese():
    workout, diet = suggest_plan(32.0)
    assert "Intense" in workout
    assert "Low-fat" in diet
