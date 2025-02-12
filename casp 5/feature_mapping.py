import numpy as np

map_feature = {
    "University": "university",
    "cross": "grade",
    "sex": "gender",
    "birth_ye": "birth_date",
    "a_1": "close_friend_count",
    "a_2": "spent_time_friend1",
    "a_3": "spent_time_friend2",
    "a_4": "chatting_online",
    "b_6": "body_image",
    "b_7": "diet_plan",
    "breakfastroutindays": "breakfast_routindays",
    "breakfastfriday": "breakfast_friday",
    "naharroutinday": "lunch_routinday",
    "naharfriday": "lunch_friday",
    "shamroutinday": "dinner_routinday",
    "shamfriday": "dinner_friday",
    "Sweet": "sweet",
    "saltysnack": "saltysnack",
    "noshabeh": "soda",
    "MiveyeTazehe2halati": "fresh_fruit",
    "h_35_b": "dry_fruit",
    "h_36": "fresh_juice",
    "h_37": "packed_juice",
    "h_38": "vegetables",
    "h_39": "milk",
    "h_42": "fastfoods",
    "z_52": "physical_activity",
    "z_54": "physical_activity_hour",
    "h_57": "TV_watching_routinday",
    "h_58": "TV_watching_friday",
    "h_61": "computer_work_routinday",
    "h_62": "computer_work_friday",
    "h_63_1": "sleep_hours_routinday",
    "h_64_1": "sleep_hours_friday",
    "t_65": "injury_number",
    "t_66": "injury_place",
    "t_67": "injury_cause",
    "t_68": "injury_treatment_place",
    "y_69": "fight_number",
    "y_70": "litigant",
    "y_71": "carry_weapons",
    "k_73": "victim_number",
    "k_74": "bully_number",
    "l_75_1": "father_hookah",
    "l_75_2": "mother_hookah",
    "l_75_3": "sibling_hookah",
    "l_75_4": "others_hookah",
    "l_76_1": "father_smoker",
    "l_76_2": "mother_smoker",
    "l_76_3": "sibling_smoker",
    "l_76_4": "others_smoker",
    "m_77": "comfort_father",
    "m_78": "comfort_mother",
    "m_79": "comfort_brother",
    "m_80": "comfort_sister",
    "m_81": "comfort_friend",
    "n_82": "headache_number",
    "n_83": "stomach_ache_number",
    "n_84": "back_pain_number",
    "n_85": "worthless_number",
    "n_86": "angriness_number",
    "n_87": "worried_number",
    "n_88": "insomnia_number",
    "n_89": "confusion_number",
    "n_90": "depression",
    "n_91": "anxiety_number",
    "n_92": "mental_health_overview",
    "s_95_3": "smoking_type",
    "s_96": "current_smoker_status",
    "s_100": "smoke_anxiety_reduction",
    "s_101": "smoke_focus",
    "s_102": "smoke_social_acceptance",
    "s_103": "smoke_feeling_grown_up",
    "s_104": "smoke_feeling_loved",
    "s_105": "smoke_confidence_boost",
    "s_106": "smoke_pleasure",
    "s_107": "smoke_staying_awake",
    "s_108": "smoke_leisure",
    "s_109": "smoke_escaping_problems",
    "weight_1": "weight",
    "height_2": "height",
    "waist_3": "waist",
    "wrist4": "wrist",
    "hip": "hip",
    "systolic": "systolic",
    "diastoli": "diastoli",
    "age": "age",
    "catage": "catage",
    "familynu": "family_size",
    "ap_2": "home_ownership",
    "ap_3": "father_edu",
    "ap_4": "mother_edu",
    "ap_5": "father_job",
    "ap_6": "mother_job",
    "ap_7": "car_ownership",
    "ap_8": "computer_ownership",
    "ap_9": "school_type",
    "ap_17": "ap_17",
    "ap_18": "ap_18",
    "ap_19": "ap_19",
    "ap_20": "ap_20",
    "ap_21": "ap_21",
    "numberch": "children_number",
    "ap_23": "birth_order",
    "bp_28": "birth_weight",
    "bp_29": "milk_type",
    "bp_30": "breast_feeding_duration",
    "bp_31": "complementary_feeding",
    "dp_41": "bread_type",
    "dp_42": "oil_type",
    "dp_43": "table_salt",
    "dp_44": "dairy_type",
    "dp_46": "fatty_dairy",
    "dp_47": "usual_dairy",
    "dp_48": "grains",
    # "dp_49": "fastfoods",
    "dp_50": "meat",
    "dp_51": "liverandkalepache",
    "dp_52": "bread",
    "dp_53": "rice",
    "dp_54": "potato",
    "dp_65": "friedfoods",
    "dp_69": "reduce_fat",
    "dp_70": "use_liquid_oil",
    "dp_71": "increase_vegetables",
    "dp_72": "reduce_sugar",
    "dp_73": "reduce_salt",
    "dp_74": "reduce_fast_food",
    "dp_75": "fruit_nut_substitute",
    "hp_94": "injury_parent_ask",
    "hp_95": "injury_complication",
    "region": "region",
}
map_feature_4 = {
    "universi": "university",
    "cross": "grade",
    "sex": "gender",
    "birth_ye": "birth_date",
    "a_1": "close_friend_count",
    "a_2": "spent_time_friend1",
    "a_3": "spent_time_friend2",
    "a_4": "chatting_online",
    "bodyimag5halati": "body_image",
    "barnamenutrition4halati": "diet_plan",
    "breakfastroutindays": "breakfast_routindays",
    "breakfastfriday": "breakfast_friday",
    "naharroutinday": "lunch_routinday",
    "naharfriday": "lunch_friday",
    "shamroutinday": "dinner_routinday",
    "shamfriday": "dinner_friday",
    "Sweet": "sweet",
    "saltysnack": "saltysnack",
    "noshabeh": "soda",
    "MiveyeTazehe2halati": "fresh_fruit",
    "MiveyeKhoshk": "dry_fruit",
    "Swetenedbeverage": "fresh_juice",
    "abmiveyebastebandishodeh": "packed_juice",
    "vegtebale": "vegetables",
    "Milk": "milk",
    "fastfoods": "fastfoods",
    "newphysicalactivietyhour": "physical_activity_hour",
    "PhysicActive": "physical_activity",
    "TVwatchingroutinday": "TV_watching_routinday",
    "TVwatchingFriday": "TV_watching_friday",
    "Computerworkroutinday": "computer_work_routinday",
    "ComputerworkFriday": "computer_work_friday",
    "Sleephoursroutinday": "sleep_hours_routinday",
    "SleephoursrFriday": "sleep_hours_friday",
    "injurynumber": "injury_number",
    "h_44": "injury_place",
    "h_45": "injury_cause",
    "h_46": "injury_treatment_place",
    "physicalfightnumber": "fight_number",
    "i_48": "litigant",
    "hamlselahnumber": "carry_weapons",
    "victimnumber": "victim_number",
    "bullynumber": "bully_number",
    "madargelyani": "mother_hookah",
    "pedargelyani": "father_hookah",
    "baradrkhahargelyani": "sibling_hookah",
    "sayerfradgelyani": "others_hookah",
    "pedarsigari": "father_smoker",
    "madarsigari": "mother_smoker",
    "baradaryakhaharsigari": "sibling_smoker",
    "sayerafradkhanevadehsigari": "others_smoker",
    "l_56": "comfort_mother",
    "l_59": "comfort_friend",
    "l_55": "comfort_father",
    "l_58": "comfort_sister",
    "l_57": "comfort_brother",
    "confusionnumber": "confusion_number",
    "worthlessnumber": "worthless_number",
    "insomnianumber": "insomnia_number",
    "m_62": "back_pain_number",
    "m_61": "headache_number",
    "worriednumber": "worried_number",
    "m_60": "stomach_ache_number",
    "angrinessnumber": "angriness_number",
    "depression": "depression",
    "Anxietynumber": "anxiety_number",
    "SRH4halati": "mental_health_overview",
    "activesmokertype": "smoking_type",
    "activecurrentsmoker": "current_smoker_status",
    "n_85": "smoke_leisure",
    "n_83": "smoke_escaping_problems",
    "n_87": "smoke_pleasure",
    "n_86": "smoke_feeling_grown_up",
    "n_79": "smoke_anxiety_reduction",
    "n_80": "smoke_social_acceptance",
    "n_82": "smoke_confidence_boost",
    "n_81": "smoke_focus",
    "n_77": "smoke_staying_awake",
    "n_78": "smoke_feeling_loved",
    "weight_1": "weight",
    "height_2": "height",
    "waist_3": "waist",
    "wrist_5": "wrist",
    "hip_4": "hip",
    "systolic": "systolic",
    "diastoli": "diastoli",
    "age": "age",
    "catage": "catage",
    "family_a": "family_size",
    "v124_a": "home_ownership",
    "fathereducation6halati": "father_edu",
    "mothereducation6halati": "mother_edu",
    "fatherjob": "father_job",
    "motherjob": "mother_job",
    "scholltype": "school_type",
    "v129_a": "car_ownership",
    "v130_a": "computer_ownership",
    "livingparent": "livingparent",
    "childerennumber": "children_number",
    "birthorder": "birth_order",
    "birthweight": "birth_weight",
    "milktype": "milk_type",
    "beastfeedingduration": "breast_feeding_duration",
    "complementryfeeding": "complementary_feeding",
    "breadtyp": "bread_type",
    "oiltype": "oil_type",
    "saltadde": "table_salt",
    "dairytype": "dairy_type",
    "fattydairyparent": "fatty_dairy",
    "usualdairyparent": "usual_dairy",
    "grains": "grains",
    "meat": "meat",
    "liverandkalepache": "liverandkalepache",
    "bread": "bread",
    "rice": "rice",
    "potatoandfresh": "potato",
    "friedfoods": "friedfoods",
    "d_55": "fruit_nut_substitute",
    "d_51": "reduce_fast_food",
    "d_54": "increase_vegetables",
    "d_50": "reduce_salt",
    "d_53": "reduce_sugar",
    "d_49": "reduce_fat",
    "d_52": "use_liquid_oil",
    "injery_5": "injury_parent_ask",
    "v203_a": "injury_complication",
    "region": "region",
}

