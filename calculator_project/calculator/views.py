from django.shortcuts import render

def index(request):
    return render(request, 'calculator/index.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation')
        result = None

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Division by zero'

        return render(request, 'calculator/index.html', {
            'result': result,
            'num1': num1,
            'num2': num2,
            'operation': operation
        })
    return render(request, 'calculator/index.html')
