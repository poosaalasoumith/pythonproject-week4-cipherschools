from csv import writer
with open("class17-file.csv","w") as f:
          csv_writer=writer(f)
          csv_writer.writerow(["name","country"])
          csv_writer.writerow(["mohit","INDIA"])
          csv_writer.writerow(["harshit","INDIA"])

          # writerows([["name","country"],["mohit","INDIA"],["harshit","INDIA"]])