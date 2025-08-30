# Valid Vote

from datetime import date

def vote(year = date.today().year):
	date.today().year
	age = date.today().year - year
	if age < 16:
	   return f'Age {age}: VOTE DENIED.'
	elif 16 <= age < 18 or age > 65:
	   return f'Age {age}: OPTIONAL VOTE.'
	else:
		return f'Age {age}: MANDATORY VOTE'
    	
print(vote())
    	