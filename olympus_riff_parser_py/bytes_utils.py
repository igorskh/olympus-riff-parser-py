def bytes_to_int(four_bytes, byteorder="little"):
    """
    Convert 4 bytes to an integer.

    Args:
        four_bytes (bytes): 4 bytes to convert

    Returns:
        int: The decimal value
    """
    if len(four_bytes) != 4:
        raise ValueError("Input must be exactly 4 bytes")

    return int.from_bytes(four_bytes, byteorder=byteorder)
