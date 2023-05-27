import jsonlines

# Path to the file
file_path = "/Users/stevenclark/.convokit/downloads/subreddit-wallstreetbets/utterances.jsonl"

# Open the file
with jsonlines.open(file_path) as reader:

    # Counter variable
    counter = 0

    # Loop over the file
    for obj in reader:
        # Let's print each object
        print(obj)

        # Increment the counter
        counter += 1

        # To avoid printing the entire file, let's break after the first 2 entries
        if counter == 2:
            break
