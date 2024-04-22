# %%
from language_model import initialize_llm
from utils import (
    get_model_dict,
    describe_unique_values,
    describe_strong_correlations,
    describe_transformations,
)
from sklearn import datasets

# %%
X, y = datasets.load_iris(return_X_y=True, as_frame=True)
# %%
function_headers = describe_transformations(
    filename="preprocessing_tools.py", skip_args=["df", "drop_old"], if_def=False
)
unqiue_values = describe_unique_values(X, 5)
correlations = describe_strong_correlations(X, 0.3)

prompt = f"Useful information about columns:\n{unqiue_values}\n{correlations}\n\nAvailable column transformations (tools):\n{function_headers}\n\nLets think step by step about what new features we can create using available columns and tools:\n"
print(prompt)
# %%

# %%
llm = initialize_llm(
    model_path=get_model_dict(use_cache=False)["MISTRAL-7B-INSTRUCT-V0.2.Q6_K"],
    chat_format="mistral-instruct",
    n_gpu_layers=-1,
    n_ctx=512 * 16,
    n_batch=512 * 8,
)
# %%
