# Tristan White
# IT -140 Project Two
# The Sandlot Text Based Adventure Game

# Tristan White
# IT-140 Project Two - Text Based Game
# The Sandlot Adventure (Final)

def show_instructions():
    """Print the game title, goal, and valid commands."""
    print("Welcome to the Sandlot Adventure!")
    print("Goal: Collect all the baseball gear BEFORE you enter the Beast's Lair.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get (or get item)")
    print("Type 'exit' anytime to quit.\n")


def show_status(current_room, inventory, rooms):
    """Show the player's current room, inventory, item in room, and available directions."""
    print("\n---------------------------")
    print(f"You are in: {current_room}")

    item_here = rooms[current_room].get("item")
    if item_here:  # only print if it's not None / not empty
        print(f"You see: {item_here}")

    # directions are any keys except "item"
    directions = [k for k in rooms[current_room].keys() if k != "item"]
    if directions:
        print("Available directions:", ", ".join(directions))
    else:
        print("Available directions: None")

    print("Inventory:", ", ".join(inventory) if inventory else "(empty)")
    print("Commands: go North/South/East/West | get | exit")
    print("---------------------------")


def main():
    # One dictionary holding both room links and items
    rooms = {
        "Front Yard": {
            "South": "Fence Line",
            "East": "Storage Shed",
            "item": None
        },
        "Fence Line": {
            "North": "Front Yard",
            "South": "Escape Path",
            "West": "Side Yard",
            "East": "Beast's Lair",
            "item": "Hams Catchers Mask"
        },
        "Side Yard": {
            "East": "Fence Line",
            "South": "Tree Line",
            "item": "Squints Glasses"
        },
        "Tree Line": {
            "North": "Side Yard",
            "item": "Smalls Glove"
        },
        "Storage Shed": {
            "West": "Front Yard",
            "South": "Old Doghouse",
            "item": "Bens Bat"
        },
        "Old Doghouse": {
            "North": "Storage Shed",
            "West": "Dead End Alley",
            "item": "Baseball"
        },
        "Dead End Alley": {
            "East": "Old Doghouse",
            "South": "Escape Path",
            "item": "Brandons Glove"
        },
        "Escape Path": {
            "North": "Fence Line",
            "item": "Smalls Hat"
        },

        # Villain room
        "Beast's Lair": {
            "West": "Fence Line",
            "item": "The Beast"
        }
    }

    required_items = {
        "Hams Catchers Mask",
        "Squints Glasses",
        "Smalls Glove",
        "Bens Bat",
        "Brandons Glove",
        "Smalls Hat"
    }

    inventory = []
    current_room = "Front Yard"

    show_instructions()

    while True:

        # Lose condition: entered Beast's Lair without all items
        if current_room == "Beast's Lair" and set(inventory) != required_items:
            show_status(current_room, inventory, rooms)
            print("\nNOM NOM...GAME OVER!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        # Win condition: collected all items AND reached Escape Path
        if set(inventory) == required_items and current_room == "Escape Path":
            show_status(current_room, inventory, rooms)
            print("\nCongratulations! You collected all the gear and escaped!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        show_status(current_room, inventory, rooms)

        command = input("Enter your command: ").strip()

        if not command:
            print("Invalid command. Use: go North/South/East/West, get, or exit.")
            continue

        command_lower = command.lower()

        # Exit command
        if command_lower == "exit":
            print("Thanks for playing!")
            break

        # Get item command (accepts "get" or "get item")
        if command_lower in ("get", "get item"):
            item_here = rooms[current_room].get("item")

            # Can't pick up villain
            if current_room == "Beast's Lair":
                print("You can't pick that up!")
                continue

            if item_here is None:
                print("There is no item to pick up here.")
                continue

            if item_here in inventory:
                print("You already picked that up.")
                continue

            inventory.append(item_here)
            rooms[current_room]["item"] = None
            print(f"{item_here} added to your inventory.")
            continue

        # Movement command: "go <direction>"
        parts = command.split()
        if len(parts) == 2 and parts[0].lower() == "go":
            direction = parts[1].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way.")
        else:
            print("Invalid command. Use: go North/South/East/West, get, or exit.")


main()
