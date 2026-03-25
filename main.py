import json
from analyzer import analyze_job

#Loads Job List
def load_jobs():
    try:
        with open("JobAnalyzer/jobs.json", "r") as file:
            return json.load(file)
    except:
        print("\nFile 'jobs.json' is missing/invalid!")
        print("Please run Job Scraper to generate file.")
        print("Exiting program.\n")
        return False
    
#Display jobs
def show_jobs(jobs):
    for i, job in enumerate(jobs[:5], 1):
        print(f"\n {i}. {job['title']} - {job['company']}")

#Saves analysis
def save_analysis(result):
    with open("JobAnalyzer/analysis.txt", "a") as file:
        file.write(result + "\n")

#Clears analysis.txt
def clear_analysis():
    with open("JobAnalyzer/analysis.txt", "w") as file:
        pass

#Main logic
def main():
    jobs = load_jobs()
    if not jobs:
        return
    while True:
        print("\n1.Show jobs")
        print("2.Analyze jobs")
        print("3.Analyze specific job")
        print("4.Clear analysis file")
        print("5.Exit")
        choice = input("\nEnter option: ")

        #Show jobs option
        if choice == "1":
            show_jobs(jobs)
            continue

        #Analyze jobs (all)
        elif choice == "2":
            for i, job in enumerate(jobs[:5], 1):
                print(f"\n{i}. {job['title']} - {job['company']}")

                result = analyze_job(job)
                save_analysis(result)
                print(result) 
            continue

        #Analyze job (specified)
        elif choice == "3":
            job_choice = (input("Enter job index: "))

            #Check if input is a digit
            if job_choice.isdigit():
                job_choice = int(job_choice)
            else:
                print("\nThats not a number!")
            if 1 <= job_choice <= len(jobs): #Check if entered index exists
                for i, job in enumerate(jobs, 1):
                    if i == job_choice:
                        print(f"{i}. {job['title']} - {job['company']}")
                        result = analyze_job(job)
                        print(result)
                        save_analysis(result)
            else:
                print("\nIndex does not exist.")

        #Clear analysis file
        elif choice == "4":
            confirm = input ("Are you sure?: (y/n)").lower()
            if confirm == "y":
                clear_analysis()
        elif choice == "5":
            break
        else:
            print("\nOption does not exist!")
            continue
if __name__ == "__main__":
    main()