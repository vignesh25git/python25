feedback = input("Enter the feedback")

with open("feedback.txt","a") as file:
    file.write(feedback + "\nE")

print("Feedback saved Thanks!!!")