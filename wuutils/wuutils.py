#!/bin/env python3

''' Utility to push weather data to wunderground '''


def wupush(station, password, wdata):
    ''' Push weather data to weather underground

        args:
             station     the station ID as registered with wunderground.com
             password    the password registered with this ID

             wdata       dict containing any of the weather field data per API
                         (Abbreviated list)

                         dateutc - [YYYY-MM-DD HH:MM:SS (mysql format)]
                                   (if not exist, wu server uses now )
                         winddir - [0-360]
                         windspeedmph - [mph]
                         windgustmph - [windgustmph ]
                         humidity - [%]
                         tempf - [temperature F]
                         rainin - [rain in]
                         dailyrainin - [daily rain in accumulated]
                         baromin - [barom in]
                         dewptf- [dewpoint F]
                         weather - [text] -- metar style (+RA)
                         clouds - [text] -- SKC, FEW, SCT, BKN, OVC
                         softwaretype - [text] ie: vws or weatherdisplay

        Ref: http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
    '''

    # Configuration Parameters
    # ........................
    import requests

    # Weather Underground URL
    # Ref:  http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
    # Note:  If browse to the following URL will get brief usage
    wu_url = 'https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php'      # noqa: E501

    # Create the Post data
    # .....................
    # Note:   fields ID and PASSWORD must be in caps.
    # Note:   Required fields: action, ID, PASSWORD, dateutc
    post_data = dict(wdata)

    # Add the ID and PASSWORD to the requests data
    post_data['ID'] = station
    post_data['PASSWORD'] = password

    # Add the action to indicate making weather data upload
    post_data['action'] = 'updateraw'

    # if the dateutc field not exist, tell server to use now()
    if 'dateutc' not in post_data.keys():
        post_data['dateutc'] = 'now'

    # HTTP GET Request
    r = requests.get(wu_url, params=post_data)

    # todo: check response text for 'success' or 'INVALIDPASSWORDID'
    # r.content returns b'success\n'
    # r.text also has 'success\n'

    # Return True if good response.
    # pylint: disable=E1101
    return (r.status_code == requests.codes.ok)
