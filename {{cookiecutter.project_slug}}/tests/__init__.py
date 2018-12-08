import os
import sys

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

sys.path.append(dir)
sys.path.append(f'{dir}/app')
