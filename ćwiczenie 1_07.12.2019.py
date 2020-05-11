
l = [1, 3, 5, 11, 13, 21, 43, 56]
l2 = []

for element_l in l:
    l2.append(element_l**2)
    print(l2)

names = ['ania', 'gosia', 'pawel', 'piotrek']
capitalized_names = [n.capitalize() for n in names]


stopnie = [45, 90, 180, 360]
radiany = []
for d in stopnie:
     rad = d*3.14/180
     radiany.append(rad)

radiany2 = [d*3.14/180 for s in stopnie]
#firstnames = [d['firstnmes'] for d in dict_list]

l = [ 10.3, 12.5, 18.1, 20.4, 16.3, 9.7]
temp_fah = []
for c in l:
    tf = c*1.8+32
    temp_fah.append(tf)
    temp_fah2 = [c*1.8+32 for c in l]
    print(temp_fah2)

#METODY







