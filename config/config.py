config = {
    "capture": {
        "file_naming": "page_{:03d}.jpg",
        "num_captures": 10,
        "save_location": r"C:\Users\hacks\Documents\diyscannerfiles\testing\captured_dir"
    },
    "processing": {
        "resize_dimensions": (1024, 768),
        "contrast": 1.5,
        "brightness": 1.0,
        "crop_margins": (10, 10, 10, 10),
        "save_location": r"C:\Users\hacks\Documents\diyscannerfiles\testing\processed_dir"
    },
    "pdf": {
        "ocr_enabled": True,
        "output_location": r"C:\Users\hacks\Documents\diyscannerfiles\output_dir"
    }
}
