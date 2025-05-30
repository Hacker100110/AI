def print_rooms(rooms, vacuum_location):
    for i, status in enumerate(rooms):
        tag = " (V)" if i == vacuum_location else ""
        print(f"Room {'A' if i == 0 else 'B'}: {status}{tag}")

def main():
    rooms = [
        input("Enter the status of Room A (C for Clean, D for Dirty): ").strip().upper(),
        input("Enter the status of Room B (C for Clean, D for Dirty): ").strip().upper()
    ]

    if any(r not in ('C', 'D') for r in rooms):
        print("Invalid input! Please restart the program and use 'C' or 'D'.")
        return

    pos = input("Enter the initial position of the vacuum cleaner (A or B): ").strip().upper()
    vacuum = 0 if pos == 'A' else 1 if pos == 'B' else -1

    if vacuum == -1:
        print("Invalid input! Please restart the program and use 'A' or 'B'.")
        return

    print("Initial State:")
    print_rooms(rooms, vacuum)

    for step in range(5):
        print(f"\nStep {step + 1}:")
        if rooms[vacuum] == 'D':
            print(f"Cleaning Room {'A' if vacuum == 0 else 'B'}")
            rooms[vacuum] = 'C'
        else:
            print(f"Room {'A' if vacuum == 0 else 'B'} is already clean.")
            vacuum = 1 - vacuum
            print(f"Moving to Room {'A' if vacuum == 0 else 'B'}")
        print_rooms(rooms, vacuum)
        if rooms == ['C', 'C']:
            print("\nBoth rooms are clean. Ending function.")
            break

if __name__ == "__main__":
    main()
