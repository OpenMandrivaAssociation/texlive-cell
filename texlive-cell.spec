# revision 20756
# category Package
# catalog-ctan /macros/latex/contrib/cell
# catalog-date 2010-12-15 11:00:48 +0100
# catalog-license pd
# catalog-version 1.28/2.03
Name:		texlive-cell
Version:	1.28.2.03
Release:	2
Summary:	Bibliography style for Cell
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cell
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cell.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an "apa-like" style (cf. apalike.bst in the BibTeX
distribution), developed from the same author's JMB style. A
supporting LaTeX package is also provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/cell/cell.bst
%{_texmfdistdir}/tex/latex/cell/cell.sty
%doc %{_texmfdistdir}/doc/latex/cell/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
