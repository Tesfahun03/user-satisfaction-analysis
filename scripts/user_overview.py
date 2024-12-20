
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt


def user_behavior(data, application):

    # Step 1: Ensure the 'Start' and 'End' columns are in datetime format
    data['Start'] = pd.to_datetime(data['Start'])
    data['End'] = pd.to_datetime(data['End'])

    # Step 2: Calculate session duration in seconds (or ms if needed)
    data['Duration (s)'] = (data['End'] - data['Start']).dt.total_seconds()

    # Step 3: Group by user (e.g., IMSI) and application type (e.g., 'Application')
    aggregated_data = data.groupby(['IMSI', application]).agg(
        num_sessions=('Bearer Id', 'count'),  # Number of sessions per user and app
        total_duration=('Duration (s)', 'sum'),  # Total duration of sessions in seconds
        total_dl=('Total DL (Bytes)', 'sum'),  # Total download data in Bytes
        total_ul=('Total UL (Bytes)', 'sum'),  # Total upload data in Bytes
        #total_data_volume=('Total Data Volume (Bytes)', 'sum')  # Total data volume (DL + UL)
    ).reset_index(drop = True)

    return aggregated_data