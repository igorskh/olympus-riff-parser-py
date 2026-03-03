import struct

from .datetime_utils import format_timestamps
from .bytes_utils import bytes_to_int


DATETIMES_OFFSET = 38
DATETIMES_BLOCK_SIZE = 24
OFFSET_TO_INDEX_MARKS = 316
INDEX_MARK_BLOCK_SIZE = 4
MAX_INDEX_MARKS = 99


def read_olym_chunk(data: bytes) -> dict[str, any]:
    """
    Read and parse the 'olym' chunk from the provided byte data.

    Args:
        data (bytes): The byte data containing the 'olym' chunk.

    Returns:
        dict: A dictionary containing the parsed 'olym' chunk data.
    """

    start_datetime, end_datetime = format_timestamps(
        data[DATETIMES_OFFSET : DATETIMES_OFFSET + DATETIMES_BLOCK_SIZE]
        .decode("ascii")
        .strip()
    )

    index_marks = []
    block_size = INDEX_MARK_BLOCK_SIZE
    for i in range(MAX_INDEX_MARKS):
        index_start = OFFSET_TO_INDEX_MARKS + i * block_size
        index_end = OFFSET_TO_INDEX_MARKS + (i + 1) * block_size
        d = data[index_start:index_end]
        if d == b"\xff\xff\xff\xff":
            break

        int_data = bytes_to_int(data[index_start:index_end])
        index_marks.append(int_data / 1000)

    return {
        "index_marks": index_marks,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
    }


def parse_riff_subsection_olym(
    file_path: str, target_subchunk_id=b"olym"
) -> dict[str, any]:
    """
    Parse the 'olym' subchunk from a WAV file.

    Args:
        file_path (str): The path to the WAV file.
        target_subchunk_id (bytes): The ID of the subchunk to parse.

    Returns:
        dict: The parsed data from the 'olym' subchunk.
    """
    with open(file_path, "rb") as f:
        riff = f.read(12)
        if len(riff) < 12:
            raise ValueError("File too small to be a valid WAV file")
        chunk_id, _, format = struct.unpack("<4sI4s", riff)
        if chunk_id != b"RIFF" or format != b"WAVE":
            raise ValueError("Not a valid WAV file")

        while True:
            header = f.read(8)
            if len(header) < 8:
                break
            subchunk_id, subchunk_size = struct.unpack("<4sI", header)

            if not subchunk_id == target_subchunk_id:
                f.seek(subchunk_size, 1)
            else:
                return read_olym_chunk(f.read(subchunk_size))

    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Parse the 'olym' chunk from a WAV file.")
    parser.add_argument("file_path", type=str, help="Path to the WAV file")
    args = parser.parse_args()

    result = parse_riff_subsection_olym(args.file_path)
    if result is not None:
        print("Index Marks (seconds):", result["index_marks"])
        print("Start Datetime:", result["start_datetime"])
        print("End Datetime:", result["end_datetime"])
    else:
        print("No 'olym' chunk found in the file.")
