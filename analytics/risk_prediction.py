def calculate_risk(age, heart_rate, blood_pressure, glucose_level):

    risk_score = 0

    if age > 60:
        risk_score += 2

    if heart_rate > 120:
        risk_score += 2

    if blood_pressure > 160:
        risk_score += 2

    if glucose_level > 180:
        risk_score += 2

    if risk_score >= 5:
        return "HIGH"

    elif risk_score >= 3:
        return "MEDIUM"

    else:
        return "LOW"