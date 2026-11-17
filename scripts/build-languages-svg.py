#!/usr/bin/env python3
"""Rebuild assets/languages.svg from GitHub language bytes across all repos.

Requires the GitHub CLI (`gh`) authenticated as a user who can read
AzizurRahmanEmon's private repositories. A scheduled GitHub Action in this
public repo cannot do that with the default GITHUB_TOKEN; a PAT with `repo`
scope would be required, so the committed SVG is a dated static snapshot.
"""

from __future__ import annotations

import json
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "languages.svg"
USER = "AzizurRahmanEmon"
TZ = ZoneInfo("Asia/Dhaka")


def gh_json(args: list[str]):
    out = subprocess.check_output(["gh", *args], text=True)
    return json.loads(out)


def repo_names(visibility: str) -> list[str]:
    repos = gh_json(
        [
            "repo",
            "list",
            USER,
            "--visibility",
            visibility,
            "-L",
            "200",
            "--json",
            "name",
        ]
    )
    return [r["name"] for r in repos]


def languages(name: str) -> dict[str, int]:
    return gh_json(["api", f"repos/{USER}/{name}/languages"])


def main() -> None:
    private = repo_names("private")
    public = repo_names("public")
    totals: dict[str, int] = defaultdict(int)
    for name in private + public:
        for lang, nbytes in languages(name).items():
            totals[lang] += nbytes

    grand = sum(totals.values())
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    top, rest = ranked[:5], ranked[5:]
    other = sum(b for _, b in rest)
    now = datetime.now(TZ)
    stamp = now.strftime("%-d %b %Y")
    tz_label = "Asia/Dhaka"

    rows = [(name, 100.0 * nbytes / grand) for name, nbytes in top]
    other_names = ", ".join(n for n, _ in rest) if rest else "none"
    other_pct = 100.0 * other / grand if grand else 0.0
    top_pct = 100.0 - other_pct

    W, H = 1200, 268
    bar_x, bar_max_w, bar_h = 210, 820, 12
    row_y0, row_h, label_x, pct_x = 88, 30, 48, 1080

    def txt(*parts: str) -> str:
        return "\n".join(parts) + "\n"

    body = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        '  <title id="title">Language mix across all public and private repositories</title>',
        f'  <desc id="desc">Snapshot {stamp}, {tz_label}. Computed from GitHub language bytes across {len(private) + len(public)} repositories ({len(private)} private, {len(public)} public).</desc>',
        "  <defs>",
        '    <clipPath id="frame"><rect width="1200" height="268" rx="16"/></clipPath>',
        '    <linearGradient id="accent-line" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">',
        '      <stop stop-color="#22D3EE" stop-opacity="0"/>',
        '      <stop offset="0.5" stop-color="#22D3EE" stop-opacity="0.7"/>',
        '      <stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>',
        "    </linearGradient>",
        "  </defs>",
        '  <g clip-path="url(#frame)">',
        f'    <rect width="{W}" height="{H}" fill="#0D1117"/>',
        '    <path d="M0 1h1200" stroke="url(#accent-line)" stroke-width="2"/>',
        f'    <text x="48" y="40" font-family="Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif" font-size="18" font-weight="700" fill="#E6EDF3">Languages across {len(private) + len(public)} repositories</text>',
        f'    <text x="48" y="62" font-family="Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif" font-size="13" fill="#8B949E">Public and private, by GitHub language bytes · Snapshot {stamp} ({tz_label})</text>',
        f'    <text x="1152" y="40" text-anchor="end" font-family="Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif" font-size="13" font-weight="600" fill="#22D3EE">{len(private)} private · {len(public)} public</text>',
    ]
    for i, (name, pct) in enumerate(rows):
        y = row_y0 + i * row_h
        cy = y + 14
        track_y = y + 10
        width = max(4, round(bar_max_w * (pct / 100.0)))
        body += [
            f'    <text x="{label_x}" y="{cy}" font-family="Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#E6EDF3">{name}</text>',
            f'    <rect x="{bar_x}" y="{track_y}" width="{bar_max_w}" height="{bar_h}" rx="6" fill="#161B22"/>',
            f'    <rect x="{bar_x}" y="{track_y}" width="{width}" height="{bar_h}" rx="6" fill="#22D3EE"/>',
            f'    <text x="{pct_x}" y="{cy}" font-family="SF Mono, Consolas, Liberation Mono, Menlo, Courier, monospace" font-size="13" fill="#8B949E">{pct:.2f}%</text>',
        ]
    body += [
        f'    <text x="48" y="250" font-family="Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif" font-size="11" fill="#8B949E">Top 5 languages shown ({top_pct:.2f}% of {grand:,} bytes). {other_names} together are {other_pct:.2f}%.</text>',
        '    <path d="M0 267h1200" stroke="url(#accent-line)" stroke-width="2"/>',
        "  </g>",
        "</svg>",
    ]
    OUT.write_text(txt(*body))
    print(f"Wrote {OUT}  private={len(private)} public={len(public)} total_bytes={grand}")
    for name, nbytes in ranked:
        print(f"  {name:20} {nbytes:12,}  {100.0 * nbytes / grand:6.2f}%")


if __name__ == "__main__":
    main()
