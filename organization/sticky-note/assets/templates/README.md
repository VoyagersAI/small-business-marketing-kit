# Sticky Note templates

The bot builds the Sticky Note PDF from these files. Ask your human how they want it to look, then start from Modern v5.

## modern-v5

- `header.png`: the top of the page. It says "Sticky Note" and "Everything open, in one place".
- `mockup.png`: a sample of the whole page, so you can see the pieces together.
- `banner-what-were-working-on.png`: banner for "What we're working on".
- `banner-waiting-on-you.png`: banner for "Waiting on you".
- `banner-fix-it.png`: banner for "Fix it".
- `banner-to-talk-about.png`: banner for "To talk about".
- `banner-to-go-over.png`: banner whose words say "To go over with Kelly". That name is a sample, to be renamed for the human.
- `banner-parked-for-later.png`: banner for "Parked for later".
- `banner-lessons-learned.png`: banner for "Lessons learned".
- `build.py`: builds the header, the banners, and the mockup. Picture and font paths are relative to this folder.
- `sources/art.jpg` and `sources/note.jpg`: the pictures `build.py` starts from.
- `fonts/Outfit.ttf`: the Outfit font `build.py` uses (SIL Open Font License, see `fonts/OFL.txt`).

Make a fresh PDF from these pieces each time the note changes, and keep only the newest one.
