# Ajay's Engineering Wiki — Instructions for Claude

This vault is a personal engineering wiki (Obsidian). It exists for recall, problem solving, exam preparation, and cross-domain insight. Notes must be useful to a student returning later, not transcripts of source material or conversations.

Full reference: `LLM Wiki Guide.md`. Entry point: `00 Home.md`. Change history: `Wiki Maintenance Log.md`.

## Skills for building the wiki

| Task | Skill |
| --- | --- |
| New atomic concept note | `/wiki-concept-note` |
| New course / subject MOC | `/wiki-course-moc` |
| Solved tutorial / problem note, tutorial index | `/wiki-tutorial-problem` |
| Deciding on and creating diagrams, graphs, flowcharts, infographics | `/wiki-visuals` |

The skills are built from `Templates/Atomic Concept Note.md` and `Templates/Course MOC.md`. Keep the templates and skills in sync if either changes.

## Editing protocol (do this before any broad change)

1. Read `00 Home.md`.
2. Read the relevant subject MOC (`* - MOC.md`).
3. Read two or three nearby notes to match notation, style, and link conventions.
4. Preserve existing content unless it is clearly duplicated, broken, or empty.
5. After adding or moving notes, update links in the nearest MOC in the same pass.
6. Decide whether the new or changed note needs a diagram, graph, flowchart, or infographic; if so, create it and embed it.
7. Log large structural changes (new MOCs, renamed folders, new templates, bulk additions) in `Wiki Maintenance Log.md` under a dated `## YYYY-MM-DD` heading.

## Structure rules

- Every major subject has a map of content whose filename ends in ` - MOC`.
- Every new concept note is linked from the nearest MOC.
- Keep notes atomic: one idea, definition, method, or solved pattern. Exceptions: MOCs, tutorial indexes, synthesis pages.
- Solved tutorial questions go in the relevant tutorial folder and are linked from the tutorial index.
- Use Obsidian `[[wikilinks]]`, never bare paths, for internal navigation. Use aliases (`[[Path/Note|Display]]`) when the display title should be cleaner.
- Do not create a duplicate when an existing note already covers the concept — extend or link it instead (the Fluid Mechanics log entry is the model: keep `Buckingham Pi Theorem`, link to it).
- Link aggressively where it supports learning: prerequisites, sibling methods, equations, solved examples, cross-domain analogies, contrasting cases. Skip links that only restate the folder hierarchy.
- Tags sparingly: `MOC`, `course`, `concept`, `tutorial`, `synthesis`, `llm`, plus subject tags (`EE1100`, `fluid-mechanics`, `strength-of-materials`, `differential-equations`). Prefer links and MOCs over new tags.
- Notes start with valid YAML frontmatter delimited by `---` lines.
- Do not build on empty `Untitled*` notes unless asked. If one is clearly a misplaced duplicate, mention it before deleting or repurposing it.
- Never silently delete knowledge. When renaming, check incoming links and keep aliases.

## Cross-domain pattern

When a concept recurs in another subject, add a bridge that explains **why** the structure matches, not just that it does:

```md
## Cross-domain links
- [[Other Concept]] — same mathematical structure because ...
```

Recurring structures in this vault: linear ODEs, eigenvalue problems, conservation laws, energy methods, time constants, resonance, stability, impedance, second moments. Bridges usually belong in or are indexed from `Cross-Domain Synthesis/Cross-Domain Synthesis - MOC`.

## Quality standard

A good note answers: What is it? Why does it work? When do I use it? How does it connect to everything else I know? A strong engineering note also answers: Can I visualize it? Can I apply it to a problem? Where does the same math appear elsewhere?

The goal is a connected mental model that gets more useful each revisit — not maximum note, link, equation, or image count. Structure should be useful, not template-compliant: omit headings that do not apply.

## Conventions seen in the existing vault

- **Course layout (one pattern for every subject).** Inside a course folder: numbered topic folders (`01 Dimensionless Numbers`, `02 …`) holding concept and method notes; `Problems/` for tutorials, assignments and solved questions; `Revision/` for formula banks, how-to-solve guides, question banks and mock papers; `Resources/` for PDFs, books, slides and manuals; `assets/` for generated figures; `Tools/` for verification and plot scripts. Create only the folders a course needs. The site builder turns each numbered folder into a chapter and strips the number.
- Top-level subject folders: `MathFlow/` (maths), `Mechanical Engineering/` (all mechanical, physics and mechanics courses; it was called `mech stuff`), `Basic Electrical Engineering/`, `Cross-Domain Synthesis/`, `Entrepreneurship/` (`Problems/` is private and not published), `CS stuff/`.
- Link notes by basename (`[[Note]]`), never by folder path, so a note can move without breaking links. Figures are named with a short course prefix (`FM-*.png`, `A610-*.png`).
- Generated visuals are stored in the subject's `assets/` folder and embedded from the note.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
