# masterskills

Personal hosted Claude Code plugin marketplace. One repo, one plugin, 382 skills. Add the
marketplace once on a machine, install the plugin, and every skill is available everywhere.

## Install on a new machine

```
/plugin marketplace add nicolasdonatelli/masterskills
/plugin install masterskills@masterskills
```

Or from the CLI:

```bash
claude plugin marketplace add nicolasdonatelli/masterskills
claude plugin install masterskills@masterskills
```

`marketplace add` also accepts a full URL or a local path, which is useful before the repo is
pushed:

```bash
claude plugin marketplace add C:/Users/nicol/GitHub/masterskills
```

## Update

```bash
claude plugin marketplace update masterskills
```

Installed plugins track the marketplace, so a `git push` here is all that a new skill needs to
reach every machine.

## Layout

```
.claude-plugin/marketplace.json   generated — the marketplace manifest Claude Code reads
marketplace.config.json           hand-edited — owner, version, plugin blurbs
plugins/masterskills/
  .claude-plugin/plugin.json      generated — the plugin manifest
  skills/<skill-name>/SKILL.md    the skills themselves
SKILLS.md                         generated — browsable index of every skill
scripts/build_manifest.py         regenerates the three generated files from disk
scripts/sync_skills.py            moves skills between ~/.claude/skills and this repo
```

The filesystem is the source of truth. Nothing lists skills by hand — whatever sits at
`plugins/masterskills/skills/<name>/SKILL.md` is what ships.

## Adding or changing a skill

1. Author it where Claude Code already loads it (`~/.claude/skills/<name>/SKILL.md`), or create
   the directory directly under `plugins/masterskills/skills/`.
2. If you authored it locally, bring it in:

   ```bash
   python scripts/sync_skills.py pull --apply
   ```

3. Regenerate the manifests:

   ```bash
   python scripts/build_manifest.py
   ```

4. Commit and push. Other machines pick it up on the next `marketplace update`.

`build_manifest.py` warns — without failing — when a `SKILL.md` has no `description`, when a
frontmatter `name` disagrees with its directory name, or when two skills claim the same name.
Both scripts are stdlib-only Python 3.9+; `sync_skills.py` is a dry run unless given `--apply`.

## Adding a second plugin

Create `plugins/<new-plugin>/skills/…`, add a matching entry to the `plugins` array in
`marketplace.config.json`, and rerun `build_manifest.py`. It writes that plugin's
`plugin.json` and folds it into the marketplace manifest.

## Versioning

Bump `version` in `marketplace.config.json` and rerun the build script — it stamps the
marketplace manifest and every `plugin.json` from that one value.

## License

MIT. See [LICENSE](LICENSE).
