![Header image with a dark purple background. There is an outline of a pink book to the left. To the right side, the words "DIY BOOK SCANNER" are depicted in pink and blue.](assets/readme_header.png)

This software is intended to streamline workflow for book scanning, specifically with the [Archivist DIY Book Scanner.](https://diybookscanner.org/archivist/) More specifically, it offers a front-end GUI where users can control camera and image processing settings and preview their images for digitization of printed materials.

Importantly, as this is part of my research in digital humanities methods, digitization, and archiving, **this software is in active development.** Many of the features listed below currently have the necessary framework to be fully functional, but development is ongoing and, naturally, things often break in the process. In the interest of making the process of learning software development more visible from the perspective of a new programmer, this software is publicly accessible, even if not yet complete. I will continue to update here as I near completion of the project, particularly with more documentation of that process.

## Proposed Features
- Capture images using DigiCamControl
- Offer user control over DSLR settings, including ISO, aperture, and shutter speed
- Uses trained YOLOv5 model to automatically detect edges of book pages for streamlined image cropping
- Offer user control over image post-processing settings, including image brightness, rotation, and contrast
- Combine images into an OCR-readable PDF

## Directory Structure
- `assets/`: Image files for GUI and project documentation
- `gui/`: Source code for GUI developed with tkinter and ttkbootstrap
- `scanning/`: Source code for the scanning workflow
- `utils/`: Various dev files that interact with both the scanning and GUI source code

## More information
To learn more about this project and my archival work, you can visit the [Fourth Ward Oral History Project website.](https://www.fourthwardhistory.org/crd702)