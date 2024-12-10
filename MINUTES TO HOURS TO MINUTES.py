MINUTES TO HOURS TO MINUTES
minutes=int(input('enter minutes: '))
hours=minutes//60
print(hours)
hours=int(input('enter hours: '))
minutes=hours*60
print(minutes)
                                  OR

minutes=int(input('enter minutes: '))
hours=minutes//60
remaining_minutes=minutes%60
print(f"Time: {hours} hours and {remaining_minutes} minutes")
