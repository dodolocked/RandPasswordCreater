import argparse
#随机密码生成工具
parser = argparse.ArgumentParser()
parser.add_argument('-max',type=str,default=16,help='默认16')
parser.add_argument('-min',type=str,default=8,help='默认8')
args = parser.parse_args()

def generate_random_password(min_length, max_length):
    import random
    import string

    if min_length > max_length:
        raise ValueError("Min必须小于Max")

    # Define the requirements of the password
    symbols = "*#@!_$"  #可加入符号
    
    # Randomly choose a length between min_length and max_length
    password_length = random.randint(min_length, max_length)

    # Create a pool of characters to choose from
    characters = string.ascii_letters + string.digits + symbols

    # Generate a random password
    random_password = ''.join(random.choice(characters) for i in range(password_length))

    return random_password
print(generate_random_password(args.min, args.max))