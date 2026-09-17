# Reference-Based Mix Feedback

Turning the spectral distance between a rough mix and a reference track into
mixing guidance a beginner can act on.

**Status:** in progress (see [Milestones](../../milestones)) · **Last updated:** TBD

---

## Research question

> Can the spectral difference between an amateur mix and a reference track be
> translated into specific, actionable mixing guidance — and does that guidance
> agree with what an experienced engineer actually does to the same mix?

## Motivation

Getting a mix to sound right seems to require either expensive plugins or an ear
trained well enough to get there with stock tools. Without either, a producer is
stuck knowing something is wrong but not what, or where. Reference tracks are the
standard advice for closing that gap, but comparing by ear is exactly the skill
the beginner doesn't have yet.

This project asks whether the comparison can be made explicit. Not "does this
sound like the reference" but "your 200–500 Hz band sits 4 dB above the
reference; that region is where the muddiness you're hearing lives."

## Approach

1. **Normalize.** Reference tracks are mastered and will be far louder than a
   rough mix. Without loudness matching, every comparison is dominated by level.
2. **Extract.** Band energy distribution, spectral centroid, rolloff, flatness,
   dynamic range, stereo width.
3. **Difference.** Compare the mix against the reference feature by feature.
4. **Translate.** Map differences that exceed a threshold onto concrete
   suggestions, with the band, the direction, and the magnitude stated.
5. **Validate.** Run the system on mixes that an instructor later revised, and
   check whether the suggested direction matches the revision actually made.

Step 5 is what keeps this from being a plausible-sounding heuristic. The
validation pairs are limited in number and that limit is reported, not hidden.

## Data

| Role | Source | Notes |
|---|---|---|
| Mixes under analysis | Own recordings and coursework | TBD |
| Reference tracks | Commercial releases in comparable styles | Not redistributed |
| Validation pairs | Coursework mixes with an instructor's revision | TBD, small n |

**No audio is distributed in this repository.** Reference material is
commercially released, and the coursework contains an instructor's work and the
author's unreleased material. See [`data/README.md`](data/README.md) for what is
published instead.

## Results

TBD

## Limitations

TBD — spectral proximity to a reference is not the same as a good mix;
instrumentation differences shift what the target should be; the validation set
is small; agreement in direction is weaker evidence than agreement in magnitude.

## Repository structure

```
data/        manifest and documentation (audio excluded)
src/         normalization, feature extraction, suggestion logic
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

Code: MIT. Analysis of copyrighted reference material is limited to derived
numerical features; no audio is redistributed.
