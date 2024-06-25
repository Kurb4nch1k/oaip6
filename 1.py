def main():
    def quarters(points):
        quarters_count = {1: 0, 2: 0, 3: 0, 4: 0}

        for x, y in points:
            if x > 0:
                if y > 0:
                    quarters_count[1] += 1
                else:
                    quarters_count[4] += 1
            else:
                if y > 0:
                    quarters_count[2] += 1
                else:
                    quarters_count[3] += 1

        return quarters_count

    points = [(1, 2), (-3, 4), (-2, -5), (3, -1), (0, 0), (0, 7)]
    result = quarters(points)
    print("Количество точек в каждой четверти координатной плоскости:", result)

if __name__ == "__main__":
    main()
