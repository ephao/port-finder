# Port Finder

This Python script helps you find unused ports on a specified host within a given range.

## Files

- `\main.py`: Main script to run the port finder
- `\utils.py`: Utility functions for checking ports
- `\config.py`: Configuration settings

## Usage

Run the script from the command line with the following syntax:

```
python main.py <start_port> <end_port> [--host <hostname>]
```

Example:
```
python main.py 8000 9000
```

This will check for unused ports between 8000 and 9000 on localhost.

To specify a different host:
```
python port-finder-main.py 80 100 --host example.com
```

## Requirements

- Python 3.6 or higher

## Configuration

You can modify default settings in the `config.py` file:

- `DEFAULT_HOST`: Default host to check (default: 'localhost')
- `MIN_PORT` and `MAX_PORT`: Allowed port range
- `DEFAULT_START_PORT` and `DEFAULT_END_PORT`: Default port range if not specified

## License

This project is open source and available under the [MIT License](LICENSE).
