While working on a web project, we give a (user id) to users who register on the site. However, if we are dealing with distributed systems, this may be a bit complicated for beginners. Thanks to this code, you can give a unique (user id) to every user registered in the system.


How does it work? 

We optionally collect some of the user's data. These data:

    -IP Address E.g:   192.168.1.1

    -MAC Address E.g:   68:7F:74:F2:EA:56

    -UUID E.g:    123456789014

Then optionally we adding a random number 1 to 100000000:

    -Number E.g:  8348349


We then put this data in order
data = f"{ip}{mac}{uuid}{number}

Then we hash this data



Usage:

Import file to project:

        from device_id.get_internal_device_id import get_internal_device_id

Function example:

        device_id = get_internal_device_id(mac_address=True,ip_address=True,uuid=True,randomizer=False)
        print(device_id)


While creating this id, you can determine what data it contains. The example above is default. By setting the randomizer option to True, you can add a random number between 1 and 100000000 to the end of the data set before hashing.

Values ​​you mark as False will return to 0 by default.