mapping_university = {
    "khozestan-ahvaz": "khozestan",
    "boshehr": "bushehr",
    "ardabil": "ardabil",
    "azar garbi": "azar gharbi",
    "azar gharbi": "azar gharbi",
    "khorasan shomali-bojnord": "khorasan shomali",
    "qazvin": "qazvin",
    "lorestan": "lorestan",
    "khorasan razavi-mashad": "khorasan razavi",
    "kordestan": "kordestan",
    "yazd": "yazd",
    "kerman-kerman": "kerman",
    "kermanshah": "kermanshah",
    "isfahan": "isfahan",
    "markazi": "markazi",
    "shahid beheshti": "shahid beheshti",
    "sistan-zabol": "sistan",
    "ilam": "ilam",
    "kohkiloye": "kohgiluyeh",
    "4 mahal bakhtiyari": "chaharmahal bakhtiyari",
    "hormzgan": "hormozgan",
    "sistan-zahedan": "sistan",
    "semnan-semnan": "semnan",
    "golestan": "golestan",
    "mazandaran-babol": "mazandaran",
    "kerman-jiroft": "jiroft",
    "hamadan": "hamedan",
    "semnan-shahrod": "semnan",
    "khozestan-dezfol": "dezful",
    "alborz": "alborz",
    "kerman-rafsanjan": "rafsanjan",
    "azar shargi": "azar sharghi",
    "zanjan": "zanjan",
    "fars-shiraz": "fars",
    "gilan": "gilan",
    "qom": "qom",
    "fars-jahrom": "jahrom",
    "isfahan-kashan": "kashan",
    "tehran": "tehran",
    "khorasan razavi-sabzavar": "sabzevar",
    "khorasan razavi-neishabor": "neishabor",
    "fars-fasa": "fasa",
    # "": np.nan,
    "tabriz": "tabriz",
    "fasad": "fasa",
    "ardebil": "ardabil",
    "kurdestan": "kordestan",
    "khorasan shomali": "khorasan shomali",
    "charmahal": "chaharmahal bakhtiyari",
    "khorasan jonobi": "khorasan jonoubi",
    "mazandaran": "mazandaran",
    "kohkiloyeh": "kohgiluyeh",
    "babol": "babol",
    "zabol": "zabol",
    "arak": "arak",
    "behbahan": "behbahan",
    "kerman.jiroft": "jiroft",
    "esfarayen": "esfarayen",
    "iran": "iran",
    "saveh": "saveh",
    "dezful": "dezful",
    "abadan": "abadan",
    "torbat jam": "torbat jam",
    "fars": "fars",
    "iranshahr": "iranshahr",
    "shahidbeheshti": "shahid beheshti",
    "torbat heidariyeh": "torbat heidariyeh",
    "bam": "bam",
    "shahrood": "shahrood",
    "jahrom": "jahrom",
    "shoshtar": "shushtar",
    "larestan": "larestan",
}

