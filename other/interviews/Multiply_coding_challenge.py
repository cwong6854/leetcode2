def solve(width, height, length, mass) -> str:
    """
    Objective:

    Sort the packages into their expected categories

    

    Rules:

    You work in an automated factory and your objective is to write the method that will dispatch the packages to the correct stack, according to their volume and mass.

    A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimension is greater or equal than 150 cm.

    A package is heavy when its mass is greater or equal than 20 kg.

        

    You must dispatch the packages in the following stacks:

            STANDARD: standard packages (those which are not bulky nor heavy) can be handled normally.

            SPECIAL: packages that are either heavy or bulky can't be handled automatically.

            REJECTED: packages that are both heavy and bulky are rejected.

    

    Implementation:

    Implement the method solve(width, height, length, mass) (units are centimeter for the dimensions and kilogram for the mass). This method must return a string: the name of the stack where the package should go.

    

    Constraints:

            20 ≤ width, height, length ≤ 200

            10 ≤ mass ≤ 1000

    """
    is_bulky, is_heavy = False, False
    volume = width * height * length

    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True
    if mass >= 20:
        is_heavy = True    
    if volume >= 1000000:
        is_bulky = True
    if is_bulky and is_heavy:
        return "REJECTED" 
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
if __name__ == "__main__":
    assert solve(160, 70, 70, 10) == "SPECIAL"
    assert solve(120, 100, 100, 10) == "SPECIAL"
    assert solve(90, 90, 118, 10) == "STANDARD"
    assert solve(120, 100, 50, 30) == "SPECIAL"
    assert solve(80, 110, 80, 70) == "SPECIAL"
    assert solve(70, 80, 90, 10) == "STANDARD"
    assert solve(100, 120, 60, 19) == "STANDARD"
    assert solve(150, 70, 70, 10) == "SPECIAL"
    assert solve(120, 100, 100, 10) == "SPECIAL"
    assert solve(90, 90, 118, 10) == "STANDARD"
    assert solve(120, 100, 110, 20) == "REJECTED"
    assert solve(80, 110, 80, 70) == "SPECIAL"
    assert solve(70, 80, 90, 10) == "STANDARD"
    assert solve(100, 150, 60, 30) == "REJECTED"
    print("ALL TEST CASES PASS")