import ast

generalized = {("increase in facial hair", "increased hair growth on parts of the body","unwanted hair growth","excessive hair growth","hair loss","loss of hair","unusual hair thinning", "thin hair","brittle hair","change in hair color","abnormal hair growth in women","temporary hair loss","hair thinning","increase in size of fine body hair","increase in darkness of fine body hair","hair color changes","increased hair growth","abnormal hair loss","changes in hair texture","thinning of hair","changes in the appearance of the hair","reversible hair loss","increased hair growth on the face","increased hair growth on the arms", "increased hair growth on the back", "hairy tongue","dry hair","thinning hair","unusual hair growth on the face in women","unusual hair growth on the body in women","excessive hair growth on the face in women","excessive hair growth on the body in women","oiliness of hair","dryness of hair","hair discoloration","oily hair","hair growth in unusual places","facial hair","hair color turning lighter","hair color turning gray","increase in pubic hair","growth of hair on face","loss of hair on scalp","increased hair growth on head","increased hair growth on face","increased hair growth on eyelashes","increased hair growth on chest","unusual hair growth","thicker body hair","thicker facial hair",): "change in body hair",
("red bumps around hair follicles","swollen bumps around hair follicles","painful bumps around hair follicles","itchy bumps around hair follicles","pimples around hair follicles"): "irritation around hair follicles",

("extreme hunger","hunger","unusual hunger","sudden hunger","increased hunger","increase in hunger","feeling very hungry","feeling more hungry than usual","feeling hungry",): "hunger",

("increase in thirst","feeling very thirsty","thirst","increased thirst","feeling more thirsty than usual","feeling thirsty","extreme thirst","excessive thirst","unusual thirst","being thirsty",): "thirst",

("burning of the lips","burning of the tongue", "burning of skin", "muscle burning", "burning in the underarm area", "burning in the mouth","burning in the throat", "burning nose","chest burning","burning sensation on the skin"): "burning of body parts",

("eye burning","burning sensation in eye(s)","burning in the eye","discomfort in the eye", "temporary burning of the eye", "swollen eyes","red eyes","teary eyes","painful eyes","sensitivity to light","eye pain","eye redness","eye tearing","dry eyes","irritated eyes","dry eye", "eyes more sensitive to light than usual","light hurting your eyes", "red eyelids", "pain in the eye","pressure in the eye","redness of the eye", "eye irritation","watery eyes","eye sensitivity to light", "swelling in the eye","increased sensitivity of your eyes to light", "eye swelling", "burning of the eyes", "burning eyes","excessive tears","eye discharge","crusty eyes","discharge from the eyes","irritation of the eyes","pain of eyes","pain of eyelids","redness of eyes","redness of eyelids","eyes sensitive to light","reddened eyes","redness of the eyes","inflamed eyes","itching of the eyes","painful dryness of the eyes","constant dryness of the eyes","burning in the eyes","rash with red eyes","rash with swollen eyes","redness in or around the eye","sore eyes","itchy eye(s)","watery eye(s)","red eye(s)","itching of the eye","burning of the eye","stinging of the eye","bleeding around the eye","stinging of the eyes","increased eye redness","increased eye itching","pain with eye movement","swelling in the eyes","stinging eyes","runny eyes","feeling that something is in your eye","sticky eyes","bloody eyes","feeling that something is in the eye","eye crusting","sensitivity to bright light","eye discomfort","eyelid swelling","stinging in the eye","bleeding within the eye","sensitivity of your eyes to light","increased eye tearing","dryness of the eyes","eye problems","difficulty moving eyes","temporary stinging of the eye","increased redness of the eye that continues for more than 48 hours","increased itching of the eye that continues for more than 48 hours","increased swelling of the eye that continues for more than 48 hours","raised eyelids","redness of the eyelid","discharge of the eye","discharge of the eyelid","pain of the eye","pain of the eyelid","itching eyes","discharge from eyes","itchy eye","tingling of the eyes","other eye problems","red eyelid(s)","swollen eyelid(s)","pain in eye(s)","sensitivity of eyes to light","eye itching","excessive tearing from the eye","discharge from the eye","eyelid pain","eyelid irritation","feeling like something is in your eye","scratchy eye","eye lid redness","irritation of the eyelid","irritation of the eye","temporary stinging in the eyes","temporary burning in the eyes","broken blood vessels in the eyes","eyelid problems","red eye",): "eye discomfort or irritation",

("swelling around the eyes","swelling around the eye", "swelling of your eyes", "swelling of your eyelids", "swelling in your eyelids","swelling of eyes","swelling of the eyelids","swollen eyelids","swelling of eyelids","sudden swelling of the eyes","swelling in or around the eye","swelling around eyes","swelling of the eyelid",): "swelling around the eyes",

("eye discoloration", "darkening of the eyes","changes in color of eyes","pale eyes","discoloration of the eye",): "eye discoloration",

("yellowing of whites of eyes", "jaundice", "yellowing of white parts of the eyes", "yellowing of the whites of the eyes", "swelling of the eye","yellowing of the white part of your eyes","yellowing of the whites of your eyes","yellowing of the eye","yellowing of the white of your eyes","yellowing of the whites of eyes","yellowness of the eyes","yellowing of whites of the eyes", "tearing in eyes","yellow of eyes",): "jaundice",

("uncontrolled eye movements", "uncontrollable eye movements", "unwanted eye movements","fast, repeating eye movements that you cannot control","fast eye movements that you cannot control","repeated eye movements that you cannot control","uncontrollable movements of the eyes","abnormal eye movements",): "uncontrollable eye movements",

("burning, especially on the bottoms of the feet", "burning pain in your arms","burning pain in your legs","burning sensation in the hands","burning sensation in the feet", "burning of the feet", "burning of the fingers",): "extremity burning",

("pink eye","pink eyes","pink eye(s)","symptoms of pink eye",): "pink eye",

("burning sensation when urinating", "burning when you urinate"): "burning when you urinate",

("unusual feelings of the lips","unusual feelings of the tongue","unusual feelings of the fingers","unusual feelings of the feet","abnormal sensation in the eyes"):"unusual feelings in parts of body",

("sudden tightening of the muscles in the hands","sudden tightening of the muscles in the feet","sudden tightening of the muscles in the face","sudden tightening of the muscles in the throat"): "sudden tightening of muscles",

("pain in the arm","pain in the back","pain in the neck","pain in the stomach",): "Pain in parts of body",

("weakness in hands","weakness in feet","weakness in other parts of the body"): "Weakness in parts of body",

("repeated nausea","repeated vomiting"): "nausea",

("nail swelling","nail redness","nail pain","nail splitting","nail breaking","nail separation from nailbed","nail loss from nailbed"): "Nail problems",

("new shortness of breath","worsening shortness of breath"): "shortness of breath",

("hives on arms","hives on lower legs","hives on buttocks","hives on trunk"): "hives on parts of body",

("new fever","persistent fever"):"Fever",

("seeing things that do not exist", "hallucinating", "hearing voices that do not exist"): "Hallucinating",

("feeling unsteady","trouble keeping your balance"): "Feeling Unsteady",

("blistering of the skin","blisters of the skin"): "Blistering Skin",

("sudden faintness", "faintness"): "faintness",

("sudden mood changes","unusual mood changes"): "mood changes",

("itching in the area where this medication was injected", "itching near the spot that this medication was injected", "itching at the spot that this medication was injected", "itching that occurs a few days after stopping this medication after taking for a long time", "itching near the spot this medication was injected", "itching in the place this medication was injected", "itching at the place where this medication was applied", "itching at the place where you applied this medication", "itching in the place where you applied this medication", "itching near the spot where this medication was injected", "itching at the place where this medication was inserted", "itching of the skin where you injected this medication", "itching where the medication was applied", "itching at the injection site", "injection site itching", "itching at injection site", "itchiness at the injection site", "itching at the this medication injection site"): "itchiness where the medication was applied",

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

("severe lower abdominal pain 3 to 5 weeks after taking this medication", "severe lower abdominal pain (3 to 5 weeks after taking this medication)"): "severe lower abdominal pain 3 to 5 weeks after taking this medication",

("worsening oozing in a place you injected this medication", "oozing pus in the place where you applied this medication", "oozing at the place where you applied this medication", "oozing in the place where you applied this medication", "fluid at the injection site", "pus at the injection site"): "oozing where the medication was applied",

("burning in the areas where you applied this medication", "burning in the place this medication was injected", "burning at the place where you applied this medication", "burning feeling at or near the area that you applied this medication", "burning in the place where you applied this medication", "burning after instilling this medication", "burning where the medication was applied", "burning at injection site", "burning around the injection site"): "burning where the medication was applied",

("worsening warmth in a place you injected this medication", "warmth in the areas where you applied this medication", "warmth in the place this medication was injected", "warmth in the place where this medication was injected", "warmth in the place where you applied this medication","warmth near the injection site", "injection site warmth", "feeling of warmth at the injection site", "feeling of warmth around the injection site", "warmth at the injection site", "heat at the injection site"): "warmth where the medication was applied",

("stinging in the areas where you applied this medication", "stinging in the place where you applied this medication", "stinging after instilling this medication", "stinging where the medication was applied", "stinging at injection site"): "stinging where the medication was applied",

("soreness in the areas where you applied this medication", "soreness near the place where this medication was injected", "soreness at injection site", "soreness at the injection site"): "soreness where the medication was applied",

("sores at the spot where this medication was injected", "sores at the place where this medication was applied", "sores where the medication was applied", "sores at the injection site"): "sores where the medication was applied",

("dryness at the place where this medication was applied", "dryness at the site where this medication was injected"): "dryness where the medication was applied",

("skin blistering in the area where this medication was injected", "blistering at the place where this medication was applied", "blistering at the place where you applied this medication", "blistering in the place where you applied this medication", "blisters where the medication was applied", "blistering at injection site", "blistering at the injection site"): "blistering where the medication was applied",

("painful eyes if this medication comes in contact with eyes","irritated eyes if this medication comes in contact with eyes","red eyes if this medication comes in contact with eyes","loss of vision if this medication comes in contact with eyes"): "irritation of eyes if medication comes into contact with eyes",

("irritation at the place where you applied this medication", "irritation in the place where you applied this medication tape", "irritation in the place where you applied this medication", "irritation in the place where this medication was injected", "irritation where the medication was applied","irritation at the injection site", "injection site irritation"): "irritation where the medication was applied",

("tenderness in the place where this medication was injected", "tenderness in the place where you applied this medication", "tenderness of the skin where you injected this medication", "tenderness at the injection site", "tenderness near the injection site", "injection site tenderness"): "tenderness where the medication was applied",

("hardness in the place where this medication was injected", "hardness in the place this medication was injected", "hardened area of skin at the injection site", "hardness at the injection site", "hardness at injection site", "hardening at the injection site"): "hardness where the medication was applied",

("tingling in the area where this medication was injected", "tingling in the place where this medication was injected", "tingling at the injection site"): "tingling where the medication was applied",

("nausea after stopping this medication and for up to 1 year afterwards", "vomiting after stopping this medication and for up to 1 year afterwards"): "nausea after stopping this medication and for up to 1 year afterwards",

("feeling of coldness at the injection site", "feeling of coldness around the injection site"): "feelings of coldness where medication was applied"
}

labels_ordered = open("./create_multilabel_dataset/label_order_full.txt").read()
labels_ordered = ast.literal_eval(labels_ordered)

for lst in generalized.keys():
    for side_effect in lst:
        print(side_effect)
        labels_ordered.remove(side_effect)
    labels_ordered.append(generalized[lst])
    
print(labels_ordered)
print(len(labels_ordered))

with open('./create_multilabel_dataset/label_order_full.txt', 'w', encoding="utf-8") as f:
    for item in labels_ordered:
        f.write(f'"{item}",')

