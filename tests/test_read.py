import pytest
from olympus_riff_parser_py import parse_riff_subsection_olym

def test_parse_riff_subsection_olym():
    result = parse_riff_subsection_olym("samples/sample_2_marks.wav")
    assert result is not None
    assert "index_marks" in result
    assert "start_datetime" in result
    assert "end_datetime" in result

    assert len(result["index_marks"]) == 2

    assert result["index_marks"][0] == 4.365
    assert result["index_marks"][1] == 9.38

    assert result["start_datetime"] == "2026-03-03 22:37:42"
    assert result["end_datetime"] == "2026-03-03 22:37:56"