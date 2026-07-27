import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email: str) -> bool:
     
    return bool(EMAIL_REGEX.match(email))



if __name__ == "__main__":
    def main():
    
        test_emails = [
            "rodrigomoraes!@#.com",  
            "rodrigomoraes@outlook.com",  
        ]
        print(is_valid_email(test_emails[0]))
        print(is_valid_email(test_emails[1]))
            if is_valid_email(test_emails[0]):
                print(f"{test_emails[0]} is a valid email.")
    main()