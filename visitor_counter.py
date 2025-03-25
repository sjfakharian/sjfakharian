import json


COUNTER_FILE = "counter.json"


def read_counter():
    try:
        with open(COUNTER_FILE, "r") as f:
            data = json.load(f)
            return data.get("visits", 0)
    except FileNotFoundError:
        return 0


def update_counter(count):
    with open(COUNTER_FILE, "w") as f:
        json.dump({"visits": count}, f)


def increment_counter():
    count = read_counter() + 1
    update_counter(count)
    return count

# اجرای اسکریپت
if __name__ == "__main__":
    new_count = increment_counter()
    print(f"Total Visits: {new_count}")
