"""Semiotic Velocity Tool v5.3 core pipeline."""

import re

import imagehash
import yaml
from PIL import Image


class SemioticVelocityPipeline:
    """Classify visual and nominal Stańczyk deployments."""

    def __init__(self, config_path):
        with open(config_path, "r", encoding="utf-8") as config_file:
            self.config = yaml.safe_load(config_file)

        target = self.config["target_objects"][0]
        self.thresholds = target["thresholds"]
        self.anchors = target["linguistic_anchors"]

    def process_visual_stream(self, image_path, original_canvas_path):
        """Classify an image with the v5.3 dHash thresholds."""
        try:
            image = Image.open(image_path)
            original = Image.open(original_canvas_path)
            hamming_distance = imagehash.dhash(image) - imagehash.dhash(original)

            if hamming_distance <= self.thresholds["tier_a_hamming"]:
                return "Tier A: Direct Reproduction"
            if hamming_distance <= self.thresholds["tier_b_hamming"]:
                return "Tier B: Close Derivative"
            if hamming_distance <= self.thresholds["tier_c_hamming"]:
                return "Tier C: Loose Derivative"

            return (
                "Out of core hashing bounds. "
                "Routing to advanced Tier D SIFT matching."
            )
        except Exception as error:
            return f"Error processing image stream: {error}"

    def process_linguistic_stream(self, text_content):
        """Evaluate nominal references using morphology and context anchors."""
        text_lower = text_content.lower()

        has_root = any(
            root.lower() in text_lower for root in self.anchors["roots"]
        )
        has_fragment = any(
            re.search(rf"\b{re.escape(fragment.lower())}", text_lower)
            for fragment in self.anchors["fragments"]
        )

        if not (has_root or has_fragment):
            return "No motif detected."

        has_primary = any(
            anchor.lower() in text_lower
            for anchor in self.anchors["primary_anchors"]
        )
        has_secondary = any(
            anchor.lower() in text_lower
            for anchor in self.anchors["secondary_anchors"]
        )
        is_false_positive = any(
            term.lower() in text_lower
            for term in self.anchors["exclusion_terms"]
        )

        if (has_primary or has_secondary) and not is_false_positive:
            return "Tier E: Verified Nominal Deployment"

        return "Linguistic match found, but failed contextual anchor safety check."
