#!/usr/bin/env bash

SED_SCRIPT="
s/(\w)iong\b/\1s/g;
s/(\w)uang\b/\1l/g;
s/(\w)iang\b/\1l/g;
s/(\w)uan\b/\1r/g;
s/(\w)ong\b/\1s/g;
s/(\w)eng\b/\1g/g;
s/(\w)ang\b/\1h/g;
s/(\w)uai\b/\1k/g;
s/(\w)ing\b/\1k/g;
s/(\w)iao\b/\1n/g;
s/(\w)ian\b/\1m/g;
s/(\w)iu\b/\1q/g;
s/(\w)ei\b/\1w/g;
s/(\w)ue\b/\1t/g;
s/(\w)ve\b/\1t/g;
s/(\w)un\b/\1y/g;
s/(\w)uo\b/\1o/g;
s/(\w)ie\b/\1p/g;
s/(\w)ai\b/\1d/g;
s/(\w)en\b/\1f/g;
s/(\w)an\b/\1j/g;
s/(\w)ou\b/\1z/g;
s/(\w)ua\b/\1x/g;
s/(\w)ia\b/\1x/g;
s/(\w)ao\b/\1c/g;
s/(\w)ui\b/\1v/g;
s/(\w)in\b/\1b/g;
s/\bsh(\w)/u\1/g;
s/\bch(\w)/i\1/g;
s/\bzh(\w)/v\1/g;
s/\ba\b/aa/g;
s/\bo\b/oo/g;
s/\be\b/ee/g;
s/\bang\b/ah/g;
s/\beng\b/eg/g;
s/\bhng\b/hg/g"

sed -i_ -E "$SED_SCRIPT" "$@"
