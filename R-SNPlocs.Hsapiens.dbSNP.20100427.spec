%global packname  SNPlocs.Hsapiens.dbSNP.20100427
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.99.6
Release:          1
Summary:          SNP locations for Homo sapiens (dbSNP BUILD 131)
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-IRanges R-GenomicRanges 
Requires:         R-methods R-IRanges R-GenomicRanges 
Requires:         R-Biostrings R-BSgenome R-BSgenome.Hsapiens.UCSC.hg19 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-IRanges R-GenomicRanges
BuildRequires:    R-methods R-IRanges R-GenomicRanges 
BuildRequires:    R-Biostrings R-BSgenome R-BSgenome.Hsapiens.UCSC.hg19 

%description
SNP locations and alleles for Homo sapiens extracted from dbSNP BUILD
131:human_9606 (based on GRCh37). The source data files used for this
package were created by NCBI on 24-26 March 2010. WARNING: The SNPs in
this package are based on the GRCh37 genome. Note that the GRCh37 genome
is the same as the hg19 genome from UCSC except for the mitochondrion
chromosome. Therefore, the SNPs in this package can be "injected" in
BSgenome.Hsapiens.UCSC.hg19 but this injection will exclude chrM (i.e.
nothing will be injected in that sequence).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tools
