from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))

    sum_result = my_int1 + my_int2

    out1 = Output(sum_result, "sum_result", party1)

    return [out1]
