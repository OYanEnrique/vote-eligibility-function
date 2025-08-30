# 🗳️ Voting Eligibility Checker (Brazil)

A simple script that demonstrates a Python function, `vote()`, which determines a person's voting eligibility based on Brazilian law.

## Features

The core of this project is the `vote()` function, which encapsulates the specific age-based voting rules for Brazil:

* **Below 16**: Voting is denied.
* **16 to 17** or **Over 65**: Voting is optional.
* **18 to 65**: Voting is mandatory.

The function takes a birth year as an argument, calculates the person's current age, and returns a formatted string with their status.

## How to Use

The script as it is will produce a fixed output because it is not interactive. To use the function to check any birth year, you should make it interactive.

### 1. Run the Default Script

Running the script as-is will always check the current year, resulting in age 0.

```sh
> python vote_check.py
Age 0: VOTE DENIED.
```

### 2. Make it Interactive (Recommended)

To check any birth year, modify the last line of the script to ask for user input.

**Change this line:**
```python
print(vote())
```

**To this:**
```python
birth_year = int(input("Enter a birth year: "))
print(vote(birth_year))
```

Now, when you run the script, it will be interactive:

```sh
> python vote_check.py
Enter a birth year: 1990
Age 35: MANDATORY VOTE
```
