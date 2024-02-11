def decode(msg_to_decode, file_to_train):
    # Read the contents of the file to train
    with open(file_to_train, 'r') as file:
        lines = file.readlines()

    # Create dictionary to store the training data hash table for decoding
    decode_sequence = {}

    # Iterate through each line to create the decode training data hash table
    for line in lines:
        parts = line.split()
        part_key = int(parts[0])
        part_value = ' '.join(parts[1:])
        decode_sequence[part_key] = part_value

    # create the variable to store the decoded message
    result = ""

    # Read the contents of the file to decode
    with open(msg_to_decode, 'r') as msg_file:
        msg_lines = msg_file.readlines()

    # Iterate through each line to decoded the message
    for line in msg_lines:
        parts = line.split()
        for part in parts:
            # Convert the part to an integer and look up the corresponding value in the decode_sequence
            result += decode_sequence[int(part)] + ' '

    return result.strip().lower()


# Example usage
file_used_to_train = 'coding_qual_input.txt'
message_to_decode = 'input.txt'
decoded_message = decode(message_to_decode, file_used_to_train)
print(decoded_message)

# The decode function reads two text files, one for training and one for decoding. It creates a dictionary (decode_sequence) from the training file, mapping integer keys to corresponding string values. It then reads the message file to decode, splits each line into parts, looks up the corresponding values in the dictionary, and appends the results to the result variable. Finally, the function returns the decoded message in lowercase after stripping any leading or trailing whitespaces.
