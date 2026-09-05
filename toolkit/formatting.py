from typing import List, Sequence

def format_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    """Format rows and columns into an aligned ASCII table."""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], len(str(cell)))
            else:
                widths.append(len(str(cell)))
    
    sep = "+-" + "-+-".join("-" * w for w in widths) + "-+"
    header_line = "| " + " | ".join(h.ljust(w) for h, w in zip(headers, widths)) + " |"
    data_lines = [
        "| " + " | ".join(str(cell).ljust(w) for cell, w in zip(row, widths)) + " |"
        for row in rows
    ]
    return "\n".join([sep, header_line, sep] + data_lines + [sep])
