from semiotic_velocity.pipeline import SemioticVelocityPipeline


def pipeline():
    return SemioticVelocityPipeline("config/targets.yaml")


def test_nominal_stream_is_separate_from_visual_tiers():
    result = pipeline().process_linguistic_stream("Stańczyk Jana Matejki")
    assert result["machine_nominal_class"] == "N1"
    assert result["machine_visual_tier"] is None
    assert result["requires_human_validation"] is True


def test_diacritic_normalised_matching():
    result = pipeline().process_linguistic_stream("Stanczyk w obrazie Jana Matejki")
    assert result["machine_nominal_class"] == "N1"


def test_false_positive_control():
    result = pipeline().process_linguistic_stream("Stańczyk piłkarz po meczu")
    assert result["machine_nominal_class"] is None
