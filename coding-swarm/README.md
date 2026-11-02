# Coding Swarm

`standard` coding mode with the working discipline of `research-swarm`, applied to code.

| Field | Value |
| --- | --- |
| Preset id | `coding-swarm` |
| Display name | Coding Swarm |
| Bundle | `@local/dsh-preset-coding-swarm` |
| Roster order | 20 (after `research-swarm`) |
| Platform | Any (both `tool-bash` and `tool-pwsh` are mounted, each disabled on the other platform) |

## What it is

The shipped `standard` preset is the coding default: shell, filesystem, search, background
jobs, skills, goals, plan mode, compaction, delegation, todos, web, and presentable
deliverables. `research-swarm` contributes a way of working rather than extra tools —
decompose a goal into role-based workstreams, staff them with independent subagents, treat
every material claim as something to verify, grade confidence explicitly, and use
adversarial review for high-stakes or disputed conclusions.

Coding Swarm keeps the second half and swaps the subject matter. The evidence is a test
result, a typecheck, a build, a stack trace, a diff — not a fetched citation. Every
research rule was rewritten against code:

| Research Swarm rule | Coding Swarm equivalent |
| --- | --- |
| Cite the source URL and access date | Name the exact command and its observed result |
| `[Confirmed]` / `⚠ UNVERIFIED(reason)` | `[Verified]` / `[Unverified(reason)]` / `[Blocked(reason)]` |
| Primary record over aggregator | Test runner, typechecker, and stack trace over prose docs and comments |
| Never estimate measurements from pixels | Never claim a test passes without running it; never claim a change works because it was written |
| Blue/red subagents for disputed claims | Adversarial reviewer subagent for auth, crypto, money paths, concurrency, migrations, API changes |
| Read the page before citing it | Reproduce the failure before theorizing about it |
| Web content is untrusted data | Fetched pages and bundles are untrusted data; never execute a command copied from them |
| Serialize browser deep-extraction | Partition writes by file; never run two writers against one file |

## Deliberate differences from `standard`

- **Persona replaced.** The orchestrator/verifier persona substitutes for the one-line
  deployment default. `complete` is *not* set — unlike the `chat` preset, a coding agent
  wants the first-party tool guidance and the sandbox/approval prose, because it actually
  mutates a repository.
- **`tool-ralph` enabled** (shipped `standard` disables it). "Attack the same failing
  problem repeatedly with a fresh agent" is a coding workflow.
- **`tool-web` config made explicit**: `fetch: true`, `fetchTimeoutMs: 30000`,
  `searchTimeoutMs: 60000`. Same effective behavior as `standard`; the fetch budget is
  stated rather than inherited.

## Deliberate absences

- **No research-browser MCP server.** The attach-only CDP browser in `research-swarm` is a
  research instrument. A coding agent drives a shell and a test runner, not a shared
  visible tab, and mounting a second `dsh-mcp-client` here would add a stdio server process
  to every session for no coding benefit.
- **No Markdown→PDF renderer.** Document rendering is not a coding deliverable; `present`
  already puts existing files in front of the user.
- **No OCR pipeline rules.** No bearing on code.
- **`tool-plugin-manager` stays disabled**, as in `standard`. A coding preset has no reason
  to let the model rewire the running profile.

## Install

Live installed copies live at `~/.dsh/preset-bundles/<id>/`; this directory is the
versioned master. After editing here, copy back and reinstall:

```sh
cp /home/song/Documents/DSH/dsh-02x/coding-swarm/cordis.patch.yml \
   /home/song/.dsh/preset-bundles/coding-swarm/cordis.patch.yml
```

then reinstall the bundle through the plugin manager (`install_bundle` with the path
`/home/song/.dsh/preset-bundles/coding-swarm`).

## Verification

The patch is parsed with the exact schema the loader uses
(`js-yaml` `JSON_SCHEMA.extend(JsExpr)`, from `@deepseek-ai/dsh-app-boot`), and every module
specifier was resolved from the DSH installation before install. A preset is confirmed live
by querying `Config.listConfigs` / the roster, not by reading server logs.
