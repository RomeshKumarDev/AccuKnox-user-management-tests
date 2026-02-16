from collections import Counter

log_file = 'access.log'

ip_addresses = []
page_list = []
error_pages = 0

with open(log_file, 'r') as file:
    for line in file:
        data = line.split()

        ip_addresses.append(data[0])     
        page_list.append(data[6])       
        status_code = data[7]            
        if status_code == '404':
            error_pages += 1

print("Log Analysis Report")
print(f"Total requests: {len(ip_addresses)}")
print(f"Unique IP addresses: {len(set(ip_addresses))}")

print("\nTop Pages:")
for page, count in Counter(page_list).most_common(5):
    print(page, "-", count)

print("\nTop IPs:")
for ip, count in Counter(ip_addresses).most_common(5):
    print(ip, "-", count)

print("\nTotal 404 errors:", error_pages)
