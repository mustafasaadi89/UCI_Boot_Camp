import csv
import os





for i in range (1,20):
    path="budget_data_"+str(i)+".csv"
    if os.path.isfile("raw_data/"+path)== True:
        appended_path="appended_"+path
        csv_path=os.path.join("raw_data",path)
        #print(csv_path)
        total_months=0
        total_revenue=0
        total_change=0
        total_change=0
        greatest_increase=0
        greatest_decrease=0
        prior_value = 0
        with open(csv_path,newline="") as csv_file:
            current_file=csv.reader(csv_file)
            next(csv_file)
            for row in current_file:
                total_months=total_months+1
                total_revenue=total_revenue+float(row[1])
                #print(total_months)
                #print(total_revenue)
                if prior_value != 0:
                    current_value=float(row[1])
                    change=(current_value-prior_value)
                    if change > greatest_increase:
                        greatest_increase=change
                        total_change=total_change+change
                        prior_value=float(row[1])

                    elif change < greatest_decrease:
                        greatest_decrease = change
                        total_change=total_change+change
                        prior_value=float(row[1])
                    
                    else:
                        total_change=total_change+change
                        prior_value=float(row[1])
                
                else:
                    prior_value=float(row[1])
                average_change= total_change / total_months
            
            print("FINANCIAL ANALYSIS")
            print("----------------------------------")
            print("Total Months: " + str(total_months))
            print("Total Revenue: "+ str(total_revenue))
            print("Average Revenue Change: "+ str(average_change))
            print("Greatest Increase in Revenue: "+ str(greatest_increase))
            print("Greatest Decrease in Revenue: "+ str(greatest_decrease))
            with open(appended_path,"a",newline="") as newfile:
                csv_writer=csv.writer(newfile, delimiter=",")
                csv_writer.writerow(["FINANCIAL ANALYSIS"])
                csv_writer.writerow("[_____________________________________________________]")
                csv_writer.writerow(["Total Months:", total_months])
                csv_writer.writerow(["Total Revenues:", total_revenue])
                csv_writer.writerow(["Average Revenue Change:", average_change])
                csv_writer.writerow(["Greatest Increase in Revenue:", greatest_increase])
                csv_writer.writerow(["Greatest Decrease in Revenue:", greatest_decrease])
    else:
        print("no more files")
        break