from random import *



class unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        print("{0} 유닛을 생성하였습니다.".format(self.name))

    def damaged(self, damage):
        self.damage = damage
        self.hp -= damage
        print("{0}이 공격을 받습니다.\n[현재 남은체력] : {1}".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

class Attack_unit(unit):
    def __init__(self, name, hp, damage, speed):
        unit.__init__(self, name, hp)
        self.damage = damage
        self.speed = speed
    
    def move(self, location):
        self.location = location
        print("{0} : {1}방향으로 공격을 시작합니다. [속도 {2}]"\
            .format(self.name, self.location, self.speed))


class Fliable(unit):
    def __init__(self, name, hp,flyingspeed):
        unit.__init__(self, name, hp)
        self.flyingspeed = flyingspeed

class Fliable_attack_unit(Fliable):
    def __init__(self, name, hp, flyingspeed, damage):
        Fliable.__init__(self, name, hp, flyingspeed)
        self.damage = damage

    def move(self, location):
        self.location = location
        print("{0} : {1}방향으로 공격을 시작합니다. [속도 {2}]"\
            .format(self.name, self.location, self.flyingspeed))

class marine(Attack_unit):
    def __init__(self):
        Attack_unit.__init__(self, "마린", 100, 5, 1)

    def steampack(self):
        if self.hp > 0 :
            self.hp -= 10
            self.damage += 3
            self.speed += 1
            print("[스팀팩 사용] hp : {0}\tdamage : {1}\tspeed : {2}"\
                .format(self.hp, self.damage, self.speed))
        else :
            print("{0} 스팀팩을 사용할 수 없습니다.".format(self.name))


class tank(Attack_unit):
    global size_mode_develope
    
    def __init__(self):
        Attack_unit.__init__(self, "탱크", 300, 25, 1)

    def size_on(self):
        self.size_mode_develope = size_mode_develope
        if self.size_mode_develope == True :
            self.mode_status = True
            self.speed = 0
            self.damage *= 2
            print("[시즈모드 사용] hp : {0}\tdamage : {1}\tspeed : {2}"\
                .format(self.hp, self.damage, self.speed))
    
    def size_off(self):
        self.size_mode_develope = size_mode_develope
        if self.size_mode_develope == True :
            self.mode_status = False
            self.speed = 1
            self.damage /= 2
            print("[시즈모드 해제] hp : {0}\tdamage : {1}\tspeed : {2}"\
                .format(self.hp, int(self.damage), self.speed))

class wraith(Fliable_attack_unit):
    def __init__(self):
        Fliable_attack_unit.__init__(self, "레이스", 150, 5,5)

def game_start():
    print("[알림] 게임을 시작합니다.")

def game_over():
    print("Player : gg\n[알림] Player가 게임을 나갔습니다. 게임을 종료합니다.")


# 유닛생성 및 부대지정
group = []
m1 = marine()
m2 = marine()
m3 = marine()
m4 = marine()
group.append(m1)
group.append(m2)
group.append(m3)
group.append(m4)

t1 = tank()
t2 = tank()
t3 = tank()
group.append(t1)
group.append(t2)
group.append(t3)

w1 = wraith()
w2 = wraith()
group.append(w1)
group.append(w2)

# 공격 준비 및 이동
size_mode_develope = True
print("[알림] 시즈모드 개발이 완료되었습니다.")

for unit in group:
    unit.move("1시")
    if isinstance(unit, marine) == True :
        unit.steampack()
    elif isinstance(unit, tank) == True :
        unit.size_on()
    unit.damaged(randint(10,301))

game_over()

    