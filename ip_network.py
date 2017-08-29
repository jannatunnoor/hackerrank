__author__ = 'jnoor'
ip = '172.16.8.1'
ip_list = ['192.168.8.8', '172.16.0.1', '117.0.0.1', '103.12.10.10', None , '', '100.a.b.10', '0.0.0.0', '-1.2.3.4','1.2']


def is_valid_ip(ip):
    try:
        parts = ip.split('.')
        return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
    except ValueError:
        return False # one of the 'parts' not convertible to integer
    except (AttributeError, TypeError):
        return False # `ip` isn't even a string

def valid_ip_list(ip_list):
    return [ip for ip in ip_list if is_valid_ip(ip)]

print valid_ip_list(ip_list)

print('********************************************************')

def ip_to_network(ip):
    octet = ip.split('.')
    if int(octet[0]) <= 127:
        return "%s.0.0.0"%(octet[0])
    elif 127 < int(octet[0]) < 192:
        return "%s.%s.0.0"%(octet[0],octet[1])
    else:
        return "%s.%s.%s.0"%(octet[0],octet[1],octet[2])


net = ip_to_network(ip)
print net

ip_list = ['192.168.8.8', '172.16.0.1', '117.0.0.1', '103.12.10.10', '38.108.92.110', '127.0.1.50', '192.168.8.2']
ip_list1 = []
net_list = set([ip_to_network(x) for x in ip_list1])

if ip_to_network(ip) in net_list:
    print True

print net_list
print('################')

auth_server_list = ''.split(',')
print auth_server_list
valid_auth_server_list = [ip for ip in auth_server_list if is_valid_ip(ip)]
auth_network_list = set([ip_to_network(x) for x in valid_auth_server_list])
print valid_auth_server_list, auth_network_list

