  <h1>Bluetooth Keep-Alive</h1>

  <h2>keepalive.py</h2>

  <p>This Python script prevents Bluetooth speakers from turning off due to inactivity by sending inaudible sounds, keeping the speakers on.</p>

  <h3>Prerequisites</h3>

  <ul>
    <li>Python 3.7 or above</li>
  </ul>

  <h3>Installation</h3>

  <ol>
    <li>Install Python:
      <ul>
        <li>Windows: Visit the official Python website at <a href="https://www.python.org/downloads/windows/">https://www.python.org/downloads/windows/</a> and download the latest Python version. Run the installer and follow the instructions.</li>
        <li>macOS: macOS comes pre-installed with Python. Open the Terminal and type <code>python3 --version</code> to check if Python is installed. If not, you can install it using Homebrew or from the official Python website.</li>
        <li>Linux: Open the Terminal and run the following command based on your Linux distribution:
          <ul>
            <li>Ubuntu/Debian: <code>sudo apt-get install python3</code></li>
            <li>Fedora: <code>sudo dnf install python3</code></li>
          </ul>
        </li>
      </ul>
    </li>
  </ol>

  <h3>Usage</h3>

  <ol>
    <li>Open a terminal or command prompt.</li>
    <li>Navigate to the directory where the <code>keepalive.py</code> script is located.</li>
    <li>Run the script using the following command:</li>
  </ol>

  <pre><code>python keepalive.py</code></pre>

  <p>The script will start sending inaudible sounds to your Bluetooth speakers, preventing them from turning off due to inactivity.</p>

  <h2>keepalive_win.py</h2>

  <p>This Python script does everything that <code>keepalive.py</code> does, but it also creates an icon in the system tray, which can be used to exit the script. Additionally, the script is designed to be converted into a standalone executable using tools like PyInstaller.</p>

  <h3>Prerequisites</h3>

  <ul>
    <li>Python 3.7 or above</li>
    <li>Required Python libraries: <code>numpy</code>, <code>sounddevice</code>, <code>pystray</code>, <code>Pillow</code></li>
  </ul>

  <h3>Installation</h3>

  <ol>
    <li>Install Python and the required libraries (follow the instructions mentioned in the previous section).</li>
    <li>Clone or download the repository to your local machine.</li>
  </ol>

  <h3>Usage</h3>

  <ol>
    <li>Open a terminal or command prompt.</li>
    <li>Navigate to the directory where the <code>keepalive_win.py</code> script is located.</li>
    <li>Run the script using the following command:</li>
  </ol>

  <pre><code>python keepalive_win.py</code></pre>

  <p>The script will start sending inaudible sounds to your Bluetooth speakers, preventing them from turning off due to inactivity. It will also create an icon in the system tray.</p>

  <p>To exit the script, right-click on the system tray icon and select "Exit".</p>

  <h3>Converting to Standalone Executable</h3>

  <p>You can use tools like PyInstaller to convert the <code>keepalive_win.py</code> script into a standalone executable.</p>

  <ol>
    <li>Install PyInstaller:</li>
  </ol>

  <pre><code>pip install pyinstaller</code></pre>

  <ol start="2">
    <li>Navigate to the directory where the <code>keepalive_win.py</code> script and the icon.ico files are located.</li>
    <li>Run the following command to create the standalone executable:</li>
  </ol>

  <pre><code>pyinstaller --onefile --icon=icon.ico keepalive_win.py</code></pre>

  <p>This will generate a standalone executable file in the <code>dist</code> directory.</p>

  <p>The standalone executable can be distributed and run on Windows systems without the need for Python or any additional dependencies.</p>

  <h2>License</h2>

  <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more information.</p>