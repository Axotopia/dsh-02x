# dsh-02x

Custom agent presets for DeepSeek Harness **0.2.0-rc.2**, one installable bundle per subdirectory.

These presets were migrated from the legacy layout (`~/.dsh/.agent-presets/<id>/` with
`preset.yml` + `agent.cordis.yml`), which rc.2 no longer reads. Each directory is now a
self-contained Cordis bundle that declares its preset as an
`@deepseek-ai/dsh-agent-preset` row.

## Layout

Each preset subdirectory contains:

| File | Purpose |
| --- | --- |
| `cordis.patch.yml` | The bundle patch — inserts the `preset-<id>` declaration row |
| `package.json` | Bundle manifest (`dsh.bundle.patch` → `./cordis.patch.yml`) |
| `agent.cordis.yml` | Original legacy entry list, kept for reference |
| `preset.yml` | Original legacy metadata (name / description / order) |
| assets | Whatever the preset carries: `skills/`, `plugin/`, `server/`, `scripts/`, `mappings/`, `reference/` |

Relative specifiers inside `cordis.patch.yml` (e.g. `name: ./plugin/mdpdf-plugin.mjs`)
resolve beside the patch file, so each directory is portable.

## Presets

| Directory | Display name |
| --- | --- |
| `chat` | Chat |
| `debate-team` | Debate Team |
| `legal-financial-consul` | Legal-Financial Consul |
| `medical-technician` | Medical Technician |
| `mikrotik` | MikroTik Fleet |
| `ocr-md` | OCR to Markdown |
| `ocr-md-json` | OCR-MD-JSON |
| `property-researcher` | property-researcher |
| `researcher-browser` | Researcher |
| `research-swarm` | Research Swarm |
| `revit-tools` | Revit Tools |
| `statement-consolidator` | Statement Consolidator |
| `vacation-planner` | Vacation Planner |
| `zero-click` | Zero-Click |

## Installing

From the DSH Web plugin page, or via the plugin manager with the absolute path to the
preset directory:

```
plugin_manager install_bundle /home/song/.dsh/preset-bundles/<preset-id>
```

On this machine the live installed copies live at `~/.dsh/preset-bundles/<id>/`
(the profile links them directly); this repository is the versioned master. After
editing a preset here, copy it back and reinstall the bundle.

## Migration notes

- `@deepseek-ai/dsh-workflow-worker-thread` was retired in rc.2; the 11 presets that
  used it now mount `@deepseek-ai/dsh-workflow-ptc` (same `provider: spawn` config).
- All `!!js` Loader expressions, comments and block scalars were carried over verbatim.
- `server/` directories keep `package.json` + lockfiles; `node_modules/` is not
  committed — restore with `npm ci` (or `pnpm install`) inside the server directory.
- Push access uses the repo-scoped deploy key `dsh-02x-local` (SSH alias
  `github-dsh-02x`).
