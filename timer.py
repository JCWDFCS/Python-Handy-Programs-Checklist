from datetime import datetime, date, time, timedelta

def main():
    # start timing
    input('Press enter to start ...')
    start_time = datetime.now()
    print('Start time:', start_time.strftime('%X.%f'))

    # stop timing
    input('Press enter to stop ...')
    stop_time = datetime.now()
    print('Stop time:', stop_time.strftime('%X.%f'))
    # calculate elapsed time
    time_elapsed = stop_time - start_time
    days = time_elapsed.days
    mins, secs = divmod(time_elapsed.seconds, 60)
    microseconds = time_elapsed.microseconds
    hrs, mins = divmod(mins, 60)

    time_object = time(hrs, mins, secs, microseconds)
    if hrs > 0 or mins > 0:
        print('Hours/minutes: ' + time_object.strftime('%H:%M'))
    print('Seconds:', time_object.strftime('%S.%f'))

if __name__ == '__main__':
    main()
