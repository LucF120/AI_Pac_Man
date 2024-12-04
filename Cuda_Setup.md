<h3>Steps to Enable Cuda (To Train Pacman on GPU)</h3>
<ul>
<li>Set up an anaconda environment running python version 3.11.5</li>
<li>Install the Cuda Toolkit 12.4 for your computer's operating system: https://developer.nvidia.com/cuda-12-4-0-download-archive</li> 
<li>Run: conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 pytorch-cuda=12.4 -c pytorch -c nvidia</li>
<li>Run: pip install gymnasium</li>
<li>Run: pip install ale-py</li> 
<li>Run: pip install matplotlib</li>
<li>Run: git clone https://github.com/allenyxu2004/CS4100_Pac_Man.git</li>
<li>cd into project directory, and run: python pacman_dqn_implementation.py</li>
</ul>

<h3>Visualizing PacMan (If running pacman.py results in: gymnasium RuntimeError: Failed to initialize SDL renderer)</h3>
<li>Set up the previously mentioned conda environment</li>
<li>Run: conda install -c conda-forge sdl2</li>
