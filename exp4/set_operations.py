L = set(input("Enter successful IPs: ").split())
F = set(input("Enter failed IPs: ").split())
B = set(input("Enter blacklisted IPs: ").split())

both_status = (L & F) - B
print("Both logged and failed, not blacklisted:", both_status)

only_failed = F - L
print("Attempted but never succeeded:", only_failed)

only_blacklisted = B - (L | F)
print("Only blacklisted, never attempted:", only_blacklisted)


required = set(input("Enter required skills: ").split())
applicant = set(input("Enter applicant skills: ").split())
outdated_input = input("Enter outdated skills: ")
outdated = set(outdated_input.split())
missing_skills = (required - applicant) - outdated
print("Missing required skills (excluding outdated):", missing_skills)
