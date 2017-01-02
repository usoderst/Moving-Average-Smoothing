import os
import csv
import matplotlib.pyplot as plt
#Ulrik Soderstrom

out_file = input("Please enter new csv file name: WARNING: include quotations ")
#out_file = "output.csv"

path = input("Enter path to a folder with data ")


Colsmooth = int(input('Please enter which column by number you wish to smooth: '))

Colrange = int(input('Please enter the moving average value: '))

temp = []
count = 0

for filename in os.listdir(path):
    print("Reading in file: ")
    print(filename)
    if count != 0:
        Data_File = open(path+filename, "r")
        first_line = Data_File.readline()
        for line in Data_File:
            line_list = [x.strip() for x in line.lower().split(",")]
            if line_list[Colsmooth] == 'na':
                line_list[Colsmooth] = holder_temp
            temp.append(float(line_list[Colsmooth]))
            holder_temp = line_list[Colsmooth]
    else:
        count += 1

def ma(temperature, range_):
    value = [] #initial value
    counter = 0
    for i in range(0,len(temperature)-1):
        if(counter >= len(temperature)-range_):
            return value
        else:
            #moving avererage processing
            s = sum(temperature[counter:counter+range_])
            value.append(s/range_)
        counter +=1


Smoothed_Column = ma(temp, Colrange)

counter = 0

xaxis = []
yaxis = []

Smoothed_Data = [[] for _ in range(len(Smoothed_Column)+Colrange)]


for line in Smoothed_Column:
    if counter <= Colrange:
        for i in range(0, Colrange):
            Smoothed_Data[counter].append(counter)
            Smoothed_Data[counter].append("NA")
            yaxis.append(0)
            xaxis.append(counter)
            counter += 1
    Smoothed_Data[counter].append(counter)
    Smoothed_Data[counter].append(line)
    yaxis.append(line)
    xaxis.append(counter)
    counter += 1

fig, ax = plt.subplots()

Title = "Smoothed Data" 

ax.plot(xaxis,yaxis, label ="Smoothed Data")
ax.plot(xaxis,temp, label = "Raw Data")

legend = ax.legend(loc='upper center', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
for label in legend.get_texts():
    label.set_fontsize('large')
for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

fig.suptitle('Moving Average Smoothing by ' + str(Colrange))

fig.savefig(filename + 'MAplot' + str(Colrange) + '.pdf')



output = (filename + "MAsmoothed" + str(Colrange))

new_header = []
new_header.append("CT")

with open(out_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(new_header)
    writer.writerows(Smoothed_Data)

print("Done...")