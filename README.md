# dsh-02x

Custom agent presets for **DeepSeek Harness 0.2.x**, one installable bundle per subdirectory.

**Tested on DSH `0.2.2-rc.5`** (the current npm `latest`). The bundles are written against
the 0.2.x bundle format introduced after `0.2.0-rc.2`; they also load on `0.2.1-rc.5`.
Presets declare their plugin rows by bare package name (`@deepseek-ai/dsh-tool-bash`, not
`...@0.2.2-rc.5`), so the running DSH release always supplies matching plugin versions —
nothing here needs repinning per release.

Each directory is a self-contained Cordis bundle that declares its preset as an
`@deepseek-ai/dsh-agent-preset` row. The older layout this replaced —
`~/.dsh/.agent-presets/<id>/` holding `preset.yml` + `agent.cordis.yml` — is no longer read
by any 0.2.x release, which is why these directories carry both the new patch and the old
files for reference.

## Version requirements

| Requirement | Detail |
| --- | --- |
| DSH | `0.2.1-rc.5` or newer; verified on `0.2.2-rc.5` |
| Node.js | Whatever the installed DSH requires. **0.2.2+ needs Node ≥ 24.9**; earlier 0.2.x releases run on Node 22. |
| Extras | Some presets call local MCP servers or CLIs (`pdfcraft`, `gridcraft`) and expect them on the machine — see each preset's own README. |

DSH ships authoritative per-release migration notes at
`docs/upgrade-guide/` inside the installed package. Read those before upgrading across a
release line; the breaks below are only the ones that touched these presets.

## Layout

Each preset subdirectory contains:

| File | Purpose |
| --- | --- |
| `cordis.patch.yml` | The bundle patch — inserts the `preset-<id>` declaration row |
| `package.json` | Bundle manifest (`dsh.bundle.patch` → `./cordis.patch.yml`) |
| `agent.cordis.yml` | Legacy entry list, kept for reference |
| `preset.yml` | Legacy display metadata (name / description / order) |
| assets | Whatever the preset carries: `skills/`, `plugin/`, `server/`, `scripts/`, `mappings/`, `reference/` |

Relative specifiers inside `cordis.patch.yml` (e.g. `name: ./plugin/mdpdf-plugin.mjs`) are
rewritten to file URLs **only** for rows inserted at the top level of an `insert:` list.
A row nested in a preset declaration's `config.plugins` is *not* rewritten: it resolves
against the profile rather than the bundle, fails to import, and the tool is silently
absent at runtime — no boot error. Those rows must use the bundle's installed package
name, `@local/dsh-preset-<id>/plugin/mdpdf-plugin.mjs`, as every preset here now does.

## Presets

| Directory | Display name |
| --- | --- |
| `chat` | Chat |
| `coding-swarm` | Coding Swarm |
| `debate-team` | Debate Team |
| `legal-financial-consul` | Legal-Financial Consul |
| `medical-technician` | Medical Technician |
| `ocr-md` | OCR to Markdown |
| `ocr-md-json` | OCR-MD-JSON |
| `property-researcher` | property-researcher |
| `researcher-browser` | Researcher |
| `research-swarm` | Research Swarm |
| `revit-tools` | Revit Tools |
| `statement-consolidator` | Statement Consolidator |
| `vacation-planner` | Vacation Planner |

Also in this repository, not a preset:

| Directory | What it is |
| --- | --- |
| `vector-db/` | An Ollama `num_ctx` VRAM calculator plus the DSH knowledge-base plugin docs. No `preset.yml` / `cordis.patch.yml`, so it is not mounted as a preset — see `vector-db/README.md`. |

## Installing

Copy the preset directory wherever you keep bundles, then install by absolute path from the
DSH Web plugin page or via the plugin manager:

```
plugin_manager install_bundle /absolute/path/to/dsh-02x/<preset-id>
```

Installing executes plugin code in the Host process, so it asks for approval. After
installing, check the roster: a preset whose activation failed stays listed with a
diagnostic and cannot compose a session. Validate changed behaviour in a **new** session —
existing sessions keep the plugin revision they started with.

If you keep live copies outside the repository (this project's are under
`~/.dsh/preset-bundles/<id>/`, linked directly into the profile), copy edits back there and
reinstall the bundle.

## Upgrading DSH: why presets can look "deleted"

Worth understanding before an upgrade, because the failure is silent:

The preset registry mounts every child plugin row eagerly. If **one** row cannot be
imported, the whole mount rejects, the preset is marked `broken`, and the Web picker filters
broken rows out of the roster. A single stale specifier therefore makes a preset vanish from
the UI with no error surface — indistinguishable from data loss. Nothing is actually lost:
the bundle files are untouched, and fixing the row brings the preset back.

Two such breaks landed in the 0.2.x line, both documented in DSH's own
`docs/upgrade-guide/v0.2.1-rc.1/subagent-control-tools/`:

- **`@deepseek-ai/dsh-tool-subagent-control/list-agents` was removed.** `list_agents` now
  registers from the parent package together with `send_message` and `interrupt_agent`.
  Delete any separate `/list-agents` row; if the plain `dsh-tool-subagent-control` row is
  already present, nothing needs replacing. Disabling that shared row now disables all
  three tools.
- **`modelSelectionSettings` was renamed to `modelSelection`** on
  `@deepseek-ai/dsh-tool-subagent`, and model discovery became opt-in via
  `modelDiscovery: true`. Both default to false. The rename is *not* fatal — unknown config
  keys are ignored — but leaving it silently turns off child model selection.

All presets here are migrated past both. Before upgrading, you can check your own bundles the
same way: confirm every `@deepseek-ai/...` package and subpath a preset names still exists in
the target release's installed tree.

## Migration notes

- `@deepseek-ai/dsh-workflow-worker-thread` was retired in `0.2.0-rc.2`; the presets that
  used it now mount `@deepseek-ai/dsh-workflow-ptc` (same `provider: spawn` config).
- All `!!js` Loader expressions, comments and block scalars were carried over verbatim. Note
  that `!!js` is valid in bundle patches but **not** in a profile's own `cordis.patch.yml`,
  where an `!!js` entry aborts profile loading with an unknown-tag YAML error.
- `server/` directories keep `package.json` + lockfiles; `node_modules/` is not committed —
  restore with `npm ci` (or `pnpm install`) inside the server directory.
- Some presets hardcode absolute paths belonging to the original author's machine. Replace
  them with your own, or remove those rows if you do not run the backing service.
- Presets whose composition embeds a firm's private positioning, correspondence, or measured
  writing profile are not published here. Build those locally and keep their reference
  material out of any repository you share.
