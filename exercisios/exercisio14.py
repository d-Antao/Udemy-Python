def doplicaçao(num):
    return 2 * num

def triplicaçao(num):
    return 3 * num

def quadriplicaçao(num):
    return 4 * num

def creat_multipliers(multiplier):
    def multipliers(num):
        return multiplier * num
    return multipliers