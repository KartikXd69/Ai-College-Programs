def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case: only 1 disk
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Step 1: move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Step 2: move the largest disk from source to destination
    print("Move disk", n, "from", source, "to", destination)

    # Step 3: move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Number of disks
n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')