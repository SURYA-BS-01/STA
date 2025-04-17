def test_do_while_loop(n):
    i = 0
    while True:
        print(f"Do-While loop iteration: {i}")
        i += 1
        if i >= n:
            break

# Run the test
test_do_while_loop(5)
