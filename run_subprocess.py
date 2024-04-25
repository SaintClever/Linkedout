import os, subprocess, time


def loading(count):
        print(f"Loading {count * "."}")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")



def subprocess_runner():
    model_process = subprocess.Popen(["python3", "-m", "models.models"])
    jobs_process = subprocess.Popen(["python3", "-m", "job_boards.jobs_to_db"])
    pandas_data_process = subprocess.Popen(["python3", "-m", "data_analysis.pandas_data.data_manipulation"])
    pandas_csv_process = subprocess.Popen(["python3", "-m", "data_analysis.pandas_data.data_to_csv"])

    count = 0
    while model_process.poll() == None or jobs_process.poll() == None or pandas_data_process.poll() == None or pandas_csv_process.poll() == None:
        loading(count)

        if model_process.poll() != None:
            print("Model process completed succesfully")

        if jobs_process.poll() != None:
            print("Jobs process completed succesfully")

        if pandas_data_process.poll() != None:
            print("Pandas data process completed succesfully")

        if pandas_csv_process.poll() != None:
            print("Pandas csv process completed succesfully")

        count += 1

subprocess_runner()
