# Tetris AI

A modern implementation of Tetris featuring both manual play and an AI player, built with Pygame. The AI uses genetically trained parameters to achieve exceptional performance, capable of playing indefinitely while maximizing line clears.

```
████████ ███████ ████████ ██████  ██ ███████ 
   ██    ██         ██    ██   ██ ██ ██      
   ██    █████      ██    ██████  ██ ███████ 
   ██    ██         ██    ██   ██ ██      ██ 
   ██    ███████    ██    ██   ██ ██ ███████ 
```                                              

## Features

- **Dual Control Modes**
  - Switch between manual and AI control in real-time
  - Toggle control modes via on-screen button
  - Observe AI demonstration of optimal gameplay strategies

- **AI Player**
  - Genetically trained parameters for optimal performance
  - Position evaluation based on:
    - Aggregate height
    - Complete lines
    - Holes
    - Bumpiness

- **Responsive Interface**
  - Dynamic screen size adaptation
  - Consistent aspect ratio maintenance
  - Fullscreen support
  - Scaled UI elements

- **Performance Metrics**
  - Real-time line clear counter
  - Mode indicator (AI/Manual)

## Getting Started

### Prerequisites

```bash
python 3.x
pygame
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tetris-ai.git
cd tetris-ai
```

2. Install required packages:
```bash
pip install pygame
pip install random
```

3. Run the game:
```bash
python main.py
```

## Controls

### Manual Mode
- Left/Right Arrow: Move piece horizontally
- Up Arrow: Rotate piece
- Down Arrow: Soft drop
- Space: Hard drop
- F: Toggle fullscreen

### AI Mode
- Click AI/Manual button to toggle AI control
- Set AI move speed at startup (default: 0.01 seconds)

## AI Implementation

The AI evaluates positions using four key metrics:

```python
class AI:
    def __init__(self, height_weight, lines_weight, holes_weight, bumpiness_weight):
        self.height_weight = height_weight      # -0.510066
        self.lines_weight = lines_weight        #  0.760666
        self.holes_weight = holes_weight        # -0.35663
        self.bumpiness_weight = bumpiness_weight# -0.184483
```

These parameters enable the AI to:
- Minimize tower heights
- Maximize line clears
- Prevent hole creation
- Maintain surface smoothness

## Technical Implementation

- Pygame-based graphics engine
- Custom renderer for responsive scaling
- Matrix operations for board state evaluation
- Consistent gameplay physics across display sizes

## Contributing

Contributions are welcome through pull requests. Please ensure you:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with clear documentation

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.

## Credits

Original Tetris concept by Alexey Pajitnov