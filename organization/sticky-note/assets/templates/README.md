# Sticky Note templates

These are the blank Sticky Note templates. Ask your human whether the note is for one person or for a team, and how they want the page to look. Then offer the blank that fits.

## When to offer each one

- **Simple, for one person (template A).** Offer `fill-in/simple.html` when one human and their bot keep the note. They make a copy, replace every [bracket] with their own words, and delete the example rows.
- **Team (template B).** Offer this when people share the note with their bots. The same words are in three files, so offer the one they can open: `fill-in/team.html`, `fill-in/team.docx`, or `fill-in/team.pdf`.
- **Page shells, for the pretty PDF.** Use these when you build the PDF. `page-shells/plain.html` is a simple page. `page-shells/hue-modern.html` is the modern look. `page-shells/render.py` fills either shell from a plain text note.
- **modern-v5.** The pictures for the header and the banners, plus the script that draws them. Use these when you are building or refreshing that look.

## fill-in

Blank notes a person can copy and fill in. Every spot that changes is written in [brackets], like [owner name], [Your name], or [Team name].

- `simple.html`: template A, for one person and their bot. The title line is "[Your name] and [Bot name]".
- `team.html`, `team.docx`, and `team.pdf`: template B, for a team. All three say the same thing. The title line is "[Team name] Sticky Note". It also has who is on the team, what is happening today, what is waiting on a person, what to go over together, and what is blocked.

## page-shells

HTML pages with four placeholders: `{{TITLE}}`, `{{UPDATED}}`, `{{MADE}}`, and `{{BODY}}`. `render.py` replaces them.

- `plain.html`: a simple page. It uses Helvetica or Arial, which are already on most computers.
- `hue-modern.html`: the modern look, with green and yellow notes. The Outfit font and the header picture are saved inside this file. You can send this one file to anyone and the page still looks right.
- `render.py`: fills a shell from a plain text note and writes an HTML file you can turn into the PDF.

How to run it, from this templates folder:

```
python3 page-shells/render.py note.md page-shells/hue-modern.html note.html
```

Swap in `page-shells/plain.html` if they want the simple page.

The note is plain text:

1. Line 1 is the title. It can start with #.
2. Line 2 is the updated line, in your human's own time zone, with a label (for example, "Updated Tue 9:40 AM CT").
3. The rest is the body, with headings and lists.
4. A heading written as `##` that starts with ⭐ becomes the Top 3 box.
5. A heading written as `##` that starts with ⏱ becomes the Got 10 minutes box.

The script stamps `{{MADE}}` with the clock time the file was built. Put your human's time zone on line 2, which is the updated line they read.

The script needs the Python markdown package. If the command says that package is missing, install it with `pip install markdown`.

The Outfit font inside `hue-modern.html` is under the SIL Open Font License. The license text is in `modern-v5/fonts/OFL.txt`.

## modern-v5

- `header.png`: the top of the page. It says "Sticky Note" and "Everything open, in one place".
- `mockup.png`: a sample of the whole page, so you can see the pieces together.
- `banner-what-were-working-on.png`: banner for "What we're working on".
- `banner-waiting-on-you.png`: banner for "Waiting on you".
- `banner-fix-it.png`: banner for "Fix it".
- `banner-to-talk-about.png`: banner for "To talk about".
- `banner-to-go-over.png`: banner whose words say "To go over with [owner name]". Put the bot owner's name in the brackets. The bot owner ([owner's name]) has final approval.
- `banner-parked-for-later.png`: banner for "Parked for later".
- `banner-lessons-learned.png`: banner for "Lessons learned".
- `build.py`: builds the header, the banners, and the mockup. Picture and font paths are relative to this folder.
- `sources/art.jpg` and `sources/note.jpg`: the pictures `build.py` starts from.
- `fonts/Outfit.ttf`: the Outfit font `build.py` uses (SIL Open Font License, see `fonts/OFL.txt`).

Make a fresh PDF from these pieces each time the note changes, and keep only the newest one.
