# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one fixed
# plan, the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money, to /output/entry.txt. The gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space, and the judge
# reads exactly the bytes written, line ends included, so write no line end you
# do not mean to show. The program runs twice with no network, and both runs
# must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: fix dead booking links for restaurants, salons and clinics that lose customers every day.",
        "Day 1: search Google Maps for 200 restaurants and salons, click each 'Book' button and phone number, and list the 40 whose booking page is dead or whose number is wrong.",
        "Day 2: build a working booking page for 5 of them, free, with their real menu or services and a working calendar link.",
        "Days 3-10: email each owner a link to their fixed page, showing the broken link beside the working one, and charge $99 to switch it live plus $29 a month to watch the link and keep it working.",
        "Days 11-30: fix 3 a day, ask each buyer for a review, and drop any town where fewer than 1 in 10 owners reply.",
        "The owner already wanted bookings; their system is broken, not their demand, so they answer fast and pay to fix a leak instead of buying something new.",
        "10 fixes in week one is $990, plus $29 a month from each buyer. Keep $50 for a domain and email tool; the rest is profit.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
