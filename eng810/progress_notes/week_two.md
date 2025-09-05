---
title: Week Two Documentation Notes
course: ENG 810
semester: Fall 2025
tags: #documentation
created: 2025-08-22
---

# Concept Diagrams

I started creating some concept diagrams for the scanner to start working through some potential issues that have to do with Windows compatability with the Raspberry Pi and the like. While I have historically used Windows and it's the OS that's familiar to me, the sketches do make me lean a bit more toward seeing if I can operate everything off the Raspberry Pi. 

![DIY Scanner Concept Diagram](eng810/concept_diagrams/scanner_diagrams.png)

Some challenges I think I would need to take time to work through:
- Experimenting with the Raspberry Pi I have borrowed from Jon's dad. It currently is set up to play retro games, so I need to install the OS onto an SD card and work on booting it, setting up an IDE, and installing Python. 
- Researching to see what kinds of cameras can be used with the Raspberry Pi and how connectivity would work. Can I use just the one?
- Look into the case kit that we have in Ricks. Does it extend the Raspberry Pi capabilities? How so?

# Python Courses
- [University of Helsinki MOOC on Python programming](https://programming-22.mooc.fi/)
- [Hardvard CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
- [futurecoder](https://futurecoder.io/)
- [W3Schools tutorials](https://www.w3schools.com/python/default.asp)

# Model Codes & Softwares
- [Spreads](https://github.com/DIYBookScanner/spreads)
    - Intended for use with the Archivist DIY Scanner I have built, but has not been updated in documentation or worked on in about a decade, which may pose some interesting questions about the limitations of the software and the like. There's also lots of documentation of issues relating to the software on the [DIY Scanner forums](https://diybookscanner.org/forum/), which would be a helpful resource for learning more about this issue.
- [DIY Scanner Forum: Programs, software releases, and more](https://diybookscanner.org/forum/)
    - This has a lot of information about various issues relating to the book scanning process, including use of OCR, training of object detection algorithims (i.e. YOLO), and debugging issues with existing softwares that have been used by the community, such as Spreads.

# Reviewing ECE Senior Design Project Files
- Acoustic Feedback for Coffee Roasting
    - My first question is why? I am intrigued by the goal here, and are they collecting data on taste tests?
    - The design documents for both of these projects were helpful models for drawing up my own. I used Excalidraw, which has some nice libraries for icons for software development too, so I think it'll eventually be worth revisiting the practice of creating a concept diagram once I get the basic infrastructure set up first (i.e. setting up the cameras, etc.). I have created some by hand on my tablet, and I will be importing those files into the GitHub soon, but I think I want to read a bit about best practices for UI and UX before I attempt making further diagrams.
    - The modularity of their documentation is also really nice, especially in comparison to what I was doing as I first built the scanner. I'll also put that info in the GitHub, but I am starting to better understand why using YAML to encode metadata into markdown for notes is a good way to keep things organized, at least for a platform like GitHub. I feel like that would make taking notes while coding much more approachable, as I've previously seen it as too overwhelming while I'm just starting to learn how to program.
    - I *really* like that they document their accomplishments. That's a cool way to keep track of progress.
    - I appreciate the user guide too. I took a technical documentation course in undergrad, and I definitely think that would be an important thing to me to work on, is both a guide for how to potentially use the software, but also documentation relating to its creation. Definitely makes me want to revisit the documentation from building the scanner and better organize it. I have it all in one document with all the dates and everything organized as bullet points, which would be better broken out into multiple files.
- Scrambled EGG
    - I noticed it with the coffee roasting project as well, but this definitely makes the electrical aspect of things more apparent to me, particularly in their subsystem breakdown. Historically, I have only ever worked with things mechanically and essentially outsourced help with electrical work to others for things like DIY car and home repairs. With that said, I am interested in repurposing a foot pedal from the lab to use to trigger both of the cameras for the scanner. This makes it a lot faster to scan, as the operator of the scanner can focus on raising the book to the glass press plates and turning pages without being interrupted to operate the cameras. I've been meaning to learn some basics around soldering and electrical engineering, and we have a soldering set up in the CRDM space. I don't know what repurposing the pedals would entirely entail, but I am interested in exploring those options. It may even be that I can simply find the correct adapter to test whether the pedal is readable on Windows/Linux, but if not, they only have six prongs in the connectors, which seems to associate with the "back", "play", and "forward" pedals, so I have a feeling that the wiring should be fairly straightforward.
    - I looked at one of their code files, and I saw that they do a nice job of writing what each block of code does as its function, which is a practice I feel like I should start doing.
