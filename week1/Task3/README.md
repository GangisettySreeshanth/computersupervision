# Week 1 - Task 3

## Objective

To merge a one-minute audio track with a video.

## Tools Used

* FFmpeg
* Pixabay (for audio source)

## Procedure

1. Downloaded a one-minute song from Pixabay.
2. Trimmed the audio to 60 seconds using FFmpeg.
3. Merged the trimmed audio with the video created in Task 2.

## Commands Used

Audio trimming:
ffmpeg -i song.mp3 -t 60 trimmed_audio.mp3

Merging audio with video:
ffmpeg -i output.mp4 -i trimmed_audio.mp3 -c:v copy -c:a aac -shortest final_video.mp4

## Output

* Final video with audio track added

## Learning Outcome

* Learned how to process audio using FFmpeg
* Understood how to merge audio and video streams

## Audio Source

https://pixabay.com/music/search/1%20minute/

