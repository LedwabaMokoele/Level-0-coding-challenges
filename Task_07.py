def convert_to_celcius(farenheit):
    celcius = 5/9*(farenheit-32)
    return celcius
def convert_to_farenheit(celcius):
    farenheit = (9/5 * celcius) + 32
    return farenheit
c = convert_to_celcius(115)
f = convert_to_farenheit(c)
print(c)
print(f)