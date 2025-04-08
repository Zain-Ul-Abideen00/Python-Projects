import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")

    while True:
        try:
            # Get time input
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))

            if hours < 0 or minutes < 0 or seconds < 0:
                print("Please enter positive numbers.")
                continue

            total_seconds = hours * 3600 + minutes * 60 + seconds

            if total_seconds == 0:
                print("Please enter a time greater than 0.")
                continue

            break
        except ValueError:
            print("Please enter valid numbers.")

    print("\nTimer started!")

    while total_seconds > 0:
        # Calculate hours, minutes, and seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        # Format time display
        time_display = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(f"\r{time_display}", end="")

        # Wait for one second
        time.sleep(1)

        # Decrease total seconds
        total_seconds -= 1

    print("\n\nTime's up!")

if __name__ == "__main__":
    countdown_timer()
