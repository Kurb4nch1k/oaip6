def future(*masses, **constants):
    VIN = 100
    acceleration_constant = constants.get('acceleration_constant', 0)

    total_mass = sum(masses)

    if total_mass * acceleration_constant > VIN:
        return "ACCELERATION"
    elif total_mass * acceleration_constant < VIN:
        return "DECELERATION"
    else:
        return "UNCHANGED"

def main():
    result = future(10, 20, 5, acceleration_constant=2)
    print("Предсказание будущего вселенной:", result)

if __name__ == "__main__":
    main()
