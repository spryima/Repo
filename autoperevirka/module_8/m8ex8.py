from collections import Counter


def get_count_visits_from_ip(ips):
    return list(Counter(ips))

def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]


print(get_count_visits_from_ip(ips = [
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.252",
    "85.157.172.252"
]))
print("+++")
print(get_frequent_visit_from_ip(ips = [
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.252",
    "85.157.172.252"
]))