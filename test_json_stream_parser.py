import json
import io
from json_stream_parser import load_iter


def test_ok_coverage():
    cases = r'''
        0
        123
        1.0
        1.123
        1.0e9
        1e9
        1e+1
        1e-1
        -1
        ""
        "asdf"
        "\u0020"
        "\b\f\n\r\t\\\/\""
        []
        [[]]
        [1]
        ["asdf", 123]
        {}
        {"": ""}
        {"1": 1, "2": 2}
        true
        false
        null
    '''

    expected = '\n'.join([json.dumps(json.loads(x)) for x in cases.splitlines() if x.strip()])
    parsed = '\n'.join(json.dumps(x) for x in load_iter(io.StringIO(cases)))
    assert expected == parsed
