FROM ubuntu:latest
COPY . /workdir
WORKDIR /workdir
RUN conda env update --name torch_base --file scripts/torch_base.yml --prune
CMD echo "$CONDA/bin" >> "$GITHUB_PATH" \
conda activate torch_base