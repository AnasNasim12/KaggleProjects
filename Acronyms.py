def generate_acronym(phrase):
    if not phrase.strip():
        return "Please enter a valid phrase."
    
    words = phrase.split()
    acronym = ""
    
    for word in words:
        if word.isalnum():  # Check if the word contains only alphanumeric characters
            acronym += word[0].upper()
    
    if not acronym:
        return "No valid words found in the phrase."
    
    return acronym

def main():
    user_input = input("Enter a Phrase: ")
    acronym = generate_acronym(user_input)
    print("Acronym:", acronym)

if __name__ == "__main__":
    main()
