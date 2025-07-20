# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!", 
    "bart": "Eat My Shorts!", 
    "marge": "Mmm~mmmmm", 
    "homer": "d'oh!",
    "maggie": "(Pacifier Suck)"
}
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])