FROM alpine:latest

RUN apk update
RUN apk add git cmake clang clang-dev make gcc g++ libc-dev linux-headers

RUN git clone https://github.com/mguentner/cannelloni.git
WORKDIR /cannelloni


RUN cmake -DCMAKE_BUILD_TYPE=Release
RUN make
RUN make install

# default port
EXPOSE 20000 
ENTRYPOINT ["cannelloni", "-C", "s", "-I", "ccan_0"]