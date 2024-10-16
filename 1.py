def performance(percentage):
    if percentage >= 90:
        return "Excelent Performance"
    elif percentage >= 80:
        return "Very Good Performance"
    elif percentage >= 70:
        return "Good Performance"
    elif percentage >= 60:
        return "Average Performance"
    else:
        return "Below Average Performance"

percentage = float(input("persentase: "))
print("Performance : ", performance(percentage))