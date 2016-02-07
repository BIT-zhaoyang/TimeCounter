"""
File: TimeCounter.py
Author: Yang Zhao
Description: This coarse program calculate the times used on studying. This is a
very initialing program so every time the user has to start/terminate the
program manually. The program shows time spended on study today, in the past 2
weeks, in the total past.
"""

from counter import Counter
import datetime
import time

def getRecord():
    """
    Records are stored in records.txt.
    The first line stores total time in 0 0 0 seconds. The three 0s
    corresponds to year, month, day.
    The second to 15th lines store time of past 2 weeks in 14 lines
    seperately in year, month, day, seconds.
    The 16th line stores today's info in year month day seconds. Note
    this may also represent info of last time we run this program.
    """
    record = open('records.txt')
    total = Counter(record.readline())
    past2weeks = []
    line = record.readline()
    while line != "\n":
        past2weeks.append(Counter(line))
        line = record.readline()
    today = Counter(record.readline())
    record.close()
    return total, past2weeks, today

def update(total, past2weeks, today):
    """ This function update the records.txt file with latest
    total, past2weeks, today values. """
    
    record = open('records.txt', 'w')
    # Write total
    content = "0 0 0 " + str(total.getTime()) + "\n"
    record.write(content)

    # Write past2weeks
    for item in past2weeks:
        year = item.getDate().getYear()
        month = item.getDate().getMonth()
        day = item.getDate().getDay()
        time = item.getTime()
        content = str(year) + " " + str(month) + " " +  str(day) + " "+\
                     str(time) + "\n"
        record.write(content)
    record.write("\n")

    # Write today
    year = today.getDate().getYear()
    month = today.getDate().getMonth()
    day = today.getDate().getDay()
    time = today.getTime()
    content = str(year) + " " + str(month) + " " +  str(day) + \
                 " " + str(time)+ "\n"
    record.write(content)
    
    record.close()
    
def main():
    # 1. Update records, then show welcome, summary
    # 1.1 Get records
    [total, past2weeks, today] = getRecord()
    # 1.2 Greeting
    print("==============================================")
    print("Hello, welcome to challenge yourself.")
    print("How far are you away from being an expertise?")
    print("==============================================\n")

    # 1.3 Update records
    # In this part, we will update total and past2weeks
    # Get current day when re-run this pogram
    current = datetime.datetime.now()
    cYear = current.year
    cMonth = current.month
    cDay = current.day
    cDate = Counter([cYear, cMonth, cDay])
    # Compare to recorded day to see if they are the same
    # If they are the same, it means we have ran this program before
    # in the same day. Nothing to be done.
    # If they are different, it means a new day starts and we have to
    # update the array of past2weeks.
    if cDate != today:
        past2weeks.append(today)
        while len(past2weeks) != 0 and cDate - past2weeks[0] > 14:
            past2weeks.pop(0)
        total = total + today
        today = Counter([cYear, cMonth, cDay])
        update(total, past2weeks, today)

    # 1.4 summary
    print("Time you have spent on your dream:")
    print("Total: " + str(total))
    p2w = sum(past2weeks, Counter())   # temporary variable to hold summation
                                        # time in past 2 weeks
    print("Past 2 weeks: " + str(p2w))
    print("Today: " + str(today))

    # 2. Ask when to start/end and record
    while True:
        answer = input("\nStart to work now? (Y/N): ")
        if answer == "Y" or answer == "y":
            print("\n\nLet's do it now!.")
            break
        else:
            return
    start = int(time.time())
    print("\n\nPress D when you finish studying:")
    while True:
        answer = input()
        if answer == "D" or answer == "d":
            end = int(time.time())
            today.addTime(end - start)
            break
    
    # 3. Update again
    # Here we only update today
    update(total, past2weeks, today)

    # 4. Show summary again
    print("\n\n\n==============================================")
    print("Up till now, you have been working for: ")
    print("Total: " + str(total))
    p2w = sum(past2weeks, Counter())   # temporary variable to hold summation
                                        # time in past 2 weeks
    print("Past 2 weeks: " + str(p2w))
    print("Today: " + str(today) + "\n")
    print("Carry on!")
    print("==============================================")
    

if __name__ == "__main__":
    main()
##    # 1. Update records, then show welcome, summary
##    # 1.1 Get records
##    [total, past2weeks, today, day] = getRecord()
##    # 1.2 Greeting
##    print("==============================================")
##    print("Hello, welcome to challenge yourself.")
##    print("How far are you away from being an expertise?")
##    print("==============================================\n")
##
##    # 1.3 Update records
##    # Get current day when re-run this pogram
##    current = datetime.datetime.now()
##    cYear = current.year
##    cMonth = current.month
##    cDay = current.day
##    cDate = Counter([cYear, cMonth, cDay])
##    # Compare to recorded day to see if they are the same
##    # If they are the same, it means we have ran this program before
##    # in the same day. Nothing to be done.
##    # If they are different, it means a new day starts and we have to
##    # update the array of past2weeks.
##    if cDate != today:
##        while len(past2weeks) != 0 and cDate - past2weeks[0] >= 14:
##            past2weeks.pop(0)
##        past2weeks.append(today)
##        today = Counter([cYear, cMonth, cDay])
