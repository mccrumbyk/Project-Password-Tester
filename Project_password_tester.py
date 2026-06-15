import re


def check_password_strength(password: str) -> tuple[str, list[str], int]:
    """
    Check whether the password contains:
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one number

    Returns:
        strength_label (str): Weak, Medium, or Strong
        missing_requirements (list[str]): List of missing requirements
        requirements_met (int): Number of requirements met
    """

    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"[0-9]", password))

    requirements_met = sum([has_uppercase, has_lowercase, has_number])
    missing_requirements = []

    if not has_uppercase:
        missing_requirements.append("an uppercase letter")
    if not has_lowercase:
        missing_requirements.append("a lowercase letter")
    if not has_number:
        missing_requirements.append("a number")

    if requirements_met == 3:
        strength_label = "Strong"
    elif requirements_met == 2:
        strength_label = "Medium"
    else:
        strength_label = "Weak"

    return strength_label, missing_requirements, requirements_met


def main() -> None:
    """Run the password strength tester until all requirements are met."""
    print("Password Strength Tester")
    print("-" * 25)

    while True:
        password = input("Enter a password to test: ").strip()

        if not password:
            print("\nError: No password entered. Please try again.\n")
            continue

        strength_label, missing_requirements, requirements_met = check_password_strength(password)

        print("\nResults")
        print("-" * 25)
        print(f"Requirements met: {requirements_met}/3")
        print(f"Strength: {strength_label}")

        if missing_requirements:
            print("Missing:")
            for requirement in missing_requirements:
                print(f"- {requirement}")
            print("\nPlease try again.\n")
        else:
            print("Your password meets all requirements.")
            break


if __name__ == "__main__":
    main()