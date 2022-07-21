# K-Jo (k-jo@oxdynamics.com) - Oxford Dynamics - July 2022
#
# This script converts GIFs from ShapeNet into mp4-formats. Furthermore,
# it extracts the corresponding captions from the dataset csv-file.

import pandas as pd
import moviepy.editor as mp
import os

df = pd.read_csv("/Users/kerri/Documents/programming/Udemy Codes/Gifs/metadata.csv")
column_object = df['wnlemmas']
column_captions = df['name']
static_path = "/Users/kerri/Desktop/models-screenshots/screenshots/"
static_video_name = "video"

exact_caption = True # does the user wants to get exact caption

if exact_caption == True:
    video_captions = open("video_captions_exact.csv","a")
elif exact_caption == False:
    video_captions = open("video_captions_simple.csv","a")

for i in range(0, column_object.shape[0]):
    try:
        element_of_first_column = df["fullId"][i]
        if column_object[i] == 'bed' or column_object[i] == 'table':
            if exact_caption == True:
                processed_caption = " ".join(column_captions[i].split())
            elif exact_caption == False:
                if column_object[i] == 'bed':
                    processed_caption = 'bed'
                elif column_object[i] == 'table':
                    processed_caption = 'table'
            video_captions.write("video" + str(i) + ": " + processed_caption + "\n")

            dynamic_path = element_of_first_column[4:]
            full_path = static_path + dynamic_path + "/" + dynamic_path + ".gif"
            clip = mp.VideoFileClip(full_path)

            dynamic_video_name = str(i)
            full_video_name = static_video_name + dynamic_video_name + ".mp4"
            clip.write_videofile(full_video_name)
    except:
        pass

video_captions.close()
