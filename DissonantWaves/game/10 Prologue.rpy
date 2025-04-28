#Reminder: Don't feed josh too many compliments - they'll get to his head.
label Act0:
    label Act0_Diner1:
        #Prologue, Scene 1 - Diner

        show black with dissolve

        "{i}Ding ding{/i}"

        show bg diner with dissolve

        "The familiar jingle of the diner door announces my presence. I scan the room until my eyes set on a certain duo at our usual corner window seat."
        "I pause for a second at the entrance, taking my time to see every detail of the diner I had been going to since I was a kid. After all, it would
        be a while till I would set foot in the establishment again."
        "Waving at the waitress, Claire, behind the counter and making sure the owner and cook, Frank, knew I was in so I could give him a friendly nod (he gets mad if
        I visit and don't say hello) I catch the last snippets of my childhood friends' conversation."

        show May happy at halfleft

        May.c worried "Luke, that's not how it works, and you know it."

        show Luke happy at halfright

        Luke.c "Yeah, I know, but think about it."        
        May.c "I'm not putting a tie on my cat so you can call him ‘Professor Mittens'."
        Luke.c "But isn't that so much more sophisticated than just regular ‘Mittens'?"
        May.c "I don't think Mittens cares how sophisticated his name is, he's a cat!"

        menu:
            "Interrupt them":
                jump Act0_Diner1_Choice1_Option1
            "Laugh along":
                jump Act0_Diner1_Choice1_Option2
            "Sarcastically comment":
                jump Act0_Diner1_Choice1_Option3
            "Let them continue":
                jump Act0_Diner1_Choice1_Option4

    label Act0_Diner1_Choice1_Option1:
        TempRay.n "You two finished? Or should I wait until Luke's shitty idea runs its course?"
        "Luke grins in my direction as May mouths out a ‘thank you' for the save. I can't leave these two alone for one second, I swear."
        Luke.c happy "If it isn't the big bastard himself! What took you so long?"
        TempRay.n "Packing, like you should've been doing."

        jump Act0_Diner2

    label Act0_Diner1_Choice1_Option2:
        "I laugh at the two's antics, giving Luke a pat on the back. Luke's a good guy but I think he runs May's sanity down to its very last end.
        It's a good thing she's used to it."
        TempRay.n "Luke being Luke?"
        May.c neutral "You have no idea. You finished packing yet?"
        TempRay.n "Yeah, just got it done actually, why I was a little late, sorry about that."
        Luke.c neutral "No problem dude. Glad you showed up though, Frank will be glad to see another friendly face before we're gone."
        TempRay.n "We won't be gone long, I'm sure he'll cope. You packed yet?"

        jump Act0_Diner2

    label Act0_Diner1_Choice1_Option3:
        TempRay.n "This another one of Luke's bright ideas?"
        "Luke snorts at the comment, though May vigorously nods her head, relieved to be brought out the conversation."
        May.c "I doubt Luke will ever get to the stage of ‘budding entrepreneur' but if his business ideas are anything like his regular ideas, god help us all."
        Luke.c "Yeah yeah, keep up your sarcastic wall. I know you think it's a good idea. Where were you anyway?"
        TempRay.n "Practicing blood magic."
        May.c neutral "Or packing."
        "I point a finger towards May in affirmation. At least my snarky repertoire isn't lost on everyone."
        May.c "Something you should have been doing too, Luke."

        show Luke neutral
        jump Act0_Diner2

    label Act0_Diner1_Choice1_Option4:
        "I let them continue, slipping into the booth and sitting opposite them. Seems they're still too engrossed in their conversation to notice me.
        I'll be honest, sometimes it's hard to tell if their arguments are affectionate or if they actually do hate each other."
        Luke.c "That cat has feelings too you know!"
        May.c "All his feelings to you are anger. Much like mine actually."
        Luke.c neutral "The kitten doesn't fall far from the litter. Mostly because they always land on their feet."
        May.c "That doesn't work when you change apples for cats, Luke."
        "May rolls her eyes, the exaggeration of the motion also clues her in on the fact I was sitting across from them. I give her a small shy smile
        and she breaks out into a grin."
        May.c neutral "You're finally here! You all done packing then?"
        "I nod my head in confirmation. Luke gives a thumbs up at the news though that's not lost on May."
        May.c "You should follow in their footsteps you know."

        jump Act0_Diner2

    label Act0_Diner2:
        "Luke waves his hand dismissively, laughing a little."
        Luke.c neutral "That's a tomorrow morning job."
        "May looks at me exasperatingly and all I can do is shrug in response. May's been trying to get Luke organised for our entire lives.
        The closest she's ever gotten is managing to get Luke to bring a spare change of underwear at a sleepover. Once."

        show Claire happy at farright with dissolve

        Claire.c "If it ain't our esteemed customers. What can I get you lot today?"
        May.c happy "Our usuals, please."
        Claire.c "Of course, three hot chocolates, with extra cream, extra marshmallows and a little umbrella in each."
        "The first time we came to Frank's Diner we foolishly got Luke to order for the three of us. After that it became a kind of ritual, whether
        I liked the hot beverage or not, it did somehow taste much better in this diner with May and Luke."
        May.c "Oh and can it come with a message?"
        Claire.c "Absolutely, what do you want it to say this time?"

        show May neutral

        "May blushes. She always did this. May would always come up with some sort of message to say to use but she always thought it was way too
        cringy and embarrassing. Never stopped her from following through with it though."
        May.c "Bonds forged in the fires of friendship."

        show Luke happy

        "Luke stifles a laugh and I smirk in response. May glares at us, only causing Luke and I to laugh out loud."
        May.c "Shut it."
        Claire.c "I think it's beautiful, darling. Don't let those two get to you, they'll be lost once you leave."

        show Luke neutral

        "May smirks in victory as Luke and I share a hurt look."
        Claire.c "Anyway, who am I making this out to?"
        Luke.c "Claire? We've been going here for ages."
        Claire.c "Don't be like that, hun. You three will be out of our hair soon, at least let me pretend like it's our first meeting.
        Brings back the memories, I'm sure Frank will appreciate it too."
        May.c "The first one is to May."
        Claire.c "Thanks, sweetie, now is that with a ‘y' or an ‘ae'?"
        May.c "A ‘y'. Like the month."
        Claire.c "Thanks. What about you, son?"
        Luke.c "It's Luke. Spelt like the name. Luke."
        "Claire smirks, jotting it down on her pad before turning to me."
        Claire.c "And your name, hun?"

        # Custom name functionality for Ray
        label namingRay:
            $ clairePatience = 5
            $ playerName = renpy.input("What is your name?", "Ray", length = 15, exclude = " 0123456789+=,.?!<>").strip() or "Ray"
            $ playerNameLower = playerName.lower()
            if playerNameLower in bannedContent:
                Claire.c "No, that's not right."
                jump namingRay
            else:
                Claire.c "Is [playerName] right?"
                menu:
                    "Yes":
                        jump Act0_Diner3
                    "No":
                        $ clairePatience -= 1
                        if clairePatience == 1:
                            Claire.c @ worried "I swear on your aunt's flowerbeds, do not make me come over there and rename you myself."
                            "Claire stares at me for a moment and then brightens up again."
                        elif clairePatience == 0:
                            $ Ray.n = "Ray"  
                            jump Act0_Diner3
                        jump namingRay
        jump Act0_Diner3

    label Act0_Diner3:
        $ Ray = PlayerCharacter(Character(playerName),name = playerName)

        Claire.c "Wonderful, that's three hot chocolates with extra cream, extra marshmallows and a little umbrella out to May, Luke and [Ray.n]. I'll be back shortly."
        "Claire smiles one more time before leaving to make our drinks."

        hide Claire happy with dissolve

        May.c "Going back to your packing, Luke-"
        "May is cut off by Luke groaning, obviously not in the mood for another lecture. May's eyes soften slightly, I guess she might
        actually let him off easy for once."
        May.c "Just, make sure you actually do it. I'd check myself in the morning, but my train's at 6."
        "Luke sighs and I follow suit with a sad smile."

        show Luke worried

        Luke.c "Can't believe you're gone for good."
        "May had always been the most ambitious of our little group. Whilst Luke and I were steadily going through the motions of uni life,
        May was making sure she could get herself out of our sleepy town of Creekford when we got back."
        "Now she had got some big shot internship job at a media company in the city.
        Which also meant for the first time in our lives, our trio would be split up."
        May.c "You know we can't stay here forever. Creefkford's home to two types of people. Families and the retired. We're neither of those,
        it was gonna happen eventually."
        Ray.c "Still didn't think it would all happen so soon."
        Luke.c "Yeah, felt like a lifetime away."
        "It was a shock to be sure when May told us about the news. Though it was an inevitable shock. Luke and I knew at some point May would
        go on to achieve her dreams, working in television and making all us in Creekford proud."
        "We just hoped we could sit and hang out at this diner forever. Hopeless thoughts, we know, didn't mean we couldn't believe in the fantasy."
        May.c "I'm not gone forever, guys. It feels like you people think I'm dying or something."
        "May's official going away party was yesterday. Practically everyone in town had to send their best wishes to the pride of Creekford.
        Honestly it was a lot of pressure, but May handled it well, she always does."

        show Luke neutral

        Luke.c "Remember to call us, alright? We're not letting you get away from us."
        Ray.c "Yeah, you'll still be putting up with me and Luke until we turn grey. Don't think you're escaping just yet."
        "I wouldn't say Luke and I were riding May's coattails, but there was always a sense that she was ahead of us. She knew what she wanted to do
        and actually worked her ass off to get there, meanwhile Luke and I just kinda spent our time sitting around."
        "Sometimes I wonder if everyone just see us as May's cheerleaders, or worse, think we're holding her back."
        May.c "You're sounding like my mums, I'll call, don't worry. Normally I'm the one fussing over you guys. I still remember when both of you fell in the creek.
        You idiots nearly gave me a heart attack."

        show Luke happy

        "We laugh at the memory. It was about 6 or 7 years ago. We were younger and much more confident in our abilities, or overconfident, I guess.
        Luke thought he could jump further than me, obviously I took that as a personal challenge and one thing led to another."
        "Needless to say, emergency services were called and Luke and I weren't allowed out of our houses for a month. Good times.
        We mull on the years of cherished adventures. Time we'll keep wanting to relive, but never will. For life goes on."

        show Luke worried

        Luke.c "Hey, May? Can you promise us something?"
        "The very rare sight of Luke being serious. He'd been taking May's leaving pretty hard. Of course, we were both torn up about it, but Luke even more so."
        "He has this crazy idea that May and I will go on to do great things and leave him behind to flounder on his own. Like we'd ever leave him."
        May.c "Of course. So long as its not about cats and ties."

        show Luke neutral

        "Luke's lips quirk into a smirk but he quickly looks away from the two of us, staring outside of the window and taking in the summer view."
        Luke.c "Promise me you won't forget about us?"
        "May gives me a knowing look. She caught on as quickly as I did to what Luke was thinking."
        May.c "Come here big guy."

        show May neutral at mid with move

        "She wraps him up in a hug before turning her head towards me."
        May.c "And don't think you're getting away from this either."
        "I join in on the hug, a little awkwardly because of the fact I have to lean over the table but the sentiment stands.
        May whispers into the group, making sure her words are felt passionately to the two of us."
        May.c "I will never forget you guys. No matter what happens, no matter what life throws at us. We'll face it, together. Because that's who we are.
        So don't think for even for a second, I'd stop loving and caring about you guys. It just won't happen."
        May.c "Now no more of this, or I'll cry. And if I cry, you cry, Luke. And if you and I cry, [Ray.n] cries. And that won't look good for any of us."
        "We all nod and separate just in time for Claire to come back to our table to deliver our drinks."

        show May neutral at halfleft with move
        show Claire happy at right with dissolve

        Claire.c "Frank's still tied up in the kitchen but he wanted me to tell you guys that although you ‘troublesome trio' might be gone,
        you'll always have a home here at the diner."
        Claire.c "You'll be going off on your own adventures now but don't forget to come back and check in with us folk in Creekford. We'd appreciate it."
        "The rest of us offer our assurances that we'd be back. Creekford may be a sleepy town in the middle of nowhere, but it was our sleepy town in the middle of nowhere."

        hide Claire happy with dissolve

        "Once she leaves, May leans against the table, grinning at Luke and I."
        May.c "Now, enough about me. Are you guys excited about going to the island?"
        "Ah, yeah, the island. One of the perks about May's brand spanking new job was that she was given the task of finding two extra participants for the
        upcoming reality tv show she would be helping out on. {i}Maybe Manawa?!{/i} The upcoming show taking the world by storm."
        "Guess Luke and I would be able to get one last bit of leeching out of our money horse that was our best friend. Was I actually excited to go to the island?"

        menu:
            "Of course":
                jump Act0_Diner3_Choice1_Option1
            "No. I hate the idea":
                jump Act0_Diner3_Choice1_Option2
            "No. I hate the idea (sarcastic)":
                jump Act0_Diner3_Choice1_Option3
            "Cautiously optimistic":
                jump Act0_Diner3_Choice1_Option4

        label Act0_Diner3_Choice1_Option1:
            Ray.c "Of course. What's there not to like? We've barely ever been out of Creekford and now we get an all expense covered trip to an island? I can't wait!"
            Luke.c "What do you mean ‘barely ever been out of Creekford'? Remember that holiday I planned after sixth form? You guys said you loved it."
            "May bristles and I can only give an uneasy smile in Luke's direction. He's opened the wrong can of worms."
            May.c "You said we were going to Argentina."
            "The response from our friend is through gritted teeth, the sheer malice behind the words causes Luke and I to shrivel up in fear."

            show Luke happy

            Luke.c "And we did."
            "Although in a life-or-death scenario, Luke still tries to defend himself, though the conviction behind the words falls flat against May's ire."
            Ray.c "No offence man, but I don't think you explained the trip properly."
            Luke.c "What do you mean?"
            "May's fist comes flying down against the table, the salt and pepper briefly being launched into the air from the force."
            May.c "I packed an entire suitcase and came over to your house just to sit on your sofa and watch a 4-hour documentary!"
            Luke.c "Oh. I was wondering why you were so dolled up just to see ‘Argentina: the home experience'. In my defence though, that documentary was very immersive."
            May.c "I mean, it was. But that's not the point!"

            $ Ray.friendly += 1
            jump Act0_Diner4

        label Act0_Diner3_Choice1_Option2:
            Ray.c "No. I hate the idea. Sand is coarse and rough and gets everywhere. And what else do I have to enjoy? People? A TV show? Sounds like a waste of our time."
            "May rolls her eyes at my perfectly reasonable response."
            May.c "Come on, [Ray.n]. It'll do you some good to get out the house and see the world. We've been trapped in Creekford for way too long."

            show Luke happy

            Luke.c "Trapped in Creekford? What about that holiday I planned after sixth form?"
            Ray.c "That was shit and you know it."
            "Luke lets out an over-dramatic gasp, as if I'd accused him of murder. May however nods her head in agreement with me, pointing an accusatory finger at Luke."
            May.c "You said we were going to Argentina!"
            Luke.c "And we did!"
            "Luke still tries to defend himself, though the conviction behind the words falls flat against May and I's ire."
            Ray.c "A 4-hour documentary {i}about{/i} Argentina is not the same as {i}going{/i} to Argentina."
            "May's fist comes flying down against the table, the salt and pepper briefly being launched into the air from the force."
            May.c "I packed a suitcase and everything!"
            "She looks distraught as she reminds herself of the memory."
            Luke.c "Oh. I was wondering why you were so dolled up just to see ‘Argentina: the home experience'. In my defence though, that documentary was very immersive."
            May.c "I mean, it was. But that's not the point!"

            $ Ray.direct += 1
            jump Act0_Diner4

        label Act0_Diner3_Choice1_Option3:
            Ray.c "No. I hate the idea. Being excited for a free holiday? To a beautiful island? Perish the thought."
            "May playfully rolls her eyes."
            May.c "I guess I'll just uninvite you then. I'm sure there would be hundred of other people more than willing to take your place."
            "Keeping in character I shared a mock look of horror with Luke."
            Ray.c "You wouldn't dare!"
            May.c "Oh, I would. Say goodbye to your one-way ticket to finally getting out the house."

            show Luke happy

            Luke.c "We get out the house all the time. What about that holiday I planned after sixth form."
            "I snort at the memory as May gives out an exasperated sigh."
            Ray.c "Oh yeah, the ‘Argentina' trip. What an enrichening experience."
            Luke.c "You guys said you liked it."
            Ray.c "I was being sarcastic."
            Luke.c "It's very hard to tell over text you know. May enjoyed it, didn't you?"
            "May bristles and I give Luke a smirk. Poor bastard is about to get the chewing out of a life time."
            May.c "You said we were going to Argentina."
            "The response from our friend is through gritted teeth, the sheer malice behind the words causes Luke to shrivel up in fear."
            Luke.c "And we did."
            "May's fist comes flying down against the table, the salt and pepper briefly being launched into the air from the force."
            May.c "It was a 4-hour long documentary about going to Argentina!"
            Ray.c "It was a 4-hour long documentary about going to Argentina."
            May.c "I packed an entire suitcase!"
            Ray.c "She packed an entire suitcase."
            May.c "I spent a month learning Spanish!"
            Ray.c "She spent a month learning Spanish."
            May.c "[Ray.n], you're not helping."
            Ray.c "I'm not helping."
            "She looks distraught as she reminds herself of the memory."
            Luke.c "Oh. I was wondering why you were so dolled up just to see ‘Argentina: the home experience'. In my defence though, that documentary was very immersive."
            May.c "I mean, it was. But that's not the point!"

            $ Ray.sarcastic += 1
            jump Act0_Diner4

        label Act0_Diner3_Choice1_Option4:
            Ray.c "Uneasy, but cautiously optimistic."
            "May gives an encouraging smile."
            May.c "You'll be fine, [Ray.n]. Luke's got your back, haven't you Luke?"

            show Luke happy

            "Luke gives a mock salute."
            Luke.c "Yes, Ma'am. I shall protect the president with my life!"
            Ray.c "We have prime minister, not a president…"
            "Luke ignores my comment, instead opting to offer a reassuring pat on the shoulder."
            Luke.c "It's not like we haven't been abroad before. Remember that holiday I planned after sixth form?"
            "May bristles at the mention of the trip. Uh oh."
            Ray.c "Maybe we shouldn't."
            Luke.c "What? Why not? You guys said you liked it."
            May.c "You said we were going to Argentina."
            "The response from our friend is through gritted teeth, the sheer malice behind the words causes Luke and I to shrivel up in fear."
            Luke.c "And we did."
            "Although in a life-or-death scenario, Luke still tries to defend himself, though the conviction behind the words falls flat against May's ire."
            May.c "It was a 4-hour long documentary about going to Argentina!"
            "Luke shrivels but keeps resolve."
            Luke.c "It was actually only 3 hours and 42 minutes."
            May.c "I packed an entire suitcase!"
            "Luke sinks lower."
            Luke.c "You prepare too much anyway."
            May.c "I spent a month learning Spanish!"
            "Luke looks to me to provide any help though I vigorously shake my head no. He'd dug his own grave. I'll say something nice at his eulogy."
            Luke.c "Spanish is a useful language to know even if you never actually go to Argentina."
            "May stands from her seat to go and hit Luke though that only makes the small chuckle I was trying to stifle to finally be let loose.
            May stops herself before making contact and regards me with a soft smile, dissipating the tension in the room. She sets herself back down."
            Luke.c "In my defence, that documentary was very immersive."
            "May sighs."
            May.c "I mean, it was. But that's not the point."

            $ Ray.shy += 1
            jump Act0_Diner4

    label Act0_Diner4:
        show Luke neutral

        Luke.c "Whatever the point was, the only point that I want to continue pushing is how good this island trip is going to be!"
        "Luke's somewhat forced segue was convincing enough for May to drop the topic and have the conversation continue."
        May.c "You have researched the island, right?"
        "Luke waves a hand dismissively once again."
        Luke.c "Research-smesearch. Right [Ray.n]?"

        menu:
            "Agree":
                jump Act0_Diner4_Choice1_Option1
            "Disagree":
                jump Act0_Diner4_Choice1_Option2

        label Act0_Diner4_Choice1_Option1:
            $ Luke.affection += 1

            Ray.c "Research-smesearch."

            show Luke happy

            "Luke grins and we high-five to May's disappointment."
            May.c "I don't know why I even bother with you two."
            Ray.c "You love us really."

            show Luke neutral

            Luke.c "No matter how deep down you bury it."

            jump Act0_Diner5

        label Act0_Diner4_Choice1_Option2:
            Ray.c "Actually…"
            Luke.c "No, don't tell me you have turned to the prepared side!"
            "Luke looks betrayed whilst May looks proud."
            May.c "Ah yes, young padawan, finally you have harnessed your true potential to be prepared."
            Luke.c "I have never felt such heartbreak until today."

            jump Act0_Diner5
        

        label Act0_Diner5:
            "May ignores Luke, pulling out her laptop from her bag underneath the table. I smile slightly as I see the various badges and patches May has
            decorated her trusty backpack with."
            "Luke and I had been saved by that backpack more times than we could count, always having exactly what we
            needed at any given time."
            "Of course, what we needed was normally an extra pen for an exam or something but that didn't stop the legend of May's
            backpack continuing to be a stalwart companion in our admittingly mundane life."
            May.c "Here's a bit of background on the island."
            "May gently pushes her drink to the side, careful not to spill any of it and opens up her laptop so Luke and I can see."
            May.c "You will be going to the deserted Island of Manawa, just off of Auckland Island."
            Ray.c "Near New Zealand, right?"
            Luke.c "Whoa, do you think I should use my Auzzie accent?"
            May.c "People from New Zealand have a different accent than those from Australia, Luke."
            Luke.c "I'll just use a New Zealand accent then."
            Ray.c "Will it be like your Scottish accent?"

            show Luke happy

            Luke.c "Yep."
            Ray.c "Then no. Just no."

            show Luke neutral

            "Luke and I's repertoire is interrupted as May tries to get us back on track."
            May.c "Right, other than accents, everything else about the island is pretty normal. The weather should be sunny most of the time, it shouldn't change at all.
            The trees look creepy but that's about it."
            May.c "You'll be on the island for about 15 days and will be given challenges every day for essentials like food."
            May.c "After every challenge there will be a public vote on who they like the best.
            That person will then get to request an item of their choice from home to be shipped to them on the island."
            Ray.c "A popularity contest?"
            Luke.c "We're great at those! There has never been a person who has not been swooned by our charm."
            Ray.c "What about Mr Barnett?"
            Luke.c "I said ‘person', [Ray.n], not monster. That guy wouldn't know love if it slapped him in the face. Which his ex-wives did, multiple times."
            May.c "He liked me."
            Luke.c "Yeah, well, everyone likes you. ‘Pride of Creekford this' ‘Pride of Creekford that', you could've accidentally strangled the pet chicken and
            they still would've liked you."
            Ray.c "Didn't you do that Luke?"

            show Luke worried

            Luke.c "By accident! He was so fluffy… Anyway, I got into shit because of that, but if Miss I-Could-Do-No-Wrong did it, I'm sure she would've gotten a medal."
            May.c "The medals were just plastic Luke, they weren't anything to bring home."

            show Luke neutral

            Luke.c "You only say that because you brought them all home."
            May.c "[Ray.n] got a medal, once."
            Luke.c "Yeah, because he partnered with you about the volcano project."
            Ray.c "It was a good volcano."
            May.c "Reminds me of the one in that Argentina documentary"
            Luke.c "You were just going on about hating that documentary!"
            "*Buzz* *buzz*"
            "May picks out her phone from her back pocket, grimacing slightly once she sees the notification."
            May.c "Shit, it's Ma, she's saying I'm going to be late."
            Luke.c "Oh, yeah, I forgot about that."
            May.c "We'd probably be stuck here talking forever."
            "There's a halfhearted attempt at a laugh from the group."

            menu:
                "Lighten the mood":
                    jump Act0_Diner5_Choice1_Option1
                "Insult Luke":
                    jump Act0_Diner5_Choice1_Option2
                "Make a joke":
                    jump Act0_Diner5_Choice1_Option3
                "Stay quiet":
                    jump Act0_Diner5_Choice1_Option4

            label Act0_Diner5_Choice1_Option1:
                Ray.c "We can always come back here after May gets settled in. Creekford's not too far from London."
                Luke.c "Yeah, you're right [Ray.n], I keep thinking this gonna be the last time we see you, May but you can come back whenever you want."
                May.c "Of course. I already told you I wasn't leaving you guys behind. Think of it as another adventure for Maytopia to brag over
                the puny forces of Lukchasaurs and [Ray.n]'s Army."
                Luke.c "You really should've changed your name, dude."
                Ray.c "I was late and the ‘Warlocks of Sintaris' registration period was almost up."
                May.c "Ah, we might have to put on hold some painting sessions until after you guys get back and my workload dies down."
                Luke.c "That sucks, I just got a new box yesterday."
                May.c "You know Threshgar Riders aren't viable in standard, right?"

                show Luke happy

                Luke.c "But they have dual blades! I get to roll double the dice!"
                May.c "2d4 is still pretty bad, Luke."
                Luke.c "‘2d4 is still pretty bad Luke' Alright, just because I don't play with Mandrazi Savages. Every. Single. Time."

                show May happy

                May.c "It's not my fault Syllvanus of the Hunt has 345 firepower which dwarfs your Threshgar Riders pitiful 54 firepower even with the added
                bonus of pack tactics if you ran them with Runsvari attack hounds."
                May.c "That would only get them to 129, which doesn't even dent my Intinius
                Sentinel Guard's 216 shield power. I don't even need to run Ofgrindus' orb of protection on them."

                show May neutral

                Luke.c "But I spent 50 quid to get the golden versions…"
                Ray.c "I think they're pretty cool, Luke"
                Luke.c "And that's why we're bezzie mates, [Ray.n]."
                May.c "Do you really want the last thing we talk about to be Warlocks of Sintaris?"

                show Luke neutral

                Luke.c "No, no I do not."

                $ Ray.friendly += 1
                jump Act0_Diner6


            label Act0_Diner5_Choice1_Option2:
                Ray.c "That's only because Luke doesn't shut his goddamn mouth half the time. He'd talk a con artist into sleep."
                Luke.c "Hurtful. I can't help but feel this unsolicited attack is because of the fact my Threshgar Riders recently came in the post
                and you're scared I'll trounce you next time we fight."
                May.c "I mean when you say ‘trounce', technically Threshgar Riders aren't viable in standard Warlocks of Sintaris play."

                show Luke happy

                Luke.c "What? But they have duel blades! I roll double the dice!"
                Ray.c "Double nothing is still nothing, mate."
                Luke.c "It's actually 2d4."
                May.c "2d4 is still pretty bad, Luke."

                show Luke neutral

                Luke.c "‘2d4 is still pretty bad Luke' Alright, just because I don't play with Mandrazi Savages. Every. Single. Time."

                show May happy

                May.c "It's not my fault Sylvanus of the Hunt has 345 firepower which dwarfs your Threshgar Riders pitiful 54 firepower
                even with the added bonus of pack tactics if you ran them with Runsvari attack hounds."
                May.c "That would only get them to 129, which doesn't even dent my Intinius Sentinel Guard's 216 shield power.
                I don't even need to run Ofgrindus' orb of protection on them."

                show May neutral

                Luke.c "But I spent 50 quid to get the golden versions…"
                Ray.c "Cause you're a fucking idiot, Luke. I had to buy you lunch for a week because you spent all your money."
                Luke.c "And that's why we're bezzie mates, [Ray.n]."
                May.c "Do you really want the last thing we talk about to be Warlocks of Sintaris?"
                Luke.c "No, no I do not."

                $ Ray.direct += 1

                jump Act0_Diner6


            label Act0_Diner5_Choice1_Option3:
                Ray.c "Forever? I couldn't stomach another second with either of you."
                May.c "Hardy har, [Ray.n]. You're so funny."
                Ray.c "I know, you don't have to be so upfront about it, May, my fans might be listening and get jealous."
                Luke.c "Fans? What do they call themselves, your Warlocks of Sintaris army name?"
                May.c "Why did you go for [Ray.n]'s Army?"
                Ray.c "Because I have the creativity of a thousand poets."

                show Luke happy

                Luke.c "He was late to the registration period."
                Ray.c "I was also late to the registration period."
                Luke.c "Oh, speaking of Warlocks of Sinatris, my Threshgar Riders came in the post yesterday."
                May.c "You know Threshgar Riders aren't viable in standard, right?"
                Luke.c "But they have dual blades! I get to roll double the dice!"
                May.c "2d4 is still pretty bad, Luke."

                show Luke neutral

                Luke.c "‘2d4 is still pretty bad Luke' Alright, just because I don't play with Mandrazi Savages. Every. Single. Time."

                show May happy

                May.c "It's not my fault Syllvanus of the Hunt has 345 firepower which dwarfs your Threshgar Riders pitiful 54 firepower even with
                the added bonus of pack tactics if you ran them with Runsvari attack hounds."
                May.c "That would only get them to 129, which doesn't even dent my Intinius Sentinel Guard's 216 shield power.
                I don't even need to run Ofgrindus' orb of protection on them."

                show May neutral

                Luke.c "But I spent 50 quid to get the golden versions…"
                Ray.c "And I shall mourn them until the end of time. Those poor pennies, needlessly thrown away to fuel one man's incessant
                need to put large half-naked men on two-headed boars."
                Luke.c "Why does everything come with a backhanded comment with you?"
                Ray.c "Because we're, as you like to say ‘bezzie mates', any and all opportunities to take you down a peg, I will."
                Luke.c "Sometimes I wish you wouldn't."
                May.c "Do you really want the last thing we talk about to be Luke's love half-naked men?"
                Luke.c "No, no I do not."

                $ Ray.sarcastic += 1
                jump Act0_Diner6

            label Act0_Diner5_Choice1_Option4:
                "There's a moment of contemplative silence."
                Luke.c "Oh! I just remembered-"
                "I really meant a moment."
                Luke.c "My Threshgar Riders came in the post yesterday. Ah, we probably won't be having a painting session in a while though."
                May.c "Painting session or not, you do know Threshgar *Riders aren't viable in standard play, right?"
                Luke.c "What do you mean? I even picked them out with [Ray.n] this time so I wouldn't pick ones with bad stats."
                Ray.c "I did say you might want to get the Tazerhis Scatterback instead."

                show Luke happy

                Luke.c "But does the Tazerhis Scatterback have duel blades? I don't think so."
                Ray.c "It has 200 more firepower though."
                Luke.c "Firepower isn't everything in Warlocks of Sintaris, it's about the loyalty your troops have to your leader and the passion they have for your cause!"
                May.c "You can't roleplay Warlocks of Sintaris Commander Edition, there aren't any rules for it."
                Luke.c "I don't need rules to showcase the fight of my men, May. You wouldn't get it due to your inferior army."

                show May happy

                May.c "My Syllvanus of the Hunt has 345 firepower which dwarfs your Threshgar Riders pitiful 54 firepower even with the added bonus of pack
                tactics if you ran them with Runsvari attack hounds."
                May.c "That would only get them to 129, which doesn't even dent my Intinius Sentinel Guard's 216 shield power.
                I don't even need to run Ofgrindus' orb of protection on them."

                show Luke neutral

                Luke.c "Jokes on you, I don't even know what half of those words meant."

                show May neutral

                May.c "That's why you lose, Luke. Whenever we play co-op you never pay attention to troops on the other side."
                Luke.c "I pay attention all the time, right [Ray.n]?"
                Ray.c "Well…"
                Luke.c "I said I pay attention all the time, right [Ray.n]? As in, [Ray.n] my bestest of best buddies who strings together the
                bonds of friendship in the forge of camaraderie? You wouldn't leave your brother out to dry, right [Ray.n]?"
                Ray.c "I guess not."
                Luke.c "And that's why we're bezzie mates, [Ray.n]."
                May.c "Do you really want the last thing we talk about to be Warlocks of Sintaris?"
                Luke.c "No, no I do not."

                $ Ray.shy += 1
                jump Act0_Diner6

            label Act0_Diner6:
                "May stands, causing Luke and I to do the same. We managed to stall as much time as we could but the eventuality was always going to be there."
                Luke.c "This is it."
                May.c "Seems like it."
                "May smiles despite it all, and her optimism is infectious."
                May.c "I'll text you guys as soon as I arrive."
                Ray.c "You better."
                May.c "You guys better do the same too when you get to Manawa. And don't forget to bring your portable charger, you won't have any electricity over there. Got it?"
                Luke.c "Yeah, yeah."
                "Luke is dismissive but he definitely appreciates May's caring attitude."
                May.c "Good, I'll be going then."
                "May slides her laptop back into her bag and finishes off the rest of her drink before enveloping me in a goodbye hug."
                May.c "I'm going to miss you, [Ray.n]."
                Ray.c "I'm going to miss you, too."
                May.c "You better call if something goes wrong, I don't want to be left out the loop."
                Ray.c "Likewise."
                May.c "And take care of Luke for me? You know how he is, so you'll have your work cut out for you without me around."
                Ray.c "Don't worry, May. It'll be alright."
                "‘It'll be alright' is such an empty phrase. Only meant to reassure both yourself and the person you're saying it to. We both have no idea if it's going to be alright. No idea at all."
                "We separate, May then turning to Luke, opening up her arms as she slowly engulfs him in a hug of his own."
                Luke.c "I don't want you to go."
                May.c "I know. But I have to."
                Luke.c "Yeah. Yeah, you do. So make us proud."
                "They break from the hug and May starts her way over to the door, waving goodbye to Claire and Frank as she goes. Just before she leaves she turns back to us, beaming a patented May smile."
                May.c "This is Otter Three to Stoat One and Ferret Two, do you receive me, over?"
                Luke.c "This is Stoat One."
                Ray.c "This is Ferret Two."
                Luke.c "We receive you, over."
                May.c "I am clear for takeoff. Before I sign off I'd like to make sure you two wouldn't have too much fun without out me."
                Ray.c "Wouldn't dream of it, Otter Three."
                May.c "Good. Until next time then. I love you guys, I care about you guys and I will always be there for you guys. This is Otter Three, signing off."
                "May gives a final salute, which Luke and I return before leaving the diner."

                scene bg diner with fade

                "{i}*Ding Ding*"

                show Luke worried at mid
                jump Act0_Diner7

            label Act0_Diner7:
                #Prologue, Scene 2 - Diner
                Luke.c "She's going to be alright, right?"
                Ray.c "You sound like a broken record, mate. Of course, she'll be fine. It's us I'm worried about."
                "Luke laughs, though it seems quite forced."
                Luke.c "What are we gonna do now?"
                Ray.c "What do you mean?"
                Luke.c "May's off doing her own thing now, and we're still here in Creekford, like we always have.
                Nothing's changed for us, [Ray.n]. We're still the same kids we were ten years ago."
                Ray.c "Then what do you suppose we do?"
                "My question is answered with silence. A silence we both knew too well. May was the one with the dream and the drive, we were just the cheerleaders. 
                Now we have nothing to cheer for."
                Ray.c "We can think of it when we get back from the island."
                "Luke nods, trying to find any semblance of his usual cheery self."

                show Luke neutral

                Luke.c "You think we'll find some cool people on the island?"

                menu:
                    "Be optimistic":
                        jump Act0_Diner7_Choice1_Option1
                    "Be pessimistic":
                        jump Act0_Diner7_Choice1_Option2

                label Act0_Diner7_Choice1_Option1:
                    Ray.c "I think so. We'll have to work together anyway so I doubt anyone will be an arsehole. And as you've said, there hasn't been a single
                    person who hasn't succumbed to our charm."
                    Luke.c "You're right! Here's hoping they're hot, I'll need all the motivation I can get to get out of this depression."

                label Act0_Diner7_Choice1_Option2:
                    Ray.c "I doubt it. There's billions of people out there but with our luck, the island will be full of arseholes."
                    Luke.c "Dude, you were supposed to cheer me up, not pile on my misery."
                    Ray.c "I'm telling you how it is."
                    Luke.c "Can you tell me how it isn't then?"
                    Ray.c "Fine, the island will be full of supermodels, just waiting for your affection."
                    Luke.c "Now that's more like it."

            label Diner_6:
                show Luke neutral
                Ray.c "May's gone for one minute and you're already perving around."
                show Luke happy
                Luke.c "It's not perving, it's appreciating the human form, [Ray.n]. Don't act like you'd be disappointed if a bunch of supermodels rocked up on the island."
                show Luke neutral
                Ray.c "Depends on what kind."
                Luke.c "Enlighten me then."
                Ray.c "We really need to change your priorities."
                Luke.c "Well I doubt anyone on that island is gonna play Wizards of Sintaris, paint their models with us, join our ultimate frisbee team and like artsy movies."
                Ray.c "You hate artsy movies."
                Luke.c "May didn't."
                Ray.c "Yeah well we're not replacing her, are we?"
                Luke.c "I know. I just miss her already."

                menu:
                    "Reassure him":
                        jump Diner_Reassure_6
                    "Make fun of him":
                        jump Diner_Make_Fun_6
                    "Make fun of him (sarcastically)":
                        jump Diner_Sarcasm_6
                    "Comfort him":
                        jump Diner_Comfort_6

                label Diner_Reassure_6:
                    Ray.c "I know, I do too."
                    Luke.c "Sometimes I wish she didn't take that job at all."
                    Ray.c "You know it was what she wanted. It was what's best for her."

                    show Luke worried

                    Luke.c "That's what I keep telling myself. ‘It's what's best for her'. ‘This is what she wanted'. And I know it's selfish and dickish and shit
                    but what about what I want?"
                    Luke.c "What if all I wanted was to stay in Creekford with you and May forever? Why do we have to move on from being kids?
                    Why do we have to work our arses off just to leave our friends and family behind?"
                    Ray.c "Luke…"
                    Luke.c "I know. I know. Just, venting, you know?"
                    Ray.c "Hey, no matter what happens, I'm still here, man. Always will be."

                    show Luke neutral

                    Luke.c "I know, dude. That's why we're bezzie mates."

                    $ Ray.friendly += 1
                    jump Diner_7

                label Diner_Make_Fun_6:
                    Ray.c "She's been gone 5 minutes dude. Grow up."

                    show Luke worried

                    Luke.c "That's what I've been hearing over and over and over again. ‘Grow up, Luke'. ‘It's what she wanted, Luke'. ‘It's what's best for her, Luke'.
                    And I know it's selfish and I know it's dickish and shit but what about what I want?"
                    Luke.c "What if all I wanted was to stay in Creekford with you and May forever? Why do we have to move on from being kids? Why do we have to work our
                    arses off just to leave our friends and family behind?"
                    Ray.c "Luke you know damn well the answers. You need to stop this."
                    Luke.c "I know. I know. Just, venting, you know?"
                    Ray.c "Yeah, well, if you vent anymore I'll have to shut you up myself."
                    Luke.c "Miss her as much as I do?"
                    Ray.c "Course."

                    show Luke neutral

                    Luke.c "That's why we're bezzie mates."

                    $ Ray.direct += 1
                    jump Diner_7

                label Diner_Sarcasm_6:
                    Ray.c "Welp, she's out the door now. You'll have to propose some other time."

                    show Luke worried

                    Luke.c "You can't tell from my very disappointed face, but I'm laughing at your joke."
                    Ray.c "I'm sure you are. The problem is the fact your face instead portrays the feeling of a puppy being punted off a cliff Sparta style.
                    We just have to let May get on with what she's doing and deal with it."
                    Luke.c "That's what I've been hearing over and over and over again. ‘Deal with it, Luke'. ‘It's what she wanted, Luke'. ‘It's what's best for her, Luke'.
                    And I know it's selfish and I know it's dickish and shit but what about what I want?"
                    Luke.c "What if all I wanted was to stay in Creekford with you and May forever?
                    Why do we have to move on from being kids? Why do we have to work our arses off just to leave our friends and family behind?"
                    Ray.c "Because life, man. The big man upstairs is knocking on your door telling you to get outta bed and continue living. So you have to. May's answered the call, so we have to too."
                    Luke.c "Damn."
                    Ray.c "Pretty deep, eh?"
                    Luke.c "Pretty deep."
                    Ray.c "A shame it means literally nothing."

                    show Luke neutral

                    Luke.c "Yeah, but I appreciated it, that's why we're bezzie mates."

                    $ Ray.sarcastic += 1
                    jump Diner_7

                label Diner_Comfort_6:
                    "I put my hand on his shoulder and try to muster up my most encouraging smile. I wish there was something I could say or something
                    I could do to put Luke at ease. Whatever I did, it seemed to help Luke enough."

                    show Luke worried

                    Luke.c "I've been hearing the same thing over and over again. ‘It's what's best for her'. ‘This is what she wanted'.
                    And I know it's selfish and dickish and shit but what about what I want?"
                    Luke.c "What if all I wanted was to stay in Creekford with you and May forever?
                    Why do we have to move on from being kids? Why do we have to work our arses off just to leave our friends and family behind?"
                    "I let the silence rest after Luke's outburst. Everything he had bottled up after the last few days surrounding
                    May's departure came ever flowing out in a cascade of anger. Once he calmed down I decided to speak up."
                    Ray.c "It's alright."
                    "The same words I'd used before. Just as empty as before. But sometimes you just need to say something, no matter how much truth it holds.
                    Luke nods absentmindedly."
                    "The silence gets heavier and heavier until it feels as though we needed May back for nothing
                    other than to help us hold up this quiet."
                    Luke.c "She's been gone five minutes and I already miss her so much."
                    Ray.c "I miss her too."
                    Luke.c "I know you do. It's probably just as hurtful to you as it is to me, sorry for bringing it up, man."
                    Ray.c "If it makes you feel better man, I'm here for it."

                    show Luke neutral

                    Luke.c "Thanks, that's why we're bezzie mates."

                    $ Ray.shy += 1
                    jump Diner_7
                    
    label Diner_7:
        Ray.c "You know, you're the only one who says that."
        Luke.c "Says what?"
        Ray.c "‘Bezzie mates.'"

        show Luke happy

        Luke.c "Really? Well people should say it more."
        Ray.c "Wouldn't that make you less special?"
        Luke.c "I'm already more than special enough you know. You're lucky to know me."
        Ray.c "Lucky is a bit of a stretch."
        Luke.c "Would you prefer the term fortunate? Blessed?"
        Ray.c "I'd prefer forced."
        Luke.c "You're mean."
        Ray.c "You're sensitive."
        "We laugh and it's just like old times again. May or not, we'd just have to try and make it work, somehow."

        show Luke neutral

        Luke.c "You know, I'm really glad you're here with me, man."
        Ray.c "Uh oh, we're getting sentimental again."
        Luke.c "Quiet, let me praise you and our friendship. We've been basically dicking around our entire lives, never knowing what to do or where to go."
        Ray.c "We always managed to find the top of that hill though."
        Luke.c "Yeah, we'd always find that tree. What did we call it again?"
        Ray.c "Something dumb. Like the Tree of Adventure?"
        Luke.c "Oh right! Adventure Tree!"
        Ray.c "Yeah, that's it! Adventure Tree."
        Luke.c "Right, well yeah, where was I again?"
        Ray.c "We were dicking around?"
        Luke.c "Yes, we dicked around. A lot. Especially before May was around. But we dicked around together."
        Ray.c "That sounds suspicious, mate."
        Luke.c "Stop it. We did everything together and it was great, and it still is great. I'm just glad we never grew apart, you know?"
        Ray.c "I think recruiting May to our ranks really held us together. We had something, or someone to help achieve their dreams."
        Luke.c "May really helped, you're right. I still can't believe she was still able to be so optimistic, especially the situation we found her in."
        Ray.c "Yeah, fucking Alex. They were such a dick. Remember when they confronted us for ‘stealing' May away?"
        Luke.c "Of course. You were like ‘back off, you won't hurt her again' and then they tried to fight you."
        Ray.c "Yeah. I'll be honest, dude, you got your arse handed to you."

        show Luke happy

        Luke.c "Hey, I got one good hit in! You were too busy getting May to safety and calling the police. I had to hold down the fort."
        Ray.c "We could've all ran, you just wanted your movie scene sacrifice moment."
        Luke.c "It helped, didn't it?"
        Ray.c "Yeah, it did, man. You were really cool and May and I couldn't be more grateful for it."

        show Luke neutral

        "Luke smiles. He really was the hero that day and though he tries to play it down he does enjoy the story being brought up every now and then."
        Luke.c "Ah, you keep getting me sidetracked. Reminiscing aside, there is no one else in the world I'd rather have on that island than you. So, like, there, be happy or grateful or whatever."
        "Luke awkwardly grins and I laugh. What a dork."
        Ray.c "Same back at you, man. Friends for life."
        "I raise my fist towards Luke who smirks in response."
        Luke.c "Friends for life."
        "We fist bump and Luke stands up from our table, practically radiating excitement."
        Luke.c "This trip is gonna be great!"
        Ray.c "You still need to pack, remember?"
        "Luke falters slightly, Claire giggles away to herself behind the counter. Typical Luke, his mood flip flops more than a light switch."
        Luke.c worried "Shit."

        jump Plane_1

    label Plane_1:
        #Prologue, Scene 3 - Plane
        #CG of [Ray.n]'s POV in plane with Luke to the side, looking at a tablet with the names of each contestant for the plane ride.
        #Over the top, the chosen characters will appear and present their videos.

        scene bg plane

        "{i}Whir whir."
        pause(2)
        extend "{i}Whir whir."
        """The gentle hum of the plane along with the much less gentle sound of Luke snoring, allowing me a rare bit of time to myself.

        Everything since the diner has been a bit of a blur, getting through customs and making sure Luke had everything packed kinda
        just fused together in my mind into a general period of business."

        There was surprisingly little time to process everything. May brought up the fact she was leaving, so there was a combination
        of happiness, worry and depression with that.

        Then the news of the trip to Manawa Island which brought with it excitement and apprehension.
        And finally actually saying goodbye to one of my bestfriends which was of course heavily bittersweet.

        I had never been so busy in my life and I had never felt just so tired. Mentally and physically to be honest.
        I was so caught up in everything happening around me that I hadn't really realised just how tired this had all made me.

        Obviously Luke didn't either, for his head is resting against the side of the plane, his mouth opened so wide he could swallow a bus.

        I smile at the sight. At least I had this lovable idiot with me. It makes this whole experience seem a lot less daunting.

        I hadn't even considered the fact I would actually be on TV. Which is weird, when May had signed Luke and I up to the show
        we had been left pretty much in the dark about what was going on.

        Maybe they wanted real reaction or something. Who knows. All we had to do was record a video of ourselves and state who we
        are and stuff like that, you know, like all the introduction videos on reality television.

        Let's hope it won't be as ridiculously over-top as that rubbish.

        Damn, I was gonna be on a TV show. It had only hit me just now. It's not just a holiday, it's a holiday where thousands of people will see me.

        Every conversation, every fuck-up, every triumph, everyting was going to be recorded and shown to people laughing either with me or against me.
        It was all quite…"""

        menu:
            "Exciting":
                "Exciting. I had never done anything like this before and honestly, I was really looking forward to it."
                "Maybe I could finally put myself on the map, make a name for myself or simply just enjoy the fact that I was lucky
                enough to be selected so I can make the most of it."

                $ Intro_Vid_Feelings = 1
                jump Plane_2

            "Annoying":
                "Annoying. I had never done anything like this before and honestly, I am already half prepared to quit."
                "I don't want a bunch of people judging me or needlessly picking up on every little thing I do wrong or differently.
                Whatever. I'm mainly doing this for May but we'll see what happens."

                $ Intro_Vid_Feelings = 2
                jump Plane_2

            "Funny":
                "Funny. I had never done anything like this before and honestly, I think it'll be hilarious how it all turns out."
                "It could completely blow up in my face to point I'd never want to show myself in public again or it could be a
                complete success and I'll be having to sign autographs and commit felonies I'd be later vehemently deny when accused of in the future.
                Anything could happen."

                $ Intro_Vid_Feelings = 3
                jump Plane_2

            "Terrifying":
                "Terrifying. I had never done anything like this before and honestly, I am dreading every second. What if I mess up?"
                "It'll be broadcast to everyone in the world and then I'd be ridiculed for years! I know I'm doing this for May but I
                don't think I'll ever be comfortable being so vulnerable to so many people like this. Still, we'll see what happens."

                $ Intro_Vid_Feelings = 4
                jump Plane_2

    label Plane_2:
        """Whatever I feel, or whatever I think it doesn't actually matter because there is literally nothing I can do to prepare myself.

        Which is the most frustrating thing, I'm caught in a limbo of running myself round in circles trying to wrap my head around my
        world being changed so emphatically so quickly whilst also shipping myself off to a place I know nothing about to be in a show I have no idea what do in.

        If there was ever a time to stop over thinking things and just chill the fuck out, now would be the time. However I'm almost sure that's not how my brain works.
        I'll need to busy my mind with something else. It doesn't exactly get rid of the problem but drawing out the noise is enough of a solution for me at the moment.

        May gave Luke and I a link to the introduction videos of the other contestants so we could get a feel for them before we met them.
        It's one of those things where I almost wish I could have that for everyone I met, it would at least stop the awkward small talk 
        section of trying to figure someone out.

        Pulling the videos up on my phone I'm kinda taken aback by how many people there are going to be. Twenty including myself. How the hell are they going to give
        everyone enough screen time? People are probably going to get voted off the island I'm guessing. Or brutally murdered to appease our unruly producer overlords.

        For some reason I'm leaning to the former.

        Who's introduction video should I see?"""

        jump Intro_Vid_1

    label Intro_Vid_1:
        menu:
            "Jason":
                "I click on the ‘Jason' video, a disgruntled man who seems to want to be anywhere other than in front of his camera from his constant scowl and narrowed eyes."
                Jason.c "Hey. I'm Jason. Jason Baxter. I don't want to be here and I think this introduction video stuff is pointless. I like video games.
                I'm coming to the island cause I want to. That's it."
                "The video cuts off just as abruptly as it starts. From the way he spoke, it was like Jason was being sent to prison.
                Not exactly a people person, but you never know, maybe he fits the whole hard exterior but sweet interior trope."
                "I heard Wizards of Sintaris is getting a video game adaptation so maybe we'll have something to talk about."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_1

            "Arthur":
                "I click on the ‘Arthur' video, being greeted with someone's back as they move a bunch of papers off a desk. He turns rather suddenly, adjusting his 
                glasses slightly before putting on  a small smile."
                Arthur.c "Hello there. My name is Arthur Wilson, a Psychology Professor at Cambridge University. Ah, so I'm technically ‘Professor' Arthur Wilson, or
                ‘Doctor' Arthur Wilson to others in my field."
                Arthur.c "Formalities aside I've come to the island to hopefully continue my research, I'd tell you more but I'd be afraid I'd talk you into a coma 
                about this kind of thing.
                You'll have to stay tuned. I'm most looking forward to meeting my other contestants, I'm sure they'll prove themselves more than interesting."
                Arthur.c "Well, that's all from me, I hope you've gotten a good impression. Goodbye."
                "Not only a professor but also a doctor. I don't think you could have gotten someone more intelligent.
                If he's a psychology dude he'll probably be able to read me like a book. Let's hope he's illiterate.
                Still, I might like to ask about his research, it must be quite important."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_1

            "Senna":
                "I click on the ‘Senna' video, two people, a small girl with blue hair and what I'd assume to be her mother next to her on a bed,
                the mother smiles though the blue haired girl merely stares into the camera. I hold back an involuntary shiver."                
                "Senna's Mother" "Hello there. I'm here to introduce to you my daughter Senna. As you can see, she's a bit shy but don't let that fool you, she's a 
                very sweet girl.
                Senna's a creative sort, she's usually found taking bits and pieces from magazines and newspapers, collaging them together into some mystical image 
                only she sees."
                "She's also a sporty girl, she likes her basketball and isn't one to back down. I've never seen her so determined to do something more than coming 
                onto this show and I can only hope you'll see her like I see her. Right, say goodbye Senna."
                Senna.c "Goodbye Senna."
                "The video ends before I can determine whether or not the joke was intentional. Still, she seems nice and anyone who isn't embarrassed to have 
                their parents gush about them on live television must be worth hanging out with."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_1

            "Willow":
                "I click on the ‘Willow' video, the sight of a girl in one of the darkest rooms I've seen appears. Thankfully she puts on a side lamp,
                giving view to what looks like a stuffed wolf plushie, something that is in heavy contrast to the the deep purple lipstick and black 
                eyeshadow of the contestant."
                Willow.c "Hey. I'm Willow. I like picnics, long walks on the beach and getting railed from behind. I came to the island because I like
                collecting sea shells to give to orphans and eating coconuts whole."
                Willow.c "I really hope to gain lifelong friends on the island so we can then hold hands and sing kumbaya and defeat evil spirits with the power of friendship.
                Thanks. Bye."
                "At first I wasn't sure but Willow ramped up the sarcastic meter so hard I can't quite tell if she's hoping to be funny or is just
                constantly fed up with everyone's shit."
                "I can't believe the producers actually let this go, it's hilarious but seems to undermine what they're trying to achieve.
                Anyway, it'll be fun seeing her put some people in their place, so long as it isn't me of course."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_1

            "Camilla" :
                "I click on the ‘Camilla' video, immediately the sounds of a revving motorbike announce the presence of the contestant.
                It seems like she's attached a go pro to her helmet as she tears down an open dusty road."
                "I can't see her face, only the road ahead of her but a husky voice emanates above the engine."
                Camilla.c "Hey, Camilla here. Sorry I'm taking you guys for an impromptu spin, but I just modified the aftermarket exhaust and wanted to hear this baby purr.
                You can probably tell but I'm a bit of a motorhead, I like my cars and my bikes."
                Camilla.c "You probably wanted to see my face, which is much better than you're imagining, trust me, but I thought I'd show you guys the beauty of mi casa, my home, Argentina.
                There's nothing better than getting out on the road in a country you love, right?"
                Camilla.c "Anyway I'll have to cut it here, I've got to get back to change, got a volleyball match in 15. I'll see you guys around."
                "Cool was the only word that came to mind. This girl is cool as hell. The kind of cool that could be played off as kinda full on.
                She was definitely confident in who she is, cocky might be too much of a stretch but there was one thing for sure, I wanted to know more about this girl."
                "Plus, Argentina? Luke's gonna have a field day with all his documentary knowledge. Actually, that's probably a bad thing."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_1

            "Next":
                jump Intro_Vid_2
            "Stop":
                jump Plane_3

    label Intro_Vid_2:
        menu:
            "Addison":
                "I click on the ‘Addison' video, the peppy girl on the other end gives a fun two fingered salute and smiles wide to the camera, clearly comfortable with the attention."
                Addison.c "Hiya guys! I'm Addison, I'm probably most known by my social media name Under My Wing, I do motivational videos to help you gain the confidence to bring
                out the real you. Cause you're great. I know you are and I want other people to know it too!"
                Addison.c "You can probably tell but I like to keep my glass half full, to most people it might seem like I overfill that glass sometimes but I believe in
                myself and want to share that with the world.
                I'm hoping to use this opportunity to encourage other people to go out there and chase their dreams, you know, get out of their comfort zone and really
                test themselves."
                Addison.c "Anyway enough of my rambling, it's great to meet you, until next time!"
                "Now I feel like getting up and taking on the world. Which would probably give me some weird looks considering I'm on a plane, though her enthusiasm is palpable.
                I'll have to look her up and see some of her videos, if anything just to give myself the needed motivation to get out of bed."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_2

            "Captain Cain":
                "I click on the ‘Captain Cain' video and instantly see a gruff looking old man muttering underneath his breath whilst a younger voice tries to encourage
                him to look into the camera."
                Cain.c "What do I do again, Dani? Is the thingie on? Are we rolling?"
                "Danielle" "You're all good, Dad. Introduce yourself."
                Cain.c "Good morning. I am Captain Harrison Cain, it is currently 10 o'clock, the weather is clear, approximately-"
                "Danielle" "You're not giving a report, Dad. Loosen up a little!"
                Cain.c "I am loose! Look how loose I am! There isn't a goose looser than me right now. Why can't you just do this for me?"
                "Danielle" "People need to get to know you. At least try to be nice?"
                Cain.c "Fine, fine. I'm Harrison Cain, ex-military. I like to fish. Is that good enough?"
                "Danielle" "Come on, give them a little more. Talk about your walkman, or the fact you still use a Notkia Brick and play Tetroos?"
                Cain.c "I don't want them to know that! They could use it against me! I play Tetroos in the safety of my own home on my perfectly acceptable mobile device
                without the worry that someone can know about it. I don't want people to know that - they could beat my high-score."
                "Danielle" "Okay, fine. This is Harrison Cain, he's recently just retired from service and is still trying to reintegrate back into society.
                The fact he's glaring at me is testament to that."
                "Danielle" "This lovely voice you're listening to is his ever-understanding daughter Danielle Cain.
                I just want my old man to enjoy a new relaxed life and hope somehow, some way, someone can break that shell of his."
                Cain.c "Do not break my shell."
                "I smirk at the video. Those two seem to have a good relationship. I must say I don't quite know just how approachable this ‘Captain' is,
                but it seems like he's a good sport at least."
                "I now know I won't die on that island, ex-military is a surefire way of making sure
                I won't be murdered by anyone without someone jumping to my rescue. That is, if I make a good enough impression."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_2

            "Riley":
                "I click on the ‘Riley' video, the woman who I assume to be my newest contestant gives a solid nod to the camera, one that has me fixing my posture
                subconsciously for some reason before she starts her introduction."
                Riley.c "Hi, I'm Riley, Riley Campbell. I am 25 years old from ____, England and am a current proud member of the Royal Marines Commando,
                having earnt my Green Beret at 17. Currently I am on leave and thought I may try my hand at leisurely lounging on beaches rather than defending them."
                Riley.c "From my training I can say that I'm more than ready for anything the island can throw at me, but I'm looking forward to seeing what it can come up with.
                Right then, I'll be signing off. Goodbye."
                "A Royal Marine Commando, eh? I have no idea what that entails but I'm assuming she's a certified badass. Neat.
                I must say I'm surprised at the jump from armying (is that a real word?) about to gameshow participating in your holiday time.
                Guess this woman doesn't like sitting around on her hands."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_2

            "Aaron":
                "I click on the ‘Aaron' video, the man greeting me on the other side is welcoming, he fixes the sleeve on his flannel shirt and beams a smile."
                Aaron.c "Hello! Nice to meet you, I'm Aaron Lee. I'd like to impress you with some kind of grand speech about how great I am but there isn't much to tell I'm afraid.
                I've got a boring office job which is just as I say, boring."
                Aaron.c "I'm just a normal guy with a normal life, which might actually be weird, not many people like me get on reality TV shows like this."
                Aron.c "Oh, I should probably put this in here, though it will probably get me lynched on the internet: I'm a vegan, and an environmentalist.
                So yes, I am indeed the most monstrous of obnoxious keyboard warriors and social media posters but if you can get past those supposedly
                dastardly traits of mine I'd appreciate it."
                Aaron.c "I'm also a budding musician, so hopefully I'll be able to play you guys a song or two, who knows.
                Alright, I'll see you guys on the island."
                "Wow, I don't believe it. Another ordinary normal person. He seems like just the chill, nice guy that I'd like to get to know.
                At least if everyone else hates me, this guy won't. Maybe I'll even be able to hear one of his songs, depending on if he's actually any good or not."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_2

            "Charlotte" :
                "I click on the ‘Charlotte' video, a young woman walks into the room like she owns the place, stopping when she's at the centre of the camera's
                view and placing a hand on her hip."
                Charlotte.c "I'm Charlotte Weaver, I'm 20 years old and owner of Dress Well, one of the leading up and coming fashion shops in the market.
                I know it's hard to believe that I'm so young and yet have a successful business but I didn't just stumble into it, it took hard work, long hours and determination."
                Charlotte.c "That's exactly what I'm going to bring to the island, there isn't a challenge I won't win, I will not be overlooked just because of who I am.
                Watch this space, I'm going to make this show my own."
                "A girl who knows what she wants and will stop at nothing to get it. A dangerous woman but also an inspirational one.
                She's doing things at 20 that I don't even think I could do at 74. I'll probably have to be tactful when I talk to her, it feels like it could very easily
                blow up in my face."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_2

            "Next":
                jump Intro_Vid_3
            "Stop":
                jump Plane_3

    label Intro_Vid_3:
        menu:
            "Nick":
                "I click on the ‘Nick' video, the man on the screen carries the camera, I'd assume on his phone, around with him as he walks through various rooms,
                a permanent winning smile on his features."
                Nick.c "Why hello my beautiful people. The name's Nick, short, sweet rolls off the tongue, among other things, I'm sure you'll come to love it, as you will me.
                I'm a straight shooting guy and I'll be real with you, I've come to the island to find that special someone to cozy up with on the sands."
                Nick.c "But failing that, I'm just here to have a good time. I'm a travel journalist so I'm always happy to see some lovely scenery.
                And the lovelies who happen to be in that scenery. Looking forward to finally meeting you lot intimately on the island. Nick, out."
                "Wow, the most aggressively sexual introduction I've ever witnessed. I'll have to see just how flirtatious he is in person.
                Something tells me that even if I decided I wasn't interested, which of course I'm not ruling out yet, this guy wouldn't take no for an answer."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_3

            "Elliot":
                "I click on the ‘Elliot' video, a boy shyly fixes his mousey brown hair, tugging slightly on the purple strand nervously.
                Eventually he brings his eyes away from the floor to look at the camera."
                Elliot.c "Um, hello. I'm Elliot. Elliot Raptis. Sorry, I'm not exactly very good at impressions. Um, uh, I quite like painting. I do it, sometimes.
                So, there's that, I guess."
                Elliot.c "I also like photography, it um, passes the time. I quite like it because some things in life can only be experienced once,
                but every moment in life should be cherished, so capturing moments in a video or a picture means that moment isn't forgotten."
                Elliot.c "Coming to the island means I can capture more memories that happen once in a lifetime. That's what I enjoy doing.
                Um, sorry, I've probably spoken too much. Goodbye."
                "Although he seemed like a deer in the headlights for the majority of the video, when he got to talking about what he enjoys, Elliot finally seemed relaxed.
                Hopefully I can catch him when he's like that, I might have a chance at a decent conversation with him then."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_3

            "Emma":
                "I click on the ‘Emma' video and instantly recognise the face that pops up. Luke raves about her all the time, supposedly a ‘just talking' streamer called EmooseTalks. She certainly looks at home in front of the camera."
                Emma.c "Hello, hello! I'm Emma, or EmooseTalks on Twinch. I'm really excited to be on {i}Maybe Manawa?!{/i} It feels like a great way to get to know different people
                and learn more about them. If you guys know me, then you'll know just how much fun I get meeting new people, and getting to do that on a sunny island? Amazing!"
                Emma.c "A bit about me, if I were to sum myself up into a word, I'd probably say ‘lively'. I like going out and doing things and helping people.
                Every Tuesday on stream we raise money for charity and I'm all about giving back to the community.
                Check me out if you have the time but if not I'll see you on the island. Bye bye!"
                "If Luke knew EmooseTalks was going to be on the show I doubt he'd be able to contain himself. Still, celebrity status aside, she seems like a real nice girl.
                I hope I'll be able to get to know her, though I'll porabbly spend most of my time making sure Luke doesn't drool everywhere."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_3

            "Juliette":
                "I click on the ‘Juliette' video and am greeted with a girl in a very extravagant blue dress, she hums a song for a little while until she realises the camera is recording and then starts her introduction."
                Juliette.c "Grüezi! I am Lady Juliette von Arx, daughter of the duchess of a small kingdom called Sweissland. Yes, that is a real place and yes we are very small,
                but we are wanting to be more widely recognised. It is with great pleasure that I've been given the opportunity to be apart of {i}Maybe Manawa?!{/i}."
                Juliette.c "I hope to gain lots of friends and raise awareness of my humble country. This is my first trip out of Sweissland and
                I am looking forward to learning all I can whilst on the island. Hope to see you soon."
                "Huh, we have legitimate royalty among the contestants. I can't say I've heard of this kingdom, Sweissland so maybe it'll be cool to get to know
                Juliette and talk about her people. Plus, if anything, I'm almost one hundred percent sure this'll come up in a pub quiz one day and I'd like to be prepared."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_3

            "Alek" :
                "I click on the ‘Alek' video though I'm instead redirected to a page which tells me that the video cannot be found.
                Odd, I thought I downloaded all these correctly. Guess this ‘Alek' will remain a mystery until I meet them on the island."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_3

            "Next":
                jump Intro_Vid_4
            "Stop":
                jump Plane_3

    label Intro_Vid_4:
        menu:
            "Star":
                "I click on the ‘Star' video, though I'm instead subjected to 'Never Gonna Give You Up' by Rick Astley.
                Annoyed at the now very dead meme, I scroll to the comments and see a single post from the username ‘HawtAsFuk' which just reads 'Wait and see ;)'."
                "I can't quite tell whether I like this ‘Star' or not, and I can't quite tell whether that's a good thing or a bad thing. Probably a bad thing."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_4

            "Javier":
                "The ‘Javier' video is not a video, rather a simple statement on who he is and what he does. And it's not pretty."
                "{i}‘Javier is currently a convicted criminal who will be arriving on the island on Day 3. The production crew would like to assure
                both watchers and contestants that the utmost care has been used in order to ensure both the safety of the contestants whilst also
                maximising entertainment value."
                "{i}Javier has been thoroughly tested and is supposed to encourage the idea of rehabilitating criminals so they can better reintegrate into society.'"
                "They have actually sent a convicted criminal onto the island with us. And they didn't tell us a thing.
                I have half a mind to call up May and ask her what the hell is going on but it's not like it'll mean anything now."
                "What am I gonna do about it? I can't exactly jump out of the plane. I don't particularly know what to think, it's better that I just move on."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_4

            "Joe":
                "I click on the ‘Joe' video and I see a cheerful looking man who has the biggest smile I've ever seen in my life.
                He gives out a hearty chuckle as the video starts and then gets on with his introduction."
                Joe.c "Ahoy there! The name's Martinez. Joe Martinez. But everybody just calls me Uncle Joe. I own a diner, called Joe's Diner."
                Joe.c "Creative, isn't it? But I like to think the simpler an idea, the easier it is to convey to someone, and the easier it is to convey to someone,
                the easier it is to understand and get on board with."
                Joe.c "I love cooking, dancing, singing, the whole shabang.
                Though if you value your hearing you may want to get out the kitchen when I'm doing it! Haha! I'm hoping to have some fun on the island, not too much of course,
                I don't want to anger the wife! Haha! Anyway, I've talked your ear off enough, get ready for some Uncle Joe, ladies and gentlemen, I'll be here all series!"
                "I can't help the smile on my lips once the video is over. This ‘Uncle Joe' certainly has a radiant energy, one that you can't help but join in on.
                I'm hoping me and the big guy will get along well though judging by this video it seems like Uncle Joe could get along with everyone."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_4

            "Luke":
                "Taking a quick glance over at the sleeping corpse of Luke, I smirk before checking out his introduction video."
                Luke.c "Yo! The name's Luke, Luke Armstrong. I'm 20, like Kung Fu movies like Red Dragon, Legend of the Fire Fist and play Ultimate Frisbee on the weekend
                with my friends. Speaking of friends, my best friend, [Ray.n], is also going to be on the show."
                Luke.c "They're great! You wouldn't know just by looking at them but they're one of the best people you could ever meet, trust me, if there's anyone you should
                look out for or talk to, it's [Ray.n]. No questions asked. Damn, I spent the whole time talking about [Ray.n] but I should've been talking about me!"
                Luke.c "Well, I'm great too! So, yeah, I guess. This isn't how this was supposed to go… Uh, I'll see you dudes on the island. Peace!"
                "I stifle a laugh, trying not to wake the sleeping beauty next to me. Trust that goofball to spend the whole time he was trying to talk about
                himself talking about something completely off-topic. Still, there isn't a greater friend out there than the one sitting right next to me."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_4

            "[Ray.n]" :
                "Curiosity gets the better of me and I take a look at my own video. I took a few takes and sent them in so it'll be interesting to see which
                one they chose in the end. Also I'm extremely self centred, though I assumed that was obvious by now."

                if Intro_Vid_Feelings == 1:
                    Ray.c "Hi there! My name’s [Ray.n]. There isn’t much to say about me but I’m really looking forward to meeting everyone on the island.
                    Here’s hoping we have something in common! Luckily one of my mates, Luke, is going to be on the island with me, which is great."
                    Ray.c "There’s nothing like the feeling of knowing you’ve got someone watching out for you, no matter what.
                    I’m just excited for the opportunity and can’t wait to get stuck in. Here’s to hitting the ground running and doing well on the show!"

                elif Intro_Vid_Feelings == 2:
                    Ray.c "Look, this isn’t really my thing. I don’t like beaches, I don’t like islands and I don’t like people. I’m doing this for a friend.
                    Still, if push comes to shove I’ll do what I must."
                    Ray.c "I’ve still got to look out for Luke, who’s also on the island.
                    He’ll get himself into all kinds of mess that I’ll have to clean up. So look forward to that, I guess."

                elif Intro_Vid_Feelings == 3:
                    Ray.c "Hello. I’m [Ray.n], named after the God of Lukewarm Swimming Pools and your parents’ disappointment.
                    I’ll be completely honest, this introduction stuff is very awkward and unnecessary, so let’s just skip."
                    Ray.c "All you need to know is that I’m [Ray.n], I’m here with my buddy Luke, and we aim to not die of starvation or
                    coconut related ‘accidents’ with our time on the show."

                elif Intro_Vid_Feelings == 4:
                    Ray.c "Um, hello. I’m [Ray.n]. I come from a small town called Creekford. My friend, Luke, is also on the show.
                    He normally does the talking out of the two of us. Uh, we play Ultimate Frisbee on the weekends, which most people look at us funny for."
                    Ray.c "Probably shouldn’t have said that. I’m not particularly fond of being on camera, as you can probably tell.
                    Still, I hope all goes well and the show runs well."

                "I inwardly cringe. I don’t think there was going to be any other reaction to seeing myself on camera.
                Still, I would have hoped they’d picked a take where I had better hair."

                $ Watch_Intro_Vid = True
                jump Intro_Vid_4

            "Next":
                jump Intro_Vid_1
            "Stop":
                jump Plane_3

    label Plane_3:
        if Watch_Intro_Vid == False:
            "Actually, I don’t want to look at any videos. I’ll keep it a surprise.
            Maybe I’ll just peruse some of the articles around the show, though it basically just goes over what I already know."
        else:
            "Right, that's probably enough for now. Anything more and I think my brain will explode.
            Let's wake up Sleeping Beauty and tell him we're nearly ready to land."

        Ray.c "Hey, Luke. We're landing."
        "For a second it seemed as though Luke was going to continue snoring forever, and by the amount of disgruntled faces on the people around us he'd be
        dead within the next minute."
        "Luckily Luke abruptly wakes himself up mid-snore, and would have smashed his head into the back of the seat in front
        of him if it weren't for his seat-belt."
        Luke.c "We there?"
        "After stifling a yawn, Luke presses his face up against the window of the plane, like a kid looking into an aquarium for the first time.
        Or a guess like a kid on an airplane, that might have been a more apt simile."
        Ray.c "Going to start landing in just a few minutes."
        Luke.c "Fucking ace, dude. The world is about to see the reincarnation of the Bezzie Mates!"
        Ray.c "What now?"
        Luke.c "Think about it, man! Or if you're not gonna think about it, it's okay cause I've done all the thinking for the two of us. May's gone, right?
        And at the minute we have no idea what to do. This is the perfect time to wipe the slate clean, pick life up by its balls and reinvent ourselves. Luke and [Ray.n] 2.0!"
        Ray.c "What if I liked the original model?"
        Luke.c "Too bad, we're like a Windows update or Thanos. We are inevitable. OG [Ray.n] was cool, but [Ray.n] 2.0 can be even better.
        Take everything you liked about who you were before and then add that on to this next version of yourself.
        The island will be a completely different experience to everything we've done before so be prepared to show people how you want to be seen."
        Ray.c "Such as?"
        Luke.c "You can be whatever you want to be! You can be friendly, sarcastic, shy, hell you can even be an arsehole all the time if you wanted to.
        All I'm saying man is that you only get to make a first impression once, and we're about to meet tons of new people. So go out there, experiment a bit."
        Ray.c "And if it all goes to shit?"
        Luke.c "Well you'll still have me, buddy. I ain't going anywhere no matter what you do. Who knows? Maybe you'll even find that special someone."
        "Luke grins a large pattened dumb shit-eating grin and makes a love heart with his hands, slowly moving towards my face and smushing them into my cheek as I try to turn away."
        Luke.c "You cannot escape the big L-O-V-E, [Ray.n]. It's inescapable, it's undeniable, it's-"
        Ray.c "Inevitable?"
        Luke.c "I was going to say ‘it's a much better substitute than watching Keanu Reeves romcoms and eating fancy sounding ice-cream'. But yes, it is also inevitable."
        Ray.c "Fancy sounding ice-creams?"
        Luke.c "Yeah, I mean what the fuck even is the pralines in ‘pralines and cream'?"
        Ray.c "I have no idea man."
        Luke.c "Neither do I."
        "{i}Good afternoon passengers. This is your captain speaking. We will shortly be landing in Auckland Airport. The time is 1:25 pm.
        The weather looks good and we are expecting to land approximately fifteen minutes ahead of schedule."
        "{i}The weather in Auckland is clear and sunny, with a high of 25 degrees for this afternoon. If the weather continues to cooperate you should
        get a great view of the city as we descend. We thank you for flying with us and hope you've enjoyed the ride."

        jump Ship_1

    label Ship_1:
        scene bg ship

        "Almost as soon as we landed Luke and I were getting ushered various ways, having catch up to a suited man who’s walking speed gave track stars a run for their money. 
        Get it? Run for their… forget it. Anyway we were quickly pushed into a car headed straight for Waitematā Harbour. A ship named The Liverbird awaited us, 
        along with the rest of the contestants, though there wasn’t a spare moment of time to begin introducing ourselves, 
        for staff members for the show were whisking everyone away before we could start conversation."

        show Luke neutral at halfright

        Luke.c "You’d think they’d at least let us get to know each other before going through all the legal, gameshow mambo jumbo."
        Ray.c "I’m just wondering why we’re not getting the same treatment."
        "{i}You look lost, lad. Don’t know where to go, like?"

        "We turn to a scruffy looking man, a cigarette hanging out his mouth and a fiddler cap on his head.
        I’d assume he was the captain, or the production staff have very lax uniform regulations."

        show Captain neutral at halfleft

        "Captain" "What ye looking at, la? Never seen a scouser outta Merseyside, like?"
        Luke.c "I uh, no, actually. What’s someone from Liverpool doing out here?"
        "Captain" "That’s proper insulting like, la. Think we’re all skint and can’t get outta the docks, like?"
        Luke.c "What? No, what I’m trying to say is-"
        "The Captain bursts out laughing, startling Luke out of his uncomfortable apologetic stance. He looks towards me but I can only shrug in bafflement."
        "Captain" "I’m pulling your leg, like, lad. I’m just the captain. I take it you’re on the show?"
        Ray.c "Yeah, uh, I’m [Ray.n], that’s Luke."
        "Captain" "Boss, la. If you want a word of advice, like, these are a bunch of muppets only out for themselves, like.
        I’d swerve the whole show, like if I were you. Don’t sit right with me."
        Luke.c "How come?"
        "Captain" "Just a feeling, like, lad. I’ll be starting the ship now youse are on. I’d say you’d want to talk to that fella, he’s got his head screwed straight."
        "The Captain jabs a finger towards a large man in a burgundy striped shirt before heading off.
        Briefly stunned by the interaction, Luke and I share a look of bemusement and head the Captain’s words."

        hide Captain neutral

        "Upon hearing our approach, the man turns around and gives possibly the biggest smile I’d ever seen.
        One that stretched so wide you’d consider it ingenuous, yet there had never been such sincereness in a gesture than this."

        show Joe neutral at farleft

        Joe.c "Well what do we have here? A couple young lads ready to take on the island!"
        "The man wraps us both up into a bone-crushing hug, seemingly tearing through the normal awkwardness of a first encounter to instead
        make it seem as though we were just reuniting with a treasured relative at a family gathering."
        Joe.c "Call me Uncle Joe, nice to meet you. Judging by the looks, I’d say you’re [Ray.n] and Luke."
        Luke.c "How’d you know?"
        Joe.c "By your introduction videos of course. You see, I’m terrible with names and faces so I wanted to make sure I knew everyone before I met you all.
        Now how have you guys been? Good trip?"

        menu:
            "It was good":
                Ray.c "It was good. Despite the sleeper agent beside me here trying to break the sound barrier with his snores.
                We’re a long way from home, that’s for sure but it seems like a nice chance to experience something new, you know?"
                Joe.c "That’s the spirit! New opportunities and experiences are the backbone for an interesting life is what I always say.
                I’m glad you guys took the chance to come out here, these kinds of offers don’t arise very often so it’s great you’re here."

            "It was bad":
                Ray.c "It was bad. Luke kept snoring on the plane so I couldn’t get any sleep."
                Luke.c "I’m sorry I need my beauty sleep."
                Ray.c "From the looks of things, you didn’t get enough."
                Luke.c "That’s cause your face radiates ugliness, I can’t look my best with you dragging me down with you."
                Joe.c "Haha! Look at you two go, like an old married couple. Sorry to hear the trip over wasn’t great but I’m glad you’re here now.
                We can try and turn that bad mood around."

            "Just the worst (sarcastic)":
                Ray.c "Just the absolute worst. We went on a paid for flight in economy plus, it was like I was spending days of my life in hell.
                And there was this one guy, can’t remember his name, I think it rhymed with puke, anyway, the loudest snorer you have ever heard.
                I would’ve preferred to swim quite frankly."
                Luke.c "I wouldn’t, I haven’t worked on my breaststroke form in years."
                Joe.c "Haha! I’d like to see that. I can see why it might’ve been bad though. Even in economy plus your seating space is small.
                I’m built to be loved and hugged, not squeezed into the smallest leg room available for hours on end."
                Joe.c "Still, I’m glad you managed to make it, through hell and all."

            "Let Luke answer":
                Luke.c "It was great! [Ray.n] and I have never been so far away from home before so this is all completely new.
                I think I might have annoyed a couple people on the plane though. I dozed off for a bit and I’ve been told I’m a loud snorer. How bad was it [Ray.n]?"
                Ray.c "Well, we didn’t exactly make any friends on the trip over…"
                Joe.c "Don’t worry about it! You might not have made any friends on the way over but I guarantee you’ll make some here.
                In fact, you’ve just made one right now. I’m glad you’re here and we’ll make it a good one from here on out."

        Luke.c "Thanks, Uncle Joe. How was your trip?"
        Joe.c "Oh it was great, I’m coming over from Miami but I’m originally from Cuba. It was a long flight, of course probably not as long as yours though it meant
        I could get a bit of me time, you know? A bit of Uncle Joe time to relax, read a book or two, catch up on stuff I’d been behind on, that kind of thing.
        Of course it was sad leaving the family behind, it always is, but they’re all off doing their own thing."
        "A situation quite similar to mine and Luke’s. With the way Luke’s shoulders drop and the sigh that leaves his lips it quite obvious he’s being reminded of May too."
        Luke.c "We know that feeling all too well."
        Joe.c "Oh? I don’t want to pry but I can tell you that from reputable unbiased sources, also known as my wife, I’m a great listener."
        "Luke looks over to me, asking the silent question on if we want to burden Uncle Joe with our feelings.
        I give a shrug in response, not one of apathy but rather one that left the decision up to Luke, it’s his problem as much as mine and if he wants to share it then I am too."
        Luke.c "Ah, it’s just, we’ve got this friend, May..."
        "Luke doesn’t really know how to continue, so I decide to fill out some gaps until he regains his train of thought."
        Ray.c "She’s someone we’ve grown up our entire lives with, someone who’s always doing things for us, she’s even the one who got us these tickets.
        But, like your family, she’s going off to do her own thing."
        Luke.c "And it should be a good thing, and it is, we’re so glad she’s going out there and achieving her dreams, we just- I just, feel so-"
        Joe.c "Empty?"
        "Uncle Joe seemed to take the words right out of Luke’s mouth, though the large man just smiles and knowing smile at the two of us."
        Joe.c "Listen here my young friends, cause I want to make this clear. This feeling of emptiness, of sadness, maybe loneliness, where it seems like a
        piece of you is missing is valid. It’s so valid and totally normal that sometimes our minds trick ourselves into thinking it’s not."
        Joe.c "But it is. And that’s because these people, who mean so much to us do become a piece of ourselves, their presence is felt so deeply in your
        heart that when they go, a piece of you goes with them."
        Joe.c "But then you gotta remember that though a piece of you goes with them,
        a piece of them is left with you. She ain’t gone, fellers. She’s merely taking the next step, waiting for you to take it too. And you will. I can feel it inside you."
        Luke.c "Hey. Can I hug you again?"
        Joe.c "Of course! [Ray.n], you’re not getting away either! I’ve got a free hugging arm and no one to hug with it."
        "A jovial hug ensues and I must say how nice this whole moment is. The first contestant we meet is a lovable family man who gives great advice.
        This trip might not be that bad at all."
        Ray.c "How are your family then, Uncle Joe?"
        Joe.c "Oh they’re great! My wife, Maya, is just about the coolest woman you’ll ever meet in your life. She’s a cop, head of her own division and by god
        if you see the way my Maya took down thugs, man it’s like I’m falling in love all over again. Then I’ve got my two kids, bundles of joy the both of them are."
        Joe.c "My daughter, Hope, she’s the eldest, is currently training to be a lawyer. I must say I hardly get any of the words she says when she explains what she’s
        doing but if there’s anyone intelligent enough to seize whatever it is that she sets her mind to, it’s Hope."
        Joe.c "My son, Justice, is on a football scholarship at Florida State. Ah, American football to you guys that is.
        Coach said the kids got something special and I know he does."
        Joe.c "Now Justice might not be the brightest boy by my god does that boy work his ass off to get where
        he is today, Hope too. They’re gonna go on to do such great things those two. I couldn’t be prouder."
        "There’s a whimsical smile on Uncle Joe’s face and I can tell there’s nothing he likes more than talking about his family."
        Luke.c "They sound great."
        Joe.c "Oh they are, I’m sure they’d love you guys as well. I know I do. But listen to me, going on and on about myself, what about you guys, how are your family?"
        Ray.c "They’re good, mine and Luke’s parents are friends so when we were little we’d hang out all the time."
        Luke.c "To be honest, the folks down at the diner, Frank and Claire are basically part of our extended family too."
        Joe.c "Did you say, diner?"
        "Uncle Joe’s eyes light up so bright I feel like I need to put sunglasses on."
        Ray.c "Yeah, Frank’s Diner. Best hot chocolate in the world."
        Joe.c "Ohoho, on contraire, mi amor. I’m sure this Frank serves great hot chocolates, in fact you could probably put him up as one of the best,
        but the best hot chocolate in the world? When you haven’t even ventured into Uncle Joe’s Diner?"
        Luke.c "You have a diner?"
        Joe.c "It’s my pride and joy! I’d even call it my third child. Hope and Justice always get a kick out of that. I’ve been cooking up a storm and serving
        cups of Uncle Joe for the last 25 years. There isn’t a place cozier, nor friendlier than Uncle Joe’s Diner, that’s the Uncle Joe guarantee."
        Joe.c "I’d like to get in touch with this Frank of yours though, he seems like a good guy, anyone who owns a diner is."
        Ray.c "Well I’m sure he’d love to get in touch with you too. He keeps to himself most of the time but he really does like meeting new people."
        Joe.c "Then it’s settled, after this show, I’m taking you back to Miami with me so you can meet the family and see the diner, then we’ll travel to Creekford."
        Luke.c "How did you-"
        Joe.c "I told you I saw those introduction videos. I’ve seen them all about a thousand times. That way I know what to talk about with everyone so they can
        go on about what they’re passionate about, you know?"
        Joe.c "Anyway, we’ll go back to Creekford and Frank can whip up a cup of Joe for Uncle Joe, how does that sound?"
        "Uncle Joe wiggles his eyebrows for what I’d assume to be added emphasis."
        Luke.c "Amazing!"
        "Uncle Joe claps his hands and lets out a hearty laugh before grabbing each of us into a firm handshake, sealing the deal. However impromptu and sudden
        the arrangement is, I find myself not only looking forward to the island but also about what happens afterwards as well."
        Joe.c "I’m glad to hear it. Oh, you probably haven’t had a chat with any of the staff members or Shane, right? You should probably find one of them so
        they know you’re around and the Captain hasn’t just left without you, haha!"
        Luke.c "Shane?"
        Joe.c "Yes, he’s the presenter for the show. He’s also one of the main producers or something. Got a lot of pull, I hear. Anyway you should probably
        meet him, if anything just to say hello. Couldn’t hurt."
        Joe.c "In the meantime I’ll wrestle up the rest of our friends so we can all properly meet out on the deck, sound good?"
        "Luke and I both nod and Uncle Joe smiles. He points us in the direction of a blonde haired man before wrapping his arm around a guy in a leather
        jacket who almost immediately tenses up."
        Joe.c "Hey, Jason, right? How are you feeling?"

        show Jason neutral at halfright

        Jason.c "Like I’m running out of personal space."
        Joe.c "Personal space? What’s that? Haha!"

        hide Jason
        hide Joe

        "Luke and I leave the two to their own devices and head on over to Shane."

        show Shane neutral at halfright

        Shane.c "Heyo, it’s the newbies, finally made it on board?"
        Luke.c "Yeah, thanks for-"
        Shane.c "Don’t mention it. How are you feeling?"
        Ray.c "It’s been-"
        Shane.c "Great to hear, great to hear. Let me give you the lowdown on how this is gonna go, okay? We get to the island, I head down first, do my thing,
        hype up the show and then I say something like ‘and here are the contestants!’ that’s your que to come on down past the camera, got it?"
        Luke.c "Yeah, cool, that’s fine, is there anything we need to know about, like, the island or the show specifically?"
        Shane.c "I wouldn’t sweat the details, mate. You get on the island, you find your cabin, you do the challenges, you talk to your fellow contestants,
        chat around, do a bit of schmoozin and boozin, create a bit of drama, we get it on tv and then everyone goes home happier, richer and more famous
        than they ever were before. You dig?"
        Luke.c "Sure, we just wanted to ask a few more questions if that’s alright."
        Shane.c "Sure, kid. I’ve got 5, shoot."

        jump Ship_2

    label Ship_2:
        menu:
            "Island":
                if Shane_Time_Limit < 1:
                    Shane.c "Clock is ticking guys. You'll have to find that out yourself. I'll be off."

                    jump Ship_3

                Ray.c "Could you tell us more about the island?"
                Shane.c """There’s not much to tell. The campsite is quite nice and big, you’ll each get your own cabin that has all the essentials,
                course for things like showering you’ll have to use the waterfall, it’s not too far from camp don’t worry and for the toilet you’ll have to use the portaloo."
                
                Or just go out in nature I guess. In the centre of camp there’s a firepit where you can all commune and a bit off to the side is a dinning area
                with a bunch of picnic tables set up. There’ll be a small teepee nearby as well which will have a laptop in it."
                
                This’ll how we’ll contact you about challenges or otherwise. There is some electricity, mainly if you are in desperate need of charging your phone
                in case of emergency, stuff like that. We’ve got pretty good camera coverage of most of the island so don’t fret if you think you’re going too far."
                
                So long as you stick around camp maybe the outskirts of the forest, the beach and the cliff, you’ll be fine."""

                $ Shane_Time_Limit += -1
                jump Ship_2

            "Voting":
                if Shane_Time_Limit < 1:
                    Shane.c "Clock is ticking guys. You'll have to find that out yourself. I'll be off."

                    jump Ship_3

                Ray.c "How does the whole voting thing work?"
                Shane.c "There’s nothing for you to do, other than be likeable I guess. We won’t tell you when a vote is about to happen, just to keep your reactions and
                stuff natural, but once voting has begun you’ll be able to see how things are going on the laptop."
                Shane.c "If you win, we’ll give you a message and then you’ll be able to request something of your choice to be sent in.
                Of course you can’t ask for just anything, but we’ll do our best to cater to what you want."

                $ Shane_Time_Limit += -1
                jump Ship_2

            "Challenges":
                if Shane_Time_Limit < 1:
                    Shane.c "Clock is ticking guys. You'll have to find that out yourself. I'll be off."

                    jump Ship_3

                Luke.c "What about the challenges?"
                Shane.c "Ah, you’ll have to wait and see. Don’t worry, we’re not about to force you to eat cockroaches or sleep next to snakes.
                Though that’ll be good tv I’ve been explicitly told by my boss who’s running the show that this is to showcase how people can work together,
                so it’ll mainly be team based stuff."

                $ Shane_Time_Limit += -1
                jump Ship_2

            "Show":
                if Shane_Time_Limit < 1:
                    Shane.c "Clock is ticking guys. You'll have to find that out yourself. I'll be off."

                    jump Ship_3

                Luke.c "Anything you can tell us about the show as a whole?"
                Shane.c "My boss’ whole idea for the show is to get real people together and see how well they can cooperate.
                Sounds like boring tv but this is how he wants to do it."
                Shane.c "He really wants to capture the ‘real’ part of ‘reality tv’. All you need to do is act as yourselves and that’s all that’s asked of you.
                To be honest, you’ll probably even forget we’re here at all."
                Shane.c "Of course he do encourage you to react to the audience and stuff so as a way to get you in touch with them, one of the portaloos actually
                has a camera in it, one where you can talk about your feelings and thoughts about whatever is going on straight to the audience."
                Shane.c "Think of it as a place to just vent your frustrations or something, we’ll edit it all down to the juicy bits made for television."

                $ Shane_Time_Limit += -1
                jump Ship_2

    label Ship_3:
        "After watching Shane saunter off, Luke clicks his neck, rolls his shoulders and does a bit of stretching."

        hide Shane neutral

        Luke.c "Right, I’m raring to go meet the rest of the cast. You ready?"

        menu:
            "Of course":
                Ray.c "Born ready, mate. Let’s go out there and make some friends."
                Luke.c "Don’t get too attached. I don't want to lose my Bezzie Mate status."
                Ray.c "Woah, no one could dethrone you. I said make friends, not Bezzie Mates. That’ll be a whole different kettle of fish."
                Luke.c "It must have been hard enough to get the first kettle of fish, you wouldn’t want the trouble of getting another."
                Ray.c "That’s why you’ll forever hold the title of Bezzie Mate."
                Luke.c "Ah, victory by default, my favourite way to win."

            "No":
                Ray.c "No, I’d rather shove forks into my eyes than this."
                Luke.c "Christ, man, keep it light. Guess I shouldn’t worry about losing my Bezzie Mate status."
                Ray.c "I don’t think anyone would want to steal your made up title for our friendship."
                Luke.c "You never know these days, [Ray.n]. There are thousands of petty little thieves who would want to take what we have."
                Ray.c "Well at the moment, you have no competition."
                Luke.c "Ah, victory by default, my favourite way to win."

            "Optimistic (sarcastic)":
                Ray.c "I am practically beaming with excitement. Who wouldn’t want to fail at awkward social interaction and then
                potentially say something wrong knowing fully well you’ll have to then spend the rest of the show with that person you pissed off on a deserted island."
                Luke.c "All I asked is if you were ready, Christ. Now I know I shouldn’t worry about losing my Bezzie Mate status."
                Ray.c "Don’t act so relieved yet, there could still be someone out there, waiting in the wings, ready to usurp you for my affection."
                Luke.c "And yet I don’t see much of a line."
                Ray.c "I’m guessing they’ve all taken a collective lunch break. You are safe for now."
                Luke.c "Ah, victory by default, my favourite way to win."

            "I’m Terrified":
                Ray.c "I am absolutely terrified."
                Luke.c "Woah, don’t be, man. Take a deep breath, close your eyes, remember how great you are then you’ll be fine."
                Ray.c "For reason I don’t think it’ll be that easy."
                Luke.c "What? Of course it will be. I know you’re great and so they will too. At least I don’t have to worry about losing my Bezzie Mate status."
                Ray.c "You were worried?"
                Luke.c "Not as worried as you are now about social interaction. Honestly [Ray.n], I don’t think there has been a single person who hasn’t liked you.
                You’ll be fine, I should know, I’m your current Bezzie Mate."
                Ray.c "By the looks of things, that’s not going to change anytime soon."
                Luke.c "Because of our tight bond?"
                Ray.c "Because of the lack of candidates."
                Luke.c "Ah, victory by default, my favourite way to win."

    "When we stepped back out onto the deck we finally got to see the sheer number of contestants we’d have to get to know over the next week or so.
    I catch Uncle Joe’s eye as he’s mid conversation and he gives his little eyebrow wiggle and gestures slightly with his head to the crowd."
    Luke.c "Dude…"
    "I look back at Luke to see him basically drooling over one of the contestants."
    Luke.c "That’s Camilla. She’s, like, the coolest person alive."
    "The aforementioned Camilla notices us staring and shoots us a lazy smirk and a wink. Luke practically melts at the attention."
    Luke.c "Dude, dude, dude! Was that at me? Was it at you? She definitely winked, right? That wasn’t just my imagination?"
    Ray.c "I have no idea, man."
    Luke.c "Well it was definitely at us. It is here that I instate the Bezzie Mate code."
    Ray.c "The Bezzie Mate code?"
    Luke.c "The Bezzie Mate code. Specifically under paragraph 12, sentence 3, stanza 7, chorus 4, enactment 10, which states as follows:"
    Luke.c "‘The Bezzie Mate of whom first laid eyes upon the suitable suitor for thy future linage shalt be granted first attempt at courtship.
    If thy first Bezzie Mate were to fail in their task, then the second Bezzie Mate shalt be granted permission to enact.’"
    Ray.c "Knock yourself out, mate. I’ll see about chatting with some of the others."
    Luke.c "Really? Yes! Don’t you worry, mate, I’ll work the ol’ Luke-charm and once we’re getting it on as if Marvin Gaye was singing directly
    to us, we’ll slide on into your conversation and help you out."
    Ray.c "And in the small chance-"
    Luke.c "Very small chance."
    Ray.c "In the very small chance it doesn’t work out?"
    Luke.c "Then I’d have warmed her up so much for you that touching her would give you third degree burns."

    hide Luke

    "Luke saunters up to Camilla who if anything just looks amused. She gives me a brief look, one that I give an apologetic smile to,
    before changing my attention to the rest of the crowd."
    Luke.c "Hey! Do you come here often?"
    "With that conversation going great I decided to chat with…"

    $ Ship_Jason_Willow = 0
    menu:
        "Jason and Willow":
            $ Jason.affection += 1
            $ Willow.affection += 1
            show Willow neutral at halfleft

            Willow.c "Watch out, new arrival incoming."

            show Jason neutral at halfright

            Jason.c "Why…"

            menu:
                "Friendly":
                    Ray.c "Hi there. Nice to meet you."
                    Willow.c "Right back at you, fellow friend. I know Jason here is just dying to meet new people."

                    $ Ship_Jason_Willow = 1

                "Sarcastic":
                    $ Willow.affection += 1

                    Ray.c "What a lovely way to enter a conversation. ‘Why’?"
                    Jason.c "Fuck’s sake, another smartarse."
                    Willow.c "Oh no, we’re multiplying. If anyone else comes along you won’t be able to count that high."

                    $ Ship_Jason_Willow = 2

                "Direct":
                    $ Jason.affection += -1

                    Ray.c "You got a problem with me?"
                    Jason.c "Maybe I do. What are you gonna do about it."
                    Willow.c "He’ll probably just out-brood you. Actually, I don’t think that’s possible."

                    $ Ship_Jason_Willow = 3

                "Shy":
                    $ Jason.affection += 1

                    "I silently step over to them but don’t make an attempt to interrupt their conversation."
                    Willow.c "Either you’re mute or you prefer to silently judge people. I’d usually do that from afar."
                    Jason.c "I already prefer them over you. Talk less."
                    Willow.c "Oh no, Jason doesn’t like me. I’m practically crying."

                    $ Ship_Jason_Willow = 4

            Jason.c "Bite me, Willow."
            Willow.c "I wouldn’t want to. Your stereotypical persona will cut my tongue, edgelord."
            Jason.c "*growls*"
            Ray.c "Do you guys know each other?"
            Jason.c "No, quite the opposite. I wanted to stand here, alone, for the rest of the trip. She came over and started annoying me."
            Willow.c "I was going to do the same but then I saw Jason’s sad little puppy dog face and I couldn’t help coming over."
            Jason.c "Say that again and I’ll kill you."
            Willow.c "I’m already dead inside, try it."
            "Jason growls again and Willow smirks. After a moment of staring at each other, Jason huffs and looks away.
            Willow addresses me with smugness, like she’d won that particular bout."
            Willow.c "I can see why it feels like we know each other, Jason’s taking my snark quite well.I’m surprised he hasn’t turned around and walked away yet."
            Jason.c "I’m definitely thinking about it. Then I’d leave you alone though, and god knows you wouldn’t make any friends."
            Willow.c "Would you look at that, he can take it and throw it back. I was about to feel bad but now I know we can have a bit of back and forth."
            "Willow looks at me, and her expression drops. Her smirk turns into a tight frown as she looks at me with scrutiny."
            Willow.c "The jury’s still out on you."

            if Ship_Jason_Willow == 1:
                Ray.c "Take all the time you need. I can wait for the verdict."
                Willow.c "You know it’s really hard to act decidedly pissed off for no reason when you keep being nice and friendly. Ruins our vibe, you know? 
                We’re supposed to brood in the corner."
                Ray.c "Guess I didn’t get the memo."
                Jason.c "That’s a good thing."
                Willow.c "Yeah I guess you’re right. Batman over here has enough angst for the three of us."
                Jason.c "Wouldn’t that make you my Robin?"
                Willow.c "I think the new guy seems more fit for the job. Speaking of which, we never actually did the whole introduction thing, did we? I’m Willow."

            elif Ship_Jason_Willow == 2:
                Ray.c "I’m waiting with baited breath. For how could I ever live with myself if I didn’t get validation from you."
                Willow.c "Hmm, the sarcasm was good, I’d say it was delivered too dramatically though. B+."
                Jason.c "You’re grading them? On whose authority?"
                Willow.c "Just stand over there and sulk, okay? You’ll pop a blood vessel being that curious."
                Jason.c "Uhuh. You ever stop being such a mega-bitch?"
                Willow.c "No. It’s one of my core character traits spawned from my mountainous amount of personal issues. I think it’s hereditary."
                Ray.c "I think I have that trait too."
                Willow.c "Guess it’s only passed amongst the elite. Me and, oh, we haven’t actually done that whole introduction thing, have we? I’m WIllow."

            elif Ship_Jason_Willow == 3:
                Ray.c "Well it’s a good thing I don’t give a shit what the jury thinks."
                Jason.c "Why the fuck are you still here?"
                Willow.c "Calm, Jason. They clearly don’t care much for witticism, nor can their tiny brain comprehend that our insults aren’t barbed at one another. They remind me a lot of you."
                Jason.c "That’s not a good thing."
                Willow.c "Eh, swings and roundabouts. They certainly don’t play along as well as you do."
                Ray.c "That’s just because your games are bad."
                Willow.c "You’re the one who came over to us. This is how we are. You know what? Let’s just pretend this last bit didn’t happen, I don’t need Jason punching someone on the first day. We haven’t even done the whole introduction thing, have we? I’m WIllow."

            elif Ship_Jason_Willow == 4:
                "I let the silence hang for a second, not feeling inclined to comment on what Willow said."
                Jason.c "Well? Has ‘the jury’ come up with something?"
                Willow.c "Not yet, though they do appreciate the quiet time to think."
                Jason.c "I don’t think enough people appreciate that."
                Willow.c "Oh? I couldn’t fathom who you’re referring to."
                Jason.c "I can think of one. She definitely talks too much."
                Willow.c "You should take it as a complement, you’re easy to talk to. Both of you are. I doubt I’d talk nearly as much to other people.
                Maybe they just provide the other half of a conversation. Whereas you two just… stare."
                Jason.c "It’s because we couldn’t care less about what you are saying."
                Willow.c "Hey, at least I’m trying the whole social interaction thing. Speaking of, we haven’t actually introduced ourselves properly yet, have we? I’m Willow."

            Jason.c "I’m Jason."
            Ray.c "I’m [Ray.n]."
            Willow.c "Great, now that that’s sorted, I think I’ll be heading inside to read, I’ve had enough social interaction for one day.
            We should do this again, maybe. I don’t like talking to anyone else and for what it’s worth, this wasn’t too bad."
            Jason.c "Speak for yourself."
            Willow.c "Now I know we have to do this again, if anything just so I can see you grimace again."
            Jason.c "I’m constantly grimacing. That’s my thing."
            Willow.c "True, and you’re great at it. Later [Ray.n], Jason."
            Jason.c "I’m uh, not going to move from here, it’s furthest away from everyone and people should leave me alone now,
            so not to be rude and all but could you, you know. Go away?"

            hide Jason
            hide Willow

        "Arthur and Senna":
            $ Arthur.affection += 1
            $ Senna.affection += 1

            "There is silence as I approach the group, the only way I can tell they’ve actually recognised my presence is when the guy in the suit nods in my direction. 
            I go to introduce myself but he puts up a hand to stop me."
            Arthur.c "If you could give it a moment, I’ve asked Senna here something."
            "I turn to the blue-haired girl to see her staring rather blankly in my direction."

            menu:
                "Friendly":
                    $ Arthur.affection += 1

                    Ray.c "Oh, sorry."
                    Arthur.c "No problem."
                    Senna.c "Good experience."
                    Arthur.c "Ah, of course. From what I can tell. You’ve probably not gone out too much, after all you’re still young and all that, 
                    so this does seem like a worthwhile endeavor."
                    "The man regards Senna with a gentle smile before turning to me and sticking out a hand."
                    Arthur.c "I’m Arthur, it’s nice to meet you."
                    "I shake Arthur’s hand and offer a handshake towards Senna."
                    Ray.c "It’s nice to meet you too."
                    Arthur.c "I’m afraid she doesn’t really do handshakes."
                    "Just as he says this, Senna, almost in rebellion, takes my hand in a surprisingly strong grip and nods her head my way."
                    Arthur.c "Huh. Are you an approachable person, [Ray.n]?"
                    Ray.c "Not as much as the next person."
                    Arthur.c "I think you’re selling yourself a bit short there. Especially with how Senna’s just reacted."
                    Ray.c "Is she not like this very often?"

                "Sarcastic":
                    $ Arthur.affection -= 1
                    Ray.c "So do we wait for, like, a signal? Does her hair turn blue when she’s thinking and when she’s come up with an answer it turns yellow or something?"
                    Arthur.c "Not quite. Possibly if you keep quiet we may find out."
                    "Senna continues to stare, a bit like a robot who’s system’s been fried."
                    Ray.c "I’ll be honest, I think Senna needs some oil rather than time. Seems like her gears are a bit clogged. I’m [Ray.n] by the way."
                    Arthur.c "Arthur."
                    "Though the response is terse, Arthur still brings out his hand for me to shake. After the pleasantries of social interaction are over Arthur 
                    goes to properly introduce Senna."
                    Arthur.c "This is-"
                    Senna.c "Good experience."
                    "There’s a brief beat of confused silence though it gives me enough of a period to capitalise on some good comedic timing."
                    Ray.c "Well hello, Good Experience, it’s very nice to meet you. I must say it is a quite peculiar
                    name, French, perhaps?"
                    Arthur.c "She was answering my question on why she wanted to come to the island, [Ray.n]. Though if you must, I’d say it sounds more Greek."
                    Ray.c "What do you think, Senna?"
                    Arthur.c "You may have to wait a bit there, sometimes it takes her some time to-"
                    Senna.c "Spiritual."
                    Arthur.c "Huh."
                    Ray.c "That’s not exactly a language, good try though."
                    Arthur.c "I wouldn’t have thought so but you seem to be able to get Senna out of her shell better than I can."
                    Ray.c "Is she not like this very often?"

                "Direct":
                    Ray.c "Well what the hell is she waiting for? Answer the question."
                    Arthur.c "Give her some time."
                    Senna.c "Good experience."
                    Ray.c "The hell does that mean?"
                    Arthur.c "I asked her why she wanted to go to the island. Judging by how she’s carried herself, I’d highly doubt she’s very well travelled, so the 
                    show had extra appeal. Is that the same for you?"
                    Ray.c "Does it matter?"
                    Arthur.c "Of course it matters. Finding that one thing doesn’t matter, very easily allows you to think another thing doesn’t matter which 
                    eventually boils down to nothing mattering. Which is rather the wrong mindset to have, is it not?"
                    Ray.c "Sweeping statement, much?"
                    Arthur.c "Of course. How else do you get your point across without extended hyperbole anymore?"
                    Ray.c "I don’t like how all your sentences end with me being asked a question."
                    Arthur.c "Why not?"
                    Senna.c "You did it again."
                    Ray.c "Even the mute’s on my side."
                    Arthur.c "I must admit it is surprising seeing her so acutely engaged in what you’re saying."
                    Ray.c "You telling me she doesn’t usually pay attention to conversation?"

                "Shy":
                    "Senna refuses to break eye contact with me, no matter where I look she continues to stare with
                    looks that could kill, which I would assume would only mean she could then stare through my
                    soul as well."
                    Senna.c "Good experience."
                    "I turn to the man, hoping to get any kind of context to the situation or confirmation that saying
                    ‘good experience’ to a complete stranger is perfectly acceptable social communication
                    nowadays."
                    Arthur.c "Ah, I see."
                    "Arthur nods his head sagely before turning to me."
                    Arthur.c "Senna here was answering my question on why she wanted to come to the island.
                    Judging by how she’s carried herself, I’d highly doubt she’s very well travelled, so the show had
                    extra appeal. Oh, I’m Arthur by the way."
                    "I tentatively shake his hand, he smiles kindly."
                    Arthur.c "Sorry, didn’t mean to interrupt you earlier, Senna here sometimes takes a while to
                    process things."
                    Ray.c "Is that right?"
                    Senna.c "Sometimes."
                    Arthur.c "Huh."
                    Ray.c "Something wrong?"
                    Arthur.c "Senna answered almost instantly to you. I’d originally say it’s because you are good with
                    people, though from what I’ve observed you’d rather keep to yourself."
                    Ray.c "You’re not wrong. So is Senna usually like this?"

            Arthur.c "I wouldn’t know, though I didn’t assume so and I’m quite good at reading people. At least
            I hope so, it is the foundation of my doctorate."
            Ray.c "Doctorate?"
            Arthur.c "Ah yes, Psychology. Take that how you will."
            Ray.c "How am I supposed to take it?"
            Arthur.c "Sometimes because it isn’t one of the harder sciencies, psychology tends to not be
            taken as seriously."
            Ray.c "So you’re psychoanylsing me right now?"
            Arthur.c "Perhaps."
            "Arthur smiles."
            Arthur.c "Though if I were to be psychoanalysing anyone, it would be Senna here. I get the
            impression she is rather misunderstood."
            "Senna has decided to tune out of our conversation, looking off the boat and into the horizon,
            wind whipping around some of her short blue hair though it never seems to get in her way."

            menu:
                "Friendly":
                    Ray.c "Misunderstood? How so?"
                    Arthur.c "Normality breeds a status quo which when challenged leads to ostracisation."
                    Ray.c "Um, could I get that in English?"
                    Arthur.c "Right, sorry. Sometimes I feel the need to overcomplicate my language. In short, Senna
                    acts rather strangely compared to how ‘normal’ people act so is considered ‘weird’."
                    Ray.c "Well hopefully this show can show off how likeable she can be."
                    Arthur.c "One can only hope. It feels like she’s been alone for far too long."
                    Ray.c "Just a feeling? I thought you were supposed to work off of facts or something. Is
                    psychoanalysing mostly your own judgement?"
                    Arthur.c "A lot of it is unfortunately just your own judgement. Not much is considered concrete in
                    my line of work. Everything I say about what I think of other people is just an opinion, nothing
                    more."
                    Ray.c "No offence, but doesn’t kind of, I don’t know-"
                    Senna.c "Undermine."
                    Ray.c "Yeah, actually. Doesn’t it undermine your doctorate if it’s just built upon opinion?"
                
                "Sarcastic":
                    Ray.c "Is this the part where she flings her hand to her forehead and then monologues about the
                    tragedies of her life?"
                    Arthur.c "That would be quite the sight, but no, misunderstood in a non-shakespearean
                    monologue way."
                    Ray.c "Pray tell the words you speak in greater detail young squire."
                    Arthur.c "Normality breeds a status quo which when challenged leads to ostracisation."
                    Ray.c "Okay, neither me nor my ye olde English self have any idea what you just said."
                    Arthur.c "Right, sorry. Sometimes I feel the need to overcomplicate my language. In short, Senna
                    acts rather strangely compared to how ‘normal’ people act so is considered ‘weird’."
                    Ray.c "Ah yes, because so many of us are ‘normal’."
                    Arthur.c "I wish everyone shared your view, [Ray.n], but I feel like she’s been alone for far too long."
                    Ray.c "Just a feeling, doc? I thought you guys were supposed to work off of facts?"
                    Arthur.c "A lot of it is unfortunately just your own judgement. Not much is considered concrete in
                    my line of work. Everything I say about what I think of other people is just an opinion, nothing
                    more."
                    Ray.c "Heh, must be fun having your entire doctorate based on opinion, you an art major too?"
                    Senna.c "Creative writing."
                    Ray.c "Or creative writing. Drama maybe? Your entire career is based on what someone else
                    thinks."
                
                "Direct":
                    Ray.c "Everyone’s misunderstood or whatever. Doesn’t make a difference."
                    Arthur.c "Then Senna is even more misunderstood than how most people are misunderstood.
                    Normality breeds a status quo which when challenged leads to ostracisation."
                    Ray.c "That meant absolutely fucking nothing to me."
                    Arthur.c "Right, sorry. Sometimes I feel the need to overcomplicate my language. In short, Senna
                    acts rather strangely compared to how ‘normal’ people act so is considered ‘weird’."
                    Ray.c "You can’t exactly say she isn’t weird though. Nothing wrong with that but she is weird."
                    "Senna absentmindingly nods her head, proving my point."
                    Ray.c "See, even she agrees."
                    Arthur.c "You may have nothing wrong with it but for some reason quite a lot of people do. I feel
                    she’s been alone for far too long."
                    Ray.c "Just a feeling? That the whole basis for your doctorate or whatever, a feeling?"
                    Arthur.c "A lot of it is unfortunately just your own judgement. Not much is considered concrete in
                    my line of work. Everything I say about what I think of other people is just an opinion, nothing
                    more."
                    Ray.c "So your career is worthless."
                    Senna.c "No."
                    Ray.c "Okay, fine, maybe not worthless but it’s just made up of opinion?"

                "Shy":
                    Ray.c "Misunderstood?"
                    Arthur.c "Normality breeds a status quo which when challenged leads to ostracisation."
                    "I briefly look over to Senna to see if she got what any of what Arthur just said but her dead-
                    panned expression is even harder to understand."
                    Ray.c "Uhh…"
                    Arthur.c "Right, sorry. Sometimes I feel the need to overcomplicate my language. In short, Senna
                    acts rather strangely compared to how ‘normal’ people act so is considered ‘weird’."
                    Ray.c "That’s… not a nice feeling."
                    Arthur.c "No. No it’s not. I feel she’s been alone for far too long."
                    Ray.c "Just feel? Aren’t you supposed to just, like, know?"
                    Arthur.c "A lot of it is unfortunately just your own judgement. Not much is considered concrete in
                    my line of work. Everything I say about what I think of other people is just an opinion, nothing
                    more."
                    Ray.c "Doesn’t it feel kind of-"
                    Senna.c "Empty."
                    Ray.c "Yeah. Empty. Doesn’t it feel empty knowing your career is just based on opinion?"
            
            Arthur.c "So many things are, nowadays."
            Ray.c "I feel like I’ve had an existential crisis."
            "Arthur laughs softly, gently pushing his glasses back up the bridge of his nose. Senna, on the
            other hand, doesn’t even crack a smirk."
            Arthur.c "My bad. I’ll try to tone it back down to something more casual like the weather or
            something next time."
            Senna.c "Don’t."
            Ray.c "I’ve got to agree with Senna actually, this is much better."
            Arthur.c "Then I suppose I’ll keep it up. Until then though, I’ve got some more people I’d quite like
            to talk to before we arrive at the island. If you’ll excuse me."
            "Arthur leaves Senna and I to our own devices. Senna looks up at me, the same dead eyed
            stare as before."
            Senna.c "...Sad."
            Ray.c "Huh?"
            Senna.c "You are sad."
            "I smirk. Either Senna has learnt too much from Arthur already, or I’m even easier to read than I
            thought."
            Ray.c "Yeah, yeah I am."
            Senna.c "I am sad for you."
            Ray.c "Hey, you don’t have to do that. Thanks though."
            "The classic Senna stare for another few seconds. I must say it’s getting less and less unsettling
            the more I’m subjected to it."
            Senna.c "It is a shame."
            "And then she walks off. To what or to where I have no idea. Guess the conversation is over?"


        #"Addison, Emma and Juliette":
        #"Cain, Riley and Charlotte":
        #"Aaron and Star":
        #"Nick and Elliot":
        #"Alek and Uncle Joe":

return
