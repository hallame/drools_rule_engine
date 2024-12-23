import datetime

class Computer:
    def __init__(self, type, functions, pdate):
        self.type = type
        self.functions = functions
        self.pdate = pdate

TEST_RULES = [
    {"condition": {"type": "Type 1"}, "tests": [1, 2, 3]},
    {"condition": {"type": "Type 2", "function": "DNS"}, "tests": [4, 5]},
    {"condition": {"type": "Type 2", "function": "DDNS"}, "tests": [2, 3]},
    {"condition": {"type": "Type 2", "function": "Gateway"}, "tests": [3, 4]},
    {"condition": {"type": "Type 2", "function": "Router"}, "tests": [1, 3]},
]

DEADLINE_RULES = {
    1: 3,  # Test 1 - 3 days
    2: 7,
    3: 10,
    4: 12,
    5: 14
}

# Function to calculate the deadline based on the start date and number of days
def calc_deadline(start_date, days):
    return start_date + datetime.timedelta(days=days)

# Function to determine the tests that must be performed based on the computer's type and functions
def determine_tests(computer):
    selected_tests = []  # List to store the selected tests
    for function in computer.functions:
        for rule in TEST_RULES:
            condition = rule["condition"]
            if condition["type"] == computer.type:
                if "function" in condition and function == condition["function"]:
                    selected_tests.extend(rule["tests"])
                elif "function" not in condition:
                    selected_tests.extend(rule["tests"])
    return list(set(selected_tests))  # Remove duplicates from the list of selected tests

# Function to determine the final deadline for the tests
def determine_final_deadline(production_date, tests):
    if not tests:  # Check if the list of tests is empty
        raise ValueError("No tests selected for this computer.")
    deadlines = [calc_deadline(production_date, DEADLINE_RULES[test]) for test in tests]
    return min(deadlines)  # Return the earliest deadline

# Main function to apply the rules for tests and deadlines
def apply_rules(computer):
    tests = determine_tests(computer)  # Determine the tests to be performed
    if not tests:  # If no tests are selected, return None for the deadline
        return {
            "tests": [],
            "final_deadline": None
        }

    final_deadline = determine_final_deadline(computer.pdate, tests)  # Calculate the final deadline
    return {
        "tests": tests,
        "final_deadline": final_deadline
    }

# Example computers
computers = [
    Computer("Type 1", ["None"], datetime.date(2024, 12, 20)),
    Computer("Type 2", ["None"], datetime.date(2024, 11, 30)),
    Computer("Type 2", ["DDNS", "DNS"], datetime.date(2024, 11, 12)),
    Computer("Type 1", ["Router", "DNS"], datetime.date(2024, 12, 22)),
    Computer("Type 2", ["Gateway", "DDNS"], datetime.date(2024, 11, 3)),
    Computer("Type 2", ["Router"], datetime.date(2024, 11, 22))
]

# Apply the rules to each computer and display the results
for computer in computers:
    result = apply_rules(computer)
    print(f"Computer Type: {computer.type}, Functions: {computer.functions}, Production Date: {computer.pdate}")
    print(f"Selected Tests: {result['tests']}")
    if result["final_deadline"]:
        print(f"Final Deadline: {result['final_deadline']}")
    else:
        print("No tests assigned.")
    print("-" * 60)
