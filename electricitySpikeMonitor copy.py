import csv
from datetime import datetime


with open('ap_sensor_comparison.csv') as csvfile:
    sensor_data = csv.reader(csvfile)
    header = next(sensor_data)
    mydata = [row for row in sensor_data]


def find_losses(data):
    list_delta = []
    gain_list = []
    with open('sensorNetworkLog.txt', 'a') as f:
        for irow, index in enumerate(data):
            if float(data[irow][1]) > float(data[irow][2]):
                f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                f.write(" Current loss found at sensor: ")
                f.write("%s" % data[irow][0])
                f.write(" First sensor value: ")
                f.write("%s" % data[irow][1])
                f.write(" Second sensor value: ")
                f.write("%s" % data[irow][2])
                f.write("\n")
                list_delta.append((float(data[irow][1]) - float(data[irow][2])))
    return list_delta


def cal_loss_total(list_of_losses):
    delta_total = 0
    for krow in list_of_losses:
        delta_total += krow
    return delta_total


loss_data = (find_losses(mydata))

print("Total number of losses: ")
print (len(loss_data))

print("Cumulative value of losses: ")
print(cal_loss_total(loss_data))


















