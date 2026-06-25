def evaluate_answer(answer):
    if len(answer) < 20:
        return "Poor"
    elif len(answer) < 100:
        return "Good"
    else:
        return "Excellent"