import os
import argparse
import subprocess

SUPPORTED_FORMATS = {"jpg", "jpeg", "png"}
FFMPEG_INPUT_NAME = "input.txt"

cwd = os.getcwd()

parser = argparse.ArgumentParser(
    description='Takes all images from cwd and converts them to an .mp4 video using FFMPEG')

parser.add_argument('-fr', '--frame_rate',
                    help='Frame rate of output video, default=30', type=int, default=30)
parser.add_argument(
    '-o', '--output', help='Output name of the video, default=output', type=str, default="output")

args = parser.parse_args()

input_files = ([f for f in os.listdir() if f.split('.')
               [-1] in SUPPORTED_FORMATS])
with open(FFMPEG_INPUT_NAME, "wb") as outfile:
    for file in input_files:
        outfile.write(f"file '{cwd}/{file}'\n".encode())

process_call = f'ffmpeg -r {args.frame_rate} -f concat -safe 0 -i {FFMPEG_INPUT_NAME} -c:v libx265 -preset fast -vf format=yuv420p {args.output}.mp4'
subprocess.call(process_call)

os.remove(FFMPEG_INPUT_NAME)
