# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] — 2026-02-28

### Added
- **Pattern #13 — Title Case:** Detects and corrects English-style title casing in Hungarian headings
- **Pattern #14 — Curly quotes:** Flags `"..."` English typographic quotes; replaces with Hungarian `„..."` style
- **Second-pass audit:** Mandatory re-read step after first rewrite to catch lingering AI patterns (inspired by [@blader/humanizer](https://github.com/blader/humanizer) v2.2.0)
- `**Figyelj ezekre:**` identification fields added to patterns #15, #16, #17 for consistency
- Two new checklist entries in the Quick Reference section

### Changed
- Renumbered patterns #13–#22 → #15–#24 following insertion of two new style patterns
- `Folyamat` section restructured: second-pass audit is now an explicit numbered step
- Internal cross-references in examples and checklist updated to match new numbering

---

## [1.0.0] — 2026-02-28

### Added
- Initial release
- 22 general AI-writing patterns (Hungarian translations and adaptations of [@blader/humanizer](https://github.com/blader/humanizer))
- **Személyiség és lélek** section — original contribution; addresses soulless-but-technically-clean text that the original skill does not cover
- **M1 — Word order / focus position:** Pragmatic word order restoration for Hungarian SVO→focus rewriting
- **M2 — Sentence rhythm (burstiness):** Detection and correction of uniform AI sentence length
- **M3 — Circumlocutions (terpeszkedő kifejezések):** 20+ pattern table with terse alternatives
- **M4 — Nominalization → verb restoration:** Reverses AI tendency to turn verbs into noun phrases
- **M5 — Hungarian AI clichés:** Localized list of AI boilerplate openers and significance inflation
- **M6 — Register-aware rules:** Separate guidance for journalistic, literary, and legal/official registers
- Quick reference checklist (Hungarian-specific)
- Full before/after example with annotated change log

### Based on
- [@blader/humanizer](https://github.com/blader/humanizer) — original Claude Code skill by @blader
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — WikiProject AI Cleanup
- Hungarian corpus (2022 and earlier): Index, HVG, Magyar Narancs, Jelenkor, Litera, Constitutional Court decisions, legislative texts
