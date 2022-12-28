import random



class Jim:
    def __init__(self):
        self.name="Jim"
        self.job="salesman"
        self.HP=400
        self.agility=100
        self.strength=100
        self.confidence=100
        self.opponent=[]

    def summary(self):
        return "Name: Jim. Base HP: 400, Base Agility: 100, Base Strength: 100 ; Base Confidence: 100. Notes: Jim is a salesman who thrives on reactions, both from himself and others"
    def attackSummary(self):
        lst=[]
        lst.append(self.attack_a("summary"))
        lst.append(self.attack_b("summary"))
        lst.append(self.attack_c("summary"))
        return lst
    def attack_a(self,action):
        action=action.lower()
        if action=="summary":
            return "Name: Smirk ; Type: Status ; Effect: Raises Strength ; Notes: Extra effective on Pam"
        if action=="attack":
            if self.opponent[0]=="Pam":
                self.strength+=50
                return ["Jim raised his strength by 50 by smirking at Pam",0,0,0,0]
            else:
                self.strength+=30
                return ["Jim raised his strength by 30 by smirking at the camera",0,0,0,0]

    def attack_b(self, action):
        action = action.lower()
        if action == "summary":
            return "Name: Prank ; Type: Status ; Effect:Lowers Enemy's Confidence by 25, increases strength by 10 ; Notes: Extra Effective Against Salesman, Less Effective Against HR "
        if action == "attack":
            if self.opponent[1] == "salesman":
                self.strength+=10
                return ["Jim lowers enemy confidence by 30 by hitting them with a classic prank, going all out to get them good", 0, 0, 0,30]
            elif self.opponent[1] == "HR":
                self.strength+=10
                return ["Jim lowers enemy confidence by 20 by hitting them with a classic prank, but he held back as to not get reported", 0, 0, 20]
            else:
                self.strength+=10
                return ["Jim lowers enemy confidence by 25 by hitting them with a classic prank", 0, 0, 0, 25]

    def attack_c(self, action):
        action=action.lower()
        if action=="summary":
            return "Name: Golden-Face Gun ; Type: Attack ; Power: 85 "
        if action=="attack":
            if random.randint(1, 100) + self.confidence < 100:
                return ["Oh no! It's Golden-Face from Threat Level Midnight! He pulls a gun but misses his shot! ", 0, 0, 0, 0]
            damage=round(self.strength*0.85)
            return ["Oh no! It's Golden-Face from Threat Level Midnight! He pulls a gun and hits his opponent for %d damage"%damage,damage,0,0,0]

class Dwight:
    def __init__(self):
        self.name = "Dwight"
        self.job="salesman"
        self.HP = 350
        self.agility = 80
        self.strength = 90
        self.confidence=95
        self.opponent = []
        self.Moes=False
    def summary(self):
        return  'Name: Dwight. Base HP: 300, Base Agility:80, Base Strength: 80 ; Base Confidence: 95. Notes: He may seem like your average paper salesman, but under the surface he is much more than that'

    def attackSummary(self):
        lst=[]
        lst.append(self.attack_a("summary"))
        lst.append(self.attack_b("summary"))
        lst.append(self.attack_c("summary"))
        return lst
    def attack_a(self, action):
        action = action.lower()
        if action == "summary":
            return "Name: throat punch ; Type: Attack ; Power: 100-150 ; Notes: Extra Effective on Meredith"

        if action == "attack":
            if random.randint(1, 100) + self.confidence < 100:
                return ["Dwight throws a punch to the throat, but it's a swing and a miss!", 0, 0, 0, 0]

            if self.opponent[0] == "Meredith":
                damage=round(self.strength*(random.randint(100,200)/100))
                return ["Dwight Hits Meredith in the throat for %d damage!"%damage, damage, 0, 0, 0]
            else:
                damage = round(self.strength * (random.randint(100, 150) / 100))
                return ["Dwight Hits his opponent in the throat for %d damage!"%damage,damage,0,0,0]

    def attack_b(self,action):
        action=action.lower()
        if action=="summary":
            return "Name: Which bear is best? ; Type: Status ; Effect: lower enemy confidence by 15, and increase confidence by 10 ; Notes: Extra Effective on Jim"
        if action=="attack":
            self.confidence += 10
            if self.opponent[0]=="Jim":
                return ["BLACK BEAR! BLACK BEAR IS BEST YOU IDIOT! Go ahead and lose 20 confidence why don't you (Dwight +10 confidence as well)",0,0,0,20]
            return ["BLACK BEAR! BLACK BEAR IS BEST YOU IDIOT! Go ahead and lose 15 confidence why don't you. (Dwight +10 confidence as well)",0,0,0,15]

    def attack_c(self,action):
        action=action.lower()
        if action=="summary":
            return "Name: Call in Moes ; Type: Status ; Effect: Power+60 ; Notes: 40 % Chance Moes doesn't pick up the phone"
        if action=="attack":
            if random.randint(1, 100) <40:
                return ["Dam it Moes! Ugh, he's probably stuck in the well. He'll probably be out soon", 0, 0, 0, 0]
            self.strength+=60
            return ['"Hello Moes. Yes, this is Dwight. Can you come here, and when I punch my oppenent, you hit them too, ok? Great, see you soon" (Strength +60)',0,0,0,0]

