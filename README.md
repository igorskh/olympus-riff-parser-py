# Olympus RIFF Parser

This Python script parses the 'olym' chunk from a WAV file, extracting index marks and start/end datetimes.

Tested on WAV files created by OM System LS-P5.

## Usage

```bash
python parser.py <path_to_wav_file>
```

Example:

```bash
python parser.py example.wav
```

Output:

```
Index Marks (seconds): [0.0, 1.23, 2.34, ...]
Start Datetime: 2024-01-01 12:00:00
End Datetime: 2024-01-01 12:05:00
```