mapping_grade = {
    "rahnamayi": "intermediate",
    "ebtedayi": "elementary",
    "dabirestan": "intermediate",
    # "": np.nan,
    "elemantry": "elementary",
    "intermidiate": "intermediate",
}
mapping_close_friend_count = {
    "yeki": "one",
    "3 ta va bishtar": "three or more",
    "2 ta": "two",
    # "": np.nan,
    "aslan nadarm": "any",
    "2 dost": "two",
    "1 dost": "one",
    "3 or more": "three or more",
    "nadarad": "any",
}

mapping_chatting_online = {
    "5 ya 6 ruz dar hafte": "5 or 6 day a week",
    "1 ya 2ruz dar hafte": "1 or 2 day a week",
    "3 ya 4 ruz dar hafte": "3 or 4 day a week",
    "benodrat ya hargez": "never",
    # '': np.nan,
    "never": "never",
    "5 or 6 in week": "5 or 6 day a week",
    "3 or 4 in week": "3 or 4 day a week",
    "1 or 2 in week": "1 or 2 day a week",
    "everyday": "every day",
}

mapping_body_img = {
    "kami chag": "slightly overweight",
    "normal": "normal weight",
    "kamilagar": "complete underweight",
    "khalilagar": "very underweight",
    # '': np.nan,
    "khaili chag": "very overweight",
    "kami laghar": "slightly underweight",
    "kheili chagh": "very overweight",
    "kami chagh": "slightly overweight",
    "kheili laghar": "very underweight",
}

