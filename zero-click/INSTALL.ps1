# Zero-Click preset installer
# Copies this package into the DSH agent-preset root on this machine.
# Safe to re-run: an existing zero-click install is backed up, not overwritten.

[CmdletBinding()]
param(
    [string]$DshHome,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

function Write-Step($m) { Write-Host "  $m" }
function Write-Ok($m)   { Write-Host "  [ok] $m"   -ForegroundColor Green }
function Write-Warn2($m){ Write-Host "  [!]  $m"   -ForegroundColor Yellow }
function Write-Err2($m) { Write-Host "  [x]  $m"   -ForegroundColor Red }

Write-Host ""
Write-Host "Zero-Click preset installer" -ForegroundColor Cyan
Write-Host "===========================" -ForegroundColor Cyan
Write-Host ""

# ── locate source ───────────────────────────────────────────────────────────
$source = $PSScriptRoot
if (-not $source) { $source = (Get-Location).Path }

$composition = Join-Path $source 'agent.cordis.yml'
if (-not (Test-Path $composition)) {
    Write-Err2 "agent.cordis.yml not found next to this script."
    Write-Step  "Run the installer from inside the extracted zero-click folder."
    exit 1
}
Write-Ok "package found: $source"

# ── resolve DSH home ────────────────────────────────────────────────────────
if (-not $DshHome) {
    if ($env:DSH_HOME) { $DshHome = $env:DSH_HOME }
    elseif ($env:USERPROFILE) { $DshHome = Join-Path $env:USERPROFILE '.dsh' }
    elseif ($env:HOME) { $DshHome = Join-Path $env:HOME '.dsh' }
    else {
        Write-Err2 "Cannot determine the DSH home. Pass it explicitly:"
        Write-Step  "  .\INSTALL.ps1 -DshHome 'C:\path\to\.dsh'"
        exit 1
    }
}
Write-Ok "DSH home: $DshHome"

$presetRoot = Join-Path $DshHome '.agent-presets'
$target     = Join-Path $presetRoot 'zero-click'

# ── back up any existing install ────────────────────────────────────────────
if (Test-Path $target) {
    $stamp  = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backup = "$target.backup-$stamp"
    if ($Force) {
        Write-Warn2 "-Force set: removing existing install at $target"
        Remove-Item $target -Recurse -Force
    } else {
        Write-Warn2 "existing install found - backing up to:"
        Write-Step  "  $backup"
        Move-Item $target $backup -Force
    }
}

# ── copy ────────────────────────────────────────────────────────────────────
New-Item -ItemType Directory -Force -Path $presetRoot | Out-Null
New-Item -ItemType Directory -Force -Path $target     | Out-Null

$exclude = @('zip-package.ps1')
Get-ChildItem -Path $source -Force | Where-Object { $exclude -notcontains $_.Name } | ForEach-Object {
    Copy-Item $_.FullName -Destination $target -Recurse -Force
}
Write-Ok "copied package to $target"

# ── verify ──────────────────────────────────────────────────────────────────
$checks = @(
    @{ Path = 'agent.cordis.yml';                     Label = 'composition' },
    @{ Path = 'preset.yml';                           Label = 'metadata' },
    @{ Path = 'skills\axoworks-content\SKILL.md';     Label = 'skill: axoworks-content' },
    @{ Path = 'skills\unpolished-cadence\SKILL.md';   Label = 'skill: unpolished-cadence' },
    @{ Path = 'reference\AXOWORKS-POSITIONING-BRIEF.md'; Label = 'reference corpus' },
    @{ Path = 'reference\AXOWORKS-CADENCE.md';        Label = 'cadence profile' }
)

Write-Host ""
Write-Host "Verifying install:" -ForegroundColor Cyan
$failed = 0
foreach ($c in $checks) {
    $p = Join-Path $target $c.Path
    if (Test-Path $p) { Write-Ok $c.Label }
    else { Write-Err2 "$($c.Label) MISSING at $($c.Path)"; $failed++ }
}

$refCount = (Get-ChildItem (Join-Path $target 'reference') -File -ErrorAction SilentlyContinue).Count
Write-Step "reference files: $refCount"
$skillCount = (Get-ChildItem (Join-Path $target 'skills') -Directory -ErrorAction SilentlyContinue).Count
Write-Step "skills: $skillCount"

Write-Host ""
if ($failed -gt 0) {
    Write-Err2 "$failed check(s) failed. The install is incomplete."
    exit 1
}

Write-Host "Done." -ForegroundColor Green
Write-Host ""
Write-Step "Next steps:"
Write-Step "  1. Restart DSH so the preset roster re-scans."
Write-Step "  2. Start a session on the 'Zero-Click' preset."
Write-Step "  3. Confirm both skills appear: axoworks-content, unpolished-cadence."
Write-Step "  4. Say 'keep it unpolished' to test the cadence loop."
Write-Host ""
