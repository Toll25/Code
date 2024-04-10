# This is a sample Python script.
import statistics
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mList = [int(e) if e.isdigit() else e for e in "4,5,7,11,4,3,6,11,11,10,11,15,4,9,6,5,15".split(',')]
    print("Mode:", statistics.mode(mList))
    print("Median:", statistics.median(mList))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
