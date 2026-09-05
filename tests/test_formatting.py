from toolkit.formatting import format_table

def test_format_table():
    headers = ["Metric", "Value"]
    rows = [["latency", "1.2ms"], ["throughput", "50k ops/sec"]]
    table = format_table(headers, rows)
    assert "latency" in table
    assert "50k ops/sec" in table
