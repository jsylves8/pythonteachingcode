!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
     
mean_temp = open("mean_temp.txt", "r")
print("\n\n" + mean_temp.read())

mean_temp = open("mean_temp.txt", "a+")

mean_temp.write("Rio de Janeiro,Brazil,30.0,18.0\n")

mean_temp.seek(0)

headings = mean_temp.readline().split(",")

print(headings)

city_temp = mean_temp.readline().split(",")

city_temp