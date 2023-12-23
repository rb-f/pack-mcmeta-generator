# pack.mcmeta generator
Simple python script using tkinter to generate pack.mcmeta files

## How to use
First, download the code by pressing **Code** > **Download ZIP**. Then, extract the zip folder to access the **main.py** file.

Once you're in the file, enter the two fields requested. There are two fields to enter: Description and Pack Format.
- **Description**: The description that will be shown in the Minecraft pack files.
- **Pack format**: The pack format is the format version that will be used in Minecraft. This is needed so Minecraft can identify if your pack is compatible with this version. See https://minecraft.fandom.com/wiki/Resource_pack for a list of resource pack formats.

Now, after that, you'll only need to press **Generate pack.mcmeta**. That will generate your pack.mcmeta file and outputs it to the output box. With this, you can click the box, then press Ctrl+A to select all, then press Ctrl+C to copy. Then, you can copy it to the pack.mcmeta file.

And you're done!

## Known issues
- Generating another pack.mcmeta does **not** replace the new one and currently only inserts new generated pack.mcmeta. To work around generating another pack.mcmeta, just delete the entire output and generate again.