mapping_diet_plan = {
    "no wt ok ast": "weight is fine",
    "yes": "yes",
    "no vali bayad kam kard": "no, but it should be reduced",
    "no vali bayad bishtar kard": "no, but it should be increased",
    # '': np.nan,
    "khub": "weight is fine",
    "kam konam": "no, but it should be reduced",
    "bishtar konam": "no, but it should be increased",
    0.0: np.nan,
}

mapping_breakfast_routindays = {
    "aslan nemikhoram": "0 day",
    "1ruz": "1 day",
    "2ruz": "2 day",
    "6ruz": "6 day",
    "4ruz": "4 day",
    "5ruz": "5 day",
    "3ruz": "3 day",
    # '': np.nan
}

mapping_lunch_routindays = {
    "2 shab": "2 day",
    "5 shab": "5 day",
    "4 shab": "4 day",
    "aslan nemikhoram": "0 day",
    0.0: np.nan,
    "1 shab": "1 day",
    "3 shab": "3 day",
    "6ruz": "6 day",
    "1ruz": "1 day",
    "5ruz": "5 day",
    "3ruz": "3 day",
    "4ruz": "4 day",
    "2ruz": "2 day",
}
mapping_breakfast_friday = {"mikhoram": "yes", "nemikhoram": "no"}
mapping_lunch_friday = {1.0: "yes", 0.0: "no", "mikhoram": "yes", "nemikhoram": "no"}
# mapping_dinner_routindays = {
#     5.0: "5 night",
#     4.0: "4 night",
#     6.0: "6 night",
#     1.0: "1 night",
#     0.0: "0 night",
#     2.0: "2 night",
#     3.0: "3 night",
#     "6 shab": "6 night",
#     "1 shab": "1 night",
#     "2 shab": "2 night",
#     "5 shab": "5 night",
#     "4 shab": "4 night",
#     "3 shab": "3 night",
#     "aslan nemikhoram": "0 night",
# }
mapping_dinner_routindays = {
    5.0: 5,
    4.0: 4,
    6.0: 6,
    1.0: 1,
    0.0: 0,
    2.0: 2,
    3.0: 3,
    "6 shab": 6,
    "1 shab":1,
    "2 shab": 2,
    "5 shab": 5,
    "4 shab": 4,
    "3 shab": 3,
    "aslan nemikhoram": 0,
}


