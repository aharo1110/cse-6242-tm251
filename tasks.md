# Team 251 — Final Deliverable Task List

Project: **Analyzing Fan Reactions to World Cup Through Twitter Sentiment**
Team: William Yoo, Mason Nguyen, Adrian Haro, Shiwei He, Matthew Nguyen
Current phase: **Final Deliverables** (Final Report 21% + Poster 7% + Peer Feedback 2%)

---

## 1) Current State Snapshot (what exists today)

### Artifacts inventory (includes Google Drive folder `drive-download-20260423T200046Z-3-001/`)

**In-repo**
- `app.py` (Flask)
- `templates/index.html`, `templates/match.html`, `templates/match-no.html`, `templates/partials/footer.html`
- `static/data/fifa_tweets_sentiment.csv` (113,821 rows × 24 cols) — identical to Drive copy

**In Drive (NOT yet in repo — must be vendored into `CODE/` for submission)**
- `FIFA Data Preprocessing v1.3.ipynb` — the 10-step preprocessing notebook
- `FIFA_Sentiment_Analysis.ipynb` — VADER/TextBlob/RoBERTa + Ekman emotion classifier notebook
- `FIFA_Event_Detection.ipynb` — dual-signal event detection notebook
- `FIFA Working Data.csv` (**1.5M rows, 184 MB**) — RAW pre-dedup tweets with `Orig_Tweet`, `UserMentionNames`, `UserMentionID`, `Name`, `Place`, `Hashtags`, `RTs`, `Followers`, `Friends` — **this is the retweet/mention network source**
- `fifa_event_detection_minute_level.csv` — per-minute tweet_count, vader_mean, bert_mean, z-scores, sentiment_signal, dual_score (ready for timeline viz)
- `fifa_event_detection_results.csv` — per-event results vs. 26 curated FIFA events with volume_hit / sentiment_hit / dual_hit, gaps, peak scores (**Experiment 2 result table, numbers confirmed: 3 volume-hits, 3 sentiment-hits, 5 dual-hits → matches report's 11.5%/11.5%/19.2%**)
- `fifa_tweets_sentiment.xlsx` — Excel mirror of the sentiment CSV
- `Dashboard-repo-github.txt` — just the repo URL

### Done
- **Component 1 — Data prep**: notebook + cleaned CSV (113,821 rows, 24 cols).
- **Component 2 — Sentiment/Emotion**: notebook + labeled CSV (VADER, TextBlob, RoBERTa, 7-class emotion).
- **Component 3 — Event detection**: notebook + minute-level CSV + results CSV. Numbers in report verified against `fifa_event_detection_results.csv`.
- **Component 3b — Retweet/mention network analysis ✅ (April 23 session)**: `notebooks/FIFA_Network_Analysis.ipynb` builds labeled-author mention graph (29,389 nodes / 66,912 edges, largest CC), runs Louvain (modularity 0.502), computes per-community emotion stats + within-vs-across homogeneity. Outputs in `static/data/network/`: `community_stats.csv`, `nodes.json`, `edges.json`, `homogeneity.json`. **Key empirical finding (not yet in report): emotion does NOT cluster by community** — within-community agreement 0.4146 ≈ global baseline 0.413, assortativity 0.027. Strong structural communities exist but emotions cross community lines.
- **Component 4 — Dashboard**: Flask + D3 v5 histogram per matchdate, hoverable event region showing VADER/TextBlob + emotion pie. **Updated April 23**: dropdown now data-driven and shows match labels (`2018-07-15 — FRA-CRO`); added D3 force-directed network view with emotion-colored nodes, legend, and homogeneity summary banner; fixed pre-existing `partials/footer.html ` include-path bug (trailing-space typo was breaking all 3 templates).
- **Report sections complete**: Intro, Problem Def, Literature Survey (5 papers), Intuition (4 innovations), Method Components 1–3, Experiment 1 testbed + results, Experiment 2 testbed + results.

### Not done / placeholders in report
- Component 4 write-up: `[insert finalized part here]`
- Experiment 3 (network homogeneity): testbed questions only, **no results**
- Experiment 4 (viz usability): testbed questions only, **no experiment design, no results**
- Conclusion: `[Waiting on rest of project to be written]`
- Gantt/plan-of-activities statement: not present in draft (required, -5% if missing)
- Figures, tables, caption numbering: none in the draft

### Gaps between what the report CLAIMS vs. what CODE delivers (risk items)
These are real risks. Graders read the report against the repo.

1. **Retweet/mention network: NOT YET BUILT but now fully feasible.** `FIFA Working Data.csv` has `Orig_Tweet` (rows like `"RT @Squawka: ..."` — 423,883 RT-prefixed rows) and `UserMentionNames`. Build a User→RetweetedUser directed graph from the RT-prefixed rows, join emotion labels via `ID` back to the cleaned sentiment CSV, run community detection, compute within- vs across-community emotion homogeneity. **Risk downgraded from CRITICAL to HIGH-EFFORT.**
2. **Notebooks exist but are NOT in the git repo.** `FIFA Data Preprocessing v1.3.ipynb`, `FIFA_Sentiment_Analysis.ipynb`, `FIFA_Event_Detection.ipynb` must be copied into `CODE/` for submission. Without them, graders cannot reproduce anything.
3. **Geographic visualization promised but not built.** Raw working data has `Place` and `Name` (no lat/lon). Option A: drop geo claims in report. Option B: add a simple "Top 10 places" bar chart and qualify "geographic" as textual place field.
4. **Dashboard breadth**: only 3 matchdates enumerated in `app.py` despite ~32 matchdates in data. No team filter, time slider, or comparison. The minute-level aggregation CSV in Drive makes a real sentiment timeline easy.
5. **"31 derived features" claim vs. 24 observed columns.** Recount (the cleaned sentiment CSV is the one grader will see) and update the report number, or add the additional engineered columns.
6. **Experiment 3 depends on the network build.** Experiment 4 (usability) still requires a small user study — not avoidable, but can be done with 3–5 classmates.

### Hard submission requirements (from assignment)
Final Report zip `team251final.zip` must contain:
- `README.txt` (DESCRIPTION, INSTALLATION, EXECUTION, optional 1-min demo YouTube URL)
- `DOC/team251report.pdf` (≤6 pages, 11pt, 1" margins, exact section names: 1. Introduction, 2. Problem Definition, 3. Literature Survey, 4. Proposed method, 5. Evaluation, 6. Conclusions and Discussion)
- `DOC/team251poster.pdf` (single unified portrait poster, 30" × 40")
- `CODE/` folder (only files that are actually needed)
Plus each member individually: 3-min YouTube (unlisted) poster video named `team251poster-<lastname>`, URL submitted via Canvas.
Plus each member individually: Final Peer Feedback survey.

---

## 2) What's left on the project (team-wide)

### A. Code / Analysis
- [ ] **A0. Vendor notebooks + working data into repo `CODE/` folder** (prereq for submission). Copy the 3 notebooks and event-detection CSVs. For `FIFA Working Data.csv` (184 MB), DO NOT commit to git — instead add a `data/README.md` with download instructions + `.gitignore` rule, and include a small toy subset. **Event detection CSVs copied to `static/data/events/`.** Still TODO: copy the 3 preprocessing/sentiment/event-detection notebooks, generate toy subset, add data README + gitignore.
- [x] **A1. Retweet/mention network analysis** — `notebooks/FIFA_Network_Analysis.ipynb` done and executed. Outputs in `static/data/network/`. Stretch: add per-match subgraphs.
- [x] **A2. Network visualization in dashboard** — D3 force graph with emotion-colored nodes, degree-scaled radius, drag, tooltips, legend, homogeneity summary banner. Global graph (top 8 communities, 400 nodes). Stretch: per-match subgraph filter.
- [ ] **A3. Dashboard polish**
  - [x] Dynamic matchdates — dropdown now derives from CSV and shows `date — match_label` (e.g., `2018-07-15 — FRA-CRO`).
  - [x] Fix pre-existing `{% include 'partials/footer.html '%}` trailing-space bug blocking all templates.
  - [ ] Drive the timeline from `static/data/events/minute_level.csv` (cleaner than bucketing raw rows in JS).
  - [ ] Add team filter using `nearest_event_match`.
  - [ ] Add emotion stacked-area timeline + BERT vs VADER overlay.
  - [ ] Event markers from `static/data/events/event_results.csv` with `dual_hit=True/False` indicators.
  - [ ] Axis titles on histogram.
- [ ] **A4. Reconcile report numbers with code**
  - Feature count: the sentiment CSV has 24 columns; update "31 derived features" → correct number, or enumerate the 31 if we count engineered intermediates.
  - Decide: drop "geographic distributions" claim OR add a Place/Name bar chart using working-data fields.
- [ ] **A5. Experiment 3 results** (A1 data is ready; just needs write-up): within-community agreement **0.4146**, global baseline **0.4130**, lift **+0.002**, emotion assortativity **0.027**, modularity **0.5018**, 39 communities (size ≥ 10) over 29,389 nodes / 66,912 edges. Honest finding: structural communities exist but emotion does NOT cluster within them. Write this up + add community_stats.csv table + screenshot of force graph as figure.
- [ ] **A6. Experiment 4 design + execution**: 3–8 classmates/friends; 3–5 structured tasks on the dashboard ("identify the biggest negative event in FRA-CRO", "which match had the most joy after a goal?"), measure time-to-answer and accuracy, collect SUS-lite feedback.
- [ ] **A7. Demo toy dataset**: small subset CSV so graders can run `flask run` in seconds.

### B. Writeup (`team251report.pdf`)
- [ ] **B1.** Write Component 4 paragraph (replace `[insert finalized part here]`).
- [ ] **B2.** Rewrite Component 3 to actually describe the retweet network analysis (currently only describes event detection).
- [ ] **B3.** Write Experiment 3 description + results (depends on A1/A5).
- [ ] **B4.** Write Experiment 4 description + results (depends on A6).
- [ ] **B5.** Write Conclusion & Discussion (limitations: sparse tweet coverage on many events, retweet-dropped dedup trade-off, single-event dataset).
- [ ] **B6.** Add figures with captions: sentiment timeline for 1–2 matches, confusion of model disagreements, event-detection recall table, network community diagram.
- [ ] **B7.** Add plan-of-activities table (old plan vs revised) + effort distribution statement (already have one line, keep it).
- [ ] **B8.** Enforce formatting: ≤6 pages (excluding refs), 11pt, ≥1" margins, exact section names, title + team number + all member names on page 1.
- [ ] **B9.** References section with all cited papers (Yue 2022, Schwartz 2018, Khayyat 2019, Rout 2020, Becker 2014, + any added).
- [ ] **B10.** Proofread. Fix typos ("Effort **Discretion**" → "Effort **Distribution**", "BERTWeet" capitalization, "reconstruction" → "reconstruct" in Exp 4).

### C. Poster (`team251poster.pdf`)
- [ ] **C1.** Design single unified portrait poster, 30" × 40", ≥18pt.
- [ ] **C2.** Required sections per rubric: Motivation, Approach (algo + viz), Data, Experiments/Results, with ample graphics.
- [ ] **C3.** Export as PDF (Figma/Powerpoint/Affinity — Polo recommends Figma).

### D. Per-member 3-minute poster videos
- [ ] **D1.** Each member records their own 3-min narration of the poster. Upload unlisted YouTube, title `team251poster-<lastname>`. Submit URL via Canvas.

### E. Packaging + submission
- [ ] **E1.** `README.txt` with DESCRIPTION / INSTALLATION / EXECUTION (exact headings).
- [ ] **E2.** Optional 1-minute install/demo YouTube URL in README.
- [ ] **E3.** Build `team251final.zip` with exact structure: `README.txt`, `DOC/team251report.pdf`, `DOC/team251poster.pdf`, `CODE/…`. **Filename errors cost 5% each** per assignment.
- [ ] **E4.** Canvas submission by team's contact person.

### F. Individual (everyone)
- [ ] **F1.** Final Peer Feedback survey on Canvas (graded for completion).

---

## 3) What I (William) am taking on personally

Assumption: teammates' momentum is unclear. I'll absorb anything not-yet-owned and coordinate last-mile.

### Must-do (cannot submit without these)
- [x] **W1. Retweet network analysis pipeline** (A1) — DONE. Notebook + exports live.
- [x] **W2. Dashboard network view + unhardcode dates** (A2 + A3 partial) — DONE.
- [ ] **W3. Experiment 3 results** (A5) — data ready, just write up.
- [ ] **W4. Component 4 paragraph** in report (B1).
- [ ] **W5. Fix Component 3 write-up** to match code + add retweet network description (B2).
- [ ] **W6. Experiment 3 description + results section** (B3).
- [ ] **W7. Conclusion & Discussion** (B5).
- [ ] **W8. Plan-of-activities + effort statement** (B7).
- [ ] **W9. Reformat report to exact 6-section spec, 11pt, ≤6 pp, title block** (B8).
- [ ] **W10. References section** (B9), BibTeX or plain.
- [ ] **W11. Proofread full report** (B10).
- [ ] **W12. Package `team251final.zip`** with correct structure + filenames (E1, E3).
- [ ] **W13. Record my own 3-min poster video** (D1, mine only).
- [ ] **W14. Complete Final Peer Feedback** survey (F1).

### Should-do (if time allows — high leverage)
- [ ] **W15. Experiment 4 usability study** (A6, B4) — 5 classmates, 30 min each, small report.
- [ ] **W16. Reconcile 24 vs 31 feature count + drop or add geo** (A4).
- [ ] **W17. Figures for report** (B6) — at least 3: sentiment timeline, event-detection table, network diagram.
- [ ] **W18. Poster** (C1–C3) — only if no teammate owns it yet. Ping team first.
- [ ] **W19. README.txt + optional 1-min demo video** (E1, E2).
- [ ] **W20. Toy demo dataset + instructions** (A7).

### Coordination (do first, today)
- [ ] **W0. Post in team channel**: "I'm picking up network analysis, Experiment 3, Component 4 write-up, Conclusion, and final packaging. Who owns: poster, Experiment 4 user study, figures, README? Reply by <date>." — prevents double-work and confirms scope.

---

## 4) Suggested order of attack (30–45 min blocks)

1. **Block 1** — W0 team message; sanity-check repo; pull latest; confirm CSV columns; find raw (pre-dedup) tweet source for network.
2. **Block 2** — W1 scaffold: build retweet edge list from raw data, run Louvain, export communities + node emotion.
3. **Block 3** — W1 finish + W3 compute homogeneity/assortativity stats.
4. **Block 4** — W2 D3 network view in dashboard; unhardcode matchdates.
5. **Block 5** — W4/W5/W6/W7 report writing pass 1 (fill placeholders).
6. **Block 6** — W8/W9/W10 formatting, references, Gantt.
7. **Block 7** — W11 proofread + W16 reconcile numbers.
8. **Block 8** — W12 package zip; W13 record 3-min video; W14 peer feedback.
9. **Stretch blocks** — W15 usability study, W17 figures, W18 poster, W19 README + demo video, W20 toy dataset.

---

## 5) Open questions to answer before going deep

- What's the **final report due date** on Canvas? (Determines block budget.)
- ~~Is the **raw pre-dedup tweet CSV** preserved?~~ **Yes — `FIFA Working Data.csv` in the Drive folder.** Network build is unblocked.
- Who on the team has already started **poster** or **Experiment 4**? Don't duplicate.
- Is there a shared **Overleaf** or is the report currently only in `currentreport.txt`? Need single source of truth for the PDF build.
- What's the policy on the 184 MB `FIFA Working Data.csv` for submission? Assignment says "for large datasets, do not include them; link instead." → exclude from zip, include download instructions + a sampled subset in `CODE/data/`.
