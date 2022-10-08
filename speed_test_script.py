# Based on: https://www.educative.io/answers/how-to-detect-internet-speed-using-python
# speedtest-cli is compatible with Python up to 3.7

import speedtest


def bytes_to_mb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return bytes / MB


speed_test = speedtest.Speedtest(secure=True)
speed_test.get_best_server()

speed_test.download()
speed_test.upload()

results = speed_test.results.dict()

print(results["timestamp"])
print("Your Download speed is", round(bytes_to_mb(results["download"]), 2), " Mb.")
print("Your Upload speed is", round(bytes_to_mb(results["upload"]), 2), " Mb.")
