def count_file_contents(file_name):
    try:
        # To Open the file 
        file = open(file_name, 'r', encoding='utf-8')
        
        # Initializing counters/Flagging method to count
        num_lines = 0
        num_words = 0
        num_characters = 0

        # Traversing  the file line by line
        for line in file:
            num_lines += 1  # Incrementing the line count
            num_characters += count_characters(line)  # Counting characters in the line by incrementing in every iteration
            
            # Counting words in the line
            in_word = False
            for char in line:
                if char.isspace():
                    if in_word:
                        num_words += 1
                        in_word = False
                else:
                    in_word = True
            if in_word:
                num_words += 1

        # Closing the file
        file.close()

        # Output for the results required
        print(f"File: {file_name}")
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_characters}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_characters(line):
    # Counting characters manually in a line
    count = 0
    for char in line:
        count += 1
    return count

if __name__ == "__main__":
    # Taking file name as an input
    file_name = input("Enter the file name: ").strip()
    count_file_contents(file_name)
