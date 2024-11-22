import random

# Define workout options for each type of workout
workouts = {
    "cardio": ["Running", "Jumping Jacks", "Burpees", "Cycling", "Jump Rope", "High Knees"],
    "weightlifting": {  # Muscle-specific workouts
        "chest": ["Bench Press", "Incline Dumbbell Press", "Push-Ups", "Cable Flys", "Chest Dips", "Pec Deck", "Incline Machine Press"],
        "shoulder": ["Overhead Press", "Lateral Raises", "Front Raises", "Arnold Press", "Face Pulls", "Seated Dumbbell Press", "Barbell Shrugs"],
        "back": ["Pull-Ups", "Deadlifts", "Bent-Over Rows", "Lat Pulldowns", "T-Bar Rows", "Seated Cable Rows", "Reverse Flys"],
        "arm": ["Dumbbell Curls", "Hammer Curls", "Concentration Curls", "Triceps Pushdown", "Close-Grip Bench Press", "Overhead Triceps Extension", "Barbell Curls"],
        "biceps": ["Barbell Curls", "Incline Dumbbell Curls", "Preacher Curls", "Hammer Curls", "Cable Curls", "Reverse Curls", "Spider Curls"],
        "glutes": ["Hip Thrusts", "Bulgarian Split Squats", "Romanian Deadlifts", "Glute Bridges", "Sumo Deadlifts", "Step-Ups", "Kettlebell Swings"],
        "hamstring": ["Romanian Deadlifts", "Hamstring Curls", "Single-Leg Deadlifts", "Good Mornings", "Glute Ham Raises", "Leg Curls", "Sumo Squats"],
        "human leg": ["Squats", "Lunges", "Leg Press", "Step-Ups", "Calf Raises", "Glute Bridges", "Hamstring Curls"],
        "chest and triceps": ["Bench Press", "Incline Dumbbell Press", "Push-Ups", "Close-Grip Bench Press", "Overhead Triceps Extension", "Triceps Dips", "Chest Flys"],
        "triceps": ["Triceps Pushdown", "Close-Grip Bench Press", "Overhead Triceps Extension", "Dumbbell Kickbacks", "Skull Crushers", "Dips", "Rope Pushdowns"],
        "abdominals": ["Crunches", "Plank", "Leg Raises", "Bicycle Crunches", "Russian Twists", "Ab Rollouts", "Mountain Climbers"],
        "calf": ["Standing Calf Raises", "Seated Calf Raises", "Donkey Calf Raises", "Jump Rope", "Single-Leg Calf Raises", "Box Jumps", "Calf Stretch"],
        "quadriceps": ["Squats", "Lunges", "Leg Press", "Step-Ups", "Bulgarian Split Squats", "Front Squats", "Hack Squats"],
        "rectus abdominis muscle": ["Plank", "Crunches", "Leg Raises", "Cable Crunches", "Ab Rollouts", "Mountain Climbers", "Sit-Ups"],
        "core": ["Plank", "Side Plank", "Bird Dogs", "Dead Bugs", "Russian Twists", "Mountain Climbers", "Ab Rollouts"],
        "forearm": ["Wrist Curls", "Reverse Wrist Curls", "Farmer's Walk", "Grip Strength Squeeze", "Reverse Curls", "Plate Pinches", "Towel Pull-Ups"],
        "latissimus dorsi muscle": ["Pull-Ups", "Chin-Ups", "Lat Pulldowns", "T-Bar Rows", "Seated Cable Rows", "One-Arm Dumbbell Rows", "Bent-Over Rows"],
        "trapezius": ["Shrugs", "Barbell Rows", "Face Pulls", "Dumbbell Lateral Raises", "Upright Rows", "Farmer's Walk", "T-Bar Rows"]
    },
    "hiit": ["Mountain Climbers", "Sprint Intervals", "Box Jumps", "Plank Jacks", "Battle Ropes", "Jump Squats"]
}

def generate_workout(workout_type, rounds=None, days=None, selected_muscles=None):
    if workout_type.lower() == "cardio" or workout_type.lower() == "hiit":
        workout_options = workouts.get(workout_type.lower())
        if not workout_options:
            print("Invalid workout type.")
            return None

        reps = calculate_reps(workout_type, rounds)
        workout_routine = []
        for i in range(rounds):
            random.shuffle(workout_options)
            workout_routine.append(f"Round {i+1}: {', '.join(workout_options[:4])} ({reps})")
        return "\n".join(workout_routine)

    elif workout_type.lower() == "weightlifting":
        workout_plan = {}
        for day in range(1, days + 1):
            daily_workout = []
            for muscle in selected_muscles:
                exercises = workouts["weightlifting"].get(muscle.lower())
                if exercises:
                    daily_workout += random.sample(exercises, 1)  # Add one exercise per selected muscle
            workout_plan[f"Day {day}"] = daily_workout[:7]  # Limit to 7 exercises per day
        return workout_plan

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
