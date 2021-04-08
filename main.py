from tests.all_tests import *


def main():
    print("Updating data")
    test_update_data()
    print("Getting latest price")
    test_get_latest_price()
    print("Getting price trend")
    test_get_price_trend()
    print("Test passed")

if __name__ == '__main__':
    main()