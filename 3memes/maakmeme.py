from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open("meme_background.jpg")


afbeelding.show()


breedte = afbeelding.width
hoogte = afbeelding.height


print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")


print(afbeelding.format, afbeelding.size, afbeelding.mode)

tekengebied = ImageDraw.Draw(afbeelding)

lettertype = ImageFont.truetype("impact.ttf", 40)

tekst = "Coding in Python\nNo problemo!"

tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

afbeelding.show()

achtergrond.save("meme_background.jpg")