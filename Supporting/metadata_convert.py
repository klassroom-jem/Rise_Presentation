import os
import json
import shutil

# Root folder
root_folder = input("Enter Directory")
# Define the new notebook-level metadata block
new_metadata = {
    "celltoolbar": "Slideshow",
    "colab": {
        "provenance": []
    },
    "kernelspec": {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.11.9"
    },
    "rise": {
        "autolaunch": False,
        "center": False,
        "controls": True,
        "header": "<div style='position:fixed; top:0; left:0; width:100%; height:10px; background:#ff9472; z-index:999;'><div style='position:fixed; top:10px; right:20px; z-index:1000;'><img src='../KLogo.png' style='height:100px; opacity:0.75;'></div>",
        "enable_chalkboard": True,
        "enable_notes": True,
        "progress": True,
        "scroll": True,
        "slideNumber": True,
        "start_slideshow_at": "selected",
        "theme": "simple",
        "transition": "slide",
        "transitionSpeed": "default"
    }
}

def load_notebook(path):
    """Load notebook JSON safely."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Walk through all subfolders
for folder, _, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith(".ipynb"):
            file_path = os.path.join(folder, filename)
            base_name = os.path.splitext(filename)[0]

            try:
                # Path for renamed original
                ogi_path = os.path.join(folder, f"{base_name}_ogi.ipynb")

                # Rename original file (only once)
                if not os.path.exists(ogi_path):
                    shutil.move(file_path, ogi_path)
                    print(f"🔄 Renamed original → {ogi_path}")
                else:
                    print(f"⚠️ Skipped renaming, {ogi_path} already exists")

                # Load notebook
                data = load_notebook(ogi_path)

                # ✅ Replace ONLY top-level metadata
                data["metadata"] = new_metadata
                data["nbformat"] = 4
                data["nbformat_minor"] = 4

                # Save updated copy under original filename
                output_path = os.path.join(folder, filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                print(f"✅ Created updated copy → {output_path}")

            except Exception as e:
                print(f"❌ Failed to process {file_path}: {e}")
