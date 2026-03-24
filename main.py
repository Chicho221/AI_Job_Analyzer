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
        choice = input("Enter option: ")

        if choice == "1":
            show_jobs(jobs)
            continue
        elif choice == "2":
            for i, job in enumerate(jobs[:5], 1):
                print(f"\n{i}. {job['title']} - {job['company']}")

                result = analyze_job(job)
                print(result)
            continue
        else:
            print("\nOption does not exist!")
            continue
if __name__ == "__main__":
    main()