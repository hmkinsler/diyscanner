from utils.my_paths import capture_save_location, processing_save_location, pdf_output_location

config = {
    "capture left": { #This is for the left page, which is associated with the right camera
        "left_pg_naming": "page_{:03d}.jpg",
        "num_captures": 1,
        "save_location": capture_save_location,
        "capture_interval": 5,  # Time in seconds between captures
        "iso": 100,            # ISO value
        "aperture": 5.6,       # Aperture value
        "shutter_speed": 250 # Shutter speed as string
    },
    "capture right": { # This is for the right page, which is associated with the left camera
        "right_pg_naming": "page_{:03d}.jpg",
        "num_captures": 1,
        "save_location": capture_save_location,
        "capture_interval": 5,  # Time in seconds between captures
        "iso": 100,            # ISO value
        "aperture": 5.6,       # Aperture value
        "shutter_speed": 250 # Shutter speed as string
    },
    "processing": {
        "resize_dimensions": (800, 400),
        "rotate": 0,
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
