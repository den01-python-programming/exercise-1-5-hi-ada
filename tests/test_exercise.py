import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    out, err = capsys.readouterr()
    assert 'Hi' in out, "Output should contain Hi"
