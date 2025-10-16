import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(" ")
    return {   
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': " ".join(parts[3:])
    }

# Example usage  
line = "2024-01-22 08:30:01 INFO User logged in successfully."
result = parse_log_line(line)
print(result)  # {'date': '2024-01-22', 'time': '08:30:01', 'level': 'INFO', 'message': 'User logged in successfully.'}




#def load_logs(file_path):




#def filter_logs_by_level(logs, level):



#def count_logs_by_level(logs):



#def display_log_counts(counts):