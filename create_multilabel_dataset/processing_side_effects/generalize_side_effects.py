import ast

generalized = {
("numbness in hands", "numbness in feet", "numbness in other parts of the body", "numbness in the hands", "numbness in the arms", "numbness in the feet", "numbness in the legs", "numbness of an arm", "numbness of a leg", "numbness of face", "numbness on skin", "numbness in your hands", "numbness in your joints", "numbness in your arms", "numbness in your legs"): "numbness",
("tingling sensations", "prickling sensations", "burning sensations", "tingling of the lips", "tingling of the fingers", "tingling of the feet", "tingling in the hands", "tingling in the feet", "tingling feeling on the skin", "feeling of pins and needles", "tingling in your arms", "tingling in your legs", "tingling in hands", "tingling in feet"): "paresthesia",

("swelling of the eyes", "swelling of the face", "swelling of the lips","swelling of the throat", "swelling of the hands", "swelling of the feet", "swelling of the ankles", "swelling of the lower legs", "swelling of your face", "swelling of your tongue", "swelling of your throat", "swollen ankles", "swollen lower legs", "swollen face"): "edema",

("pain in the upper right part of the stomach", "pain in the upper right area of the stomach", "right upper abdominal pain", "pain in the right upper part of the stomach", "pain in right upper stomach area", "pain in the upper right side of the stomach"): "upper right abdominal pain",

("uncontrollable shaking of part of the body", "uncontrollable shaking of any part of the body", "shaking of your body that you cannot control", "shaking of a part of the body that you cannot control", "uncontrollable shaking of a part of your body"): "uncontrollable shaking",

("thoughts of suicide", "thoughts of dying", "thoughts of hurting yourself", "planning to hurt yourself", "trying to hurt yourself", "thinking about killing yourself", "suicidal thoughts"): "suicidal ideation or behavior",

("uncontrollable movements of the face", "uncontrollable movements of the mouth", "uncontrollable movements of the jaw", "uncontrollable movements of the lips", "uncontrollable rhythmic face movements"): "uncontrollable facial movements",

("dark urine", "dark colored urine", "brown-colored urine", "tea-colored urine", "cola-colored urine", "dark brown urine", "darkened urine", "brown discoloration of urine"): "dark urine",

("pain in hands", "pain in feet", "pain in other parts of the body", "pain in the hands", "pain in the feet", "pain in your hands", "pain in your feet"): "extremity pain",
("vision changes", "changes in vision", "blurred vision", "double vision", "vision loss", "sudden decrease of vision"): "vision problems",

("unexplained muscle pain", "unexplained muscle tenderness", "unexplained muscle weakness", "muscle aches", "muscle pain", "muscle cramps"): "muscle problems",
("bloody urine", "blood in urine", "red urine", "pink urine", "rust-colored urine"): "hematuria",

("redness on the palms of the hands", "redness on the soles of the feet", "red palms of the hands", "red soles of the feet", "redness on the palms", "redness on the soles", "redness on palms", "redness on sole(s) of the feet", "redness of skin on the palms", "redness of skin on the soles of the feet", "redness of the hands", "redness of the soles of the feet"): "palmar-plantar redness",
("pain on the palms of the hands", "pain on the soles of the feet", "pain on the palms of your hands", "pain on the soles of your feet", "pain of skin on the palms", "pain of skin on the soles of the feet", "tender palms of the hands", "tender soles of the feet"): "palmar-plantar pain",
("blisters on the palms of the hands", "blisters on the soles of the feet", "blisters on the palms of your hands", "blisters on the soles of your feet", "blisters on the palms", "blisters on the soles", "blisters on hands", "blisters on feet", "blistering of skin on the palms", "blistering of skin on the soles of the feet"): "palmar-plantar blistering",
("swelling on the palms of the hands", "swelling on the soles of the feet", "swelling on the palms of your hands", "swelling on the soles of your feet", "swelling on the hands", "swelling on the feet", "swelling of skin on the palms", "swelling of skin on the soles of the feet"): "palmar-plantar edema",
("peeling on the palms of the hands", "peeling on the soles of the feet", "peeling of skin on the palms", "peeling of skin on the soles of the feet", "peeling of skin on palms", "peeling of skin on sole(s) of the feet", "skin peeling of hands", "skin peeling of soles of feet"): "palmar-plantar peeling",
("tingling on the palms of the hands", "tingling on the soles of the feet"): "palmar-plantar tingling", 
("burning on the palms of the hands", "burning on the soles of the feet"): "palmar-plantar burning", 
("flaking on the palms of the hands", "flaking on the soles of the feet"): "palmar-plantar flaking", 
("sores on the palms of the hands", "sores on the soles of the feet"): "palmar-plantar sores",
("dryness of skin on the palms of the hands", "dryness of skin on the soles of the feet"): "palmar-plantar dryness", 
("thickness of skin on the palms of the hands", "thickness of skin on the soles of the feet", "unusual thickening of palms of hands", "unusual thickening of soles of feet that may be painful", "painful thickened patches of skin on soles", "painful thickened patches of skin on palms", "raised patches of skin on soles", "raised patches of skin on palms"): "palmar-plantar keratoderma",
("cracking of skin on the palms of the hands", "cracking of skin on the soles of the feet"): "palmar-plantar cracking",
("numbness of hands", "numbness of soles of feet", "numbness of the arms", "numbness of the hands", "numbness of the legs", "numbness of the feet", "numbness in your feet"): "extremity numbness",
("tingling of hands", "tingling of feet", "tingling of the arms", "tingling of the hands", "tingling of the legs", "pins and needles in the arms", "pins and needles in the legs", "pinprick sensation in the fingers", "pinprick sensation in the toes"): "extremity paresthesia",
("burning in the hands", "burning in the feet", "burning feeling in the hands", "burning feeling in the feet", "burning in hands", "burning in feet", "burning in arms", "burning in legs", ): "extremity burning",
("irritation at the place where you applied the ointment", 
    "irritation in a place where you injected this medication", 
    "irritation in the mouth in the area where you placed this medication", 
    "irritation in the underarm area"): "irritation where the medication was applied",
("pain in a place where you injected this medication", 
    "pain at the site where the injection was given", 
    "pain in the place where this medication was injected", 
    "pain in the treated area", 
    "pain at the injection site", 
    "pain near the injection site"): "pain where the medication was applied",

("redness in a place where you injected this medication", 
    "redness at the site where the injection was given", 
    "redness in the place where this medication was injected", 
    "redness of the treated area", 
    "redness at the injection site", 
    "skin redness where this medication was applied", 
    "redness near the injection site", "redness at the place where the injection was given"): "redness where the medication was applied",

("swelling in a place where you injected this medication", 
    "swelling at the site where the injection was given", 
    "swelling in the place where this medication was injected", 
    "swelling in the treated area", 
    "swelling at the injection site", 
    "swelling where this medication was applied", 
    "swelling near the injection site"): "swelling where the medication was applied",

("burning at the site where the injection was given", 
    "burning of the treated area", 
    "burning at the injection site", 
    "burning at the application site"): "burning where the medication was applied",

("sores in the place where this medication was injected", 
    "sores in the mouth in the area where you placed this medication", 
    "sores near the injection site"): "sores where the medication was applied",

("bleeding in the place where this medication was injected", 
    "bleeding of the treated area"): "bleeding where the medication was applied",

("stinging in the treated area", 
    "stinging at the application site"): "stinging where the medication was applied",
    
("worsening pain in a place you injected this medication", "pain at the application site","pain in the mouth in the area where you placed this medication"): "pain where the medication was applied",
    
("increase in facial hair", "increased hair growth on parts of the body","unwanted hair growth","excessive hair growth","hair loss","loss of hair","unusual hair thinning", "thin hair","brittle hair","change in hair color","abnormal hair growth in women","temporary hair loss","hair thinning","increase in size of fine body hair","increase in darkness of fine body hair","hair color changes","increased hair growth","abnormal hair loss","changes in hair texture","thinning of hair","changes in the appearance of the hair","reversible hair loss","increased hair growth on the face","increased hair growth on the arms", "increased hair growth on the back", "furry tongue", "hairy tongue","dry hair","thinning hair","unusual hair growth on the face in women","unusual hair growth on the body in women","excessive hair growth on the face in women","excessive hair growth on the body in women","oiliness of hair","dryness of hair","hair discoloration","oily hair","hair growth in unusual places","facial hair","hair color turning lighter","hair color turning gray","increase in pubic hair","growth of hair on face","loss of hair on scalp","increased hair growth on head","increased hair growth on face","increased hair growth on eyelashes","increased hair growth on chest","unusual hair growth","thicker body hair","thicker facial hair",): "change in body hair",

("red bumps around hair follicles","swollen bumps around hair follicles","painful bumps around hair follicles","itchy bumps around hair follicles","pimples around hair follicles"): "irritation around hair follicles",

("extreme hunger","hunger","unusual hunger","sudden hunger","increased hunger","increase in hunger","feeling very hungry","feeling more hungry than usual","feeling hungry",): "hunger",

("increase in thirst","feeling very thirsty","thirst","increased thirst","feeling more thirsty than usual","feeling thirsty","extreme thirst","excessive thirst","unusual thirst","being thirsty",): "thirst",

("burning of the lips", "burning of skin", "muscle burning", "burning in the underarm area", "burning in the mouth","burning in the throat", "burning nose","chest burning","burning sensation on the skin"): "burning of body parts",

("eye burning","burning sensation in eye(s)","burning in the eye","discomfort in the eye", "temporary burning of the eye", "swollen eyes","red eyes","teary eyes","painful eyes","sensitivity to light","eye pain","eye redness","eye tearing","dry eyes","irritated eyes","dry eye", "eyes more sensitive to light than usual","light hurting your eyes", "red eyelids", "pain in the eye","pressure in the eye","redness of the eye", "eye irritation","watery eyes","eye sensitivity to light", "swelling in the eye","increased sensitivity of your eyes to light", "eye swelling", "burning of the eyes", "burning eyes","excessive tears","eye discharge","crusty eyes","discharge from the eyes","irritation of the eyes","pain of eyes","pain of eyelids","redness of eyes","redness of eyelids","eyes sensitive to light","reddened eyes","redness of the eyes","inflamed eyes","itching of the eyes","painful dryness of the eyes","constant dryness of the eyes","burning in the eyes","rash with red eyes","rash with swollen eyes","redness in or around the eye","sore eyes","itchy eye(s)","watery eye(s)","red eye(s)","itching of the eye","burning of the eye","stinging of the eye","bleeding around the eye","stinging of the eyes","increased eye redness","increased eye itching","pain with eye movement","swelling in the eyes","stinging eyes","runny eyes","feeling that something is in your eye","sticky eyes","bloody eyes","feeling that something is in the eye","eye crusting","sensitivity to bright light","eye discomfort","eyelid swelling","stinging in the eye","bleeding within the eye","sensitivity of your eyes to light","increased eye tearing","dryness of the eyes","eye problems","difficulty moving eyes","temporary stinging of the eye","increased redness of the eye that continues for more than 48 hours","increased itching of the eye that continues for more than 48 hours","increased swelling of the eye that continues for more than 48 hours","raised eyelids","redness of the eyelid","discharge of the eye","discharge of the eyelid","pain of the eye","pain of the eyelid","itching eyes","discharge from eyes","itchy eye","tingling of the eyes","other eye problems","red eyelid(s)","swollen eyelid(s)","pain in eye(s)","sensitivity of eyes to light","eye itching","excessive tearing from the eye","discharge from the eye","eyelid pain","eyelid irritation","feeling like something is in your eye","scratchy eye","eye lid redness","irritation of the eyelid","irritation of the eye","temporary stinging in the eyes","temporary burning in the eyes","broken blood vessels in the eyes","eyelid problems","red eye",): "eye discomfort or irritation",

("swelling around the eyes","swelling around the eye", "swelling of your eyes", "swelling of your eyelids", "swelling in your eyelids","swelling of eyes","swelling of the eyelids","swollen eyelids","swelling of eyelids","sudden swelling of the eyes","swelling in or around the eye","swelling around eyes","swelling of the eyelid",): "swelling around the eyes",

("eye discoloration", "darkening of the eyes","changes in color of eyes","pale eyes","discoloration of the eye",): "eye discoloration",

("yellowing of whites of eyes", "yellowing of white parts of the eyes", "yellowing of the whites of the eyes", "swelling of the eye","yellowing of the white part of your eyes","yellowing of the whites of your eyes","yellowing of the eye","yellowing of the white of your eyes","yellowing of the whites of eyes","yellowness of the eyes","yellowing of whites of the eyes", "tearing in eyes","yellow of eyes",): "jaundice",

("uncontrolled eye movements", "uncontrollable eye movements", "unwanted eye movements","fast, repeating eye movements that you cannot control","fast eye movements that you cannot control","repeated eye movements that you cannot control","uncontrollable movements of the eyes","abnormal eye movements",): "uncontrollable eye movements",

("burning, especially on the bottoms of the feet", "burning pain in your arms","burning pain in your legs","burning sensation in the hands","burning sensation in the feet", "burning of the feet", "burning of the fingers",): "extremity burning",

("pink eye","pink eyes","pink eye(s)","symptoms of pink eye",): "pink eye",

("burning sensation when urinating", "burning when you urinate"): "burning when you urinate",

("unusual feelings of the lips", "unusual feelings of the fingers","unusual feelings of the feet","abnormal sensation in the eyes"):"unusual feelings in parts of body",

("sudden tightening of the muscles in the hands","sudden tightening of the muscles in the feet","sudden tightening of the muscles in the face","sudden tightening of the muscles in the throat"): "sudden tightening of muscles",

("pain in the arm","pain in the back","pain in the neck","pain in the stomach",): "Pain in parts of body",

("weakness in hands","weakness in feet","weakness in other parts of the body"): "Weakness in parts of body",

("repeated nausea","repeated vomiting"): "nausea",

("hives on arms","hives on lower legs","hives on buttocks","hives on trunk"): "hives on parts of body",

("seeing things that do not exist", "hallucinating", "hearing voices that do not exist", 'hallucinations while going to sleep', 'hallucinations while waking up','hallucinations', 'hallucination'): "hallucinating",

("feeling unsteady","trouble keeping your balance"): "Feeling Unsteady",

("blistering of the skin","blisters of the skin"): "Blistering Skin",

("itching in the area where this medication was injected", "itching near the spot that this medication was injected", "itching at the spot that this medication was injected", "itching that occurs a few days after stopping this medication after taking for a long time", "itching near the spot this medication was injected", "itching in the place this medication was injected", "itching at the place where this medication was applied", "itching at the place where you applied this medication", "itching in the place where you applied this medication", "itching near the spot where this medication was injected", "itching at the place where this medication was inserted", "itching of the skin where you injected this medication", "itching where the medication was applied", "itching at the injection site", "injection site itching", "itching at injection site", "itchiness at the injection site", "itching at the this medication injection site", "itching in a place where you injected this medication", "itching of the treated area", "itching where this medication was applied", "itching near the injection site"): "itchiness where the medication was applied",

("redness in the area where this medication was injected", "redness near the spot that this medication was injected", "redness at the spot that this medication was injected", "worsening redness in a place you injected this medication", "redness at the spot where this medication was injected", "redness in the areas where you applied this medication", "redness near the place where this medication was injected", "redness near the spot this medication was injected", "redness in the place where you applied this medication", "redness in the place this medication was injected", "redness at the place where this medication was applied", "redness at the place where you applied this medication", "redness at the place this medication was injected", "redness near the spot where this medication was injected", "redness at the place where this medication was inserted", "redness at the this medication injection site", "redness at the site where this medication was injected", "redness of the skin where you injected this medication", "redness where the medication was applied", "injection site redness", "skin redness at injection site", "redness at injection site"): "redness where the medication was applied",

("swelling in the area where this medication was injected", "swelling near the spot that this medication was injected","swelling at the spot that this medication was injected", "worsening swelling in a place you injected this medication", "swelling near the place where this medication was injected", "swelling in the place where you applied this medication", "swelling in the place this medication was injected", "swelling at the place where this medication was applied", "swelling at the place where you applied this medication", "swelling at the place this medication was injected","swelling near the spot where this medication was injected", "swelling at the place where this medication was inserted","swelling at the site where this medication was injected", "swelling of the skin where you injected this medication","swelling where the medication was applied","injection site swelling", "swelling at injection site", "swelling at the this medication injection site"): "swelling where the medication was applied",

("bruising in a place where you injected this medication", "bruising in the area where this medication was injected", "bruising near the spot that this medication was injected", "bruising at the spot that this medication was injected", "bruising at the spot where this medication was injected", "bruising of the skin near the place where this medication was injected", "bruising in the place where this medication was injected", "bruising in the place this medication was injected", "bruising near the spot where this medication was injected", "bruising in the place where you administered this medication", "bruising of the skin where you injected this medication", "bruising near the injection site", "bruising at the injection site", "bruising at injection site", "injection site bruising", "bruising at the this medication injection site"): "bruising where the medication was applied",

("a lump in the area where this medication was injected", "lump in the area where this medication was injected", "a lump in the place where this medication was injected", "a lump at the injection site", "lump at the injection site"): "lumps where the medication was applied",

("rash near the spot that this medication was injected", "rash at the spot that this medication was injected", "rash within 1 to 5 days after receiving a dose of this medication", "rash in the place where this medication was injected", "rash near the injection site", "rash at the injection site", "injection site rash"): "rash where the medication was applied",

("hives near the spot that this medication was injected", "hives at the spot that this medication was injected"): "hives where the medication was applied",

("pain near the spot that this medication was injected", "pain at the spot that this medication was injected","pain in the area where this medication was injected", "pain at the spot where this medication was injected", "pain near the place where this medication was injected", "pain in the place this medication was injected", "pain at the place where this medication was applied", "pain at the place this medication was injected", "pain in the place where you applied this medication", "pain near the spot where this medication was injected", "pain at the place where this medication was inserted", "eye pain after instilling this medication", "pain of the skin where you injected this medication", "pain where the medication was applied", "injection site pain", "pain at injection site", "pain around the injection site"): "pain where the medication was applied",

("bleeding in the area where this medication was injected", "bleeding from place where this medication was injected", "bleeding near the place where this medication was injected", "bleeding near the spot where this medication was injected", "bleeding in the place where you administered this medication", "bleeding where the medication was applied", "injection site bleeding", "bleeding at injection site", "bleeding at the injection site","a few drops of blood at the injection site", "blood collection under the skin at the injection site"): "bleeding where the medication was applied",

("blue skin discoloration in the area where this medication was injected","black skin discoloration in the area where this medication was injected", "lightening of skin at the place where this medication was applied","darkening of skin at the place where this medication was applied", "discoloration of the skin where you injected this medication","discoloration at the injection site" ): "skin discoloration where the medication was applied",

("numbness of the arms in the area where this medication was injected","numbness of the legs in the area where this medication was injected"): "numbness where the medication was applied",

("worsening oozing in a place you injected this medication", "oozing pus in the place where you applied this medication", "oozing at the place where you applied this medication", "oozing in the place where you applied this medication", "fluid at the injection site", "pus at the injection site"): "oozing where the medication was applied",

("burning in the areas where you applied this medication", "burning in the place this medication was injected", "burning at the place where you applied this medication", "burning feeling at or near the area that you applied this medication", "burning in the place where you applied this medication", "burning after instilling this medication", "burning where the medication was applied", "burning at injection site", "burning around the injection site"): "burning where the medication was applied",

("worsening warmth in a place you injected this medication", "warmth in the areas where you applied this medication", "warmth in the place this medication was injected", "warmth in the place where this medication was injected", "warmth in the place where you applied this medication","warmth near the injection site", "injection site warmth", "feeling of warmth at the injection site", "feeling of warmth around the injection site", "warmth at the injection site", "heat at the injection site"): "warmth where the medication was applied",

("stinging in the areas where you applied this medication", "stinging in the place where you applied this medication", "stinging after instilling this medication", "stinging where the medication was applied", "stinging at injection site"): "stinging where the medication was applied",

("soreness in the areas where you applied this medication", "soreness near the place where this medication was injected", "soreness at injection site", "soreness at the injection site"): "soreness where the medication was applied",

("sores at the spot where this medication was injected", "sores at the place where this medication was applied", "sores where the medication was applied", "sores at the injection site"): "sores where the medication was applied",

("dryness at the place where this medication was applied", "dryness at the site where this medication was injected"): "dryness where the medication was applied",

("skin blistering in the area where this medication was injected", "blistering at the place where this medication was applied", "blistering at the place where you applied this medication", "blistering in the place where you applied this medication", "blisters where the medication was applied", "blistering at injection site", "blistering at the injection site", "blisters in the place where this medication was injected", "blisters near the injection site"): "blistering where the medication was applied",

("painful eyes if this medication comes in contact with eyes","irritated eyes if this medication comes in contact with eyes","red eyes if this medication comes in contact with eyes","loss of vision if this medication comes in contact with eyes"): "irritation of eyes if medication comes into contact with eyes",

("irritation at the place where you applied this medication", "irritation in the place where you applied this medication tape", "irritation in the place where you applied this medication", "irritation in the place where this medication was injected", "irritation where the medication was applied","irritation at the injection site", "injection site irritation"): "irritation where the medication was applied",

("tenderness in the place where this medication was injected", "tenderness in the place where you applied this medication", "tenderness of the skin where you injected this medication", "tenderness at the injection site", "tenderness near the injection site", "injection site tenderness"): "tenderness where the medication was applied",

("hardness in the place where this medication was injected", "hardness in the place this medication was injected", "hardened area of skin at the injection site", "hardness at the injection site", "hardness at injection site", "hardening at the injection site"): "hardness where the medication was applied",

("tingling in the area where this medication was injected", "tingling in the place where this medication was injected", "tingling at the injection site"): "tingling where the medication was applied",

("nausea after stopping this medication and for up to 1 year afterwards", "vomiting after stopping this medication and for up to 1 year afterwards"): "nausea after stopping this medication and for up to 1 year afterwards",

("feeling of coldness at the injection site", "feeling of coldness around the injection site"): "feelings of coldness where medication was applied",
("erection that lasts for hours","inability to get an erection","inability to keep an erection","difficulty achieving an erection","difficulty maintaining an erection","erection that lasts longer than 4 hours","inability to have an erection","inability to maintain an erection","erection lasting more than 6 hours","erection that is painful","inability to get or keep an erection","erection that lasts for several hours or longer","an erection that lasts longer than 4 hours","frequent erections","painful erections","painful erection of the penis lasting more than 4 hours","painful erection that lasts for hours","difficulty getting an erection","difficulty keeping an erection","painful erection of the penis that lasts for several hours","erections that happen too often","erections that last too long","in men, difficulty achieving an erection","in men, difficulty maintaining an erection","unexpected erections","erections that last longer than 4 hours","erection lasting more than 4 hours","erections of the penis that happen too often","erections of the penis that do not go away","painful erection of the penis that lasts for hours"): "erection abnormalities",

("sores on the genitals","blisters in the genital area","sores in the genital area","painful blisters on the genitals","painful sores on the genitals","itchy blisters on the genitals","itchy sores on the genitals","sores in genital area","sores in your genital area","ulcers in your genital area","painful sores in genital area","painful ulcers in genital area","sores around the genitals","painful ulcers in your genital area","painful sores in the genital area","ulcers in the genital area","painful sores in genitals","painful ulcers in genitals",): "sores, blisters, or ulcers in the genital area", 

("genital itching","tenderness of the genitals","redness of the genitals","swelling of the genitals","tenderness of the area between the genitals and the rectum","redness of the area between the genitals and the rectum","swelling of the area between the genitals and the rectum","tenderness around genitals","swelling around genitals","redness of the skin around genitals"): "irritation or discomfort of the genitals",

("swelling of the vagina","redness of the vagina","irritation of the vagina","burning of the vagina","itching of the vagina","white vaginal discharge","vaginal itching","thick white vaginal discharge","heavy vaginal bleeding","vaginal discharge","thick vaginal discharge","odorless vaginal discharge","vaginal bleeding in post-menopausal women","unusual vaginal bleeding","vaginal bleeding","vaginal dryness","vaginal irritation","vaginal odor","yellowish vaginal discharge","thick, white vaginal discharge","unusual vaginal discharge","unexpected vaginal bleeding","abnormal vaginal bleeding","unusual vaginal irritation","vaginal burning","lumpy vaginal discharge","vaginal discharge that looks like cottage cheese","unpleasant vaginal discharge","increase in vaginal bleeding several days after treatment","bleeding from vagina","irregular vaginal bleeding","vaginal spotting","redness around the vagina","irritation around the vagina","sores around the vagina","yellow vaginal discharge","foul-smelling vaginal discharge",): "vaginal irritation, unusual bleeding, or discharge",


("curving of the penis","inflammation of the end of the penis","redness of the penis","itching of the penis","swelling of the penis","rash on the penis","foul smelling discharge from the penis","smelly discharge from the penis","enlarged penis","redness on the penis","irritation on the penis","sores on the penis","aching in the penis","redness of the erect penis","swelling of the erect penis","tenderness of the erect penis","unusual curving of the erect penis","breakage of the needle in the penis","nodules on the penis","hard areas on the penis",): "problems or irritation of penis", 

("sudden complete loss of vision","sudden partial loss of vision","changes in color vision","vision changes, especially at night","shadows in the center of your vision","unusual color to your vision","changes in vision at night","sudden changes in vision","vision changes especially at night","other vision problems","abnormal vision","problems with vision","change in vision","dark spots in your vision","changes in your vision","impaired vision","misty vision","foggy vision","change of vision","blurriness in the center of your vision","sudden change of vision","changes in vision, especially in low light","sudden vision problems","cloudy vision","blurriness in your vision","shadows in your vision","unusually colored vision","other changes in vision","decreased vision","blurred vision after using the drops","decrease in vision","sudden decrease in vision","sudden changes in color vision","sudden vision changes","blocked areas of vision","black spots in vision","reduced vision","unstable vision","sudden changes of vision","vision problems",): "vision problems",

("loss of peripheral vision","vision loss at night","loss of vision","blind spot in the center of your vision","sudden loss of vision","sudden severe loss of vision","a blind spot in the center of your vision","sudden loss of vision in one eye","sudden loss of vision in both eyes","peripheral vision loss",): "partial or total vision loss",

("problems with memory", "memory problems", "changes in your memory", "memory loss", "difficulty with memory", "changes in memory", "loss of memory", "decreased memory"): "memory problems",

("swelling of tongue", "sudden swelling of the tongue", "swelling of the tongue"): "swelling of tongue",

("pain in arms", "pain in the arms", "arm pain", "pain in the underarm area", "pain of an arm", "pain in arm", "painful glands of the armpit", "pain in your arms", "pain in one arm", "pain in both arms", "pain in one or both arms", "feelings of pain in an arm", "painful arm"): "arm pain", 

("pain in legs", "pain in one leg", "pain in the legs", "leg pain", "pain of a leg", "pain in one or both legs", "pain in the back of the lower leg", "pain in leg", "painful leg", "pain in a leg", "pain of legs", "pain in the lower leg that comes and goes during walking or exercise", "lower leg pain", "pain in one leg only", "pain in your legs", "feelings of pain in a leg", "dull pain in the thighs", "aching pain in the thighs", "new or unusual thigh pain", "new thigh pain", "unusual thigh pain"): "leg pain",

("pain on hands", "pain on the hands", "pain sensation in your hands", "pain of hands", "hand pain", "painful hands", "pain on the palms of your hand", "pain in the fingers", "pain in your fingers", "painful fingers", "fingers feeling painful"): "hand pain",

("chest pain", "sudden stabbing pain in the chest when breathing in", "sudden stabbing pain in the chest when breathing out", "chest pain after vomiting", "crushing chest pain", "pain in the chest area", "pain in your chest", "pain in the chest", "worsening chest pain", "sudden pain in the chest", "sudden chest pain", "chest pain that may spread to the arms", "chest pain that may spread to the neck", "chest pain that may spread to the jaw", "chest pain that may spread to the back", "chest pain that may spread to the stomach area", "upper chest pain", "pain of the chest", "increase in frequency of chest pain", "increase in severity of chest pain", "chest pain that gets worse with deep breaths", "chest pain that gets worse with cough", "sudden sharp chest pain", "sharp chest pain", "vomiting with chest pain", "more frequent chest pain", "more severe chest pain", "chest pain when you breathe", "chest pain when you cough", "new chest pain", "chest wall pain"): "chest pain",

("back pain", "pain in back", "lower back pain", "sudden pain in the back", "pain of the back", "pain in the upper back", "pain that may spread to the back", "back pain (in adults)", "pain in your back", "intense back pain", "sudden back pain", "ongoing pain that may spread to the back", "pain in the upper back between the shoulder blades", "ongoing back pain","intense low back pain", "unusual back pain", "sudden onset of lower back pain", "sudden severe back pain", "pain in the upper abdomen that spread to the back", "severe pain in the back below the ribs", "severe back pain", "back pain during the infusion", "low back pain", "sudden pain in the back area", "pain in your lower back"): "back pain",

("stomach pain", "pain in the upper right stomach area", "upper stomach pain that may spread to the back", "upper stomach pain that may get worse with eating", "pain in stomach", "pain in upper right part of stomach", "pain in the upper right part of your stomach", "ongoing pain that begins in the stomach area but may spread to the back", "upper right-sided stomach pain", "pain in the right upper stomach area", "right upper stomach area pain", "pain in the upper right part of stomach", "pain in the upper right stomach", "ongoing pain that begins in the upper left or middle of the stomach but may spread to the back", "pain in upper right part of the stomach", "ongoing pain that begins in the stomach but may spread to the back", "severe stomach pain", "continuous stomach pain", "sudden stomach pain", "right sided-stomach pain", "ongoing pain that begins in the upper left of the stomach but may spread to the back", "ongoing pain that begins in the middle of the stomach but may spread to the back", "pain in upper right side of stomach", "sudden pain in the stomach", "pain on right side of stomach area", "pain on the right side of your stomach area", "new stomach pain", "worsening stomach pain", "pain in upper right side of your stomach", "pain in the lower stomach", "stomach pain with nausea", "stomach pain with vomiting", "stomach-area pain", "pain on the right side of your stomach", "pain in the right upper side of the stomach", "pain in right upper part of the stomach", "pain in the stomach area", "ongoing pain that begins in the upper left of the stomach", "ongoing pain that begins in the middle of the stomach", "persistent stomach pain", "ongoing pain in the upper left of the stomach", "ongoing pain in the middle of the stomach", "stomach area pain", "pain in right side of stomach", "sharp pain in upper stomach area that may worsen after eating", "sharp pain in upper stomach area that may rotate to the back", "pain in your stomach area", "pain in the right upper part of your stomach", "pain in upper right part of your stomach", "ongoing pain that begins in the stomach area", "pain on the right side of the stomach", "stomach pain that may spread around to your back", "stomach pain in the upper right part of the stomach", "ongoing stomach pain", "sudden stomach area pain", "unusual stomach pain", "ongoing pain that begins in the stomach area but may spread to the back (in children)", "pain in the center of the stomach", "pain in the lower part of the stomach", "pain on the upper right side of your stomach", "pain that begins in the upper stomach area but may spread to the back", "pain that begins in the upper stomach area but may spread to the shoulder", "pain that begins in the upper stomach area with nausea", "pain that begins in the upper stomach area with vomiting", "pain that begins in the upper stomach area without nausea", "pain that begins in the upper stomach area without vomiting", "ongoing pain that begins in the stomach area, but may spread to the back", "severe stomach pain that may move to your back", "pain in the right upper area of the stomach", "painful stomach area", "middle stomach pain", "lower stomach pain", "stomach pain that will not go away", "stomach pain that may radiate to the back", "stomach pain without vomiting", "pain in the upper stomach area", "right sided stomach pain", "pain in the upper right-side of the stomach", "sudden severe stomach pain", "stomach pain that doesn't go away", "constipation with constant stomach pain", "pain in the left upper part of the stomach", "upper stomach pain", "ongoing stomach-area pain", "pain in the upper stomach", "pain in the upper part of the stomach", "right-sided lower stomach pain", "upper right stomach pain", "pain in the right stomach area", "pain in the upper middle stomach area", "right-sided stomach pain", "pain in the belly", "belly pain", "upper belly pain"): "stomach pain",

("bone pain", "severe bone pain", "pain in bones", "increased bone pain", "pain in bone"): "bone pain",

("joint pain", "pain in joints", "pain in the joints", "joint pains", "new joint pain", "worsening joint pain", "joint pain (in adults)", "painful joints", "joint aches or pains", "new or worsening joint pain"): "joint pain",

("pain in the jaw", "jaw pain", "pain in jaw", "pain in your jaw"): "jaw pain",

("mouth pain", "pain in mouth", "pain of the mouth", "pain in your mouth", "pain in the mouth", "pain of the lining of your mouth", "pain inside the mouth", "pain of the gums", "pain of the tongue", "tongue pain"): "mouth pain",

("pain when urinating", "painful urination", "pain urinating", "painful urinating", "burning pain during urination", "pain upon urination", "painful urination during treatment and for up to 3 months after your final dose", "pain with urination", "pain while urinating", "pain on urination", "pain during urination", "painful urination occurring more than 24 hours after treatment", "pain when you urinate"): "pain while urinating",

("abdominal pain", "pain in the upper abdominal area", "severe abdominal pain", "lower abdominal pain", "right-sided abdominal pain", "abdominal pain (in children)","abdominal pain that may go around to your back", "new abdominal pain", "worsening abdominal pain", "unusual abdominal pain", "sudden sharp abdominal pain", "abdominal pain that goes around to your back", "severe upper abdominal pain", "severe lower abdominal pain 3 to 5 weeks after taking this medication", "severe lower abdominal pain (3 to 5 weeks after taking this medication)"): "abdominal pain",

("skin pain", "slight pain of the skin that comes and goes", "painful skin", "pain on the skin", "pain of skin", "pain of the skin on your hands", "pain of the skin on your feet", "pain of the treated skin", "pain of the skin", "new painful area on your skin", "pain of the skin area"): "skin pain",

("throat pain", "pain in throat", "pain in the throat", "pain of the throat", "pain in your throat", "pain of the lining of your throat", "pain inside the throat"): "throat pain",

("pain from touch", "pain upon touch"): "pain from touch",

("pain from doing ordinary tasks such as combing your hair", "pain from doing ordinary tasks"): "pain from doing ordinary tasks", 

("neck pain", "pain in neck", "pain in your neck"): "neck pain",

("pain of the genitals", "pain of the area between the genitals and the rectum", "pain around genitals"): "genital pain",

("groin pain", "dull pain in the groin", "aching pain in the groin", "pain in the groin", "pain in your groin", "new or unusual groin pain", "new groin pain", "unusual groin pain"): "groin pain", 

("muscle pains", "pain in the muscles", "sudden muscle pain", "pain in muscles", "muscle pain (in adults)", "severe muscle pain", "unusual muscle pain", "pain in muscle", "painful muscles", "persistent muscle pain", "muscle pain in the forearms", "muscle pain in the lower legs", "new muscle pain", "pain in your muscles", "increased muscle pain", "muscle aches or pains", "ongoing muscle pain"): "muscle pain/aches/weakness",

("side pain", "dull side pain", "sharp side pain", "intense side pain"): "side pain",

("pain on feet", "pain on the feet", "pain sensation in your feet", "pain of feet", "painful feet","pain in the big toe", "pain in the toes", "painful toes", "toes feeling painful"): "feet pain",

("painful breasts in men", "painful breasts in women", "pain in the breasts", "breast pain", "painful breasts"): "breast pain",

("ear pain", "pain in the ears", "severe ear pain"): "ear pain",

("sinus pain", "pain of the sinuses"): "sinus pain",

("pain at the place where the injection was given", "pain at the site of injection", "pain near the site of injection", "pain at the place of injection", "pain at the place where injection was given", "pain at place where injection was given", "pain at the site of the injection", "pain in the place where you received your injection", "pain in the area where the injection was given", "pain at injection spot", "pain at the site of the injections", "pain in the place where you received the injection", "pain at site of injection"): "injection site pain",

("hip pain", "dull pain in the hips", "aching pain in the hips", "new hip pain", "persistent hip pain", "new or unusual hip pain", "unusual hip pain"): "hip pain",

("pain of the vagina", "vaginal pain"): "vagina pain",

("pain of the penis", "pain in the skin around the penis", "pain in the penis"): "penis pain",

("knee pain", "new knee pain", "persistent knee pain"): "knee pain",

("pain on swallowing", "pain when swallowing", "painful swallowing"): "pain while swallowing",

("pain at wound sites", "pain at the wound site"): "pain at wound site",

("pain in the shoulders", "pain under the right shoulder", "pain in the shoulder", "crushing shoulder pain", "pain in the tip of the left shoulder", "pain in the tip of your left shoulder"): "shoulder pain",

("fast breathing", "slow breathing", "shallow breathing", "rapid breathing", "slowed breathing", "breathing stops for a short time", "irregular breathing", "temporarily stopped breathing", "loud breathing", "high-pitched breathing"): "change in breathing rate/depth/pitch",

("pain when breathing deeply", "pain when breathing", "painful breathing"): "pain while breathing",

("difficulty breathing",  "trouble breathing", "breathing problems",  "difficulty in breathing", "new breathing problems", "worsening breathing problems", "increased difficulty breathing", "pain with deep breathing",  "difficulty breathing when lying down", "difficulty breathing during activity", "trouble breathing, especially when lying down",  "difficulty breathing, especially at night", "more trouble with breathing than normal", "sudden onset of difficulty breathing","new or worsening trouble breathing", "difficult breathing", "difficulty taking in a breath"): "difficulty breathing",

("shortness of breath", "new shortness of breath", "worsening shortness of breath", "shortness of breath after vomiting", "new or worsening shortness of breath", "sudden shortness of breath", "shortness of breath while exercising", "shortness of breath that occurs while you are at rest", "shortness of breath after a small amount of exercise", "shortness of breath after any physical activity", "shortness of breath when lying down", "shortness of breath, especially when lying down", "shortness of breath when exercising", "sudden shortness of breath immediately after inhaling this medication", "shortness of breath with everyday activity", "shortness of breath when lying flat", "shortness of breath especially when exercising"): "shortness of breath",

("sores of the gums","sores of the tongue","sores of the cheeks","sores in mouth","sores on the tongue","sore on mouth","sore on gums","sore on tongue","sore on roof of mouth","painful sores in mouth","painful sores on tongue","sores on tongue","painful sores in your mouth","sores on mouth","sores on the inside of your mouth","mouth sore","tingling sores on gums","tingling sores on mouth","itching sores on gums","itching sores on mouth","burning sores on gums","burning sores on mouth","rash with sores in the mouth","sores inside the mouth","painful sores on your mouth","painful sores in the mouth","itchy sores in the mouth","tongue sores","sores on the gums","sores on the cheeks","sores in the tongue","oral sores","blistering of mouth","blistering of insides of the mouth","blistering of the mouth","blisters around the mouth","tongue blistering","mouth blisters","blisters in mouth","blisters on tongue","blisters in the mouth","blistering inside of mouth","blistering in the mouth","painful blisters in the mouth","itchy blisters in the mouth","blisters on the mouth","blisters in your mouth","ulcers around the mouth","painful ulcers in your mouth","ulcers in the mouth","ulcers inside the mouth","ulcers on your mouth","ulcers in your mouth","painful ulcers in mouth","ulcers in mouth","ulcers on the gums","ulcers on the tongue","ulcers on the cheeks"): "mouth sores, blisters, or ulcers",

("sores on the skin","skin sore","skin sore that bleeds","skin sore that does not heal","painful sores on your skin","new sores on the skin","painful sores on the skin","itchy sores on the skin","skin sores","skin blisters","blistering skin","skin blistering","blistering of skin","blisters on skin","blisters on the skin","blistered skin","blisters of skin","blistering of your skin","blistering skin on the legs","blistering skin on the arms","blistering skin on the face","itchy blisters on the skin","painful blisters on the skin","blisters on your skin","skin blisters that are itchy","skin blisters that are painful","oozing blisters on the skin","crusty blisters on the skin","oozing blisters","crusty blisters","blisters in rash area","leg ulcers","skin ulcers","ulcers on the skin","painful ulcers on your skin","ulcers on skin that grow","ulcers on your skin"): "skin sores, blisters, or ulcers",

("sores in the throat","sores on the throat","sores in your throat","sores on throat","sores on the inside of your throat","sores inside the throat","sores in throat","painful sores in throat","painful sores in the throat","blisters in the throat","ulcers in your throat","painful ulcers in throat","painful ulcers in your throat","ulcers in the throat",): "throat sores, blisters, or ulcers",

("a sore that does not heal","sores on your body","pus-filled sores","open sores","blister-like sores","painful rash with blisters","rash with blistering","blistering","blisters","rash with blisters",): "sores, blisters, or ulcers",

("sores of the lips","sores in the corners of the mouth","sores around the mouth","sore on lips","painful sores on lips","sores on lips","painful sores on your lips","tingling sores on lips","itching sores on lips","burning sores on lips","sores in the lips","sores around the lips","sores on the lip","lip sores","blistering of lips","blistering of the lips","blisters on the lips","blisters on lips","ulcers on the lips","painful ulcers on your lips","ulcers on your lips","painful ulcers in your lips",): "lip sores, blisters, or ulcers",

("sores on the nose","sores on the inside of your nose","sores in nose","sores in your nose","painful sores in nose","painful sores in the nose","blisters in the nose","blisters on the nose","ulcers in your nose","painful ulcers in nose","painful ulcers in your nose","ulcers in the nose",): "nose sores, blisters, or ulcers",

("sore throat","return of sore throat","sore throat during treatment and for up to 3 months after your final dose","unexplained sore throat"):"sore throat",

("blistering of eyes","blistering of the eyes","blisters around the eyes","blisters on the eyes","blisters in the eyes","sores around eyes","sores around the eyes","sores on the inside of your eyes","sores in the eyes","ulcers around the eyes",): "eye sores, blisters, or ulcers",

("slowed healing of sores","sores on skin that are slow to heal","ulcers on skin that are slow to heal",):"slow healing sores or ulcers",

("blistering of the hands","rash with blisters on hands",): "hand blisters",

("blistering of the feet","rash with blisters on feet",): "feet blisters",

("unpleasant taste", "salty taste", "metallic taste", "taste changes", "bad taste in the mouth","change in the way things taste", "unusual taste in the mouth", "changes in taste", "change in taste", "sharp metallic taste", "unpleasant metallic taste", "changes in the way food tastes", "metallic taste in mouth", "change in how things taste", "sharp, unpleasant metallic taste", "bitter taste", "unpleasant taste in the mouth", "metallic taste in the mouth", "changes in your ability to taste", "unusual tastes", "garlic-like taste in the mouth", "altered taste", "soapy taste", "bitter taste after instilling the drops", "sour taste after instilling the drops", "unusual taste after instilling the drops", "bitter taste after inserting the drops", "mild taste"): "change in the way things taste",

("decreased ability to taste", "loss of sense of taste", "change in ability to taste",  "changes in ability to taste food",  "loss of taste",  "change in the ability to taste food", "loss in ability to taste food",  "change in ability to taste food", "changes in ability to taste",  "decrease in ability to taste things", "change in sense of taste","changes in your sense of taste",  "altered sense of taste", "changed sense of taste"): "change in ability to taste",

("fever", "new fever", "persistent fever", "fever after vomiting", "fever during treatment", "fever up to two or more months after stopping treatment", "return of fever", "fever that does not go away", "fever during treatment or for up to two or more months after stopping treatment", "rash with fever", "high fever", "a return of fever", "weakness with a fever", "weakness without a fever", "sore throat with fever", "fever with no known cause", "fever during treatment and for up to 3 months after your final dose", "rash with a fever", "rash without a fever", "unexplained fever", "fever for up to two or more months after stopping treatment", "muscle weakness with fever", "fever with chills", "continued fever", "cough with fever", "worsening fever", "recurrent fever", "fevers", "fever that doesnt go away", "fever within 1 to 5 days after receiving a dose of this medication", "sudden fever", "low fever"): "fever",

("lumps in the breasts", "lump under the skin at the base of the neck", "lumps in the stomach area", "breast lumps", "painful lump under your skin", "warm lump under your skin", "red lump under your skin", "unusual lumps", "painful lumps on the skin", "new lumps under your skin that is tender to touch", "unusual lumps under your skin that is tender to touch", "a lump in your breast", "flat skin lumps", "firm skin lumps", "hot skin lumps", "red skin lumps", "painful skin lumps"): "lumps", 

("black stools","tarry stools","black, tarry stool","black stool","tarry stool","black, tarry stools","black tarry stools","black and tarry stools","stools that look like tar","tarry-looking black stools","dark stools","black (tarry) stools","dark, tarry stools","tarry black stools","stool that is black and tarry","black, tarry, sticky stools","stools that are black","stools that are tarry","black stools that look like tar","dark, tarry, sticky stools","black or tarry stools",): "black or tarry stools",

("bloody stools","blood in stool","red stools","red blood in stools","bloody stool","blood in stools","bright red blood in stools","blood in your stool","blood in your stools","reddish colored stools","bright red stools","red blood in the stools","bright red blood in stool","stool that contains bright red blood","stools that have blood","blood in the stool","red stools that look like tar","stools that contain blood","stools that have blood in them","stools with blood in them",): "red or bloody stool",

("pale stools","light colored stools","light-colored stools","clay-colored stools","light colored stool","clay colored stools","white stools","temporary discoloration of your stool","pale-colored stools","yellow stools","light-colored stool","orange-colored stool","changes in stool color","pale stool color"): "pale or discolored stools",

("loose stools","watery stools","loose stool","frequent loose stools",): "loose or watery stool",

("severe diarrhea with watery stools","severe diarrhea with bloody stools",): "frequent diarrhea",

("oily stools","fatty stools","greasy stools","sticky stools","stools that are sticky",): "sticky or greasy stool",

("mucus in stools","stools that have mucus","stools that have mucus in them","stools that contain mucus","stools with mucus in them",): "mucus in stools",

("frequent stools","more frequent stools",): "frequent stools",

("breaking out in a cold sweat","cold sweat","breaking out in cold sweat","cold sweats",):"cold sweats",

("sweating","unusual sweating","excessive sweating","heavy sweating","increased sweating","decreased sweating","unusual sweating on face","unusual sweating on palms","sweating more than usual",): "unusual sweating",

("temporary discoloration of your sweat","change in color of sweat",):"sweat discoloration",

("daytime sleepiness",  "excessive daytime sleepiness"): "daytime sleepiness",

("difficulty falling asleep", "difficulty staying asleep", "falling asleep", "staying asleep", "sleepiness", "difficulty sleeping", "sleep disturbances", "excessive sleepiness", "severe trouble sleeping", "unusual sleepiness",  "extreme sleepiness", "trouble falling asleep", "trouble staying asleep", "sleeplessness", "sleep problems", "problems sleeping", "trouble sleeping", "difficulty in sleeping", "insomnia"): "difficulty sleeping/sleepiness",

("temporary inability to move while going to sleep", "sleep paralysis","difficulty moving when sleeping"): "temporary inability to move while going to sleep",

("grinding teeth during sleep", "clenching teeth during sleep"): "grinding/clenching teeth during sleep",

("temporary inability to talk while going to sleep", "temporary inability to speak while going to sleep"): "temporary inability to speak while going to sleep",

("nipple discharge","milky discharge from the nipples","breast discharge","fluid leaking from breasts","discharge from the breast","breasts that produce a liquid",): "breast/nipple discharge",

("enlargement of the breast","breast enlargement","breast enlargement in men","breast enlargement in women","enlarged breasts in men","enlarged breasts in women","increased size of the breasts","breast enlargement in males","temporary breast enlargement (in children)","enlargement of the breasts","enlarged breasts",): "breast enlargement",

("breast tenderness","tender breasts",): "tender breasts",

("swollen breasts","breast swelling",): "swollen breasts",

("decrease in breast size","decrease in breast size in women",): "decrease in breast size",

("difficulty walking","problems with walking","unsteady walking","trouble walking","difficulty walking normally","problems walking","sudden trouble walking","incoordination causing difficulty walking","unsteady walking that may cause falling","sudden difficulty walking","unsteadiness when walking","stumbling when walking","loss of balance when walking",): "problem or difficulty walking",

("changes in walking","changes in your walking","change from normal walking",): "changes in walking",


("changes in breast size","change in breast size in men","change in breast size in women",): "changes in breast size",
('anxiety', 'new anxiety', 'worsening anxiety', 'unusual anxiety', 'feelings of anxiety'): "anxiety",

('depression', 'new depression', 'worsening depression'): "depression",

('irritability', 'irritability while feeding in infants less than 6 weeks old', 'hostility', 'feelings of hostility'): "irritability/hositility",

('nervousness', 'feeling nervous'): "nervousness",

('feeling worried', 'worrying', 'excessive worry', 'extreme worry', 'excessive worrying', 'feeling unusually worried'): "feeling worried",

('overwhelming fear', 'unmanageable fear', 'irrational fears', 'unreasonable fear of developing a serious illness'): "feeling fearful",

('abnormally excited mood', 'inappropriate mood', 'mood swings', 'sudden mood changes', 'unusual mood changes', 'changes in mood', 'mood changes', 'sudden changes in mood', 'abnormally happy mood', 'extreme changes in mood', 'frenzied mood', 'depressed mood', 'mood change in females', 'high mood', 'elevated mood', 'change in mood', 'rapid changes in mood', 'frequent mood changes', 'unusual changes in mood', 'unusual changes in your mood'): "mood changes",

('loss of consciousness', 'decreased consciousness', 'sudden loss of consciousness', 'loss of consciousness for a period of time', 'unconsciousness', 'change in consciousness'): "change in consciousness",

('fainting', 'feeling faint', 'faintness', 'diarrhea that causes you to feel faint', 'near fainting episodes', 'feel faint', 'near fainting', 'sudden faintness'): "feeling faint/fainting",

("heartburn", "new heartburn", "worsening heartburn", "heart burn", "fast heart beat",): "heartburn",

("irregular heartbeat", "rapid heartbeats", "pounding heartbeats", "fast heartbeat", "pounding heartbeat", "slow heartbeat", "rapid heartbeat", "heart palpitations", "feeling like heart is skipping beats", "change in heartbeat", "slow heart rate", "changes in heartbeat", "slowed heartbeat", "fast heartbeats", "irregular heartbeats", "increased heartbeat", "decreased heartbeat", "rapid heart beat", "pounding heart beat", "irregular heart beat", "feel like heart is racing", "slow heart beat", "weak heart beat", "uneven heartbeat", "increased heart rate", "rapid heart rate", "fluttering heartbeat", "fast heart rate", "irregular heart rate", "racing heartbeat", "slowed heart beat", "feeling of racing heart", "feeling of pounding heart", "abnormal heartbeat", "heart racing", "feeling of heart racing", "feeling like heart is racing", "new irregular heartbeat", "worsening irregular heartbeat", "forceful heartbeats", "skipped heartbeat", "stopped heartbeat", "feeling of rapid heartbeat", "feeling of irregular heartbeat", "changes in heart rate", "feeling like your heart is racing", "strong heartbeat", "abnormal heart rhythms", "changes in heart beat", "changes in heart rhythm", "decrease in heart rate", "racing heart", "feeling like heart is skipping a beat", "feeling of fast heartbeat"): "changes in heartbeat",

("sensitivity to temperature in the fingers", "sensitivity to temperature in the toes",  "sensitivity to heat","sensitivity to temperature in the fingers or toes", "increased sensitivity to cold", "sensitivity to cold", "unusual discomfort in cold temperatures","intolerance to cold","change in your ability to feel cold","change in your ability to feel heat",): "change in sensitivity to temperature",

( "skin more sensitive to sunlight than usual", "light sensitivity", "sensitivity to light during treatment and for up to 3 months after your final dose","sensitivity to the sun"): "change in sensitivity to sunlight",

("skin sensitivity on one side of the body", "skin sensitivity on one side of the face","sensitive skin",): "general skin sensitivity",

('nail changes', 'nail problems', 'changes in nails', 'changes in the nails', 'problems with nails', 'nail disorders', 'changes in fingernails', 'changes in toenails', 'problems with toenails', 'problems with fingernails', 'change in shape of nail(s)', 'changes in the fingernails', 'changes in the toenails'): "nail problems/changes",

('itching of the skin around the affected toenail(s)', 'burning in the area around the affected toenail(s)', 'stinging in the area around the affected toenail(s)', 'blisters in the area around the affected toenail(s)', 'peeling of the skin around the affected toenail(s)', 'changes in the area around fingernails', 'changes in the area under fingernails', 'changes in the area around toenails', 'changes in the area under toenails'): "problems/changes of skin around the nail",

('changes in growth of finger nails', 'changes in growth of toe nails', 'ingrown toenail', 'ingrown nail(s)'): "change in nail growth",

('thin fingernails', 'changes in nail thickness', 'thickening of nails',): "changes in nail thickness nails",

('brittle fingernails', 'brittle toenails', 'brittle nails', 'weak fingernails',): "brittle/weak nails",

( 'changes in color of fingernails', 'changes in nail color', 'changes in color of finger nails', 'changes in color of toe nails', 'changes in color of nails', 'change in color of nails', 'bluish-colored fingernails', 'bluish color of fingernails',  'nail discoloration','discoloration of nail(s)','darkening of the nails', ): "change in nail color",

('nail splitting', 'nail breaking', 'nail separation from nailbed', 'nail loss from nailbed','separation of fingernail from the nail bed','separation of toenail from the nail bed', ): "nail breakage/separation from nailbed",

('nail pain', 'pain in the area around the affected toenail(s)', 'pain at the affected nail(s)', 'pain in the fingernails', 'pain in the toenails',): "nail pain",

('nail swelling', 'swelling of the nail beds on toes', 'swelling of the nail beds on fingers', 'swelling around the fingernails', 'swelling around the toenails', 'swelling around the nails', 'swelling of the skin around the affected toenail(s)', 'swelling of the fingernails', 'swelling of the toenails'): "nail swelling",

('nail redness', 'redness of the nail beds on toes', 'redness of the nail beds on fingers', 'redness around the fingernails', 'redness around the toenails', 'redness of the skin around the affected toenail(s)'): "nail redness",

('changes in the appearance of the nails', 'change in appearance of nails', 'change in the appearance of nails', 'changes in the appearance of nails'): "change in appearance of nails",

("seizures","seizure",): "seizures",

("stretch marks on the skin","stretch marks on the skin of the abdomen","stretch marks on the skin of the thighs","stretch marks on the skin of the breasts","stretch marks on your skin",): "stretch marks",

("seizures that last longer than in the past","seizures that happen more often than in the past","new seizures","increased number of seizures","seizures that happen more often","seizures that are worse than before","worsening of seizures","worsening seizures","longer-lasting seizures","seizures that last longer","seizures that are different than the seizures you had in the past","seizures that are worse or different than the seizures you had before","increased frequency of seizures","different seizures",): "change in seizures",

("severe skin rash","skin rash","rash that covers a large area of your body","rash all over the body","rash on other parts of the body","painful rash on one side of body","rash on other part of the body","rash on the skin","rash of pinpoint-sized reddish-purple spots, usually on the lower legs","rash of skin","rash in the underarm area",): "skin or body rash",

("rash","reddish purple rash","new rash","worsening rash","rash with peeling skin","severe rash","severe skin rash that keeps getting worse","red rash","scaly rash","severe rash with peeling skin","itchy rash","painful rash","mild rash","red rashes","scaly rashes","growing rash","acne-like rash","unexplained rash","pain followed by a rash","itching followed by a rash","tingling followed by a rash","rash that lasts at least 14 days"): "rash",

("rash on cheeks that is sensitive to sunlight","rash on arms that is sensitive to sunlight","red rash that may be sensitive to sunlight","scaly rash that may be sensitive to sunlight","rash on the face that worsens in the sun","rash on the arms that worsens in the sun","rash on the cheeks that is sensitive to sunlight","rash on the arms that is sensitive to sunlight","rash on the cheeks that gets worse in the sun","rash on the arms that gets worse in the sun",): "rash sensitive to sunlight",

("rash on the face","rash on the cheeks","rash around the mouth","painful rash on one side of face","rash on cheeks","rash on nose",): "face rash",

("rash on palms","rash on sole(s) of the feet","rash on the palms of the hands","rash on the soles of the feet",): "palmarplanter rash",

("burning of the tongue","tingling of the tongue","burning sensation of the tongue","numbness of the tongue","tingling in your tongue","unusual feelings of the tongue","itching of the tongue","strange feeling in the tongue",): "unusual sensations in tongue",

("tongue that sticks out of the mouth","tongue sticking out",): "tongue sticking out",

("fine, worm-like tongue movements","uncontrollable movements of your tongue","fine tongue movements","worm-like tongue movements","fine worm-like tongue movements","uncontrollable movements of the tongue","unusual movements of your tongue that you cannot control",): "uncontrollable or unusual tongue movements",

("redness of the tongue","redness of tongue",): "red tongue",

("paleness of the tongue","grayness of the tongue","black tongue","change in color of the tongue","change in color of tongue","change in tongue color",):"change in tongue color",

("tongue irritation","irritation of the tongue"):"tongue irritation",

("infection","infections","infection that lasts a long time","infections that come and go","infections that do not go away","infection at or near the area being treated",): "infection",

("signs of an infection","signs of infection","signs of infection during treatment and for up to 1 to 2 weeks after your final dose","return of signs of infection","signs of infection during treatment and for up to 1 month after your treatment","signs of infection during treatment and for 2 months after your treatment","signs of skin infection in the place where you applied this medication","signs of new infection","signs of worsening infection","signs of infection such as sore throat","signs of infection such as runny nose","signs of infection such as stuffy nose","signs of infection such as cough","signs of infection such as fever","signs of infection such as chills","signs of infection such as tiredness","sign of infection",): "signs of infection",

("nail infection","infection of the skin around the fingernails","infection of the skin around the toenails","infection around the nail","yeast infection of the nails","fungal infection of the nails"): "nail infection",

("infection around the skin","skin infection",): "skin infection",

("signs of an ear infection","signs of ear infection",): "signs of ear infection",

("yeast infection of the mouth","fungal infection of the mouth",): "yeast or fungal infection of mouth",

("yeast infection of the throat","fungal infection of the throat",): "yeast or fungal infection of throat",

("yeast infection of the skin","fungal infection of the skin",):"yeast or fungal infection of skin",

("yeast infection of the feet","fungal infection of the feet",): "yeast or fungal infection of feet",

("feeling cold","cold feeling","feeling of coldness",): "feeling cold",

("cold hands","cold feet","cold sensation in legs","feeling cold in the arms","feeling cold in the legs","cold fingers","cold toes","feeling cold, especially in the arms or legs","coldness in hands or feet","cool hands","cool feet","fingers feeling cool","toes feeling cool",) :"cold or cool extremities",

("menstrual bleeding", "menstruation",): "menstruation",

("abnormal menstrual periods", "abnormal menstrual cycles", "irregular menstrual periods", "irregular menstruation", "differences in menstrual bleeding","changes in menstrual cycle", "change in menstrual cycle", "changes in menstrual flow", "changes in menstrual bleeding patterns"): "abnormal/change in menstrual periods",

("absent menstrual periods", "missed menstrual periods", "missed menstrual period", "missed menstruation", "absence of menstrual cycle",): "absent menstrual periods",

("late menstrual periods", "late menstrual period"): "late menstrual periods",

("heavy menstrual bleeding", "heavy menstrual periods", "abnormally heavy menstrual bleeding (periods)", "menstrual bleeding that is unusually heavy", "excessive menstrual bleeding", "increased menstrual flow","heavier than usual menstrual bleeding","menstrual bleeding that is heavier than usual",  "heavier than normal menstrual periods"): "heavy/heavier menstrual periods",

("painful menstruation", "painful menstrual periods", "difficult menstruation", "painful cramps during menstrual period", ): "painful/difficult menstrual period",

("spotting between menstrual periods", "bleeding between menstrual periods",): "bleeding/spotting between menstrual cycles",

("hot skin","hot areas of skin","hot area on the skin",): "hot skin",

("hot flushes","hot flashes","hot flush","sudden wave of mild body heat","sudden wave of intense body heat",): "hot flashes",

("feeling hot","hot feeling","feeling overheated",): "feeling hot",

("constipation","constipation that lasts longer than 3 days","new constipation","worsening constipation","severe constipation",): "constipation",

("blue color of fingers","blue color of toes","blue color of the fingers","blue color of the toes","blue-colored hands","blue-colored feet",): "blue extremities",

("skin color change from pale to blue to red in the fingers","skin color change from pale to blue to red in the toes","skin color change from pale to blue to red in the fingers or toes",): "skin color change from pale to blue to red in extremities",

("skin discoloration (blue to bluish-purple)","skin turning blue","blue-colored skin",): "blue skin",

}

labels_ordered = open("./create_multilabel_dataset/label_order_temp.txt").read()
labels_ordered = ast.literal_eval(labels_ordered)
keyslst= []

for lst in generalized.keys():
    for side_effect in lst:
        # print(side_effect)
        if side_effect not in labels_ordered:
            continue
            # print(side_effect)
        else:
            labels_ordered.remove(side_effect)
    labels_ordered.append(generalized[lst])
    # if generalized[lst] == "palmar-plantar blistering":
    #     print(labels_ordered)
    # keyslst.append(generalized[lst])
    
print(labels_ordered)
print(len(labels_ordered))
# print(keyslst)

with open('./create_multilabel_dataset/label_order_full.txt', 'w', encoding="utf-8") as f:
    for item in labels_ordered:
        f.write(f'"{item}",')

