def get_input(prompt):
    while True:
        user_input = input(prompt)
        if all(bit in '01' for bit in user_input):
            return user_input
        print("Invalid input. Please enter only 0s and 1s.")


def calculate_crc(message, generator):
    data = list(map(int, message)) + [0] * (len(generator) - 1) 
    divisor = list(map(int, generator))

    for i in range(len(message)):
        if data[i] == 1: 
            for j in range(len(divisor)):
                data[i + j] ^= divisor[j]

    checksum_bits = data[len(message):]
    checksum = ''.join(map(str, checksum_bits))
    return message + checksum 


def validate_crc(received_message, generator):
    data = list(map(int, received_message))
    divisor = list(map(int, generator))

    for i in range(len(received_message) - len(generator) + 1):
        if data[i] == 1:  
            for j in range(len(divisor)):
                data[i + j] ^= divisor[j]

    return all(bit == 0 for bit in data[-(len(generator) - 1):])


def main():
    message = get_input("Enter message bits (only 0s and 1s): ")
    generator = get_input("Enter generator (only 0s and 1s): ")

    checksum = calculate_crc(message, generator)
    print("The checksum code is:", checksum)

    received_message = get_input("Enter checksum code (message + checksum): ")
    is_valid = validate_crc(received_message, generator)
    print("Data stream is valid" if is_valid else "Data stream is invalid. CRC error occurred.")


if __name__ == "__main__":
    main()
