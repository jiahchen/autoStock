FROM ubuntu:16.04
MAINTAINER jiahchen
ENV PATH /opt/conda/bin:$PATH
RUN apt update && apt install -y openssl make git gcc g++ wget bzip2 ca-certificates curl
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

COPY server /server
WORKDIR /server

RUN pip install shioaji
RUN pip install -r ./requirement.txt

EXPOSE 3000
CMD ["/bin/bash"]