# A Reinforcement Learning Environment for Job-Shop Scheduling
**University of Agder (UiA) Version**

## Getting Started
This project implements a deep reinforcement learning approach for solving the Job-Shop Scheduling (JSS) problem, as described in our associated paper. If you find this work useful, please consider citing our [paper](https://arxiv.org/abs/2104.03760).

### Prerequisites
- Visual Studio Code (VS Code)
- Docker
- A Weight and Bias (WandB) account

### Setup
1. **Environment Setup**: Open the project in a VS Code devcontainer (use `CTRL+ SHIFT + P` and select "Open in devcontainer"). This prepares your development environment.
2. **WandB Registration**:
   - Sign up at [Wandb](https://wandb.ai/).
   - Create a new project named "JSS". Make it public.
   - Copy your API key from WandB.

### Running the Application
- Start the application in VS Code using `F5`. 
- When prompted, log in to WandB by opening your browser, choosing the second login option, and pasting in your API key.

### Installation
Ensure `git`, `cmake`, `zlib1g` (and `zlib1g-dev` on Linux) are installed. Clone this repository and install the required Python packages:

```shell
git clone https://github.com/prosysscience/JSS
cd JSS
pip install -r requirements.txt
```

**Note**: This code is tested on Ubuntu 18.04 and macOS 10.15. Some issues may arise on Windows.

### Project Structure
- `dispatching_rules/`: Implements FIFO and MWTR dispatching rules.
- `instances/`: Contains Taillard's and Demirkol's instances.
- `randomLoop/`: A debug tool with action masking.
- `CP.py`: OR-Tools CP model for JSS.
- `CustomCallbacks.py`: RLLib callback for saving optimal solutions.
- `default_config.py`: Default configuration for dispatching rules.
- `env_wrapper.py`: Environment wrapper for logging best solution actions.
- `main.py`: The primary script for the PPO approach.
- `models.py`: TensorFlow model masking illegal actions.

### Important
Your instance files must follow [Taillard's specification](http://jobshop.jjvh.nl/explanation.php#taillard_def).

## Citation
```bibtex
@misc{tassel2021reinforcement,
      title={A Reinforcement Learning Environment For Job-Shop Scheduling}, 
      author={Pierre Tassel and Martin Gebser and Konstantin Schekotihin},
      year={2021},
      eprint={2104.03760},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

## License
This project is licensed under the MIT License.

