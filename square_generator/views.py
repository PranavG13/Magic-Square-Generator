from django.shortcuts import render
from .forms import MagicSquareForm

def generate_magic_square(size, target_sum):
    # Create an empty grid
    magic_square = [[0] * size for _ in range(size)]
    
    row = 0
    col = size // 2
    num = 1
    
    while num <= size * size:
        magic_square[row][col] = num
        num += 1
        new_row, new_col = (row - 1) % size, (col + 1) % size
        if magic_square[new_row][new_col]:
            row = (row + 1) % size
        else:
            row, col = new_row, new_col

    # Scaling to match target sum
    current_sum = sum(magic_square[0])
    scaling_factor = target_sum / current_sum
    for r in range(size):
        for c in range(size):
            magic_square[r][c] = int(magic_square[r][c] * scaling_factor)

    return magic_square

def magic_square_view(request):
    if request.method == "POST":
        form = MagicSquareForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            sum_value = form.cleaned_data['sum_value']
            
            # Edge case handling: check if the sum is logically valid
            if (sum_value - (size * (size ** 2 + 1) // 2)) % size != 0:
                return render(request, 'error.html', {'message': "Invalid sum for the given size."})

            magic_square = generate_magic_square(size, sum_value)
            return render(request, 'result.html', {'magic_square': magic_square})
    else:
        form = MagicSquareForm()

    return render(request, 'form.html', {'form': form})
