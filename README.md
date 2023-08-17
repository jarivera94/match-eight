# Pair Sum Finder

This is a simple Python script that finds pairs of integers from a list that sum to a given value.

## Prerequisites

You'll need to have Python 3.x installed on your system to run this script.

## Usage

1. Clone this repository to your local machine or download the `app.py` file.

2. Open a terminal or command prompt.

3. Navigate to the directory where the `app.py` file is located.

4. Run the script by using the following command:

```
python app.py <list_of_numbers> <target_sum>
```

Replace `<list_of_numbers>` with a comma-separated list of integers and `<target_sum>` with the target sum you want to find pairs for.

For example:

```
python app.py 1,9,5,0,20,-4,12,16,7 12
```


5. The script will output pairs of integers that sum to the target value.

## Example

Given the input:

```
python app.py 1,9,5,0,20,-4,12,16,7 12
```



## Notes

- The script uses a dictionary to efficiently find pairs, making it faster than O(n^2).
- Input should be provided as a comma-separated list of integers.
- Ensure that the input format follows the provided example (no spaces between integers and commas).

Feel free to modify and improve the script as needed for your use case.



