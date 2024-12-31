from utils.my_paths import capture_save_location, processing_save_location, pdf_output_location

config = {
    "capture": {
        "file_naming": "page_{:03d}.jpg",
        "num_captures": 10,
        "save_location": capture_save_location
    },
    "processing": {
        "resize_dimensions": (1024, 768),
        "rotate": 270,
        "contrast": 1.5,
        "brightness": 1.0,
        "crop_margins": (10, 10, 10, 10),
        "save_location": processing_save_location
    },
    "pdf": {
        "ocr_enabled": True,
        "output_location": pdf_output_location
    }
}
