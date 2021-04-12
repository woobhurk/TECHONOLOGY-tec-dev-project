#!/usr/bin/env bash

SED_SCRIPT="s/(\w)iong( |\t)/\1s\2/g;
s/(\w)uang( |\t)/\1l\2/g;
s/(\w)iang( |\t)/\1l\2/g;
s/(\w)uan( |\t)/\1r\2/g;
s/(\w)ong( |\t)/\1s\2/g;
s/(\w)eng( |\t)/\1g\2/g;
s/(\w)ang( |\t)/\1h\2/g;
s/(\w)uai( |\t)/\1k\2/g;
s/(\w)ing( |\t)/\1k\2/g;
s/(\w)iao( |\t)/\1n\2/g;
s/(\w)ian( |\t)/\1m\2/g;
s/(\w)iu( |\t)/\1q\2/g;
s/(\w)ei( |\t)/\1w\2/g;
s/(\w)ue( |\t)/\1t\2/g;
s/(\w)ve( |\t)/\1t\2/g;
s/(\w)un( |\t)/\1y\2/g;
s/(\w)uo( |\t)/\1o\2/g;
s/(\w)ie( |\t)/\1p\2/g;
s/(\w)ai( |\t)/\1d\2/g;
s/(\w)en( |\t)/\1f\2/g;
s/(\w)an( |\t)/\1j\2/g;
s/(\w)ou( |\t)/\1z\2/g;
s/(\w)ua( |\t)/\1x\2/g;
s/(\w)ia( |\t)/\1x\2/g;
s/(\w)ao( |\t)/\1c\2/g;
s/(\w)ui( |\t)/\1v\2/g;
s/(\w)in( |\t)/\1b\2/g;
s/( |\t)sh(\w)/\1u\2/g;
s/( |\t)ch(\w)/\1i\2/g;
s/( |\t)zh(\w)/\1v\2/g;
s/( |\t)a( |\t)/\1aa\2/g;
s/( |\t)o( |\t)/\1oo\2/g;
s/( |\t)e( |\t)/\1ee\2/g;
s/( |\t)ang( |\t)/\1ah\2/g;
s/( |\t)eng( |\t)/\1eg\2/g;
s/( |\t)hng( |\t)/\1hg\2/g;
s/( |\t)(\w)( |\t)/\1\2\2\3/g"

sed -Ei_ "$SED_SCRIPT" ./*
