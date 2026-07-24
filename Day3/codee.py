class SmartFileOrganizer:
    """A simple organizer for file-size data using common two-pointer patterns."""

    def __init__(self, files):
        """
        Initialize the Smart File Organizer.

        Parameters:
            files (list): List of file sizes in MB.
        """
        self.files = files
        self.original_files = files.copy()

    def display_files(self):
        """Display current file list."""
        print("Current File List:")
        for file in self.files:
            print(f"  {file} MB")

    def sort_files(self):
        """Sort the file sizes in ascending order."""
        if not self.files:
            print("\nNo files available to sort.")
            return

        self.files.sort()
        print("\nFiles have been sorted successfully.")
        self.display_files()

    def remove_duplicates(self):
        """Remove duplicate file sizes using a two-pointer pattern."""
        if not self.files:
            print("\nNo files available.")
            return

        self.files.sort()
        i = 0

        for j in range(1, len(self.files)):
            if self.files[i] != self.files[j]:
                i += 1
                self.files[i] = self.files[j]

        self.files = self.files[: i + 1]
        print("\nDuplicate files removed successfully.")
        self.display_files()

    def find_pair(self, target):
        """Find one pair of file sizes whose sum equals the target."""
        if len(self.files) < 2:
            print("\nNot enough files.")
            return

        self.files.sort()
        left = 0
        right = len(self.files) - 1

        while left < right:
            current_sum = self.files[left] + self.files[right]

            if current_sum == target:
                print("\nPair Found!")
                print(f"{self.files[left]} MB + {self.files[right]} MB = {target} MB")
                return

            if current_sum < target:
                left += 1
            else:
                right -= 1

        print("\nNo pair found.")

    def find_all_pairs(self, target):
        """Find all unique pairs whose sum equals the target."""
        if len(self.files) < 2:
            print("\nNot enough files.")
            return

        self.files.sort()
        left = 0
        right = len(self.files) - 1
        found = False

        while left < right:
            current_sum = self.files[left] + self.files[right]

            if current_sum == target:
                print(f"{self.files[left]} MB + {self.files[right]} MB = {target} MB")
                found = True
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        if not found:
            print("\nNo pairs found.")

    def closest_pair(self, target):
        """Find the pair whose sum is closest to the target."""
        if len(self.files) < 2:
            print("\nNot enough files.")
            return

        self.files.sort()
        left = 0
        right = len(self.files) - 1
        best_pair = None
        smallest_diff = float("inf")

        while left < right:
            current_sum = self.files[left] + self.files[right]
            diff = abs(target - current_sum)

            if diff < smallest_diff:
                smallest_diff = diff
                best_pair = (self.files[left], self.files[right])

            if current_sum < target:
                left += 1
            else:
                right -= 1

        print(f"\nClosest Pair: {best_pair[0]} MB + {best_pair[1]} MB")
        print(f"Total = {best_pair[0] + best_pair[1]} MB")

    def pair_smallest_largest(self):
        """Pair the smallest file with the largest."""
        if len(self.files) < 2:
            print("\nNot enough files.")
            return

        self.files.sort()
        left = 0
        right = len(self.files) - 1
        print("\nPairs:")

        while left < right:
            print(f"{self.files[left]} MB  <-->  {self.files[right]} MB")
            left += 1
            right -= 1

        if left == right:
            print(f"Unpaired File: {self.files[left]} MB")

    def partition_files(self, limit):
        """Move files smaller than the limit to the front."""
        left = 0

        for right in range(len(self.files)):
            if self.files[right] < limit:
                self.files[left], self.files[right] = (
                    self.files[right],
                    self.files[left],
                )
                left += 1

        print("\nPartition Completed.")
        self.display_files()

    def remove_large_files(self, limit):
        """Remove files larger than the given limit."""
        slow = 0

        for fast in range(len(self.files)):
            if self.files[fast] <= limit:
                self.files[slow] = self.files[fast]
                slow += 1

        self.files = self.files[:slow]
        print("\nLarge files removed.")
        self.display_files()

    def compress_duplicates(self):
        """Count consecutive duplicate file sizes."""
        if not self.files:
            print("\nNo files.")
            return

        self.files.sort()
        i = 0

        while i < len(self.files):
            count = 1

            while (
                i + 1 < len(self.files)
                and self.files[i] == self.files[i + 1]
            ):
                count += 1
                i += 1

            print(f"{self.files[i]} MB x{count}")
            i += 1

    def max_container(self):
        """Solve the Container With Most Water problem."""
        if len(self.files) < 2:
            print("\nNot enough files.")
            return

        left = 0
        right = len(self.files) - 1
        maximum = 0
        pair = ()

        while left < right:
            width = right - left
            height = min(self.files[left], self.files[right])
            area = width * height

            if area > maximum:
                maximum = area
                pair = (self.files[left], self.files[right])

            if self.files[left] < self.files[right]:
                left += 1
            else:
                right -= 1

        print("\nMaximum Capacity:", maximum)
        print(f"Using {pair[0]} MB and {pair[1]} MB")

    def compare_with_bruteforce(self):
        """Compare brute-force pair searching with the two-pointer approach."""
        target = int(input("Enter Target: "))

        print("\n========== Brute Force ==========")
        found = False

        for i in range(len(self.files)):
            for j in range(i + 1, len(self.files)):
                if self.files[i] + self.files[j] == target:
                    print(f"{self.files[i]} MB + {self.files[j]} MB = {target} MB")
                    found = True

        if not found:
            print("No Pair Found")

        print("\n========== Two Pointers ==========")
        self.find_pair(target)


def menu():
    files = [120, 15, 200, 40, 15, 60, 180, 75, 90]
    manager = SmartFileOrganizer(files)

    while True:
        print("\n========== SMART FILE ORGANIZER ==========")
        print("1. Display Files")
        print("2. Sort Files")
        print("3. Remove Duplicates")
        print("4. Find Pair")
        print("5. Find All Pairs")
        print("6. Closest Pair")
        print("7. Pair Smallest & Largest")
        print("8. Partition Files")
        print("9. Remove Large Files")
        print("10. Compress Duplicates")
        print("11. Maximum Container")
        print("12. Compare Algorithms")
        print("0. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            manager.display_files()
        elif choice == "2":
            manager.sort_files()
        elif choice == "3":
            manager.remove_duplicates()
        elif choice == "4":
            target = int(input("Target Size: "))
            manager.find_pair(target)
        elif choice == "5":
            target = int(input("Target Size: "))
            manager.find_all_pairs(target)
        elif choice == "6":
            target = int(input("Target Size: "))
            manager.closest_pair(target)
        elif choice == "7":
            manager.pair_smallest_largest()
        elif choice == "8":
            limit = int(input("Partition Limit: "))
            manager.partition_files(limit)
        elif choice == "9":
            limit = int(input("Remove files larger than: "))
            manager.remove_large_files(limit)
        elif choice == "10":
            manager.compress_duplicates()
        elif choice == "11":
            manager.max_container()
        elif choice == "12":
            manager.compare_with_bruteforce()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()