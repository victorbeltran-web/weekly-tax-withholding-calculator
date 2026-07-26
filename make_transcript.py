"""
Runs tax_withholding.py interactively (feeding one input at a time) and
reconstructs a realistic terminal transcript with the typed input echoed
inline after each prompt, exactly as a user would see it in a real terminal.
"""
import subprocess
import sys


def run_transcript(inputs, script_path="tax_withholding.py"):
    proc = subprocess.Popen(
        [sys.executable, script_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    transcript_lines = []
    PROMPT = "Enter weekly income for customer (or -1 to stop): $"

    def read_until_prompt():
        chunk = ""
        while True:
            ch = proc.stdout.read(1)
            if ch == "":
                break
            chunk += ch
            if chunk.endswith(PROMPT):
                break
        return chunk

    # Read initial banner + first prompt
    chunk = read_until_prompt()
    transcript_lines.append(chunk)

    for i, value in enumerate(inputs):
        # echo the typed value right after the prompt
        transcript_lines.append(value + "\n")
        proc.stdin.write(value + "\n")
        proc.stdin.flush()

        if value == "-1" or i == len(inputs) - 1:
            # program will exit after this; read whatever remains until EOF
            proc.stdin.close()
            remainder = proc.stdout.read()
            transcript_lines.append(remainder)
            break
        else:
            chunk = read_until_prompt()
            transcript_lines.append(chunk)

    proc.wait()

    return "".join(transcript_lines)


if __name__ == "__main__":
    inputs = ["450", "900", "1800", "3000", "-1"]
    text = run_transcript(inputs)
    with open("transcript_sample_run.txt", "w") as f:
        f.write(text)
    print(text)
