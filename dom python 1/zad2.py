sekunda = int(input("Sekunda u danu:"))

hh = sekunda / 3600
mm = (sekunda % 3600) / 60
ss = sekunda - int(hh)*3600 - int(mm)*60

print(str(int(hh))+ ":" + str(int(mm)) + ":" + str(ss))