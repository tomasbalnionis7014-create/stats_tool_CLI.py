from collections import Counter


def main():

    def calculate_mean(data):
        return sum(data) / len(data)

    def calculate_median(data):
        sorted_data = sorted(data)
        x = len(sorted_data)
        if x % 2 == 0:
            return (sorted_data[x // 2 - 1] + sorted_data[x // 2]) / 2
        else:
            return sorted_data[x // 2]

    def calculate_mode(data):
        data_counter = Counter(data)
        max_count = max(data_counter.values())
        modes = [k for k, v in data_counter.items() if v == max_count]
        if len(modes) == len(data):
            return None  # No mode
        return modes

    def calculate_standard_deviation(data):
        mean_value = calculate_mean(data)
        squared_differences = [(y - mean_value) ** 2 for y in data]
        variance = sum(squared_differences) / len(data)
        return variance ** 0.5

    def get_number_of_data_points():
        while True:
            no_of_numbers = input(
                "Enter how many pieces of data you will be dealing with: ")
            try:
                no_of_numbers = int(no_of_numbers)
                if no_of_numbers <= 0:
                    print(
                        "Please enter a positive integer for the number of data points.")
                    continue
                if no_of_numbers == 1:
                    print("You need at least two data points to calculate statistics.")
                    continue
                return no_of_numbers
            except ValueError:
                print("Invalid input. Please enter a valid integer you silly billy.")

    def get_data(n):
        data = []
        for i in range(n):
            while True:
                number = input(f"Enter data point {i + 1}: ")
                try:
                    number = float(number)
                    data.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        return data

    n = get_number_of_data_points()
    data = get_data(n)

    options = [
        "1) Calculate mean",
        "2) Calculate median",
        "3) Calculate mode",
        "4) Calculate standard deviation",
        "5) Exit",
        "6) Enter new dataset"
    ]

    while True:
        print("\nPlease choose an option:")
        for option in options:
            print(option)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print(f"The mean of your dataset given is: {calculate_mean(data)}")
        elif choice == "2":
            print(
                f"The median of your dataset given is: {calculate_median(data)}")
        elif choice == "3":
            mode = calculate_mode(data)
            if mode is None:
                print("There is no mode in the dataset as all values are unique.")
            else:
                print("The mode(s) of your dataset given is/are:",
                      ", ".join(map(str, mode)))
        elif choice == "4":
            print(
                f"The standard deviation of your dataset given is: {calculate_standard_deviation(data)}")
        elif choice == "5":
            print("Thanks for using the stats tool, gang 😎")
            break
        elif choice == "6":
            n = get_number_of_data_points()
            data = get_data(n)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
