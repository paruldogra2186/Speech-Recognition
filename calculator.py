import operator
import speech_recognition as s_r

print("Your speech_recognition version is: " + s_r.__version__)
r = s_r.Recognizer()
my_mic_device = s_r.Microphone(device_index=1)
with my_mic_device as source:
    print("Say what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=4)
my_string = r.recognize_google(audio)
print(my_string)


def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^': operator.xor,
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


print(eval_binary_expr(*(my_string.split())))
