import gtts as gt 
import os      
 
TamilText="வணக்கம்.அறம் செய விரும்பு, ஆறுவது சினம், இயல்வது கரவேல், ஈவது விலக்கேல், உடையது விளம்பேல். நன்றி!"
tts = gt.gTTS(text=TamilText, lang='ta')
tts.save("Tamil-Audio.mp3")
os.system("Tamil-Audio.mp3")