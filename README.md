<h1 align="center">KeepAlive Scripts</h1>

<p align="center">
  <strong>Prevent Bluetooth Speakers from Turning Off due to Inactivity</strong>
</p>

<h2>Overview</h2>

<p>This repository includes two Python scripts designed to keep Bluetooth speakers active by sending inaudible sounds at regular intervals:</p>

<ol>
  <li><code>keepalive.py</code>: A basic Python script for Windows, macOS, and Linux.</li>
  <li><code>keepalive_win.py</code>: An enhanced version for Windows with system tray functionality.</li>
</ol>

<h2>Installation Guide</h2>

<h3>Windows</h3>

<ol>
  <li>Download and install Python from the <a href="https://www.python.org/downloads/">official website</a>.</li>
  <li>Open the command prompt and verify the installation by running <code>python --version</code>.</li>
  <li>Clone or download this repository to your desired location.</li>
  <li>Navigate to the project directory in the command prompt.</li>
  <li>Run the script using the command <code>python keepalive.py</code> for <code>keepalive.py</code> or <code>python keepalive_win.py</code> for <code>keepalive_win.py</code>.</li>
</ol>

<h3>macOS</h3>

<ol>
  <li>macOS usually comes with Python pre-installed. Open the Terminal application and verify the installation by running <code>python --version</code>.</li>
  <li>Clone or download this repository to your desired location.</li>
  <li>Open the Terminal and navigate to the project directory.</li>
  <li>Run the script using the command <code>python3 keepalive.py</code>.</li>
</ol>

<h3>Linux</h3>

<ol>
  <li>Linux distributions often have Python pre-installed. Open the Terminal application and verify the installation by running <code>python --version</code>.</li>
  <li>Clone or download this repository to your desired location.</li>
  <li>Open the Terminal and navigate to the project directory.</li>
  <li>Run the script using the command <code>python3 keepalive.py</code>.</li>
</ol>

<h2>Scripts Description</h2>

<h3><code>keepalive.py</code></h3>

<p>A basic Python script that keeps Bluetooth speakers active by sending inaudible sounds at regular intervals. It is compatible with Windows, macOS, and Linux.</p>

<h3><code>keepalive_win.py</code></h3>

<p>An enhanced version of <code>keepalive.py</code> specifically for Windows, offering additional features:</p>

<ul>
  <li>Creates a system tray icon for easy access and control.</li>
  <li>Provides an option to exit the script using the system tray icon.</li>
  <li>Can be converted to a standalone executable using tools like PyInstaller.</li>
</ul>

<p>Ensure you have Python installed on your system before running these scripts. Refer to the installation guide for platform-specific instructions.</p>

<p>Feel free to explore and utilize these scripts to prevent your Bluetooth speakers from going inactive. For Windows users, the enhanced <code>keepalive_win.py</code> provides a more user-friendly experience with the system tray icon and exit functionality.</p>

<p>Please note that these scripts are provided as-is, and any usage or modification is at your own discretion. For any questions or issues, please refer to the repository's issue tracker. Enjoy uninterrupted audio experience with your Bluetooth speakers!</p>
