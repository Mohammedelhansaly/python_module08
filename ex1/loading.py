import sys
import importlib

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")

REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "matplotlib",
]

available = {}
missing = []


def check_package(pkg_name):
    try:
        module = importlib.import_module(pkg_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {pkg_name} ({version}) - Ready")
        available[pkg_name] = module
    except ImportError:
        print(f"[MISSING] {pkg_name} - Not installed")
        missing.append(pkg_name)


for pkg in REQUIRED_PACKAGES:
    check_package(pkg)

# If critical packages are missing, stop safely
critical = {"pandas", "numpy", "matplotlib"}
if critical.intersection(missing):
    print("\nERROR: Missing critical dependencies.")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Or with Poetry:")
    print("  poetry install")
    sys.exit(1)

print("\nAnalyzing Matrix data...")

# Use imported modules safely
pd = available["pandas"]
np = available["numpy"]
plt = importlib.import_module("matplotlib.pyplot")

# Simulated Matrix data
data_size = 1000
matrix_data = pd.DataFrame({
    "signal_strength": np.random.normal(loc=50, scale=15, size=data_size),
    "agent_activity": np.random.randint(0, 100, size=data_size)
})

print(f"Processing {data_size} data points...")

# Simple analysis
mean_signal = matrix_data["signal_strength"].mean()
mean_activity = matrix_data["agent_activity"].mean()

# Visualization
print("Generating visualization...")
plt.figure()
plt.scatter(
    matrix_data["signal_strength"],
    matrix_data["agent_activity"]
)
plt.title("Matrix Signal vs Agent Activity")
plt.xlabel("Signal Strength")
plt.ylabel("Agent Activity")

output_file = "matrix_analysis.png"
plt.savefig(output_file)
plt.close()

print("Analysis complete!")
print(f"Results saved to: {output_file}")
