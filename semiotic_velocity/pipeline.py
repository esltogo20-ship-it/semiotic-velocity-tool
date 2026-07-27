from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

import imagehash
import yaml
from PIL import Image


def _normalise(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


class SemioticVelocityPipeline:
    """Generate machine candidates for later human validation.

    Similarity and language rules never create final semiotic classifications.
    """

    def __init__(self, config_path: str | Path, target_object_id: str = "stanczyk-1862"):
        with Path(config_path).open(encoding="utf-8") as handle:
            self.config: dict[str, Any] = yaml.safe_load(handle)
        targets = {item["id"]: item for item in self.config["target_objects"]}
        self.target = targets[target_object_id]
        self.configuration_version = self.config["configuration_version"]

    def process_visual_stream(self, image_path: str | Path, reference_path: str | Path) -> dict[str, Any]:
        candidate = Image.open(image_path)
        reference = Image.open(reference_path)
        distance = imagehash.dhash(candidate) - imagehash.dhash(reference)
        thresholds = self.target["visual_retrieval"]["dhash_candidate_thresholds"]

        if distance <= thresholds["tier_a"]:
            suggested = "A"
        elif distance <= thresholds["tier_b"]:
            suggested = "B"
        elif distance <= thresholds["tier_c"]:
            suggested = "C"
        else:
            suggested = None

        return {
            "target_object_id": self.target["id"],
            "media_type": "image",
            "machine_visual_tier": suggested,
            "machine_nominal_class": None,
            "machine_confidence": None,
            "machine_detection_method": "dhash",
            "measurements": {"dhash_hamming_distance": distance},
            "requires_human_validation": True,
            "configuration_version": self.configuration_version,
        }

    def process_linguistic_stream(self, text: str) -> dict[str, Any]:
        anchors = self.target["linguistic_retrieval"]
        value = _normalise(text)
        roots = [_normalise(item) for item in anchors["roots"]]
        fragments = [_normalise(item) for item in anchors["fragments"]]
        mediators = [_normalise(item) for item in anchors["mediators"]]
        exclusions = [_normalise(item) for item in anchors["exclusion_terms"]]

        has_root = any(re.search(rf"\b{re.escape(item)}\b", value) for item in roots)
        has_fragment = any(re.search(rf"\b{re.escape(item)}\b", value) for item in fragments)
        excluded = any(item in value for item in exclusions)
        has_mediator = any(item in value for item in mediators)

        nominal_class = None
        if not excluded:
            if has_root:
                nominal_class = "N1"
            elif has_mediator and has_fragment:
                nominal_class = "N2"
            elif has_fragment:
                nominal_class = "N3"

        return {
            "target_object_id": self.target["id"],
            "media_type": "text",
            "machine_visual_tier": None,
            "machine_nominal_class": nominal_class,
            "machine_confidence": None,
            "machine_detection_method": "rule_based_polish_anchor_match",
            "contextual_anchor_present": has_root or has_mediator,
            "requires_human_validation": nominal_class is not None,
            "configuration_version": self.configuration_version,
        }
