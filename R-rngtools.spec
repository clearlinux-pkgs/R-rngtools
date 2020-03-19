#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rngtools
Version  : 1.5
Release  : 31
URL      : https://cran.r-project.org/src/contrib/rngtools_1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rngtools_1.5.tar.gz
Summary  : Utility Functions for Working with Random Number Generators
Group    : Development/Tools
License  : GPL-3.0
Requires: R-RUnit
Requires: R-digest
BuildRequires : R-RUnit
BuildRequires : R-digest
BuildRequires : buildreq-R

%description
[![Build Status](https://travis-ci.org/renozao/rngtools.png?branch=master)](https://travis-ci.org/renozao/rngtools)
[![codecov](https://codecov.io/gh/renozao/rngtools/branch/master/graph/badge.svg)](https://codecov.io/gh/renozao/rngtools)

%prep
%setup -q -c -n rngtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579883615

%install
export SOURCE_DATE_EPOCH=1579883615
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rngtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rngtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rngtools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rngtools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rngtools/DESCRIPTION
/usr/lib64/R/library/rngtools/INDEX
/usr/lib64/R/library/rngtools/Meta/Rd.rds
/usr/lib64/R/library/rngtools/Meta/features.rds
/usr/lib64/R/library/rngtools/Meta/hsearch.rds
/usr/lib64/R/library/rngtools/Meta/links.rds
/usr/lib64/R/library/rngtools/Meta/nsInfo.rds
/usr/lib64/R/library/rngtools/Meta/package.rds
/usr/lib64/R/library/rngtools/NAMESPACE
/usr/lib64/R/library/rngtools/R/rngtools
/usr/lib64/R/library/rngtools/R/rngtools.rdb
/usr/lib64/R/library/rngtools/R/rngtools.rdx
/usr/lib64/R/library/rngtools/help/AnIndex
/usr/lib64/R/library/rngtools/help/aliases.rds
/usr/lib64/R/library/rngtools/help/paths.rds
/usr/lib64/R/library/rngtools/help/rngtools.rdb
/usr/lib64/R/library/rngtools/help/rngtools.rdx
/usr/lib64/R/library/rngtools/html/00Index.html
/usr/lib64/R/library/rngtools/html/R.css
/usr/lib64/R/library/rngtools/tests/testthat.R
/usr/lib64/R/library/rngtools/tests/testthat/test-RNG.r
/usr/lib64/R/library/rngtools/tests/testthat/test-RNGseq.r
/usr/lib64/R/library/rngtools/tests/testthat/test-format.R
