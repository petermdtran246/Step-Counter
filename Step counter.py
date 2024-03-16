# Define your function here 
def feet_to_steps(user_feet):
    step_walked = user_feet // 2.5
    return step_walked

if __name__ == '__main__':
    input_feet = float(input())
    steps_walked = feet_to_steps(input_feet)
    print(int(steps_walked))
