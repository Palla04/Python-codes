import random
import string

def generate_random_string(template):
    # Characters to replace underscores with (alphanumeric characters)
    characters = string.ascii_letters + string.digits
    
    # Generate a new string by replacing each underscore in the template
    random_string = ''.join(random.choice(characters) if char == '_' else char for char in template)
    
    return random_string

# Example usage
template = 'a____string'
output_string = generate_random_string(template)
print("Input template:", template)
print("Generated random string:", output_string)
