def next_closest_time(time):
    # Parse the input time
    hours, minutes = map(int, time.split(':'))

    # Create a set of all the digits in the input time
    digits = set(time.replace(':', ''))

    # Start the loop to generate the next closest time
    while True:
        # Increment the minutes by 1
        minutes += 1

        # Reset minutes and increment hours if necessary
        if minutes == 60:
            minutes = 0
            hours += 1

        # Reset hours if necessary
        if hours == 24:
            hours = 0

        # Format the new time
        new_time = f'{hours:02d}:{minutes:02d}'

        # Check if all the digits are present in the new time
        if all(digit in digits for digit in new_time.replace(':', '')):
            return new_time
