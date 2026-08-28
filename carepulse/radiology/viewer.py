"""
DICOM Image Viewport & Window/Level (WW/WL) Preset Calculation Engine.
Calculates Hounsfield Unit (HU) windowing for soft tissue, bone, brain, and lung CT presets.
"""

from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class WindowPreset:
    name: str
    window_width: float  # WW
    window_center: float # WL / Level
    description: str

class DICOMViewerEngine:
    # Standard CT Hounsfield Unit (HU) Windowing Presets
    PRESETS: Dict[str, WindowPreset] = {
        "soft_tissue": WindowPreset("Soft Tissue", 350.0, 40.0, "Abdomen and mediastinum general review"),
        "lung": WindowPreset("Lung", 1500.0, -600.0, "Pulmonary parenchyma and bronchial tree"),
        "bone": WindowPreset("Bone", 2000.0, 300.0, "Skeletal cortex, trabeculae, and fracture line inspection"),
        "brain": WindowPreset("Brain", 80.0, 40.0, "Intracranial parenchyma, hemorrhage, and early ischemia"),
        "stroke": WindowPreset("Stroke", 30.0, 30.0, "Subtle grey-white matter differentiation in acute stroke"),
        "liver": WindowPreset("Liver", 150.0, 30.0, "Hepatic steatosis and focal liver lesions")
    }

    @classmethod
    def apply_windowing(cls, raw_hu: float, preset_key: str = "soft_tissue") -> int:
        """
        Maps a Hounsfield Unit (HU) value to an 8-bit grayscale display value (0-255).
        """
        preset = cls.PRESETS.get(preset_key, cls.PRESETS["soft_tissue"])
        ww = preset.window_width
        wl = preset.window_center

        lower_bound = wl - (ww / 2.0)
        upper_bound = wl + (ww / 2.0)

        if raw_hu <= lower_bound:
            return 0
        elif raw_hu >= upper_bound:
            return 255
        else:
            return int(((raw_hu - lower_bound) / ww) * 255.0)
