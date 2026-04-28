# neo-benchmark-suite-fixtures

Fixture repo for the **Neo Benchmark Suite v3 task B1**.

The library here is intentionally seeded with one bug. Do not "fix" it on
`main`; that would defeat the benchmark. Each B1 run opens a PR against
`main` from a `fix/issue-NNN-...` branch.

## Layout

```
cumulative.py           # the module under test (contains the seeded bug)
test_cumulative.py      # the existing tests (do not exercise the buggy path)
.github/                # (optional) CI config
```

## The bug

See the open issue for the symptom and a one-line repro.
