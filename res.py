import os
import colorama
import pandas as pd


def summarize(path):
    # For each file in specified path
    test_num = 0
    for file in os.listdir(path):
        # If the file is a csv file
        if file.endswith('.csv'):
            test_num += 1
            # open as dataframe
            df = pd.read_csv(f"{path}/{file}")
            # get rows that have a value of 'download' for the direction column
            downloads = df[df['direction'] == 'download']
            uploads = df[df['direction'] == 'upload']

            download_90th = round(downloads['bps'].quantile(.9) / 1_000_000, 1)
            upload_90th = round(uploads['bps'].quantile(.9) / 1_000_000, 2)
            latency = round(downloads['latency'].head(20).median(), 1)

            # print summary
            print(f"{path}{colorama.Fore.BLUE} Test {str(test_num)}: {colorama.Fore.GREEN}{file}{colorama.Fore.RESET}")
            print(f"Download: {download_90th} Mbps")
            print(f"Upload: {upload_90th} Mbps")
            print(f"Latency: {latency} ms\n")


summarize("York_wifi")
summarize("York_cell")