from enum import Enum

class SimulationMode(Enum):
    NORMAL = "normal"              # Only genuine transactions
    TRAINING = "training"          # Mixed genuine + fraud
    VELOCITY_TEST = "velocity_test"    # Only velocity fraud
    MERCHANT_TEST = "merchant_test"    # Only merchant fraud
    ACCOUNT_TEST = "account_test"      # Only account takeover