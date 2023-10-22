# Import base image
FROM python:3.11.6-slim-bookworm

RUN apt-get update && \
    apt-get install --no-install-recommends --assume-yes \
        7zip \
        wget

WORKDIR /usr/smiley_quokka

# Copy the python requirement file and run pip
COPY . .
RUN pip install -r requirement.txt

CMD ["sh","-c","/usr/smiley_quokka/script.sh"]
