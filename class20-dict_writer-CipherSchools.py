from csv import DictWriter
with open("file.csv","w") as f:
          csv_writer = DictWriter(f,fieldness=["firstname","lastname","age"])
          csv_writer.writeheader()
          csv_writer.writerow({
                    "firstname" : "harshit",
                    "lastname": "vasistha",
                    "age": 500
          })
          csv_writer.writerow({
                    "firstname" : "mohit",
                    "lastname": "vasistha",
                    "age": 500
          })
          # writerows([
          #           {"firstname": "harshith","lastname": "vasistha","age": 500},
          #           {"firstname": "harshith","lastname": "vasistha","age": 500},
          #           {"firstname": "harshith","lastname": "vasistha","age": 500},
          # ])