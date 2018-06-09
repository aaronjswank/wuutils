# Weather Underground Utility

This is a simple utility for pushing data to Weather Underground.

## Installation

Install code requirements using
```
pip install -r requirements.txt
```

Install the package using pip, ie:
```
pip install .
```

## Usage Instructions

If you do not already have one, first create a user account with 
Weather Underground.  Next, register a personal weather station to
obtain a station ID and key.

It is suggested to use a utility such as dotenv or similar for storing
the credentials for accessing the Weather Underground station.  Here
we use the dotenv package as an example.  Create a file `.env` with the
following contents, replacing the `<KEY>` and `<ID>` with the
credentials supplied by Weather Underground after a personal
weather station is registered.

```
# Environment Variable File for Program
# optional: setup with bash export command prefix to allow source .env

# Set the Username
export SECRET_ID=<ID>

# Set the secret key
export SECRET_KEY=<KEY>
```

To send weather data, simply create a dictionary with the weather
data fields as specified by the 
[personal weather station upload protocol][1].
Data can then be pushed using
```
from wuutils.wuutils import wupush

wupush(station=SECRET_ID, password=SECRET_KEY, wdata=wdata)
```
A complete example is found in the `examples` directory.

[1]: http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
