tickets = [['a1', 'a2'], ['a3', 'a4'], ['a2', 'a3']]

cities = {}
src_dest = {}

for a_ticket in tickets:
    src_dest[a_ticket[0]] = a_ticket[1]
    for a_city_idx in [0, 1]:
        if a_ticket[a_city_idx] in cities:
            cities[a_ticket[a_city_idx]][0] += 1
        else:
            cities[a_ticket[a_city_idx]] = [1, True]
        if a_city_idx:
            cities[a_ticket[a_city_idx]][1] = False

# print(cities)
# print(src_dest)


def find_src(cities):
    for a_city in cities:
        if cities[a_city][1]:
            src = a_city
            break
    return src


src = find_src(cities)
print('The source is %s' % find_src(cities))


def find_route(src, src_dest):
    path = [src]
    while src in src_dest:
        src = src_dest[src]
        path.append(src)
    return path


print('The path is %s' % (find_route(src, src_dest)))