class Stanley:
    def __init__(self):
        self.name = "Stanley"
        self.job="salesman"
        self.HP = 475
        self.agility = 50
        self.strength = 105
        self.confidence=115
        self.opponent = []
    def summary(self):
        return  'Name: Stanley. Base HP: 475, Base Agility:50, Base Strength: 115 ; Base Confidence: 115. Notes: Generaly unhappy, has a weekend lady, terrifying. Also sells paper'
    def attackSummary(self):
        lst=[]
        lst.append(self.attack_a("summary"))
        lst.append(self.attack_b("summary"))
        lst.append(self.attack_c("summary"))
        return lst
    def attack_a(self,action):
        action = action.lower()
        if action == "summary":
            return "Name: ... and shove it up your butt! ; Type: Attack ; Power: 90-130 ; Notes: The power is dependant of what is shoved up their butt"
        if action == "attack":
            if random.randint(1, 100) + self.confidence < 100:
                return ['Stanely wants to tell his oppoent to shove "it" up his butt, but cant think of an object!', 0, 0, 0, 0]
            damage=round((random.randint(65,95)/100))
            if damage<75:
                object="Bread"
            elif damage<85:
                object="Toast"
            elif damage<95:
                object="Bagels"
            elif damage==95:
                object="Doughnuts"
            return ["Take some %s, put it on a plate, then SHOVE IT UP YOUR BUTT! (%d damage)"%(object,damage*self.strength),damage*self.strength, 0, 0, 0]

    def attack_b(self,action):
        action = action.lower()
        if action == "summary":
            return "Name: Pretzel Day! ; Type: Status ; Effect: Raises Confidence by 15, Strength 25, and Health by 50"
        if action == "attack":
            self.confidence += 15
            self.confidence+=25
            self.HP+=50
            return ['"I wake up every morning on a bed thats too small, drive my daughter to a school thats too expensive, and then I got to work to a job for which I get paid too little, but on Pretzel Day? I like pretzal day" Raises Confidence by 15, Strength 25, and Health by 50 ', 0, 0, 0, 0]

    def attack_c(self,action):
        action = action.lower()
        if action == "summary":
            return "Name: Stanley Yelling ; Type: Attack ; Power: 50 ; Effect: Lower enemy confidence by 15, strength by 25 ; Notes: This move does damage and status debuffs!"
        if action == "attack":

            return ['"Boy have you lost your mind cause Ill help you find it! Whatchya looking for? Aint no body going to help you out there! Jesus can come through that door and hes not gong to help you!" Lower enemy confidence by 15 and strength by 25, and does %d damage'%round(self.strength*0.5), round(self.strength*0.5), 0, 25, 15]

class Kevin:
    def __init__(self):
        self.name = "Kevin"
        self.job = "accounting"
        self.HP = 550
        self.agility = 35
        self.strength = 100
        self.confidence = 90
        self.opponent = []

    def summary(self):
        return 'Name: Kevin. Base HP: 550, Base Agility:35, Base Strength: 100 ; Base Confidence: 90. Notes: Losing confidence both easily and often, Kevin the accountant thinks he can get back on top with his family chilli recipie and magic numbers!'
    def attackSummary(self):
        lst=[]
        lst.append(self.attack_a("summary"))
        lst.append(self.attack_b("summary"))
        lst.append(self.attack_c("summary"))
        return lst
    def attack_a(self, action):
        action = action.lower()

        if action == "summary":
            return "Name: Kevin Drops the Chilli! ; Type: Attack ; Power: 175-250 ; Notes: Not the Chili! Kevin loses 45 confidence on hit"
        if action == "attack":
            if random.randint(1, 100) + self.confidence < 100:
                self.confidence-=45
                return ["Kevin drops the chilli, and it all spills uselessly on the floor! -45 confidence", 0, 0, 0, 0]

            damage = round(self.strength * (random.randint(175, 250) / 100))
            self.confidence-=45
            return ["Kevin drops his chilli, but it hits his opponent for %d damage! However, he is disappointed, and loses 45 confidence" % damage, damage, 0, 0, 0]

    def attack_b(self,action):
        action = action.lower()
        if action == "summary":
            return "Name: Wear a wig to the Wedding! ; Type: Status ; Effect: Raise Confidence by 40!"
        if action == "attack":
            self.confidence+=40
            return ["To gain some confidence, and look sharp at Jim and Pam's wedding, Kevin decides to wear a wig! Confidence +40",0,0,0,0]

    def attack_c(self, action):
        action = action.lower()
        if action == "summary":
            return "Name: Keleven! Kevin's magic accounting number to balence his accounts ; Type: Status ; Effect: Raise strength by a random amount between -15 and 50, and raise Enemy strenght by a random amount between -20 and 10"
        if action == "attack":
            strength=random.randint(-15,65)
            negativeStrength=random.randint(-10,20)
            self.strength+=strength
            return ["Realizing that the strength of his and his oppoent isn't balenced, Kevin uses Keleven to fix it! Strength + %d, enemy strength + %d"%(strength,negativeStrength),0, 0, negativeStrength, 0]
