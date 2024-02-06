import random 
import matplotlib.pyplot as plt 

num_of_throws = 1000000
result = dict()

for _ in range (num_of_throws):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_of_dices = dice_1 + dice_2
    if sum_of_dices in result.keys():
        result[sum_of_dices] += 1
    else:
        result[sum_of_dices] = 1

probability = dict()
for dice, throws in result.items():
    prob_single = (throws / num_of_throws)
    probability[dice] = prob_single
sorted_probability = dict(sorted(probability.items()))   

print("Dice | Probability")
print("-----|------------")
for dice, prob in sorted_probability.items():
    print(f"{dice :<4} | {prob:.2%}")
    
plt.bar(sorted_probability.keys(), sorted_probability.values())
plt.show()