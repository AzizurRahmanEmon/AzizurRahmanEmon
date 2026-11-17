# GitHub profile settings

Apply these on [github.com/AzizurRahmanEmon](https://github.com/AzizurRahmanEmon) after the `AzizurRahmanEmon/AzizurRahmanEmon` repo is pushed and set as the special profile repository (public, default branch `main`, with this README).

## Profile fields

**Bio** (143 characters, under the 160-character limit):

```
Full stack developer in Dhaka. React, Next.js, Node, TypeScript. 30+ ThemeForest/CodeCanyon items. Building Shopify apps and multi-tenant SaaS.
```

**Company:** `RMN Labs`

**Website:** `https://azizur-rahman.com`

**Location:** `Uttara, Dhaka, Bangladesh`

**Social:** Set Twitter/X to `@rmnlab` (the older `@Azizur_rahmanE` account is suspended). LinkedIn and email are in the README (`linkedin.com/in/azizur-rahman2533`, `hello@azizur-rahman.com`).

**Available for hire:** turn on if the option is still shown — the CV lists remote full-time, contract, or freelance.

## Pin these 6 public repos

Pins can only be public. Do not pin private repos such as the Vellure, Lunovaire, or Zestify v2 APIs.

1. **zestify-client** — Next.js customer app for Zestify, a multi-tenant restaurant SaaS with reservations, checkout, and tenant-aware APIs.
2. **urlcap** — Browser-only tool that captures a webpage as a screenshot, GIF, or short video, with no backend.
3. **travel-journal-app** — Travel photo journal with email verification, rotating refresh tokens, TOTP 2FA, and AI summaries.
4. **daily-scheduler** — Day planner for tasks, meals, Google Calendar, end-of-day review, and a generated journal (Next.js, Neon, Drizzle).
5. **next-js-dashboard** — Next.js App Router dashboard from the official course: invoices, charts, and authenticated pages.
6. **sanity-portfolio-2** — Personal portfolio site built with Next.js and Sanity CMS.

Optional one-line descriptions you can paste into each repo’s “About” field (same wording as above) so the pins look consistent.

## After the first push

1. Make sure the profile repo is **public**. A private special repo will not render the README on your profile.
2. Enable **GitHub Actions** on the repo if prompted, then run the **Generate contribution snake** workflow once (`Actions` → workflow → `Run workflow`). It writes SVGs to an `output` branch. Until that run succeeds, the snake images in the README will 404.
3. Pin the six repos under **Customize your pins**.
4. Update the bio, company, website, and location fields above.


## Language snapshot

`assets/languages.svg` is a static chart of GitHub language bytes across all 135 repositories (96 private, 39 public), snapshotted on 17 Nov 2026 (Asia/Dhaka). A scheduled GitHub Action cannot refresh private-repo language totals with the default `GITHUB_TOKEN` in this public repo — that would need a PAT with `repo` scope. To rebuild it later, run `python3 scripts/build-languages-svg.py` from a machine logged into `gh` as AzizurRahmanEmon.

## Live demos for pinned public repos

These Vercel URLs 404'd when checked on 17 Nov 2026 (Asia/Dhaka), so they were left out of the README: `zestify-client.vercel.app`, `daily-scheduler-ten.vercel.app`, `sanity-portfolio-app.vercel.app`. The public GitHub repos themselves are still valid pin targets. Working public demos in the README: [ar-travel-journal.vercel.app](https://ar-travel-journal.vercel.app), [urlcap.vercel.app](https://urlcap.vercel.app).
