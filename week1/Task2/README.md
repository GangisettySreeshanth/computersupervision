# Week 1 - Task 2

## Objective

To extract 30 frames per second from a video and reconstruct it back into a video.

## Tools Used

* FFmpeg

## Procedure

1. Extracted frames at 30 FPS using FFmpeg.
2. Generated ~1800 images from a 1-minute video.
3. Reconstructed the images back into a video.

## Commands Used

Frame extraction:
ffmpeg -i input_video.mp4 -vf fps=30 frames/frame_%04d.jpg

Video reconstruction:
ffmpeg -framerate 30 -i frames/frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4

## Output

* Generated ~1800 frames
* Successfully reconstructed video

## Learning Outcome

* Understood frame rate concept
* Learned conversion between video and images
* Learned video reconstruction using FFmpeg

