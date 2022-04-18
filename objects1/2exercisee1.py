class animal:
    def __init__(self,name):
        self.name=name
        self.hunger=5
        self.energy=5

    def __str__(self):
        return f'{self.name},hunger {self.hunger},energy {self.energy}'

    def eat(self,grams):
        printed=0
        food_needed=(self.hunger)*50
        if grams>food_needed:
            grams=food_needed
            print('your animal didnt finish eating because it was not hungry or it ran out of energy')
            printed+=1
        available_intake=100*self.energy
        if grams>available_intake:
            grams=available_intake
            if printed==0:
                print('your animal didnt finish eating because it was not hungry or it ran out of energy')
        self.hunger-=grams/50
        self.energy-=grams/100

    def play(self,minutes):
        printed = 0
        available_hunger =(10-self.hunger)*5
        if minutes > available_hunger:
            minutes = available_hunger
            print('your animal didnt finish playing because it was too hungry or it ran out of energy')
            printed += 1
        available_energy = 5 * self.energy
        if minutes > available_energy and:
            grams = available_energy
            if printed == 0:
                print('your animal didnt finish eating because it was not hungry or it ran out of energy')

    def rest(self,minutes):
        if minutes<20:
            print('not enough time to rest')
            return
        for i in range (20,minutes+1,10):
            if (self.hunger>=10):
                print('animal is too hungry to finish resting')
                break
            else:
                if i%20==0:
                    self.energy+=1
                if i%30==0:
                    self.hunger+=1



animal1=animal("pig")
print(animal1)
food=int(input('enter the number of grams your animal will eat: '))
animal1.eat(food)
print(animal1)
# # play_time=int(input('enter the play time in minutes: '))
# animal1.play(play_time)
# print(animal1)
# rest_time=int(input('enter the rest time in minutes: '))
# animal1.rest(rest_time)
# print(animal1)

# print('1 for eating, 2 for playing, 3 for resting, 0 for finishing all activities')
# activity=int(input('enter the activity you want represented by the number: '))
#
# while activity!=0:
#     if activity==1:
#         food = int(input('enter the number of grams your animal will eat: '))
#         animal1.eat(food)
#         print(animal1)
#         activity = int(input('enter the activity you want represented by the number: '))
#
#     if activity==2:
#         play_time=int(input('enter the play time in minutes: '))
#         animal1.play(play_time)
#         print(animal1)
#         activity = int(input('enter the activity you want represented by the number: '))
#
#     if activity==3:
#         rest_time=int(input('enter the rest time in minutes: '))
#         animal1.rest(rest_time)
#         print(animal1)
#         activity = int(input('enter the activity you want represented by the number: '))
