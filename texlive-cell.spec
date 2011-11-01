Name:		texlive-cell
Version:	1.28.2.03
Release:	1
Summary:	Bibliography style for Cell
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cell
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cell.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This is an "apa-like" style (cf. apalike.bst in the BibTeX
distribution), developed from the same author's JMB style. A
supporting LaTeX package is also provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
