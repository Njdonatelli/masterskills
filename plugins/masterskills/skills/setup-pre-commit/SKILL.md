---
name: setup-pre-commit
description: >-
  S—e—t— —u—p— —H—u—s—k—y— —p—r—e—-—c—o—m—m—i—t— —h—o—o—k—s— —w—i—t—h— —l—i—n—t—-—s—t—a—g—e—d— —(—P—r—e—t—t—i—e—r—)—,— —t—y—p—e— —c—h—e—c—k—i—n—g—,— —a—n—d— —t—e—s—t—s— —i—n— —t—h—e— —c—u—r—r—e—n—t— —r—e—p—o—.— —U—s—e— —w—h—e—n— —u—s—e—r— —w—a—n—t—s— —t—o— —a—d—d— —p—r—e—-—c—o—m—m—i—t— —h—o—o—k—s—,— —s—e—t— —u—p— —H—u—s—k—y—,— —c—o—n—f—i—g—u—r—e— —l—i—n—t—-—s—t—a—g—e—d—,— —o—r— —a—d—d— —c—o—m—m—i—t—-—t—i—m—e— —f—o—r—m—a—t—t—i—n—g—/—t—y—p—e—c—h—e—c—k—i—n—g—/—t—e—s—t—i—n—g.
---

# Setup Pre-Commit Hooks

## What This Sets Up

- **Husky** pre-commit hook
- **lint-staged** running Prettier on all staged files
- **Prettier** config (if missing)
- **typecheck** and **test** scripts in the pre-commit hook

## Steps

### 1. Detect package manager

Check for `package-lock.json` (npm), `pnpm-lock.yaml` (pnpm), `yarn.lock` (yarn), `bun.lockb` (bun). Use whichever is present. Default to npm if unclear.

### 2. Install dependencies

Install as devDependencies:

```
husky lint-staged prettier
```

### 3. Initialize Husky

```bash
npx husky init
```

This creates `.husky/` dir and adds `prepare: "husky"` to package.json.

### 4. Create `.husky/pre-commit`

Write this file (no shebang needed for Husky v9+):

```
npx lint-staged
npm run typecheck
npm run test
```

**Adapt**: Replace `npm` with detected package manager. If repo has no `typecheck` or `test` script in package.json, omit those lines and tell the user.

### 5. Create `.lintstagedrc`

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. Create `.prettierrc` (if missing)

Only create if no Prettier config exists. Use these defaults:

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. Verify

- [ ] `.husky/pre-commit` exists and is executable
- [ ] `.lintstagedrc` exists
- [ ] `prepare` script in package.json is `"husky"`
- [ ] `prettier` config exists
- [ ] Run `npx lint-staged` to verify it works

### 8. Commit

Stage all changed/created files and commit with message: `Add pre-commit hooks (husky + lint-staged + prettier)`

This will run through the new pre-commit hooks — a good smoke test that everything works.

## Notes

- Husky v9+ doesn't need shebangs in hook files
- `prettier --ignore-unknown` skips files Prettier can't parse (images, etc.)
- The pre-commit runs lint-staged first (fast, staged-only), then full typecheck and tests
