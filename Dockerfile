FROM ubuntu:latest
COPY . /workdir
WORKDIR /workdir
RUN conda env update -f conda-envs/torch_base.yml
# CMD bash scripts/run-all-tests.sh