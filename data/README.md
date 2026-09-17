# Data

## Why no audio is here

Three kinds of material feed this project, and none of them can be redistributed:

- **Reference tracks** are commercial releases.
- **Validation pairs** are coursework containing an instructor's revisions.
- **The author's own mixes** are unreleased.

Committing 24-bit WAV files would also make the repository history impractical
to clone.

## What is published instead

- `tracks.csv` — one row per audio file: what it is, what role it plays, and the
  technical details needed to interpret the measurements.
- `../results/metrics.csv` — every feature computed, one row per file. The
  findings in the README and the paper follow from this file alone, so the
  analysis can be re-derived and checked without the audio.

## tracks.csv columns

| column | meaning |
|---|---|
| `track_id` | short identifier (`m01`, `r01`, …) |
| `role` | `mix`, `reference`, or `revision` |
| `pair_id` | links a mix to its instructor revision, blank otherwise |
| `title` | working title or description |
| `filename` | filename under `audio/` |
| `sample_rate` | Hz, as exported |
| `duration_s` | seconds |
| `source` | how it was obtained: own bounce, purchased release, coursework |
| `notes` | anything relevant to interpretation |

## Export procedure

Everything the author bounces uses identical settings: PCM / WAVE / 24-bit /
interleaved, project sample rate, **normalization off**. Where a mix and its
revision form a validation pair, both are bounced over the same region. Any
deviation is recorded in `notes`.

Reference tracks are used at the highest quality available. Lossy sources are
flagged in `notes`, because codec rolloff near 16 kHz distorts spectral centroid
and rolloff measurements and must not be read as a mixing difference.
