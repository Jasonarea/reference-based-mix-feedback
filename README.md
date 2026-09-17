# Spectral Characteristics of Novice and Expert-Revised Mixes

A paired-comparison study of how expert mixing revisions change the spectral
and dynamic properties of the same musical material.

**Status:** in progress (see [Milestones](../../milestones)) · **Last updated:** TBD

---

## Research question

> How do a novice's mixes and an expert's revisions of those same mixes differ
> systematically in spectral characteristics?

## Motivation

Producing a mix that "sounds right" appears to require either expensive plugins
or a trained ear capable of getting there with stock tools. Without either, a
producer is left knowing something is wrong but not what. This project attempts
to quantify that gap on a small set of paired examples, using the same source
material mixed twice — once by a novice, once revised by an instructor.

## Data

Each pair consists of two mixes of an identical arrangement: the author's own
mix and an instructor's revision of it. Because both versions originate from the
same session, the only variable is the mixing treatment itself.

| | |
|---|---|
| Pairs | TBD |
| Source | Logic Pro projects from a MIDI coursework sequence |
| Export | 24-bit WAV, project sample rate, normalization disabled |
| Scope of revision | Varies by track; recorded per pair in `data/manifest.csv` |

**Audio is not distributed in this repository.** The recordings are coursework
containing an instructor's work and the author's unreleased material. See
[`data/README.md`](data/README.md) for what is included instead and how the
published metrics can be checked.

## Method

1. **Loudness normalization.** Revised versions may include master-bus
   processing that raises level. Without normalization, that difference would be
   misread as a mixing difference. All signals are matched before comparison.
2. **Feature extraction.** Band energy distribution (with attention to the
   200–500 Hz region), spectral centroid, rolloff, flatness, and dynamic range.
3. **Paired differences.** Metrics are differenced within each pair
   (revised − original) so that per-song variation does not confound the
   comparison.
4. **Pattern inspection.** Differences are examined across pairs for directions
   that recur.

## Results

TBD

## Limitations

TBD — sample size, the varying scope of revision across pairs, and the fact that
spectral difference is not by itself evidence of perceptual improvement.

## Repository structure

```
data/        manifest and documentation (audio excluded)
src/         feature extraction and normalization modules
notebooks/   exploratory analysis
results/     computed metrics and figures
paper/       write-up draft
```

## Reproducing

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

TBD — entry point and usage.

## License

Code: MIT. Audio and figures derived from coursework recordings are not licensed
for redistribution.
