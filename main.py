from datetime import datetime as dt


# --- values ---
currhour = int(str(dt.time(dt.now()))[:2:])
currmin = int(str(dt.time(dt.now()))[3:5:])
cycle = []  # list that contains time of sleep cycles
low = 4  # 4 cycles - min time for human to sleep well
hi = 6  # 6 cycles - max time for human to sleep well
time_of_day = [{
                   'name': 'night',
                   'starthour': 0,
                   'endhour': 6
               },
               {
                   'name': 'morning',
                   'starthour': 6,
                   'endhour': 12
               },
               {
                   'name': 'day',
                   'starthour': 12,
                   'endhour': 18
               }, 
               {
                   'name': 'evening',
                   'starthour': 18,
                   'endhour': 24
               }]

# --- strings ---
now_msg = f'It\'s {currhour}:{currmin} now.'
final_msg = '   Sleep well. Coded @ 1:30 AM 10/24/18 :(   '
pst_msg = 'Preferrable sleep time:'
flen = len(final_msg)

# determine what time of day is it now
for a in time_of_day:
    if (currhour >= a['starthour'] and currhour <= a['endhour']):
        currtod = f'{a["name"]}'
        break

# --- program start ---
print(f'{"_" * flen}') # divider (----) to maintain readability
print(f'{now_msg.center(flen)}')
print(f'''{"Let's suppose you are going to bed right now.".center(flen)}''')
print(f'{pst_msg.center(flen)}')
print(f'{"_" * flen}')

# --- cycles calculation ---
for x in range(low, hi + 1):
    cycle.append(90 * x + 15)  # 90mins + time to sleep

cc = 0 # current cycle

for mins in cycle:
    hrs = 0

    while mins >= 60:
        mins -= 60
        hrs += 1

    wakeuphr = currhour + hrs
    wakeupmin = currmin + mins

    if wakeuphr > 23:
        wakeuphr -= 24

    if wakeupmin > 59:
        wakeupmin -= 60
        wakeuphr += 1

    print(f'{low + cc} cycles: ', end='')
    print(f'{hrs} hrs {mins} mins (wake up at {wakeuphr}:{wakeupmin})')
    cc += 1

if currtod == 'day': # add 20-minute break if it's day now
    wakeuphr = currhour
    wakeupmin = currmin + 20

    if wakeupmin > 59:
        wakeupmin -= 60
        wakeuphr += 1

    print(f'Short daily sleep: 20 mins (wake up at {wakeuphr}:{wakeupmin})')

print(f'{"_" * flen}\n{final_msg}')
quit()

