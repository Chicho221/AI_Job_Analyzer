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

def show_jobs(jobs):
    for i, job in enumerate(jobs[:5], 1):
        print(f"\n {i}. {job['title']} - {job['company']}")
    
def main():
    jobs = load_jobs()
    if not jobs:
        return
    while True:
        print("\n1.Show jobs")
        print("2.Analyze jobs")
        print("3.Analyze specific job")
        choice = input("Enter option: ")

        #Show jobs option
        if choice == "1":
            show_jobs(jobs)
            continue

        #Analyze jobs (all)
        elif choice == "2":
            for i, job in enumerate(jobs[:5], 1):
                print(f"\n{i}. {job['title']} - {job['company']}")

                result = analyze_job(job)
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

            for i, job in enumerate(jobs, 1):
                if i == job_choice:
                    print(f"{i}. {job['title']} - {job['company']}")
                    result = analyze_job(job)
                    print(result)
                    break   
        else:
            print("\nOption does not exist!")
            continue
if __name__ == "__main__":
    main()