# mapping_screen_timing = {
#     "aslan": "seldom/never",
#     "2 hour": "2 hour",
#     "1 hour": "1 hour",
#     "4 ya bishtar": "4 or more hour",
#     "3 hour": "3 hour",
#     "4 hour or more": "4 or more hour",
#     "seldom/never": "seldom/never",
# }
mapping_screen_timing = {
    "aslan": 0,
    "2 hour":2,
    "1 hour": 1,
    "4 ya bishtar": 4,
    "3 hour": 3,
    "4 hour or more": 4,
    "seldom/never": 0,
}
# mapping_injury_times = {
#     "0.0": "0 time",
#     "1 bar": "1 time",
#     "2 bar": "2 time",
#     "3 bar": "3 time",
#     "4 bar": "4 time",
#     "jerahat nadashtam": "No injuries",
# }
mapping_injury_times = {
    "0.0": 0,
    "1 bar": 1,
    "2 bar": 2,
    "3 bar": 3,
    "4 bar": 4,
    "jerahat nadashtam": 0,
}

mapping_injury_place = {
    "dar khane ya hayate khane": "home",
    "khiaban,jadeh ya parking": "street",
    "bejoz mavarede bala": "other",
    "madrese": "school",
    "khareje shahr": "outside the city",
    "varzeshgah ya zamine varzesh": "sports field",
    "mahale tejari ya kari": "commercial",
    "madreseh": "school",
    "khaiban": "street",
    "khaneh": "home",
    "varzeshgah": "sports field",
    "other": "other",
    "tejari": "commercial",
}
mapping_injury_cause = {
    "car": "car",
    "rah raftan ya davidan": "walking",
    "walking": "walking",
    "hadese mashin ya motor": "car-motorcycle",
    "bazi ya tamrine varzeshi": "sports or exercise",
    "skeyt": "skating",
    "skating": "skating",
    "2 charkhe savari": "bicycle",
    "bike": "bicycle",
    "gaming": "video games",
    "karhaye digar": "other",
    "other": "other",
    "dava": "fight",
    "quarrel": "fight",
    "kar": "work",
    "work": "work",
    "randane mashin ya motaor": "car-motorcycle",
    "driving a car": "car",
}
mapping_injury_treatment_place = {
    "matab": "doctor’s Office",
    "darmanga ya markaze behdasht": "health center",
    "otaghe behdasht": "treatment Room",
    "jaye diger": "other",
    "orjans": "emergency",
    "other": "other",
    "darmangah": "hospital",
    "otagh behdasht": "treatment room",
    "emergency": "emergency",
    "matabe pezeshk": "doctor’s Office",
}
# mapping_fight_number = {
#     "0": "seldom/never",
#     "2": "twice",
#     "1": "once",
#     "4": "four times",
#     "3": "three times",
#     "seldom/never": "seldom/never",
#     "2 bar": "twice",
#     "1 bar": "once",
#     "4 bar": "four times",
#     "3 bar": "three times",
# }
mapping_fight_number = {
    "0": 0,
    "2": 2,
    "1": 1,
    "4": 4,
    "3": 3,
    "seldom/never": 0,
    "2 bar": 2,
    "1 bar":1,
    "4 bar": 4,
    "3 bar": 3,
}
mappling_litigant = {
    "nadashtam": "did not have",
    "dustam": "friend",
    "ba valedeyn ya afrad bozorgsal": "parents",
    "kamelan gharibe": "stranger",
    "baradar ya khahar": "sibling",
    "nadashte": "did not have",
    "brothers or sister": "sibling",
    "gharibeg": "stranger",
    "dustan": "friend",
    "parents": "parent",
}

