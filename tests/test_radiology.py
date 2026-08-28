"""
Unit Tests for Radiology, DICOM Metadata Parsing, and PACS Viewer Windowing.
"""

import unittest
from carepulse.radiology.dicom_parser import DICOMTagParser
from carepulse.radiology.viewer import DICOMViewerEngine

class TestRadiologySubsystem(unittest.TestCase):
    def test_dicom_windowing_presets(self):
        # Soft tissue: Center 40, Width 350 -> range [-135, +215]
        # At HU 40 (center) -> exactly middle gray ~127
        gray_mid = DICOMViewerEngine.apply_windowing(40.0, "soft_tissue")
        self.assertAlmostEqual(gray_mid, 127, delta=2)

        # Bone preset: Center 300, Width 2000 -> range [-700, +1300]
        # Dense cortical bone (+1500 HU) should clamp to pure white (255)
        bone_white = DICOMViewerEngine.apply_windowing(1500.0, "bone")
        self.assertEqual(bone_white, 255)

        # Air (-1000 HU) in soft tissue should clamp to pure black (0)
        air_black = DICOMViewerEngine.apply_windowing(-1000.0, "soft_tissue")
        self.assertEqual(air_black, 0)

    def test_dicom_header_parser(self):
        metadata = {
            "0010,0020": "PAT-9988",
            "0010,0010": "DOE^JOHN",
            "0008,0060": "CT",
            "0018,0015": "CHEST",
            "0028,0010": "512",
            "0028,0011": "512"
        }
        res = DICOMTagParser.parse_header_dictionary(metadata)
        self.assertEqual(res.patient_id, "PAT-9988")
        self.assertEqual(res.modality, "CT")
        self.assertEqual(res.rows, 512)

if __name__ == '__main__':
    unittest.main()
