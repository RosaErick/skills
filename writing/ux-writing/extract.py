import fitz
import os

folder = r"c:\Dev\Noonly\soft-ui-dashboard-tailwind\.agent\skills\ux-writing\references"
pdfs = [
    "1671446040-lBPa.pdf",
    "20220201181424-2022-02-01ebook181200.pdf",
    "Don't Make Me Think, Revisited, 3rd Edition.pdf"
]

out_file = r"c:\Dev\Noonly\soft-ui-dashboard-tailwind\.agent\skills\ux-writing\extracted_content.txt"

with open(out_file, "w", encoding="utf-8") as f:
    for pdf in pdfs:
        p = os.path.join(folder, pdf)
        try:
            doc = fitz.open(p)
            f.write(f"=========================================\n")
            f.write(f"--- BOOK: {pdf} ---\n")
            f.write(f"=========================================\n\n")
            
            toc = doc.get_toc()
            f.write("--- TABLE OF CONTENTS ---\n")
            if toc:
                for t in toc:
                    f.write("  " * (t[0]-1) + str(t[1]) + f" (Page {t[2]})\n")
            else:
                f.write("No TOC found.\n")
            
            f.write("\n--- HEADINGS AND BOLD TEXT (Pages 5 to 70) ---\n")
            for i in range(5, min(70, len(doc))):
                page = doc[i]
                blocks = page.get_text("dict").get("blocks", [])
                for b in blocks:
                    if "lines" in b:
                        for l in b["lines"]:
                            for s in l["spans"]:
                                text = s["text"].strip()
                                # size > 12 is usually a heading, bold is sometimes emphasis
                                if text and (s["size"] > 14 or "Bold" in s["font"]):
                                    f.write(f"{text}\n")
            f.write("\n\n")
            doc.close()
            print(f"Processed {pdf}")
        except Exception as e:
            f.write(f"Error reading {pdf}: {e}\n\n")
            print(f"Error processing {pdf}")
