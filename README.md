# Image-to-Video Converter using FFMPEG

This script is a simple Python tool that takes all images in a specified folder and converts them into a video using FFMPEG. The resulting video is saved as an MP4 file with customizable frame rate and output name.

## Prerequisites

To run this script, you need to have the following software installed on your system:

1. Python (3.6 or later)
2. FFMPEG

## Usage

Navigate to the directory containing the script and run it with Python. Here's the usage format:

```bash
python image_to_video.py [-h] [-fr FRAME_RATE] [-o OUTPUT]
```

### Arguments:

- `-h`, `--help`: Show the help message and exit.
- `-fr FRAME_RATE`, `--frame_rate FRAME_RATE`: Frame rate of the output video. Default is set to 30 frames per second.
- `-o OUTPUT`, `--output OUTPUT`: Output name of the video. Default is "output.mp4".

### Example:

To convert all supported images in the current working directory to a video with a frame rate of 25 and save it as "my_video.mp4", use the following command:

```bash
python image_to_video.py -fr 25 -o my_video
```

## Supported Image Formats

This script supports the following image formats: JPEG (.jpg, .jpeg) and PNG (.png). It will only process files with these extensions in the specified folder.