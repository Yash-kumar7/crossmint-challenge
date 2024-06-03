import requests
import time

API_BASE_URL = "https://challenge.crossmint.io/api"
CANDIDATE_ID = "ed63c440-58f9-4978-920d-bbb86390a497"
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds

def create_polyanet(row, column):
    return send_request_with_retry("polyanets", {"row": row, "column": column})

def create_soloons(row, column, color):
    return send_request_with_retry("soloons", {"row": row, "column": column, "color": color})

def create_cometh(row, column, direction):
    return send_request_with_retry("comeths", {"row": row, "column": column, "direction": direction})

def send_request_with_retry(endpoint, data):
    retries = 0
    while retries < MAX_RETRIES:
        response = requests.post(f"{API_BASE_URL}/{endpoint}", json={**data, "candidateId": CANDIDATE_ID})
        if response.ok:
            print(f"{endpoint.capitalize()} created at ({data['row']}, {data['column']})")
            return True
        else:
            print(f"Failed to create {endpoint.capitalize()} at ({data['row']}, {data['column']}): {response.text}")
            retries += 1
            time.sleep(RETRY_DELAY)
    print(f"Maximum retries reached for creating {endpoint.capitalize()} at ({data['row']}, {data['column']})")
    return False

def create_astral_objects_from_goal_map():
    goal_map = get_goal_map()
    if not goal_map:
        return

    for row_index, row in enumerate(goal_map['goal']):
        for col_index, cell in enumerate(row):
            if cell == 'POLYANET':
                create_polyanet(row_index, col_index)
            elif cell.endswith('SOLOON'):
                color = cell.split("_")[0].lower()
                create_soloons(row_index, col_index, color)
            elif cell.endswith('COMETH'):
                direction = cell.split("_")[0].lower()
                create_cometh(row_index, col_index, direction)

def get_goal_map():
    response = requests.get(f"{API_BASE_URL}/map/{CANDIDATE_ID}/goal")
    if response.ok:
        return response.json()
    else:
        print(f"Failed to get goal map: {response.text}")
        return None

if __name__ == "__main__":
    create_astral_objects_from_goal_map()

