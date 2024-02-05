
# Windows Terminal Emulator

This project is a fully functional terminal emulator application for Windows.

## Features

- Local terminal emulation on Windows.
- Tabbed interface for managing multiple terminal sessions.
- Support for text-based UI applications like `VIM` and `htop` will work when ssh'd to a linux host.
- Customizable appearance and behavior.

## Screen Shots
<div align="center">
  <hr><img src="https://github.com/scottpeterman/tkwinterm/raw/main/screenshots/win1.png" alt="Window with color" width="400px">
</div>

## Libraries Used

- `tkinter`: Standard GUI toolkit for Python used for the application interface.
- `pyte`: A simple VTXXX-compatible terminal emulator library used for interpreting escape sequences and managing the terminal state.
- `uuid`: For generating unique identifiers for terminal sessions.
- `threading`: For managing concurrent operations.
- `winpty`: A Windows software package providing an interface to the Windows pseudo terminal (WinPTY).

## Key Classes

- `App`: The main application class that initializes the GUI, manages terminal tabs, and handles user interactions.
- `Terminal`: A class representing a single terminal instance. It handles the rendering of the terminal screen, input events, and terminal resizing.
- `WinPtyHandler`: This class manages the interaction with the local Windows command line, encapsulating the functionality provided by WinPTY.
- `KeyHandler`: A utility class for interpreting keyboard input and sending it to the terminal.

## Methodology

The core of the terminal emulation is handled by `pyte`. Here's how it's integrated into our application:

1. **Terminal Output Handling**: When output from the command line is available, it is fed into `pyte`'s `ByteStream` object. `pyte` interprets this data, which includes processing escape sequences and maintaining an in-memory representation of the terminal's screen.

2. **Screen Rendering**: The `Terminal` class translates `pyte`'s in-memory screen into text and colors in the `tkinter.Text` widget. This involves converting the screen's character cells into styled text that can be displayed in the GUI.

3. **Input Handling**: User input from the keyboard is captured by the `KeyHandler` and sent to the `WinPtyHandler`. For remote connections, input would be sent via an SSH channel.

4. **Terminal Resizing**: When the terminal window is resized, both `pyte` and `WinPtyHandler` are informed of the new dimensions. `pyte` uses this information to update its screen model, and `WinPtyHandler` adjusts the pseudo terminal accordingly.

5. **Session Management**: Each terminal tab has a unique session, identified by a UUID. This allows for multiple independent terminal sessions within the application.

## Getting Started

To run the application, ensure you have Python installed and the required packages available. Clone the repository, and run the main script:

```bash
python main_winpty.py
```

## Contributions

Contributions to the project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the GPLv3 License - see the LICENSE file for details.

## Build
```python
# Create a wheel
pip install wheel setuptools
python setup.py sdist bdist_wheel
```