# mapping_carry_weapons = {
#     "seldom/never": "seldom/never",
#     "1 day": "1 day",
#     "6 day ya bishtar": "6 or More Day",
#     "4-5 day": "4-5 day",
#     "2-3 day": "2-3 days",
#     "6 or more day": "6 or More Day",
# }
mapping_carry_weapons = {
    "seldom/never": 0,
    "1 day": 1,
    "6 day ya bishtar": 4,
    "4-5 day": 3,
    "2-3 day":2,
    "6 or more day": 4,
}

# mapping_victim_number = {
#     "seldom/never": "never",
#     "2-3 bar": "2-3 time",
#     "1 ya 2 bar": "1-2 time",
#     "bishtar az3": "3 or more time",
#     "more than 3 bar": "3 or more time",
#     "1 or 2 bar": "1-2 times",
# }
mapping_victim_number = {
    "seldom/never": 0,
    "2-3 bar": 2,
    "1 ya 2 bar": 1,
    "bishtar az3": 3,
    "more than 3 bar": 3,
    "1 or 2 bar":1,
}
# mapping_bully_number = {
#     "nagofteam": "never",
#     "faqat 1 ya 2 bar": "1-2 time",
#     "2-3 bar": "2-3 time",
#     "4 bar ya bishtar": "4 or more time",
#     "zurgugi nakardam": "never",
#     "4 or more bar": "4 or more time",
#     "1-2 bar": "1-2 time",
# }
mapping_bully_number = {
    "nagofteam": 0,
    "faqat 1 ya 2 bar": 1,
    "2-3 bar": 2,
    "4 bar ya bishtar": 3,
    "zurgugi nakardam": 0,
    "4 or more bar": 3,
    "1-2 bar": 1
}
# mapping_feeling_number = {
#     "benodrat ya hargez": "seldom/never",
#     "taqriban har mah": "every month",
#     "taqriban har hafte": "everyweek",
#     "bish az 1 bar": "more than once a week",
#     "taqriban har day": "everyday",
#     "seldom/never": "seldom/never",
#     "more than once a week": "more than once a week",
#     "every month": "every month",
#     "everyweek": "everyweek",
#     "everyday": "everyday",
# }
mapping_feeling_number = {
    "benodrat ya hargez": 0,
    "taqriban har mah": 1,
    "taqriban har hafte": 2,
    "bish az 1 bar":3,
    "taqriban har day": 4,
    "seldom/never": 0,
    "more than once a week": 3,
    "every month": 1,
    "everyweek": 2,
    "everyday":4,
}
mapping_depression = {
    "kheir": "no",
    "bekhater nadarm": "forgot",
    "bali": "yes",
    "0.0": np.nan,
    "no": "no",
    "yes": "yes",
    "be khater nadaram": "forgot",
}
# mapping_anxiety = {
#     "hargez": "seldom/never",
#     "gahi": "sometimes",
#     "benodrat": "seldom/never",
#     "hamishe": "always",
#     "bishtare vaghtha": "most of the time",
#     "seldom/never": "seldom/never",
#     "sometimes": "sometimes",
#     "most of the time": "most of the time",
#     "always": "always",
# }
mapping_anxiety = {
    "hargez": 0,
    "gahi": 1,
    "benodrat": 0,
    "hamishe": 3,
    "bishtare vaghtha": 2,
    "seldom/never":0,
    "sometimes": 1,
    "most of the time":2,
    "always": 3
}
# mappingـmental_health = {
#     "motevaset": "moderate",
#     "khob": "good",
#     "bad": "bad",
#     "aali": "excellent",
#     "perfect": "excellent",
#     "moderate": "moderate",
#     "good": "good",
#     "average":"moderate"
# }
mappingـmental_health = {
    "motevaset": 1,
    "khob": 2,
    "bad": 0,
    "aali": 3,
    "perfect": 3,
    "moderate": 1,
    "good": 2,
    "average":1
}
mapping_smoking_type = {
    "no  current smmoker": "non-smoker",
    "qalyan": "hookah",
    "sigar": "cigarette",
    "missing": np.nan,
    "sayer": "other",
    "peip": "pipe",
    "other": "other",
    "ghelyun": "hookah",
    "cigar": "cigarette",
}
# mapping_catage = {
#     "1 1-1 4": "11-14",
#     "1 5-1 9": "15-18",
#     "6-1 0": "7-10",
#     "1 1-1 4y": "11-14",
#     "1 5-1 8y": "15-18",
#     "7-1 0y": "7-10",
# }
mapping_catage = {
    "1 1-1 4": 1,
    "1 5-1 9": 2,
    "6-1 0": 0,
    "1 1-1 4y": 1,
    "1 5-1 8y":2,
    "7-1 0y": 0,
}
mapping_home_ownership = {
    "shakshi": "personal",
    "estijari": "rented",
    "shakhsi": "personal",
    "stijari": "rented",
    "sazmani": "organizational",
}
mapping_edu = {
    "ebtedaei": "elementry education",
    "bisavad": "illiterate",
    "rahnamaei": "intermediate",
    "balaye lisans": "graduate education",
    "diplom": "diploma",
    "lisans": "bachelor degree",
    "savad qorani": "quranic literacy",
    "intermediate": "intermediate",
    "diplome": "diploma",
    "illiterate": "illiterate",
    "bachelor": "bachelor degree",
    "upper than bachelor": "graduate education",
    "primary": "elementry education",
    "quranic literacy": "quranic literacy",
    "father died": "father died",  # Replacing this with 'no education'
    "mother died": "mother died",  # Replacing this with 'no education'
}

