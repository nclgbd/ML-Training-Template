FROM continuumio/miniconda3
COPY . /template
WORKDIR /template
RUN conda env update --name torch_base --file conda-envs/torch_base.yml --prune
CMD echo "$CONDA/bin" >> "$GITHUB_PATH" \
conda activate torch_base