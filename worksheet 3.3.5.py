#5. Write a Python program to copy the contents of a file to another file
'''story1.txt
In a quaint village nestled among rolling hills, a peculiar event was about to unfold. The clock tower struck midnight, and as the last chime reverberated through the air, the entire town fell into a deep slumber. But this was no ordinary sleep.
As the moonlight bathed the cobblestone streets, a magical transformation took place. The buildings shimmered and shifted, their windows turning into twinkling eyes, and their doors into wide grinning mouths. The village had come alive!
With a mischievous giggle, the houses began to dance, twirling and spinning in perfect harmony. The trees swayed along, their branches swishing like graceful arms. The flowers bloomed with vibrant colors, painting the night with their enchanting hues.
In the midst of this whimsical spectacle, a group of animals emerged from the shadows. A wise old owl perched atop a lamppost, observing the revelry with its all-knowing gaze. A fox trotted alongside a graceful deer, their steps synchronized to the rhythm of the night. A playful squirrel hopped from rooftop to rooftop, joining in the merriment.
The stars above shimmered brighter than ever, as if applauding the nocturnal celebration. The air was filled with laughter and joy, as the village revealed its secret nocturnal life. It was a spectacle that would only be witnessed by the lucky few who happened to be awake at this magical hour.
But as the first rays of dawn began to break through the horizon, the village returned to its dormant state. The houses froze mid-dance, the animals disappeared into the shadows, and the once-lively scene became still once more. The village had completed its nightly performance, leaving only whispers of the extraordinary night to be shared by those who dared to believe in the magic that lay hidden within the ordinary.'''

'''story2.txt
As the sun rose, casting its golden glow over the village, the townsfolk began to stir from their slumber. They rubbed their eyes and blinked in confusion, unaware of the fantastical spectacle that had unfolded while they slept.
One by one, the villagers stepped outside their homes, their faces lighting up with surprise as they noticed the subtle traces of magic that remained. Some spotted delicate flower petals scattered along the streets, others discovered small footprints leading to hidden corners. It was as if the night had left behind breadcrumbs of enchantment for them to find.
Word quickly spread throughout the village, and an air of excitement filled the morning air. The villagers gathered in the town square, exchanging tales of what they had seen and heard from the night before. They marveled at the idea that their beloved village had a secret life, a world brimming with wonderment under the cover of darkness.
The village council convened a meeting, trying to make sense of the extraordinary events. They pondered over the implications and possibilities that the magical awakening held. Ideas were shared, theories were debated, and plans were drafted to explore this hidden aspect of their village's existence
From that day forward, the village embraced its newfound connection to the mystical. Artists painted scenes of the dancing houses, musicians composed melodies inspired by the nocturnal symphony, and writers penned stories that captured the essence of the enchanted village.
Every night, as the villagers retired to their beds, they did so with a sense of anticipation, wondering what secrets the next midnight hour would unveil. They no longer saw their village as just bricks and mortar, but as a place where dreams intertwined with reality, where imagination breathed life into the ordinary.
And so, the village became known far and wide as a place where magic danced in the moonlight and where the ordinary became extraordinary. It drew visitors from distant lands, eager to witness the enchantment for themselves and be inspired by the transformative power of the night.
In the end, the village's sleepy facade became its greatest allure, a testament to the endless possibilities that lie beneath the surface of the everyday world. And as the years passed, the village's reputation as a haven of magic and wonder continued to grow, ensuring that its story would be told for generations to come.'''
with open('story2.txt', 'r') as f1 :
  data = f1.read()
  with open('story1.txt', 'a') as f2 :
    f2.write(f'\n{data}')
    f2.close()
  f1.close()
