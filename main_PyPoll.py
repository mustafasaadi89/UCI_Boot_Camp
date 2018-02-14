import csv
import os
import csv

for i in range(1,20):
    path="election_data_"+str(i)+".csv"
    if os.path.isfile("raw_data/"+path)== True:
        appended_path="appended_"+path
        csv_path=os.path.join("raw_data",path)
        total_votes=0

        list_candidate=[]
        candidate_votes=dict()
        #print(csv_path)
        with open(csv_path,newline="") as csv_file:
            current_file=csv.reader(csv_file)
            next(csv_file)
            for row in current_file:
                list_candidate.append(row[2])
                total_votes=total_votes+1   
                
            for j in list_candidate:
                candidate_votes[j]=candidate_votes.get(j,0)+1


            print("Election Results")
            print("-------------------------------")
            print("Total Votes: "+str(total_votes))
            print("--------------------------------")
            for key, value in candidate_votes.items():
                print(key+" : "+"{:.2%}".format((float(value)/total_votes))+" (" +str(value)+")")
            print("--------------------------")
            winner=max(candidate_votes,key=candidate_votes.get)
            print(winner)
            print("-----------------------------")
            with open(appended_path,"a",newline="") as newfile:
                csv_writer=csv.writer(newfile, delimiter=",")
                csv_writer.writerow(["Election Results"])
                csv_writer.writerow(["---------------------------"])
                csv_writer.writerow(["Total Votes: ",total_votes])
                csv_writer.writerow(["---------------------------"])
                for key,value in candidate_votes.items():
                    csv_writer.writerow([key,"{:.2%}".format((float(value)/total_votes)),value])
                csv_writer.writerow(["-------------------"])
                csv_writer.writerow(["Winner",winner])

    else:
        print("no more files")
        break
    
