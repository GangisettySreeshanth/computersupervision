# WT2 - Image Resizing using FFmpeg

## Objective

Resize images to smaller dimensions while preserving aspect ratio.

## Tool Used

* FFmpeg

## Command Used

for %f in (*.jpg) do ffmpeg -i "%f" -vf scale=384:-1 "resized_images%f"

## Explanation

* Width resized to 384 pixels
* Height automatically adjusted
* Aspect ratio preserved

## Output

Resized images stored in `resized_images/`

## Learning Outcome

* Learned image preprocessing for YOLO
* Understood importance of aspect ratio preservation

