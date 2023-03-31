import requests
from multiprocessing import Pool

url = "http://localhost:8000/add_answer/"

def send_request(x):
    answer = {"answer": "coal"}
    response = requests.post(url, json=answer)
    return response.status_code
    
def main():
    with Pool(16) as p:
        print(p.map(send_request, range(10_000)))
    
if __name__ == "__main__":
    main()