import pytest
from render import color_grading as mod

CASES = [
    ("lut_half", "m.lut_strength(0.0, 1.0, 0.5) == approx(0.5)"),
    ("lut_full", "m.lut_strength(0.0, 1.0, 1.0) == approx(1.0)"),
    ("exposure_double", "m.apply_exposure(2.0, (1.0, 2.0)) == (2.0, 4.0)"),
    ("exposure_zero", "m.apply_exposure(0.0, (1.0, 2.0)) == (0.0, 0.0)"),
    ("gamma_mid", "m.gamma_roundtrip(0.5, 2.0) == approx(0.5)"),
    ("gamma_one", "m.gamma_roundtrip(1.0, 2.0) == approx(1.0)"),
    ("rolloff_high", "m.highlight_rolloff(10.0, 1.0) == approx(1.0)"),
    ("rolloff_low", "m.highlight_rolloff(0.5, 1.0) == approx(0.5)"),
    ("black_remove", "m.black_lift(0.2, 0.1) == approx(0.1)"),
    ("black_floor", "m.black_lift(0.05, 0.1) == approx(0.0)"),
    ("contrast_sum", "m.combine_contrast(1.0, 2.0) == approx(3.0)"),
    ("hdr_ten", "m.hdr_metadata(10) == 10"),
    ("camera_pair", "m.camera_lut('cam', 'lut') == ('cam', 'lut')"),
    ("ui_excluded", "m.exclude_ui(True) is False"),
    ("srgb_four", "m.srgb_to_linear(4.0) == approx(4.0 ** 2.2)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
