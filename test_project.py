from project import map_label, pre, im_pred
from PIL import Image
import pytest
import os
import tensorflow as tf

def test_im_pred():
    model_path = "simple_model.h5"
    if not os.path.exists(model_path):
        pytest.skip("simple_model.h5 not found. Run model_training.py first.")
    model = tf.keras.models.load_model(model_path)
    Image.new("L", (280, 280), "white").save("test_letter.png")
    try:
        result = im_pred(model, "test_letter.png")
        assert isinstance(result, str)
        assert len(result) == 1
    finally:
        if os.path.exists("test_letter.png"):
            os.remove("test_letter.png")

def test_pre():
    test_img = Image.new("L", (280, 280), "white")
    processed = pre(test_img)
    assert processed.shape == (1, 28, 28, 1)
    assert processed.max() <= 1.0
    assert processed.min() >= 0.0

def test_map_label():
    assert map_label(1) == "A"
    assert map_label(26) == "Z"
    assert map_label(0) == "?"
