from tqdm import tqdm
import time
import requests

chunk_size = 1024
for x in tqdm(range(100)):
    time.sleep(0.01)