import csv
import datetime

def get_surge(testDict = {}):  # Function that checks for surge
    surge_false = True  # tracks whether a surge has occurred
    warning_occurrence = False  # checks whether warning log has been started yet
    surge_active = False
    for x in range(2, len(testDict)):  # loop through data entries
        if float(testDict[str(x)]) > 3.25:  # Check if voltage in warning limit
            if warning_occurrence is False:  # if log has not started yet
                with open("warninglog.txt", "a") as text_file:  # start log
                    warning_occurrence = True  # set log as started
                    text_file.write("\n\nWarning occurred for analysis performed at: {}\n".format(datetime.datetime.now()))  # log header
            with open("warninglog.txt", "a") as text_file:  # write warning
                text_file.write("High energy value occurred at entry: {} value was {}\n".format(x, testDict[str(x)]))  # write warning instance
            if ((float(testDict[str(x)]) > 4.9) and (float(testDict[str(x-1)]) > 4.9)) or (surge_active and (float(testDict[str(x)]) > 4.9)):  # check if surge occurred
                if surge_active is False:
                    testDict[str(x-1)] = 3.25
                    with open("output.txt", "a") as text_file:  # write first surge occurrence
                        text_file.write("A surge occurred at {} starting at entry : {} value was: {} it was over limit by: {}\n"
                                        .format(datetime.datetime.now(), x, testDict[str(x)], float(testDict[str(x)])-4.9))
                surge_active = True  # set when surge is detected
                testDict[str(x)] = 3.25
                with open("output.txt", "a") as text_file:  # write surge occurrence
                    text_file.write("A surge occurred at {} continuing at entry : {} value was: {} it was over limit by: {}\n"
                                    .format(datetime.datetime.now(), x, testDict[str(x)], float(testDict[str(x)])-4.9))
                surge_false = False  # set that a surge occured
            else:
                if surge_active:
                    with open("output.txt", "a") as text_file:  # write surge occurrence
                        text_file.write(
                            "Surge stopped before {} before entry : {} \n\n"
                            .format(datetime.datetime.now(), x))
                surge_active = False
    if surge_false:  # log that no surge occurred if no surge occurred
        with open("output.txt", "a") as text_file:
            text_file.write("No surge occurred in data, analysis performed at: {}\n".format(datetime.datetime.now()))
    return testDict

myDict = {}
with open('aP_surge.csv', 'rb') as csvfile:
    csv_input = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csv_input:
        myDict[row[0]] = row[1]
output_dict = get_surge(myDict)
with open("fixed.txt", "w") as text_file:
    for key, value in output_dict.iteritems():
        text_file.write("{},{}\n".format(key, value))

