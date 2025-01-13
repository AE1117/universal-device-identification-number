import platform
import uuid
import socket
import random
import hashlib


# Hasher
def hasher(data):
    # Encode the password as bytes
    data_bytes = data.encode('utf-8')

    # Use SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(data_bytes)

    # Get the hexadecimal representation of the hash
    return hash_object.hexdigest()


# get IP address
def get_ip_address():

    ip_address = None
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except Exception as e:
        print(f"Error~~IP-adress: {e}")
    return ip_address


# get MAC address
def get_mac_address():
    mac = None
    try:
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)])
    except Exception as e:
        print(f"Error~~MAC-adress: {e}")
    return mac


# Get UUID
def get_system_uuid():
    return uuid.uuid5(uuid.NAMESPACE_DNS, platform.node())


# Get random number
def get_random_number():
    return random.randint(1, 999999999)


def get_internal_device_id(mac_address=True, ip_address=True, uuid=True, randomizer=False):

    # MAC Address
    if mac_address == True:
        mac = get_mac_address()
        if mac is None:
            print(f"somtings gone wrong while getting universal device id.   Error~~MAC-adress: {mac}")
            exit(1)
    elif mac_address == False:
        mac = 0
    else:
        print(f"somtings gone wrong while getting universal device id.")
        exit(1)

    # IP Address
    if ip_address == True:
        ip = get_ip_address()
        if ip is None:
            print(f"somtings gone wrong while getting universal device id.   Error~~IP-adress: {ip}")
            exit(1)
    elif ip_address == False:
        ip = 0
    else:
        print(f"somtings gone wrong while getting universal device id.")
        exit(1)

    # UUID
    if uuid == True:
        try:
            system_uuid = get_system_uuid()
        except:
            print(f"somtings gone wrong while getting universal device id.   Error~~UUID")
            exit(1)
    elif uuid == False:
        system_uuid = 0
    else:
        print(f"somtings gone wrong while getting universal device id.")
        exit(1)

    # Randomizer
    if randomizer == True:
        number = get_random_number()
    else:
        number = 0


    # Create identifier
    device_identifier = f"{mac}{ip}{system_uuid}{number}"

    return hasher(data=device_identifier)
