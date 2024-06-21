from data import get_data, clean_data
from proccesing import stat


def main():
    filename = 'temp.txt'
    data = get_data(filename)
    temp = clean_data(data)
    stats_data = stat(temp)

    if stats_data:
        print(f"Minimum Temperature: {stats_data['min']}°C")
        print(f"Maximum Temperature: {stats_data['max']}°C")
        print(f"Average Temperature: {stats_data['mean']:.2f}°C")
        print(f"Median Temperature: {stats_data['median']:.2f}°C")
    else:
        print("No temperature data available.")


if __name__ == '__main__':
    main()