father_job_mapping = {
    "azad": "self-employed",  # azad refers to self-employed
    "worker/employee": "employee",
    "unemploed": "unemployed",  # fixed typo from 'unemploed' to 'unemployed'
    "keshavarz": "farmer",  # keshavarz refers to farmer
    "karmand": "employee",  # karmand refers to employee (generic term)
    "father died": "no job",  # father died, indicating no job
    "jobless": "unemployed",  # jobless refers to unemployed
    "karegar": "employee",  # karegar refers to manual laborer or worker
}
mother_job_mapping = {
    "household": "housewife",  # household refers to a homemaker or housewife
    "workoer/employee": "employee",  # fixed typo from 'workoer' to 'worker/employee'
    "others": "others",  # unspecified other jobs
    "khane dar": "housewife",  # khane dar refers to a homemaker (Persian equivalent of housewife)
    "keshavarz": "farmer",  # keshavarz refers to farmer
    "karmand": "employee",  # karmand refers to employee
    "other": "others",  # other job categories
    "karegar": "employee",  # karegar refers to manual laborer or worker
    "mother died": "no job",  # mother died, indicating no job
}

school_type_mapping = {
    "gheyre entefaei": "independent school",  # gheyre entefaei refers to non-profit schools
    "dolati": "public school",  # dolati refers to government schools
    "gheyre entefai": "independent school",  # gheyre entefai is similar to gheyre entefaei, non-profit
}
# birth_weight_mapping = {
#     "2.5-4 kg": "2.5 to 4 kg",  # standard birth weight range
#     ">4 kg": "greater than 4 kg",  # weight greater than 4 kg
#     "<2.5 kg": "less than 2.5 kg",  # weight less than 2.5 kg
#     "nemidanam": "don't know",  # 'nemidanam' means 'I don\'t know'
#     "2 50 0-4 00 0": "2.5 to 4 kg",  # correcting the format to match '2.5-4 kg'
#     "more than 4 00 0": "greater than 4 kg",  # correcting the format to 'greater than 4 kg'
#     "less than 2 50 0": "less than 2.5 kg",  # correcting the format to 'less than 2.5 kg'
# }
birth_weight_mapping = {
    "2.5-4 kg": 2,  # standard birth weight range
    ">4 kg": 3,  # weight greater than 4 kg
    "<2.5 kg": 1,  # weight less than 2.5 kg
    "nemidanam": 0,  # 'nemidanam' means 'I don\'t know'
    "2 50 0-4 00 0": 2,  # correcting the format to match '2.5-4 kg'
    "more than 4 00 0": 3,  # correcting the format to 'greater than 4 kg'
    "less than 2 50 0": 1,  # correcting the format to 'less than 2.5 kg'
}
milk_type_mapping = {
    "shire madar": "mother's milk",  # shire madar refers to mother's milk
    "shire madar va khoshk": "mother's milk and powdered milk",  # mother\'s milk and powdered milk
    "shire gav": "cow's milk",  # shire gav refers to cow's milk
    "shire khoshk": "powdered milk",  # shire khoshk refers to powdered milk
    "madar va gav": "mother's milk and cow's milk",  # mother\'s milk and cow\'s milk
    "khoshk va gav": "powdered milk and cow's milk",  # powdered milk and cow\'s milk
    "shir madar va shire khoshk": "mother's milk and powdered milk",  # same as 'shire madar va khoshk'
    "shir madar va gav": "mother's milk and cow's milk",  # same as 'madar va gav'
    "har 3": "all three",  # all three types (mother's milk, powdered milk, cow's milk)
    "shir khoshk va gav": "powdered milk and cow's milk",  # powdered milk and cow\'s milk
}
complementary_feeding_mapping = {
    "ghazaye manzel": "homemade food",  # ghazaye manzel refers to homemade food
    "har2 ama manzel bishtar": "both, but more homemade food",  # both types but more homemade food
    "qazaye amade": "ready-made food",  # qazaye amade refers to ready-made food
    "har2 ama bishtar amade": "both, but more ready-made food",  # both types but more ready-made food
    "har do vali bishtar manzel": "both, but more homemade food",  # both types, more homemade food
    "tahiye shide dar manzel": "homemade food",  # prepared in-home food
    "har do vali bishtar ghazaye amadeh": "both, but more ready-made food",  # both types, more ready-made food
    "ghazaye amadeh": "ready-made food",  # ghazaye amadeh refers to ready-made food
}
oil_type_mapping = {
    'sorkhkardani': 'cooking oil',                    # sorkhkardani refers to cooking oil
    'roqan jamed': 'solid oil',                         # roqan jamed refers to jam oil
    'roqan maye': 'liquid oil',                       # roqan maye refers to liquid oil
    'roqan heyvanu': 'animal oil',                    # roqan heyvanu refers to animal oil
    'kare': 'butter',                                   # kare refers to ghee
    'pie va donbe': 'lamb fat',               # pie va donbe refers to pie and lamb fat
    'jamed': 'solid oil',                               # jamed refers to jam oil (same as roqan jamed)
    'kareh': 'butter',                                  # kareh refers to ghee (same as kare)
    'maaye': 'liquid oil',                         # maaye refers to vegetable oil
    'sorkh kardani': 'cooking oil',                   # sorkh kardani refers to cooking oil (same as sorkhkardani)
    'heyvani': 'animal oil',                          # heyvani refers to animal oil (same as roqan heyvanu)
    'pieye va donbe': 'lamb fat'              # pieye va donbe refers to pie and lamb fat (same as pie va donbe)
}
table_salt_mapping = {
    'yes': 'yes',
    'no': 'no',
    'always': 'yes',
    'sometimes': 'yes',
    'seldom/never': 'no'
}
dairy_type_mapping = {
    'qeyre pasto porcharb': 'non-pasteurized full-fat',               
    'pastoriz mauli': 'pasteurized regular',                         
    'p porcharb': 'pasteurized full-fat',                            
    'qeyre pasto mamuli': 'non-pasteurized regular',                 
    'p kamcharb': 'pasteurized low-fat',                             
    'patorize mamuli': 'pasteurized regular',                        
    'gheyre pastorize mamuli': 'non-pasteurized regular',            
    'pastorize por charb': 'pasteurized full-fat',                   
    'pastorize kam charb': 'pasteurized low-fat',                    
    'gheyre pastorize por charb': 'non-pasteurized full-fat'         
}
injury_complication_mapping = {
    'borieidegi,sorakh shodegi,zakhme chaghu': 'cut',  
    'pichkhordegi ya keshidegi azole': 'twist',             
    'sayer': 'other',                                                         
    'dar raftegi mafsal': 'joint dislocation',                                
    'sookhtegi': 'burn',                                                      
    'shekastegi ostokhan': 'bone fracture',                                  
    'bihushi nashi az zarbe be sar ya sadame saro gardan': 'fainting',  
    'jerahate dakheli niazmande jarahi': 'internal injuries',
    'dar raftegi': 'joint dislocation',
    'other': 'other',
    'pich khordegi': 'twist',
    'ostokhan': 'bone fracture',
    'boridegi': 'cut',
    'jerahat': 'injuries',
    'sukhtegi': 'burn',
    'bihushi': 'fainting',
}
