"""Regenerate every Physics I figure (35 PNGs into ../assets) and print the numbers the notes quote.
Run from this folder:  python ph_all.py"""
import os
import runpy

here = os.path.dirname(os.path.abspath(__file__))
for name in ("ph_fig_newton", "ph_fig_osc", "ph_fig_fields", "ph_fig_orbits"):
    runpy.run_path(os.path.join(here, name + ".py"), run_name="__main__")
