world = {
  "story": "Homunculus",
  "startnode": "1",
  "passages": [
    {
      "name": "First Room (WIP)",
      "tags": "",
      "pid": "1",
      "text": "You suddenly jolt into conciousness, as if awakened from a decade long slumber. Sitting up, you notice you're completely naked, surrounded by what looks like a glowing circle with runes on it, and covered in (hopefully someone else's) blood. There is a large, steel door located along one of the walls. As your eyes get used to the dark of the room, you see a small white card with what used to be a picture and a name, but has been badly burned. You can barely make out the words ''\"Michael Clark\"''.\nAfter regaining the energy to stand, you slowly lurch to your feet. You can see your breath. Do you:\n[[Examine the room further->Examine the room further]]\n[[Check out the door->Check out the door]]",
      "links": [
        {
          "original": "[[Examine the room further->Examine the room further]]",
          "label": "Examine the room further",
          "newPassage": "Examine the room further",
          "pid": "2",
          "selection": "1"
        },
        {
          "original": "[[Check out the door->Check out the door]]",
          "label": "Check out the door",
          "newPassage": "Check out the door",
          "pid": "3",
          "selection": "2"
        }
      ],
      "cleanText": "You suddenly jolt into conciousness, as if awakened from a decade long slumber. Sitting up, you notice you're completely naked, surrounded by what looks like a glowing circle with runes on it, and covered in (hopefully someone else's) blood. There is a large, steel door located along one of the walls. As your eyes get used to the dark of the room, you see a small white card with what used to be a picture and a name, but has been badly burned. You can barely make out the words ''\"Michael Clark\"''.\nAfter regaining the energy to stand, you slowly lurch to your feet. You can see your breath. Do you:"
    },
    {
      "name": "Examine the room further",
      "tags": "1",
      "pid": "2",
      "text": "Still struggling to make out shapes in the near pitch-black room, you shuffle around and feel dust or sand under your feet. Picking it up, it stains your hands- you can tell it's some sort of ash. The only light in the room surrounds the circle you woke up in. It's not made of chalk, or paint, rather something you've never quite seen before. \n[[Check out the door->Check out the door]]",
      "links": [
        {
          "original": "[[Check out the door->Check out the door]]",
          "label": "Check out the door",
          "newPassage": "Check out the door",
          "pid": "3",
          "selection": "1"
        }
      ],
      "cleanText": "Still struggling to make out shapes in the near pitch-black room, you shuffle around and feel dust or sand under your feet. Picking it up, it stains your hands- you can tell it's some sort of ash. The only light in the room surrounds the circle you woke up in. It's not made of chalk, or paint, rather something you've never quite seen before."
    },
    {
      "name": "Check out the door",
      "tags": "1",
      "pid": "3",
      "text": "As you move closer to the large door, you can tell that it's a bit dinged up. Pulling at it does nothing, and neither does pushing. With no other option, you charge at the door. Putting all of your weight into it, a couple attempts pass before the doorframe is empty and the steel door lies 10 feet behind it. You see a small room with flickering lights on the other side.\n[[Move into the room->Airlock]]",
      "links": [
        {
          "original": "[[Move into the room->Airlock]]",
          "label": "Move into the room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        }
      ],
      "cleanText": "As you move closer to the large door, you can tell that it's a bit dinged up. Pulling at it does nothing, and neither does pushing. With no other option, you charge at the door. Putting all of your weight into it, a couple attempts pass before the doorframe is empty and the steel door lies 10 feet behind it. You see a small room with flickering lights on the other side."
    },
    {
      "name": "Airlock",
      "tags": "",
      "pid": "4",
      "text": "You step through the doorway, into a small sterile room- only to face another door. Lining the walls are lockers and some sort of anti-chemical suits. The door leading outside seems in better condition than the one you busted open to get into this room. A jumpsuit is a hell of a lot better than being naked, so you put one on despite it not really fitting that well. \n[[Examine lockers->Examine lockers]]\n[[Attempt to open the door->Attempt to open door ]]",
      "links": [
        {
          "original": "[[Examine lockers->Examine lockers]]",
          "label": "Examine lockers",
          "newPassage": "Examine lockers",
          "pid": "5",
          "selection": "1"
        },
        {
          "original": "[[Attempt to open the door->Attempt to open door ]]",
          "label": "Attempt to open the door",
          "newPassage": "Attempt to open door",
          "pid": "",
          "selection": "2"
        }
      ],
      "cleanText": "You step through the doorway, into a small sterile room- only to face another door. Lining the walls are lockers and some sort of anti-chemical suits. The door leading outside seems in better condition than the one you busted open to get into this room. A jumpsuit is a hell of a lot better than being naked, so you put one on despite it not really fitting that well."
    },
    {
      "name": "Examine lockers",
      "tags": "",
      "pid": "5",
      "text": "The lockers have small, glowing devices on where the handle would be, with a small slot that looks about the size of the ID card you found next to you when you awoke. \n[[Back to room->Airlock]]\n[[Attempt to open lockers->Attempt to open lockers]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Attempt to open lockers->Attempt to open lockers]]",
          "label": "Attempt to open lockers",
          "newPassage": "Attempt to open lockers",
          "pid": "7",
          "selection": "2"
        }
      ],
      "cleanText": "The lockers have small, glowing devices on where the handle would be, with a small slot that looks about the size of the ID card you found next to you when you awoke."
    },
    {
      "name": "Attempt to open door ",
      "tags": "1",
      "pid": "6",
      "text": "The door has a similar device attatched to it as the lockers that are also in the room- you swipe the ID you found. After a couple seconds, the door shudders open and slowly retreats to an open state. Red light floods into the airlock, pulsing from the numerous sirens. Suddenly, a warning bellows in your ears, seemingly from in the walls: ''ALERT: Primary generators OFFLINE, facility will be sealed once emergency power is drained. Recommendation: Director please collect all critical research and evacuate the facility.''\n[[Move into the large room->Hallway]]",
      "links": [
        {
          "original": "[[Move into the large room->Hallway]]",
          "label": "Move into the large room",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        }
      ],
      "cleanText": "The door has a similar device attatched to it as the lockers that are also in the room- you swipe the ID you found. After a couple seconds, the door shudders open and slowly retreats to an open state. Red light floods into the airlock, pulsing from the numerous sirens. Suddenly, a warning bellows in your ears, seemingly from in the walls: ''ALERT: Primary generators OFFLINE, facility will be sealed once emergency power is drained. Recommendation: Director please collect all critical research and evacuate the facility.''"
    },
    {
      "name": "Attempt to open lockers",
      "tags": "2",
      "pid": "7",
      "text": "After a couple aggrevating tries at figuring out how the small white card and lockers interact, you manage to open one. You see a pair of brown shoes, a small satchel, and a clean(ish) suit. \n[[Back to room->Airlock]]\n[[Search small bag->Search satchel]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Search small bag->Search satchel]]",
          "label": "Search small bag",
          "newPassage": "Search satchel",
          "pid": "8",
          "selection": "2"
        }
      ],
      "cleanText": "After a couple aggrevating tries at figuring out how the small white card and lockers interact, you manage to open one. You see a pair of brown shoes, a small satchel, and a clean(ish) suit."
    },
    {
      "name": "Search satchel",
      "tags": "1",
      "pid": "8",
      "text": "Rummaging through the small bag, you find a locked tablet, tissues, a wallet, and a folder piece of paper. Opening it, it's filled with words on just the front side. Filing through the wallet, you find a similar white card with the same name ''\"Michael Clark\"''. No matter how hard you look into the picture on the card, you can't seem to make out the shape of a face- just looking at it gives you a headache. There's a few other cards with the name on them, but no picture as well as some paper money.\n[[Back to room->Airlock]]\n[[Read folded paper->Read folded paper]]\n[[Attempt to unlock tablet->Attempt to unlock tablet]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Read folded paper->Read folded paper]]",
          "label": "Read folded paper",
          "newPassage": "Read folded paper",
          "pid": "9",
          "selection": "2"
        },
        {
          "original": "[[Attempt to unlock tablet->Attempt to unlock tablet]]",
          "label": "Attempt to unlock tablet",
          "newPassage": "Attempt to unlock tablet",
          "pid": "10",
          "selection": "3"
        }
      ],
      "cleanText": "Rummaging through the small bag, you find a locked tablet, tissues, a wallet, and a folder piece of paper. Opening it, it's filled with words on just the front side. Filing through the wallet, you find a similar white card with the same name ''\"Michael Clark\"''. No matter how hard you look into the picture on the card, you can't seem to make out the shape of a face- just looking at it gives you a headache. There's a few other cards with the name on them, but no picture as well as some paper money."
    },
    {
      "name": "Read folded paper",
      "tags": "1",
      "pid": "9",
      "text": "Skimming the paper, it appears to be some sort of speech or presentation. It talks about the next generation of Humanity- how they will be stronger, smarter, and better than ever before. It yammers on about this for the entirety of the paper, and you are left feeling little dissapointed at how familiar the words are to you. \n[[Back to room->Airlock]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        }
      ],
      "cleanText": "Skimming the paper, it appears to be some sort of speech or presentation. It talks about the next generation of Humanity- how they will be stronger, smarter, and better than ever before. It yammers on about this for the entirety of the paper, and you are left feeling little dissapointed at how familiar the words are to you."
    },
    {
      "name": "Attempt to unlock tablet",
      "tags": "1",
      "pid": "10",
      "text": "You punch in multiple 4 number combinations to the tablet, without avail.\n[[Back to room->Airlock]]",
      "links": [
        {
          "original": "[[Back to room->Airlock]]",
          "label": "Back to room",
          "newPassage": "Airlock",
          "pid": "4",
          "selection": "1"
        }
      ],
      "cleanText": "You punch in multiple 4 number combinations to the tablet, without avail."
    },
    {
      "name": "Hallway",
      "tags": "",
      "pid": "11",
      "text": "You walk through the door from the airlock into a large, octagonal room. There are 8 doors, one for each side of the room- counting the one you just walked in from. They have labels above the doors for each branch off of the hallway.\n[[To the Dorms->Dorm rooms]]\n[[To the Morgue->Morgue]]\n[[To the Lab->Laboratory]]\n[[To Training rooms->Training]]\n[[To the Library->Library]]\n[[To the Cafeteria->Cafeteria]]\n[[To the Admin rooms->Administration]]",
      "links": [
        {
          "original": "[[To the Dorms->Dorm rooms]]",
          "label": "To the Dorms",
          "newPassage": "Dorm rooms",
          "pid": "12",
          "selection": "1"
        },
        {
          "original": "[[To the Morgue->Morgue]]",
          "label": "To the Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        },
        {
          "original": "[[To the Lab->Laboratory]]",
          "label": "To the Lab",
          "newPassage": "Laboratory",
          "pid": "14",
          "selection": "3"
        },
        {
          "original": "[[To Training rooms->Training]]",
          "label": "To Training rooms",
          "newPassage": "Training",
          "pid": "15",
          "selection": "4"
        },
        {
          "original": "[[To the Library->Library]]",
          "label": "To the Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "5"
        },
        {
          "original": "[[To the Cafeteria->Cafeteria]]",
          "label": "To the Cafeteria",
          "newPassage": "Cafeteria",
          "pid": "17",
          "selection": "6"
        },
        {
          "original": "[[To the Admin rooms->Administration]]",
          "label": "To the Admin rooms",
          "newPassage": "Administration",
          "pid": "18",
          "selection": "7"
        }
      ],
      "cleanText": "You walk through the door from the airlock into a large, octagonal room. There are 8 doors, one for each side of the room- counting the one you just walked in from. They have labels above the doors for each branch off of the hallway."
    },
    {
      "name": "Dorm rooms",
      "tags": "1",
      "pid": "12",
      "text": "Entering the door marked \"Dormitories\", you walk into a medium sized room, lined with bunk beds as well as a large table in the center. Looking closely, you can see storage trunks at the foot of each bunk. \n[[Investigate the table->Investigate the table]]\n[[Investigate the storage trunks->Investigate the storage trunks]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate the table->Investigate the table]]",
          "label": "Investigate the table",
          "newPassage": "Investigate the table",
          "pid": "19",
          "selection": "1"
        },
        {
          "original": "[[Investigate the storage trunks->Investigate the storage trunks]]",
          "label": "Investigate the storage trunks",
          "newPassage": "Investigate the storage trunks",
          "pid": "20",
          "selection": "2"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "Entering the door marked \"Dormitories\", you walk into a medium sized room, lined with bunk beds as well as a large table in the center. Looking closely, you can see storage trunks at the foot of each bunk."
    },
    {
      "name": "Morgue",
      "tags": "1",
      "pid": "13",
      "text": "Passing into the morgue, you are overcome with an oppressive feeling of interruption- you are not meant to be here. In one of the corners is a pile of bodies, appearing to be hastily thrown out of the way. There is also a surgical table in the center of the room, right above red-stained drain.\n[[1->Investigate bodies]]\n[[2->Investigate table]]\n[[3->Hallway]]",
      "links": [
        {
          "original": "[[1->Investigate bodies]]",
          "label": "1",
          "newPassage": "Investigate bodies",
          "pid": "21",
          "selection": "1"
        },
        {
          "original": "[[2->Investigate table]]",
          "label": "2",
          "newPassage": "Investigate table",
          "pid": "22",
          "selection": "2"
        },
        {
          "original": "[[3->Hallway]]",
          "label": "3",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "Passing into the morgue, you are overcome with an oppressive feeling of interruption- you are not meant to be here. In one of the corners is a pile of bodies, appearing to be hastily thrown out of the way. There is also a surgical table in the center of the room, right above red-stained drain."
    },
    {
      "name": "Laboratory",
      "tags": "1",
      "pid": "14",
      "text": "Entering the room marked \"Laboratory\", you recognize equipment like scales and microscopes, but there are machines in this room that you have definitely never seen before. Some of them are covered in strange symbols, which feel eerily familiar.\n[[Investigate machines->Investigate machines]]\n[[Take a deeper look around->Deeplook]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate machines->Investigate machines]]",
          "label": "Investigate machines",
          "newPassage": "Investigate machines",
          "pid": "25",
          "selection": "1"
        },
        {
          "original": "[[Take a deeper look around->Deeplook]]",
          "label": "Take a deeper look around",
          "newPassage": "Deeplook",
          "pid": "26",
          "selection": "2"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "3"
        }
      ],
      "cleanText": "Entering the room marked \"Laboratory\", you recognize equipment like scales and microscopes, but there are machines in this room that you have definitely never seen before. Some of them are covered in strange symbols, which feel eerily familiar."
    },
    {
      "name": "Training",
      "tags": "1",
      "pid": "15",
      "text": "The room marked \"Training\" seems to be a hybrid, combining a meeting and lecture space with what seems like a gym. The classroom portion has a board, a single desk, and is filled with bookshelves, while the other portion is filled with what looks to be exercise machinery and medical tech.\n[[Investigate the Gym->Gym]]\n[[Investigate the School->School]]",
      "links": [
        {
          "original": "[[Investigate the Gym->Gym]]",
          "label": "Investigate the Gym",
          "newPassage": "Gym",
          "pid": "27",
          "selection": "1"
        },
        {
          "original": "[[Investigate the School->School]]",
          "label": "Investigate the School",
          "newPassage": "School",
          "pid": "28",
          "selection": "2"
        }
      ],
      "cleanText": "The room marked \"Training\" seems to be a hybrid, combining a meeting and lecture space with what seems like a gym. The classroom portion has a board, a single desk, and is filled with bookshelves, while the other portion is filled with what looks to be exercise machinery and medical tech."
    },
    {
      "name": "Library",
      "tags": "1",
      "pid": "16",
      "text": "Stepping into one of the larger rooms connected to the main hallway, marked \"Library\", you are greeted with an atmosphere unlike every other room you've visited so far (and a lot like the one you woke up in). Despite being a completely sealed room besides from the entrance/exit door, it appears as if a tornado has ripped the room to shreds. Book pages are strewn everywhere along the floor, and a good portion of the towering bookshelves are toppled onto eachother. Numerous symbols and charms cover almost every inch of surface area in the room, on every object- almost seared into them. It looks like there's a large pile of paper near one of the corners of the room.\n[[Investigate the bookshelves->Investigate bookshelves]]\n[[Investigate the papers->Investigate papers]]\n[[Investigate pile of papers->Investigate pile]]\n[[Back to Hallway->Hallway]]",
      "links": [
        {
          "original": "[[Investigate the bookshelves->Investigate bookshelves]]",
          "label": "Investigate the bookshelves",
          "newPassage": "Investigate bookshelves",
          "pid": "29",
          "selection": "1"
        },
        {
          "original": "[[Investigate the papers->Investigate papers]]",
          "label": "Investigate the papers",
          "newPassage": "Investigate papers",
          "pid": "30",
          "selection": "2"
        },
        {
          "original": "[[Investigate pile of papers->Investigate pile]]",
          "label": "Investigate pile of papers",
          "newPassage": "Investigate pile",
          "pid": "31",
          "selection": "3"
        },
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "4"
        }
      ],
      "cleanText": "Stepping into one of the larger rooms connected to the main hallway, marked \"Library\", you are greeted with an atmosphere unlike every other room you've visited so far (and a lot like the one you woke up in). Despite being a completely sealed room besides from the entrance/exit door, it appears as if a tornado has ripped the room to shreds. Book pages are strewn everywhere along the floor, and a good portion of the towering bookshelves are toppled onto eachother. Numerous symbols and charms cover almost every inch of surface area in the room, on every object- almost seared into them. It looks like there's a large pile of paper near one of the corners of the room."
    },
    {
      "name": "Cafeteria",
      "tags": "1",
      "pid": "17",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Administration",
      "tags": "",
      "pid": "18",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "Investigate the table",
      "tags": "1",
      "pid": "19",
      "text": "As you approach the table, you can tell there are numerous sets of cards and chips spread across it, some in neat piles. Surrounding the table are chairs, most of which are covered with ash and clothes strewn about them. Rummaging through the clothes, you find another wallet as well as a keyring with what looks like a car key. Inside the wallet is a family picture- you can't make out any of the faces for some reason, and your head begins to pound. You put the picture away.\n[[Back to room->Dorm rooms]]",
      "links": [
        {
          "original": "[[Back to room->Dorm rooms]]",
          "label": "Back to room",
          "newPassage": "Dorm rooms",
          "pid": "12",
          "selection": "1"
        }
      ],
      "cleanText": "As you approach the table, you can tell there are numerous sets of cards and chips spread across it, some in neat piles. Surrounding the table are chairs, most of which are covered with ash and clothes strewn about them. Rummaging through the clothes, you find another wallet as well as a keyring with what looks like a car key. Inside the wallet is a family picture- you can't make out any of the faces for some reason, and your head begins to pound. You put the picture away."
    },
    {
      "name": "Investigate the storage trunks",
      "tags": "2",
      "pid": "20",
      "text": "Investigating the trunks, some are locked shut while others are wide open, containing nothing but toiletries and various articles of clothing.\n[[Back to room->Dorm rooms]]",
      "links": [
        {
          "original": "[[Back to room->Dorm rooms]]",
          "label": "Back to room",
          "newPassage": "Dorm rooms",
          "pid": "12",
          "selection": "1"
        }
      ],
      "cleanText": "Investigating the trunks, some are locked shut while others are wide open, containing nothing but toiletries and various articles of clothing."
    },
    {
      "name": "Investigate bodies",
      "tags": "",
      "pid": "21",
      "text": "Moving closer to the bodies, an intense feeling of grief and loss comes over you. Pulling them off of the pile, there are six of them. You can tell that each of them has had a specific part of their body removed surgically- there is a tag on each body detailing their former profession, as well as the part that was removed:\nThe mathematician had his head removed\nThe personal trainer had their entire torso removed\nThe marine had his arms and legs removed\nThe sculptor had his hands removed\nThe sniper had his eyes removed\nThe chef had his nose and tongue removed\n[[Back to Hallway->Hallway]]\n[[Back to Morgue->Morgue]]",
      "links": [
        {
          "original": "[[Back to Hallway->Hallway]]",
          "label": "Back to Hallway",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        },
        {
          "original": "[[Back to Morgue->Morgue]]",
          "label": "Back to Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        }
      ],
      "cleanText": "Moving closer to the bodies, an intense feeling of grief and loss comes over you. Pulling them off of the pile, there are six of them. You can tell that each of them has had a specific part of their body removed surgically- there is a tag on each body detailing their former profession, as well as the part that was removed:\nThe mathematician had his head removed\nThe personal trainer had their entire torso removed\nThe marine had his arms and legs removed\nThe sculptor had his hands removed\nThe sniper had his eyes removed\nThe chef had his nose and tongue removed"
    },
    {
      "name": "Investigate table",
      "tags": "",
      "pid": "22",
      "text": "Attempting to even inch towards the surgical table in the center of the room results in an utterly repulsive feeling, every alarm in your brain firing at once to avoid this seemingly mundane object.\n[[Proceed->Pullback]]\n[[Retreat to Morgue->Morgue]]",
      "links": [
        {
          "original": "[[Proceed->Pullback]]",
          "label": "Proceed",
          "newPassage": "Pullback",
          "pid": "23",
          "selection": "1"
        },
        {
          "original": "[[Retreat to Morgue->Morgue]]",
          "label": "Retreat to Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        }
      ],
      "cleanText": "Attempting to even inch towards the surgical table in the center of the room results in an utterly repulsive feeling, every alarm in your brain firing at once to avoid this seemingly mundane object."
    },
    {
      "name": "Pullback",
      "tags": "",
      "pid": "23",
      "text": "Ignoring the chaos of your thoughts screaming at you to not go towards the table, you press on. Barely managing to take a single step every ten-ish seconds, you feel an almost physical force pushing you away from the table. Scratching at your arms and legs beckons you back to the entrance of the room, and you swear you can feel a tight grip on your shoulder.\n[[Push on->Revelation]]\n[[Retreat to Morgue->Morgue]]",
      "links": [
        {
          "original": "[[Push on->Revelation]]",
          "label": "Push on",
          "newPassage": "Revelation",
          "pid": "24",
          "selection": "1"
        },
        {
          "original": "[[Retreat to Morgue->Morgue]]",
          "label": "Retreat to Morgue",
          "newPassage": "Morgue",
          "pid": "13",
          "selection": "2"
        }
      ],
      "cleanText": "Ignoring the chaos of your thoughts screaming at you to not go towards the table, you press on. Barely managing to take a single step every ten-ish seconds, you feel an almost physical force pushing you away from the table. Scratching at your arms and legs beckons you back to the entrance of the room, and you swear you can feel a tight grip on your shoulder."
    },
    {
      "name": "Revelation",
      "tags": "4",
      "pid": "24",
      "text": "Just as you step within arm's reach of the table, you feel searing pain in your temples as your body goes limp- you fade from conciousness in less than a couple seconds. On top of ear-piercing ringing, your senses are overloaded with the sounds of saw on bone and rending flesh.\nNot sure how much time has passed, your eyes pry open to see a ring of six people standing over your idle body on the floor. You blink once and they're still there, your mind must be playing tricks on you. Once more, and they're gone. You slowly rise to your feet, back near the exit to the Hallway.\n[[Exit the Morgue->Hallway]]",
      "links": [
        {
          "original": "[[Exit the Morgue->Hallway]]",
          "label": "Exit the Morgue",
          "newPassage": "Hallway",
          "pid": "11",
          "selection": "1"
        }
      ],
      "cleanText": "Just as you step within arm's reach of the table, you feel searing pain in your temples as your body goes limp- you fade from conciousness in less than a couple seconds. On top of ear-piercing ringing, your senses are overloaded with the sounds of saw on bone and rending flesh.\nNot sure how much time has passed, your eyes pry open to see a ring of six people standing over your idle body on the floor. You blink once and they're still there, your mind must be playing tricks on you. Once more, and they're gone. You slowly rise to your feet, back near the exit to the Hallway."
    },
    {
      "name": "Investigate machines",
      "tags": "1",
      "pid": "25",
      "text": "Stepping up to the side of one of the unidentified machines, you feel beckoned towards the symbols covering it. Almost as if you were being puppeteered, your arm reaches out and brushes along multiple different symbols. As you touch them, a voice in your head whispers a word. You presume this is the meaning of the symbols. The words in your head, as they come to you, are \"Mercury\", \"Sulfur\", \"Air\", and \"Gold\". Absolutely clueless on how you were able to decipher these, you feel a connection to them that you can't even begin to explain.\n[[Back to Laboratory->Laboratory]]",
      "links": [
        {
          "original": "[[Back to Laboratory->Laboratory]]",
          "label": "Back to Laboratory",
          "newPassage": "Laboratory",
          "pid": "14",
          "selection": "1"
        }
      ],
      "cleanText": "Stepping up to the side of one of the unidentified machines, you feel beckoned towards the symbols covering it. Almost as if you were being puppeteered, your arm reaches out and brushes along multiple different symbols. As you touch them, a voice in your head whispers a word. You presume this is the meaning of the symbols. The words in your head, as they come to you, are \"Mercury\", \"Sulfur\", \"Air\", and \"Gold\". Absolutely clueless on how you were able to decipher these, you feel a connection to them that you can't even begin to explain."
    },
    {
      "name": "Deeplook",
      "tags": "2",
      "pid": "26",
      "text": "Looking around the room, you find a set of filing cabinets covered by a tarp. Lifting up the tarp, a layer of ash flies off and reveals that all of them are, unfortunately, locked. However, you find a water-damaged notebook resting on top of them. Reading it, you find 8 entries that aren't smudged into illegibility by the water damage.\n8/20/35:  Today is the founding day of our lab, while our methods will likely be frowned upon by the outside world the future of humanity is worth whatever persecution we face!\n3/9/36: Attempting to create a specimen from scratch or copying from a template clearly isn’t working we may have to take a more violent route\n4/22/36: My idea to harvest samples instead of attempting to create our own has been accepted finally. My Co-workers aren’t excited by the idea but progress requires sacrifice.\n10/14/36: Our first attempt went horribly. The medium we used for the ritual appears to have been insufficient. When we started all of the samples seemed to take in more energy than intended because of this and covered everything in a layer of gore. We have a long road ahead of us.\n9/31/37: We need to think outside of the box. We have tried practically every material on the fucking periodic table and none worked. We even drained a good portion of the budget, making a gold circle for fucks sake! \n10/7/37: I have a new idea but it's really going to be pushing things. I got the idea when we watched Jurrasic Park last night. I just hope this works.\n12/19/37: I made a crude sample of the new medium, it's gross it’s diluted as hell, and it scares the shit out of me but this crappy sample alone already matches gold in its ability to conduct energy.\n7/5/39: After all the blood sweat and tears we finally have a medium that works. It is costly as hell and a pain in the ass to make but results are results. Now we just need to harvest some fresh samples and God willing we will have done it.\n[[Back to Laboratory->Laboratory]]",
      "links": [
        {
          "original": "[[Back to Laboratory->Laboratory]]",
          "label": "Back to Laboratory",
          "newPassage": "Laboratory",
          "pid": "14",
          "selection": "1"
        }
      ],
      "cleanText": "Looking around the room, you find a set of filing cabinets covered by a tarp. Lifting up the tarp, a layer of ash flies off and reveals that all of them are, unfortunately, locked. However, you find a water-damaged notebook resting on top of them. Reading it, you find 8 entries that aren't smudged into illegibility by the water damage.\n8/20/35:  Today is the founding day of our lab, while our methods will likely be frowned upon by the outside world the future of humanity is worth whatever persecution we face!\n3/9/36: Attempting to create a specimen from scratch or copying from a template clearly isn’t working we may have to take a more violent route\n4/22/36: My idea to harvest samples instead of attempting to create our own has been accepted finally. My Co-workers aren’t excited by the idea but progress requires sacrifice.\n10/14/36: Our first attempt went horribly. The medium we used for the ritual appears to have been insufficient. When we started all of the samples seemed to take in more energy than intended because of this and covered everything in a layer of gore. We have a long road ahead of us.\n9/31/37: We need to think outside of the box. We have tried practically every material on the fucking periodic table and none worked. We even drained a good portion of the budget, making a gold circle for fucks sake! \n10/7/37: I have a new idea but it's really going to be pushing things. I got the idea when we watched Jurrasic Park last night. I just hope this works.\n12/19/37: I made a crude sample of the new medium, it's gross it’s diluted as hell, and it scares the shit out of me but this crappy sample alone already matches gold in its ability to conduct energy.\n7/5/39: After all the blood sweat and tears we finally have a medium that works. It is costly as hell and a pain in the ass to make but results are results. Now we just need to harvest some fresh samples and God willing we will have done it."
    },
    {
      "name": "Gym",
      "tags": "1",
      "pid": "27",
      "text": "In the athletic half of the room, the numerous fitness machines look well cared for and untouched. There are simple weights, treadmills, and some machines you don't recognize. Everything feels a bit like it's being saved for something.\n[[Back to Training room->Training]]",
      "links": [
        {
          "original": "[[Back to Training room->Training]]",
          "label": "Back to Training room",
          "newPassage": "Training",
          "pid": "15",
          "selection": "1"
        }
      ],
      "cleanText": "In the athletic half of the room, the numerous fitness machines look well cared for and untouched. There are simple weights, treadmills, and some machines you don't recognize. Everything feels a bit like it's being saved for something."
    },
    {
      "name": "School",
      "tags": "1",
      "pid": "28",
      "text": "Exploring the educational side of the room, everything seems pretty well put togehter, despite the lack of any other desks beside the other one. While examining the bookshelves, you realize that the subject range and sorting of the books is all over the place- Kindergarten books on animals right next to a Quantum Mechanics textbook, for example. \n[[Back to Training room->Training]]",
      "links": [
        {
          "original": "[[Back to Training room->Training]]",
          "label": "Back to Training room",
          "newPassage": "Training",
          "pid": "15",
          "selection": "1"
        }
      ],
      "cleanText": "Exploring the educational side of the room, everything seems pretty well put togehter, despite the lack of any other desks beside the other one. While examining the bookshelves, you realize that the subject range and sorting of the books is all over the place- Kindergarten books on animals right next to a Quantum Mechanics textbook, for example."
    },
    {
      "name": "Investigate bookshelves",
      "tags": "3",
      "pid": "29",
      "text": "Walking (almost wading) through the papers on the floor towards the only group of standing bookshelves, you attempt to make out some names of books on the shelf as you get closer. They're all covered in the same strange marks as the rest of the room, so you can barely make out some of the titles. Most of the books remaining in the library seem to pertain to the study of occultism.\nTaking a book off of the shelf, even the sides that would have been surrounded by other books are layered in the same now familiar markings. As you dare to open the book in your hand, you are instantly barraged with a tinnitus-inducing rumble and some sort of force between corporeal and incorporeal lunges out at you- your reaction time saves you as you dodge out of its way and close the book, returning the force to it. Shuddering and still a little in shock, you put the book back on the shelf only to realize that every other book is almost quivering in fear at what just happened. Maybe your mind is playing tricks on you again, it wouldn't be the first time.\n[[Back to the Library->Library]]",
      "links": [
        {
          "original": "[[Back to the Library->Library]]",
          "label": "Back to the Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "1"
        }
      ],
      "cleanText": "Walking (almost wading) through the papers on the floor towards the only group of standing bookshelves, you attempt to make out some names of books on the shelf as you get closer. They're all covered in the same strange marks as the rest of the room, so you can barely make out some of the titles. Most of the books remaining in the library seem to pertain to the study of occultism.\nTaking a book off of the shelf, even the sides that would have been surrounded by other books are layered in the same now familiar markings. As you dare to open the book in your hand, you are instantly barraged with a tinnitus-inducing rumble and some sort of force between corporeal and incorporeal lunges out at you- your reaction time saves you as you dodge out of its way and close the book, returning the force to it. Shuddering and still a little in shock, you put the book back on the shelf only to realize that every other book is almost quivering in fear at what just happened. Maybe your mind is playing tricks on you again, it wouldn't be the first time."
    },
    {
      "name": "Investigate papers",
      "tags": "2",
      "pid": "30",
      "text": "Hurriedly, you begin to rummage through the small sea of papers that covers your feet. A large portion of them appear to be pages of books ripped off of the shelves here, but some don't fit in with those. They're different sizes and colors, all hand-scribbled notes on different processes, using another odd set of symbols different from the one covering everything in the room.\n[[Back to Library->Library]]",
      "links": [
        {
          "original": "[[Back to Library->Library]]",
          "label": "Back to Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "1"
        }
      ],
      "cleanText": "Hurriedly, you begin to rummage through the small sea of papers that covers your feet. A large portion of them appear to be pages of books ripped off of the shelves here, but some don't fit in with those. They're different sizes and colors, all hand-scribbled notes on different processes, using another odd set of symbols different from the one covering everything in the room."
    },
    {
      "name": "Investigate pile",
      "tags": "1",
      "pid": "31",
      "text": "Approaching the pile of paper, it's raised a good couple of inches above the rest of the paperin the room, as well as having a circle around it revealing the dark and burnt floor of the library. Sifting through the paper, you find a pile of clothes, dirtied by sitting on top of a pile of ash. As you search the clothes, you find a hastily written note on a small piece of paper. It was scribbled so quickly that it's almost illegible.\nIt reads: \"What we have done here is nothing short of monstrous Theres no denying this but we did it anyway I knew something would happen to us for what we did Getting arrested kidnapping for our research even assassination wasnt off the table but it turns out we may pay for our crimes sooner than we thought Every time we studied dangerous alchemical rites there was always mention of a cost We thought it would be energy that we could supply or some sacrifice we would commit but in reality I think it is much worse Every major rite we studied came from an alchemist who went missing whose face was never seen When I tried warning the others they called me paranoid and some of them even laughed at me I figured hiding in the Library would be my best bet considering how many protective charms are here I pray Im paranoid but in the case that Im not and even these charms cant save me I ask whoever is reading this please dont repeat our mistakes\"\n[[Back to Library->Library]]",
      "links": [
        {
          "original": "[[Back to Library->Library]]",
          "label": "Back to Library",
          "newPassage": "Library",
          "pid": "16",
          "selection": "1"
        }
      ],
      "cleanText": "Approaching the pile of paper, it's raised a good couple of inches above the rest of the paperin the room, as well as having a circle around it revealing the dark and burnt floor of the library. Sifting through the paper, you find a pile of clothes, dirtied by sitting on top of a pile of ash. As you search the clothes, you find a hastily written note on a small piece of paper. It was scribbled so quickly that it's almost illegible.\nIt reads: \"What we have done here is nothing short of monstrous Theres no denying this but we did it anyway I knew something would happen to us for what we did Getting arrested kidnapping for our research even assassination wasnt off the table but it turns out we may pay for our crimes sooner than we thought Every time we studied dangerous alchemical rites there was always mention of a cost We thought it would be energy that we could supply or some sacrifice we would commit but in reality I think it is much worse Every major rite we studied came from an alchemist who went missing whose face was never seen When I tried warning the others they called me paranoid and some of them even laughed at me I figured hiding in the Library would be my best bet considering how many protective charms are here I pray Im paranoid but in the case that Im not and even these charms cant save me I ask whoever is reading this please dont repeat our mistakes\""
    }
  ]
}
