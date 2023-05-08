import os
import numpy as np
from azure.quantum import Workspace
from azure.quantum.optimization import Problem, ProblemType, Term, QuantumMonteCarlo

# from dotenv import load_dotenv

# load_dotenv()

# Create function to generate optimization problem
def generate_problem(covariance_matrix):
    n = len(covariance_matrix)
    terms = []

    for i in range(n):
        for j in range(n):
            terms.append(Term(c=covariance_matrix[i,j], indices=[i, j]))

    return Problem(name="Portfolio Optimization", problem_type=ProblemType.ising, terms=terms)

# configure azure-quantum worksapce 
workspace = Workspace(
    subscription_id = os.environ.get('SUBS_ID'),        # Add your subscription_id
    resource_group = os.environ.get('RG'),              # Add your resource_group
    name = os.environ.get('WORKSPACE'),                 # Add your workspace name
    location = os.environ.get('LOCATION')               # Add your workspace location (for example, "westus")
    )

# set up data inputs and create the optimization problem
covariance_matrix = np.array([
    [0.1, 0.02, 0.03],
    [0.02, 0.2, 0.06],
    [0.03, 0.06, 0.3]
])

problem = generate_problem(covariance_matrix)

# run QAOA algorithm in Azure Quantum
solver = QuantumMonteCarlo(workspace, sweeps = 2, 
                           trotter_number = 10, restarts = 72, seed = 22, 
                           beta_start = 0.1, transverse_field_start = 10, transverse_field_stop = 0.1)
result = solver.optimize(problem)
print("Resultado de la optimización:", result)

