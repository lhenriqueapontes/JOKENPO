# AgentOps Strategy Lab

Portfolio project for autonomous decision strategies in Python.

## Run

```bash
python src/strategy_bot.py
python src/evaluate_strategies.py
```

## What it does

- simulates a decision environment;
- compares baseline and adaptive strategies;
- uses recent history to choose actions;
- exports strategy results to CSV.

## Files

```text
src/strategy_bot.py
src/evaluate_strategies.py
reports/strategy_results.csv
```

## Next steps

- add reinforcement learning baseline;
- add stateful memory;
- add YAML configuration;
- add pytest tests;
- add dashboard for strategy comparison.

## License

MIT License.
