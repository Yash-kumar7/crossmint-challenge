# Astral Object Creation Script

This script is designed to interact with the Crossmint API to create various astral objects, such as Polyanets, Soloons, and Comeths, based on a given goal map.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)

## Usage

1. Ensure you have Python installed on your system.
2. Install the Requests library using `pip install requests`.
3. Replace the `CANDIDATE_ID` variable with your own candidate ID provided by Crossmint.
4. Adjust the `API_BASE_URL`, `MAX_RETRIES`, and `RETRY_DELAY` variables if necessary.
5. Run the script using `python script_name.py`.

## Functionality

- `create_polyanet(row, column)`: Creates a Polyanet at the specified row and column.
- `create_soloons(row, column, color)`: Creates Soloons of a specified color at the given row and column.
- `create_cometh(row, column, direction)`: Creates a Cometh with a specified direction at the provided row and column.
- `send_request_with_retry(endpoint, data)`: Sends a request to the API endpoint with retry logic in case of failure.
- `create_astral_objects_from_goal_map()`: Fetches the goal map from the API and creates astral objects based on it.

## Notes

- The `get_goal_map()` function retrieves the goal map from the API.
- The script iterates through the goal map and creates astral objects according to the specified criteria.
- Retries are attempted in case of failure to create an astral object.
- The script can be further customized or integrated into larger automation workflows as needed.
