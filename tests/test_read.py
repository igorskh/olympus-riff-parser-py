import pytest
from olympus_riff_parser_py import parse_riff_subsection_olym

def test_parse_riff_subsection_olym():
    result = parse_riff_subsection_olym("samples/sample_2_marks.wav")
    assert result is not None
    assert "index_marks" in result
    assert "start_datetime" in result
    assert "end_datetime" in result

    assert len(result["index_marks"]) == 2