def find_pairs_with_sum(nums, target_sum):
    num_dict = {}  # A dictionary to store previously seen numbers
    
    for num in nums:
        complement = target_sum - num
        if complement in num_dict:
            print(f"+ {num},{complement}")
        num_dict[num] = True
    
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python app.py <list_of_numbers> <target_sum>")
        sys.exit(1)

    numbers = list(map(int, sys.argv[1].split(",")))
    target_sum = int(sys.argv[2])

    find_pairs_with_sum(numbers, target_sum)
