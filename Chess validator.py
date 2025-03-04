def is_valid_position(position, piece_type, color, occupied_positions):
    
    if len(position) != 2 or position[0] not in 'abcdefgh' or position[1] not in '12345678':
        return False
    
    if position in occupied_positions:
        print(f"Position {position} is already occupied. Choose another one.")
        return False

    if piece_type == "bishop":
        restricted_positions = {'a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'}
        if position in restricted_positions:
            return False

    return True

def can_take(white_piece, black_piece):
    piece_type, position = white_piece
    black_type, black_position = black_piece

    if piece_type == "pawn":
        return (ord(position[0]) - ord(black_position[0]) in [-1, 1] and int(position[1]) - int(black_position[1]) == 1)
    
    elif piece_type == "rook":
        return position[0] == black_position[0] or position[1] == black_position[1]
    
    return False

def main():
    print("Welcome to the chess program!")
    print("You can choose between two white pieces: 'pawn' or 'rook'.")
    
    occupied_positions = set()  

    while True:
        white_piece_input = input("Enter your choice (e.g., pawn a2): ")
        try:
            piece_type, position = white_piece_input.split()
        except ValueError:
            print("Invalid input format. Use format: piece position (e.g., 'pawn a2').")
            continue

        if is_valid_position(position, piece_type, "white", occupied_positions):
            occupied_positions.add(position)
            print(f"You have chosen the {piece_type} at position {position}.")
            break
        else:
            print("Invalid position. Try again.")

    black_pieces = []
    while True:
        black_piece_input = input("Enter black piece choice (e.g., pawn a7) or type 'done' to finish: ")
        
        if black_piece_input.lower() == "done":
            if len(black_pieces) > 0:
                break
            else:
                print("You must add at least one black piece.")
                continue

        try:
            black_piece_type, black_piece_position = black_piece_input.split()
        except ValueError:
            print("Invalid input format. Use format: piece position (e.g., 'pawn a7').")
            continue
        
        if is_valid_position(black_piece_position, black_piece_type, "black", occupied_positions):
            occupied_positions.add(black_piece_position)
            black_pieces.append((black_piece_type, black_piece_position))
            print(f"Black piece {black_piece_type} at position {black_piece_position} added successfully.")
        else:
            print("Invalid or occupied position. Try again.")

    can_take_list = [bp for bp in black_pieces if can_take((piece_type, position), bp)]

    if can_take_list:
        print("White piece can take the following black pieces:")
        for bp in can_take_list:
            print(f"{bp[0]} at {bp[1]}")
    else:
        print("White piece cannot take any black pieces.")

if __name__ == "__main__":
    main()