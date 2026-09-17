# Data

## Why the audio is not here

Each pair consists of coursework audio: a mix by the author and an instructor's
revision of it. The instructor's work cannot be redistributed, and the author's
material is unreleased. Committing multi-megabyte 24-bit WAV files would also
make the repository history impractical to clone.

## What is included

- `manifest.csv` — one row per audio file, describing the pair it belongs to,
  the sample rate, duration, and the scope of the instructor's revision.
- `../results/metrics.csv` — every metric computed by the analysis, one row per
  file. The findings reported in the README and the paper follow from this file
  alone, so the analysis can be re-derived and checked without the audio.

## manifest.csv columns

| column | meaning |
|---|---|
| `pair_id` | identifier shared by both versions of a song (`s01`, `s02`, …) |
| `version` | `mine` or `inst` |
| `filename` | filename under `audio/` |
| `sample_rate` | Hz, as exported |
| `duration_s` | seconds |
| `revision_scope` | `track`, `master`, or `both` — what the instructor changed |
| `notes` | anything relevant: missing plugins, non-deterministic processing |

## Export procedure

Both versions of a pair are bounced from Logic Pro with identical settings:
PCM / WAVE / 24-bit / interleaved, project sample rate, **normalization off**,
and the same cycle region. Any deviation is recorded in `notes`.
