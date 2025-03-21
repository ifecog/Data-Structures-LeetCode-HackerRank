def checkRecord(s):
    """
    You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.
    The student is eligible for an attendance award if they meet both of the following criteria:

    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.
    Return true if the student is eligible for an attendance award, or false otherwise.

    Args:
        s (string): A string of characters

    Returns:
        boolean: Eligibility for attendance award
    """
    
    if s.count('A') >= 2 or 'LLL' in s:
        return False
    
    return True


# Example usage
s = "PPALLP"
print(checkRecord(s))