import json
from analyzer import analyze_job

#Loads Job List
def load_jobs():
    try:
        with open("JobAnalyzer/jobxs.json", "r") as file:
            return json.load(file)
    except:
        print("jobs.json is missing!")
        return []

def show_jobs(jobs):
    for i, job in enumerate(jobs[:5], 1):
        print(f"\n {i}. {job['title']} - {job['company']}")
    
def main():
    jobs = load_jobs()
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
if __name__ == "__main__":
    main()