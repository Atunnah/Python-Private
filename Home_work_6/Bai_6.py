def calculate_loss(x: list, y: list, w:float, b: float) -> float:
    """This function is to calculate the loss price"""
    n = len(x)
    sum = 0
    for i in range(n):
        c_i = w * x[i] + b
        sum += (c_i - y[i])**2
    return sum / (2 * n)

def gradient_descent(x: list, y: list, w: float, b: float, learning_rate: float, epochs: int) -> float:
    """This function is to find the min loss price and return w, b"""
    n = len(x)
    for epoch in range(epochs):
        dw = 0
        db = 0
        for i in range(n):
            c_i = w * x[i] + b
            dw += (c_i - y[i]) * x[i]
            db += c_i - y[i]
        dw /= n
        db /= n
        w -= dw * learning_rate
        b -= db * learning_rate
        if epoch % 1000 == 0:
            price = calculate_loss(x, y, w, b)
            print(f"Epoch: {epoch}/{epochs}, Loss: {price}")
    return w, b

x = [50, 75, 80, 60, 70, 90, 100, 65, 85, 105]
y = [600, 860, 930, 700, 800, 1040, 1150, 750, 970, 1200]
w = 0.1
b = 0.1
learning_rate = 0.0001
epochs = 2000000
trained_w, trained_b = gradient_descent(x, y, w, b, learning_rate, epochs)
new_area = 40
predicted_price = trained_w * new_area + trained_b
print(f"Gia uoc tinh cho can ho co dien tich {new_area}: {predicted_price}")
