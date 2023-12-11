from datetime import datetime, timedelta
import pytz

def get_current_week_number():
    # Get the current week number
    now = datetime.now()
    week_number = now.strftime("%U")
    return int(week_number) # Removed Adding 1 because weeks start from 1 (not 0)

def get_remaining_weeks():
    # Calculate the remaining weeks until the end of the year
    now = datetime.now()
    end_of_year = datetime(now.year, 12, 31)
    remaining_weeks = (end_of_year - now).days // 7
    return remaining_weeks

def get_remaining_workweek_days():
    # Calculate the remaining workweek days until the end of the year
    now = datetime.now()
    end_of_year = datetime(now.year, 12, 31)
    
    remaining_workweek_days = 0
    current_date = now

    while current_date <= end_of_year:
        # Check if the current day is a workweek day (Monday to Friday)
        if current_date.weekday() < 5:
            remaining_workweek_days += 1

        # Move to the next day
        current_date += timedelta(days=1)

    return remaining_workweek_days

def display_current_time_in_timezones(timezones):
    # Display the current time in different timezones
    for timezone in timezones:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        print(f"Time in {timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    # Get and display the current week number
    week_number = get_current_week_number()
    print(f"Current Week Number: {week_number}")

    # Calculate and display the remaining weeks until the end of the year
    remaining_weeks = get_remaining_weeks()
    print(f"Weeks left until the end of the year: {remaining_weeks}")

    # Calculate and display the remaining workweek days until the end of the year
    remaining_workweek_days = get_remaining_workweek_days()
    print(f"Workweek days left until the end of the year: {remaining_workweek_days}")

    # Define a list of regions and their timezones (east and west coast)
    regions = {
        "America": ["America/New_York", "America/Los_Angeles"],
        "Europe": ["Europe/London"],
        "Asia": ["Asia/Tokyo"],
        "Australia": ["Australia/Sydney"]
    }

    # Display the current time in different timezones for each region
    for region, timezones in regions.items():
        print(f"\n{region} Time:")
        display_current_time_in_timezones(timezones)

if __name__ == "__main__":
    main()
