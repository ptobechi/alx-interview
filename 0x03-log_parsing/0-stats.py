#!/usr/bin/python3
import sys
import signal

# Global variables to store the metrics


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """ Function to print the statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """ Signal handler to print stats on keyboard interruption """
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            # Extracting the status code and file size
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Updating the metrics
            if status_code in status_counts:
                status_counts[status_code] += 1
            total_size += file_size
            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()
        except (ValueError, IndexError):
            continue
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
