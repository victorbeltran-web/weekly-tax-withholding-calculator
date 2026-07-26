# Weekly Tax Withholding Calculator

A simple Python console application that calculates the tax withheld from a
customer's weekly income based on a tiered bracket system, and reports the
average weekly income and average weekly tax withholding across every
customer entered in a session.

## Tax Bracket Rules

| Weekly Income Range        | Tax Rate |
|-----------------------------|----------|
| Less than $500              | 10%      |
| $500 to less than $1,500    | 15%      |
| $1,500 to less than $2,500  | 20%      |
| $2,500 and above            | 30%      |

## Files

- `tax_withholding.py` — main program (source code)
- `pseudocode.txt` — pseudocode for the algorithm
- `make_transcript.py` — helper script used to generate sample terminal transcripts
- `render_screenshot.py` — helper script that renders transcripts as terminal-style screenshots
- `transcript_sample_run.txt`, `transcript_boundary_run.txt` — captured test transcripts
- `screenshot_sample_run.png`, `screenshot_boundary_run.png` — screenshots of the app executing

## How to Run

```bash
python3 tax_withholding.py
```

Enter a weekly income when prompted. Enter `-1` to stop and see the summary
(total income, total tax withheld, average weekly income, and average weekly
tax withholding across all customers entered).

## Example

```
Enter weekly income for customer (or -1 to stop): $450
  -> Tax rate applied : 10%
  -> Tax withheld     : $45.00
```

## Author

Prepared with Perplexity Computer.
