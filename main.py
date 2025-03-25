"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    open_file = open(filename, "r")
    data = open_file.read()

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    data = filter_nondigits(data)
    
    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    time = list(range(len(data)))
    plt.figure(figsize=(14,6))
    plt.plot(time, data, marker='o', linestyle='-', color='blue', label="Heart Rate")
    plt.title("Health Monitoring Data - Heart Rate")
    plt.xlabel("Times")
    plt.ylabel("Heart Rate (BPM)")
    plt.legend()
    plt.grid(True)

    plt.savefig("images/"+filename[5:11]+".jpg", dpi=300)
    plt.close()

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(data)
    max_hr = maximum(data)
    std_dev_hr = standard_deviation(data)

    # return all 3 values
    print(data)
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
