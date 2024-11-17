import random

# Define workout options for each type of workout
workouts = {
    "cardio": ["Running", "Jumping Jacks", "Burpees", "Cycling", "Jump Rope", "High Knees"],
    "weightlifting": ["Squats", "Deadlifts", "Bench Press", "Overhead Press", "Rows", "Pull-ups"],
    "hiit": ["Mountain Climbers", "Sprint Intervals", "Box Jumps", "Plank Jacks", "Battle Ropes", "Jump Squats"]
}

def generate_workout(workout_type, rounds):
    workout_options = workouts.get(workout_type.lower())
    if not workout_options:
        print("Invalid workout type. Please choose from 'cardio', 'weightlifting', or 'HIIT'.")
        return None

    reps = calculate_reps(workout_type, rounds)

    workout_routine = []
    for i in range(rounds):
        random.shuffle(workout_options)  # Randomize workout order for each round
        workout_routine.append(f"Round {i+1}: {', '.join(workout_options)} ({reps})")

    return "\n".join(workout_routine)

def calculate_reps(workout_type, rounds):
    if rounds < 5:
        if workout_type.lower() == "cardio":
            return "40 reps"
        elif workout_type.lower() == "weightlifting":
            return "10-maxout reps"
        elif workout_type.lower() == "hiit":
            return "3-4 minutes"
    elif 5 <= rounds <= 9:
        if workout_type.lower() == "cardio":
            return "30 reps"
        elif workout_type.lower() == "weightlifting":
            return "6-8 reps"
        elif workout_type.lower() == "hiit":
            return "2-3 minutes"
    elif rounds > 9:
        if workout_type.lower() == "cardio":
            return "20 reps"
        elif workout_type.lower() == "weightlifting":
            return "4-6 reps"
        elif workout_type.lower() == "hiit":
            return "1-2 minutes"

def restart_program():
    answer = input("Would you like another workout suggestion? (yes/no): ").lower()
    if answer == "yes":
        main()
    elif answer == "no":
        print("Thank you for using the Random Workout Generator!!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        restart_program()

def main():
    while True:
        workout_type = input("Enter the type of workout (cardio, weightlifting, HIIT): ")
        rounds = int(input("Enter the number of rounds: "))

        workout_routine = generate_workout(workout_type, rounds)
        if workout_routine:
            print("\nYour workout routine:\n")
            print(workout_routine)
            restart_program()
            break

if __name__ == "__main__":
    main()