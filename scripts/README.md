# Featured GIF scripts

Scripts that render the animated teaser GIFs used on the home page cards and paper pages.
Requires Python 3 with `matplotlib`, `numpy`, and `Pillow`. Run from the repo root:

```sh
python3 scripts/make_wacv_gif.py   images/featured/wacv2026.gif
python3 scripts/make_icip_gif.py   images/featured/icip2026.gif scripts/assets/icip2026_photo.png
python3 scripts/make_geopid_gif.py images/featured/geopid.gif   scripts/assets/geopid_photo.png
```

The photos in `assets/` are crops of the paper figures (`images/featured/icip2026.png`,
`images/featured/teaser-synergy-sarcasm.png`). Eigenvalues, attention shares, and vector
lengths in the animations are illustrative, not experimental results.
