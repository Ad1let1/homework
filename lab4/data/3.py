from datetime import datetime

def drop_microseconds(dt):
    return dt.replace(microsecond=0)

if __name__ == "__main__":
    current_dt = datetime.now()
    dt_without_micro = drop_microseconds(current_dt)
    
    print("Original datetime:", current_dt)
    print("Datetime without microseconds:", dt_without_micro)