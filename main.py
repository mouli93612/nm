# main.py
from backend import CarbonFootprintTracker
from frontend import show_intro, get_user_input, show_emission, show_total, show_suggestion

def main():
    tracker = CarbonFootprintTracker()
    total_emission = 0
    show_intro()

    while True:
        activity, amount = get_user_input()
        if activity.lower() == 'done':
            break
        emission = tracker.calculate_emission(activity, amount)
        if emission is not None:
            total_emission += emission
            show_emission(activity, amount, emission)
        else:
            print("⚠️ Unknown activity. Please try again.")

    show_total(total_emission)
    suggestion = tracker.suggest_reduction(total_emission)
    show_suggestion(suggestion)

if __name__ == "__main__":
    main()

