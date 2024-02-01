def grade(score):
    if score <= 100 and score >= 80:
        return "Your Grade is A 👨‍🎓"
    elif score < 80 and score >=71:
        return "Your Grade is B 👨‍🎓"
    elif score < 71 and score >=61 :
        return "Yur Grade is C 👨‍🎓" 
    elif score < 61 and score >=50:
        return "Your Grade is D 👨‍🎓"
    else:
        return "Your Grade is F 👨‍🎓"